"""⊕ HEALTHFIRST AI - Health Chat Agent | UFO AI Conversation"""

import streamlit as st
from utils.agent.healthcare_agent import HealthcareAgent
from utils.emergency_detector import detect_emergency_condition

# Initialize suggested topic session state
if 'suggested_input' not in st.session_state:
    st.session_state.suggested_input = None

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'conversation_count' not in st.session_state:
    st.session_state.conversation_count = 0

if 'emergency_alerts' not in st.session_state:
    st.session_state.emergency_alerts = 0

if 'agent_instance' not in st.session_state:
    st.session_state.agent_instance = HealthcareAgent()


def render_health_chat():
    """🤖 AI Health Chat interface with streaming responses."""
    
    st.markdown("""
        <div class="hero-section">
            <div class="hero-title">🤖 AI HEALTH AGENT</div>
            <div class="hero-subtitle">GROQ LLAMA 3.3 70B POWERED CONVERSATION</div>
        </div>
    """, unsafe_allow_html=True)
    
    # DEBUG PANEL (Minimal)
    with st.expander("🔍 DEBUG PANEL", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            import os
            from dotenv import load_dotenv
            load_dotenv()
            api_key = os.getenv('GROQ_API_KEY')
            st.metric("API Key", "✅ Loaded" if api_key else "❌ Missing")
            st.metric("Messages", len(st.session_state.chat_history))
            
        with col2:
            st.metric("Conversations", st.session_state.conversation_count)
            st.metric("Alerts", st.session_state.emergency_alerts)
    
    # Chat display
    chat_container = st.container()
    with chat_container:
        if st.session_state.chat_history:
            for msg in st.session_state.chat_history:
                content = msg.get("content", "")
                if not content:
                    content = "[Empty response - debugging needed]"
                
                if msg.get("role") == "user":
                    st.markdown(f"""
                        <div class="chat-message chat-message-user">
                            <strong>You:</strong> {content}
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                        <div class="chat-message chat-message-bot">
                            <strong>AI Health Agent:</strong> {content}
                        </div>
                    """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class="glow-box" style='text-align: center;'>
                    <p style='color: var(--neon-cyan);'>💬 Start a conversation above</p>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    def _process_submission(user_input: str):
        if not user_input or not user_input.strip():
            return

        user_input = user_input.strip()
        st.session_state.conversation_count += 1

        # STAGE 1: Check for emergency
        is_emergency, condition_type, emergency_msg = detect_emergency_condition(user_input)

        if is_emergency:
            st.session_state.emergency_alerts += 1
            st.markdown(f"""
                <div class="alert-emergency">
                    🚨 EMERGENCY DETECTED: {condition_type.upper()} 🚨<br>
                    {emergency_msg}
                </div>
            """, unsafe_allow_html=True)
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            st.session_state.chat_history.append({"role": "assistant", "content": emergency_msg})
            st.rerun()
            return

        with st.spinner("🔄 Processing your health request..."):
            try:
                response = st.session_state.agent_instance.process(user_input)
                if not response or response.startswith("❌"):
                    st.error(response)
            except Exception as e:
                st.error(f"❌ Error processing AI agent workflow: {str(e)}")
                response = f"⚠️ Error: {str(e)}"

        st.session_state.chat_history.append({"role": "user", "content": user_input})
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        st.rerun()

    # Input section: use chat_input so Enter submits like ChatGPT
    user_input = st.chat_input(
        "Ask your health question...",
        key="health_input"
    )

    if user_input:
        _process_submission(user_input)
    
    # Sidebar suggestions
    st.markdown("---")
    st.markdown("<h3 style='color: var(--neon-blue);'>💡 SUGGESTED TOPICS</h3>", unsafe_allow_html=True)
    
    suggestions = [
        "What are the symptoms of diabetes?",
        "How can I manage high blood pressure?",
        "What exercises are good for heart health?",
        "How much water should I drink daily?",
        "What are the benefits of meditation?",
    ]
    
    for idx, suggestion in enumerate(suggestions):
        if st.button(f"❓ {suggestion}", use_container_width=True, key=f"suggest_{idx}"):
            _process_submission(suggestion)
    
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()
    
    st.markdown("---")
    st.markdown("""
        <div style='color: var(--text-tertiary); font-size: 12px; text-align: center; padding: 20px;'>
            <p>⚠️ MEDICAL DISCLAIMER: This AI provides health information, not professional medical advice.</p>
            <p>Always consult with a healthcare professional for diagnosis and treatment.</p>
        </div>
    """, unsafe_allow_html=True)

render_health_chat()
