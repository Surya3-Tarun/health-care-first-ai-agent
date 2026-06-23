"""Health-related utilities for the HealthCare First AI platform."""

import re
from typing import Dict, List, Tuple

# Strict healthcare keyword list for intent validation
HEALTHCARE_KEYWORDS = [
    'health', 'healthcare', 'medical', 'medicine', 'medicines', 'doctor', 'doctors',
    'hospital', 'clinic', 'patient', 'consultation', 'health checkup', 'medical advice',
    'treatment', 'therapy', 'surgery', 'operation', 'ambulance', 'emergency room', 'icu',
    'symptom', 'symptoms', 'pain', 'headache', 'migraine', 'fever', 'cold', 'cough',
    'sore throat', 'body pain', 'fatigue', 'weakness', 'dizziness', 'vomiting', 'nausea',
    'diarrhea', 'constipation', 'chills', 'sneezing', 'runny nose', 'breathing',
    'breathlessness', 'shortness of breath', 'wheezing', 'chest congestion', 'numbness',
    'tingling', 'memory loss', 'snoring', 'sleep apnea', 'lung', 'lungs', 'bronchitis',
    'copd', 'asthma', 'pneumonia', 'respiratory infection', 'oxygen', 'oxygen level',
    'heart', 'heart disease', 'heart attack', 'heart failure', 'heartbeat', 'palpitations',
    'pulse', 'blood circulation', 'artery', 'vein', 'angina', 'cardiac', 'cardiology',
    'blood pressure', 'hypertension', 'cholesterol', 'stroke', 'brain', 'neurology',
    'neurological', 'seizure', 'epilepsy', 'paralysis', 'alzheimer', 'parkinson',
    'nerve pain', 'multiple sclerosis', 'stomach', 'abdomen', 'abdominal pain', 'gas',
    'acidity', 'indigestion', 'ulcer', 'gastritis', 'gerd', 'heartburn', 'pancreas',
    'digestive', 'bloating', 'food poisoning', 'kidney', 'kidney disease', 'kidney stone',
    'renal', 'urine', 'urinary', 'uti', 'bladder', 'frequent urination', 'urination pain',
    'thyroid', 'thyroid disorder', 'hypothyroidism', 'hyperthyroidism', 'hormone',
    'hormonal', 'insulin', 'metabolism', 'endocrine', 'diabetes', 'blood sugar',
    'mental health', 'mental illness', 'stress', 'anxiety', 'depression', 'panic attack',
    'insomnia', 'sleep disorder', 'nutrition', 'diet', 'healthy food', 'healthy lifestyle',
    'vitamin', 'vitamins', 'protein', 'minerals', 'calcium', 'iron deficiency',
    'hydration', 'water intake', 'calories', 'fitness', 'exercise', 'workout', 'walking',
    'running', 'yoga', 'meditation', 'weight loss', 'weight gain', 'weight management',
    'obesity', 'overweight', 'underweight', 'wellness', 'lifestyle', 'bmi',
    'body mass index', 'first aid', 'emergency', 'injury', 'burn', 'cut', 'bleeding',
    'fracture', 'sprain', 'wound', 'poisoning', 'heat stroke', 'dehydration', 'tablet',
    'capsule', 'syrup', 'drug', 'drug interaction', 'prescription', 'medicine use',
    'medicine side effect', 'side effects', 'pregnancy', 'pregnant', 'pregnancy symptoms',
    'prenatal', 'postpartum', 'period', 'menstruation', 'menopause', 'pcos', 'pcod',
    'women health', 'endometriosis', 'fibroids', 'breast cancer', 'cervical cancer',
    'men health', 'prostate', 'prostate cancer', 'testosterone', 'male fertility',
    'erectile dysfunction', 'baby', 'infant', 'newborn', 'child health', 'child fever',
    'baby care', 'growth', 'development', 'pediatric', 'pediatrics', 'vaccination',
    'vaccine', 'immunization', 'senior health', 'geriatric', 'aging', 'elderly',
    'skin', 'rash', 'acne', 'eczema', 'allergy', 'itching', 'hair loss', 'dandruff',
    'scalp', 'pigmentation', 'dry skin', 'oily skin', 'sunburn', 'fungal infection',
    'tooth', 'teeth', 'gum', 'dental', 'toothache', 'eye', 'vision', 'eye pain',
    'eye infection', 'conjunctivitis', 'ophthalmology', 'ear pain', 'hearing',
    'ear infection', 'ent', 'sexual health', 'safe sex', 'condom', 'contraception',
    'birth control', 'std', 'sti', 'sexually transmitted disease',
    'sexually transmitted infection', 'syphilis', 'gonorrhea', 'chlamydia',
    'genital herpes', 'herpes', 'hpv', 'human papillomavirus', 'hiv', 'aids',
    'human immunodeficiency virus', 'acquired immunodeficiency syndrome',
    'hiv infection', 'hiv symptoms', 'aids symptoms', 'hiv treatment', 'aids treatment',
    'antiretroviral therapy', 'cd4 count', 'viral load', 'immune system', 'immunity',
    'immunodeficiency', 'opportunistic infection', 'measles', 'mumps', 'rubella',
    'chickenpox', 'hepatitis', 'hepatitis b', 'hepatitis c', 'rabies', 'cholera',
    'leptospirosis', 'zika', 'ebola', 'monkeypox', 'mpox', 'malaria', 'dengue',
    'typhoid', 'tuberculosis', 'covid', 'covid19', 'autoimmune disease', 'lupus',
    'rheumatoid arthritis', 'cancer', 'tumor', 'tumour', 'oncology', 'chemotherapy',
    'radiation therapy', 'biopsy', 'malignant', 'benign', 'blood test', 'scan',
    'xray', 'x-ray', 'mri', 'ct scan', 'ultrasound', 'ecg', 'ekg', 'report',
    'lab result', 'cardiology', 'neurology', 'dermatology', 'psychiatry',
    'orthopedics', 'oncology', 'urology', 'gynecology', 'gynaecology',
    'ophthalmology', 'ent', 'recovery', 'rehabilitation', 'healing',
    'preventive care'
]

# Restricted keywords for non-healthcare topics
RESTRICTED_KEYWORDS = [
    'python', 'java', 'javascript', 'coding', 'programming', 'ai development',
    'machine learning', 'data science', 'algorithm', 'sports', 'cricket', 'ipl',
    'virat kohli', 'jeff bezos', 'elon musk', 'football', 'soccer', 'tennis',
    'baseball', 'basketball', 'movie', 'movies', 'film', 'music', 'song', 'actor',
    'actress', 'hollywood', 'bollywood', 'politics', 'government', 'politician',
    'election', 'vote', 'finance', 'stock', 'stocks', 'crypto', 'bitcoin',
    'ethereum', 'trading', 'investment', 'bank', 'insurance', 'money', 'history',
    'geography', 'mathematics', 'math', 'technology', 'tech', 'engineering',
    'geopolitics', 'current affairs'
]

HEALTHCARE_ONLY_RESPONSE = "I am Health Care First AI. I can only answer healthcare-related questions."

EMERGENCY_KEYWORDS = [
    'chest pain', 'heart attack', 'stroke', 'severe bleeding', 'breathing difficulty',
    'unconscious', 'seizure', 'suicide', 'self-harm', 'overdose', 'acute', 'emergency',
    'immediately', 'urgent', 'critical', 'severe'
]


def is_healthcare_question(question: str) -> Tuple[bool, str]:
    """
    Validate if a question is healthcare-related.
    Returns (is_valid, reason)
    """
    question_lower = question.lower()

    # Block any explicit non-healthcare topic immediately
    for keyword in RESTRICTED_KEYWORDS:
        if keyword in question_lower:
            return False, "restricted_topic"

    # Match any strict healthcare keyword or phrase
    for keyword in HEALTHCARE_KEYWORDS:
        if keyword in question_lower:
            return True, "healthcare_intent"

    return False, "non_healthcare"


def detect_emergency(text: str) -> bool:
    """Detect if the text contains emergency indicators."""
    text_lower = text.lower()
    for keyword in EMERGENCY_KEYWORDS:
        if keyword in text_lower:
            return True
    return False


def get_emergency_response() -> str:
    """Get the emergency alert response."""
    return """
🚨 **EMERGENCY WARNING** 🚨

If you are experiencing a medical emergency, please:

1. **CALL EMERGENCY SERVICES IMMEDIATELY**
   - Call 911 (USA)
   - Call 112 (India & International)
   - Call your local emergency number

2. **DO NOT WAIT FOR AI RESPONSE**

3. **Seek immediate medical attention**

This AI is NOT a substitute for emergency medical care.
    """


def symptom_risk_assessment(symptoms: List[str]) -> Dict:
    """Assess risk level based on symptoms."""
    risk_keywords = {
        'high': ['chest pain', 'breathing difficulty', 'severe bleeding', 'unconscious',
                 'severe headache', 'stroke', 'heart attack'],
        'medium': ['high fever', 'persistent cough', 'dizziness', 'severe pain'],
        'low': ['mild fever', 'mild cough', 'slight headache']
    }
    
    risk_level = 'low'
    for symptom in symptoms:
        if any(high in symptom.lower() for high in risk_keywords['high']):
            risk_level = 'high'
            break
        elif any(med in symptom.lower() for med in risk_keywords['medium']):
            if risk_level != 'high':
                risk_level = 'medium'
    
    return {
        'risk_level': risk_level,
        'recommendation': get_risk_recommendation(risk_level)
    }


def get_risk_recommendation(risk_level: str) -> str:
    """Get recommendations based on risk level."""
    recommendations = {
        'high': '⚠️ HIGH RISK: Seek immediate medical attention or consult a doctor urgently.',
        'medium': '⚠️ MEDIUM RISK: It is recommended to consult a healthcare professional soon.',
        'low': '✅ LOW RISK: Monitor your symptoms. Consult a doctor if symptoms persist.'
    }
    return recommendations.get(risk_level, 'Consult a healthcare professional.')


def format_healthcare_response(response: str, include_disclaimer: bool = True) -> str:
    """Format healthcare response with appropriate disclaimers."""
    if include_disclaimer:
        disclaimer = "\n\n---\n**Disclaimer:** This information is for educational purposes only and should not replace consultation with a qualified healthcare professional. Always consult a healthcare provider for diagnosis and treatment."
        return response + disclaimer
    return response


def validate_bmi_input(height: float, weight: float, unit: str = 'metric') -> Tuple[bool, str]:
    """Validate BMI input values."""
    if height <= 0 or weight <= 0:
        return False, "Height and weight must be positive values."
    
    if unit == 'metric':
        if height > 300 or height < 50:
            return False, "Height must be between 50 and 300 cm."
        if weight > 500 or weight < 20:
            return False, "Weight must be between 20 and 500 kg."
    else:
        if height > 120 or height < 20:
            return False, "Height must be between 20 and 120 inches."
        if weight > 1100 or weight < 44:
            return False, "Weight must be between 44 and 1100 lbs."
    
    return True, "Valid input"


def get_health_tips() -> List[Dict]:
    """Get general health tips."""
    return [
        {
            'title': 'Stay Hydrated',
            'description': 'Drink at least 8 glasses of water daily to maintain proper hydration.',
            'icon': '💧'
        },
        {
            'title': 'Regular Exercise',
            'description': 'Exercise for at least 30 minutes daily to maintain cardiovascular health.',
            'icon': '🏃'
        },
        {
            'title': 'Balanced Diet',
            'description': 'Consume a diet rich in fruits, vegetables, and lean proteins.',
            'icon': '🥗'
        },
        {
            'title': 'Quality Sleep',
            'description': 'Get 7-9 hours of sleep every night for optimal health.',
            'icon': '😴'
        },
        {
            'title': 'Stress Management',
            'description': 'Practice meditation, yoga, or other relaxation techniques.',
            'icon': '🧘'
        },
        {
            'title': 'Regular Checkups',
            'description': 'Visit your doctor for regular health checkups and screenings.',
            'icon': '🏥'
        }
    ]
