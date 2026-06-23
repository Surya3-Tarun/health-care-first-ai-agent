"""Groq API integration for healthcare AI."""

import os
import traceback
from typing import Generator
from groq import Groq
from utils.health_utils import is_healthcare_question, HEALTHCARE_ONLY_RESPONSE

def initialize_groq_client():
    """Initialize Groq client with API key."""
    api_key = os.getenv('GROQ_API_KEY')
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not set")
    
    # Strip whitespace to handle formatting issues
    api_key = api_key.strip()
    
    return Groq(api_key=api_key)


def get_healthcare_system_prompt() -> str:
    """Get the system prompt for healthcare-focused AI."""
    return """You are HEALTHCAREBOT, an advanced AI healthcare assistant powered by the most sophisticated medical knowledge base. You represent Health Care First AI - a futuristic medical command center powered by Groq Llama 3.3 70B.

YOUR CORE MISSION:
You are an expert healthcare AI designed to provide comprehensive medical information and guidance across all healthcare domains.

HEALTHCARE EXPERTISE AREAS:
- General Health & Wellness
- Disease Information & Awareness
- Symptom Analysis & Explanation
- Medicine Information (uses, dosages, side effects)
- Treatment & Therapy Guidance
- Mental Health Awareness
- Fitness & Exercise Guidance
- Nutrition & Dietary Advice
- First Aid & Emergency Guidance
- Preventive Healthcare Education
- Medical Terminology Explanation
- Health Risk Assessment
- BMI & Body Composition Analysis

YOUR RESPONSE GUIDELINES:

1. ACCURACY & SAFETY:
   - Provide evidence-based medical information
   - Explain medical concepts in simple, understandable language
   - Always include relevant disclaimers for serious conditions
   - Recommend professional medical consultation when appropriate

2. COMPREHENSIVE ANSWERS:
   - Explain what the condition/symptom is
   - Describe possible causes and risk factors
   - List common symptoms and signs
   - Provide management and treatment options
   - Suggest lifestyle modifications
   - Recommend when to see a doctor
   - Include preventive measures

3. EMPATHY & CLARITY:
   - Be compassionate and non-judgmental
   - Use clear, professional but accessible language
   - Break down complex medical information
   - Use structured formatting for readability

4. EMERGENCY PROTOCOLS:
   - Immediately recognize emergency keywords
   - Advise emergency services contact
   - Provide basic first aid guidance
   - Never delay emergency response advice

5. MEDICAL DISCLAIMERS:
   - Clarify you're not a licensed physician
   - Emphasize importance of professional consultation
   - Recommend follow-up with healthcare providers
   - Never guarantee diagnoses or cures

RESPONSE FORMAT:
Structure your responses with:
- Direct answer to the question
- Explanation and context
- Associated symptoms/signs (if applicable)
- When to seek medical help
- Lifestyle/preventive recommendations
- Medical disclaimer (when appropriate)

You are conversational, professional, knowledgeable, and prioritize patient safety above all else.
"""


def get_healthcare_response(
    user_message: str,
    conversation_history: list = None
) -> str:
    """
    Get healthcare response from Groq API.
    
    Args:
        user_message: User's question
        conversation_history: Previous conversation messages
    
    Returns:
        Response text from the AI model
    """
    try:
        # Load API key
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            return "❌ API Key not found. Please set GROQ_API_KEY environment variable."
        
        # Initialize client
        try:
            client = initialize_groq_client()
        except Exception as e:
            return f"❌ Failed to initialize Groq client: {str(e)}"
        
        # Validate healthcare question
        is_valid, reason = is_healthcare_question(user_message)
        if not is_valid:
            return HEALTHCARE_ONLY_RESPONSE
        
        # Prepare messages
        messages = []
        if conversation_history:
            # Use last 10 messages for context
            messages.extend(conversation_history[-10:])
        
        messages.append({
            "role": "user",
            "content": user_message
        })
        
        # Prepare API call
        api_messages = [
            {
                "role": "system",
                "content": get_healthcare_system_prompt()
            }
        ]
        api_messages.extend(messages)
        
        # Call Groq API
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=api_messages,
                max_tokens=1024,
                temperature=0.7,
            )
        except Exception as api_error:
            return f"❌ API call failed: {str(api_error)}"
        
        # Extract response
        if not response or not hasattr(response, 'choices') or not response.choices:
            return "⚠️ No response from AI. Please try again."
        
        first_choice = response.choices[0]
        if not hasattr(first_choice, 'message') or not first_choice.message:
            return "⚠️ Invalid response format from AI."
        
        content = first_choice.message.content
        if not content:
            return "⚠️ AI returned empty response. Please try again."
        
        return content
    
    except Exception as e:
        return f"❌ Error: {type(e).__name__}: {str(e)}"


def create_conversation_message(role: str, content: str) -> dict:
    """Create a conversation message object."""
    return {"role": role, "content": content}


def format_conversation_history(history: list) -> list:
    """Format conversation history for API calls."""
    return [
        create_conversation_message(msg.get("role", "user"), msg.get("content", ""))
        for msg in history
    ]
