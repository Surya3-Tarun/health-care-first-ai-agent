"""⊕ HEALTHFIRST AI - Symptom Checker | UFO Symptom Intelligence"""

import streamlit as st
from utils.health_utils import symptom_risk_assessment, get_risk_recommendation

def render_symptom_checker():
    """🔍 Interactive symptom intelligence system."""
    
    st.markdown("""
        <div class="hero-section">
            <div class="hero-title">🔍 SYMPTOM DETECTOR</div>
            <div class="hero-subtitle">INTERACTIVE HEALTH SCANNER</div>
        </div>
    """, unsafe_allow_html=True)
    
    symptoms_list = [
        "Fever", "Headache", "Cough", "Sore Throat", "Fatigue",
        "Dizziness", "Nausea", "Vomiting", "Chest Pain", "Shortness of Breath",
        "Body Ache", "Rash", "Itching", "Stomach Pain", "Diarrhea"
    ]
    
    st.markdown("<h3 style='color: var(--neon-cyan);'>Select Your Symptoms</h3>", unsafe_allow_html=True)
    
    selected_symptoms = st.multiselect(
        "Choose symptoms you're experiencing:",
        symptoms_list,
        key="symptoms_selector"
    )
    
    if selected_symptoms:
        st.session_state.symptom_assessments += 1
        
        # Assessment
        assessment = symptom_risk_assessment(selected_symptoms)
        
        risk_level = assessment.get("risk_level", "low")
        risk_color = {
            "high": "var(--neon-pink)",
            "medium": "var(--neon-blue)",
            "low": "var(--neon-green)"
        }.get(risk_level, "var(--neon-cyan)")
        
        st.markdown(f"""
            <div class="card-neon">
                <h3 style='color: {risk_color}; text-align: center;'>RISK ASSESSMENT: {risk_level.upper()}</h3>
                <p style='color: var(--text-secondary); text-align: center;'>{assessment.get('assessment', '')}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Possible causes
        if "possible_causes" in assessment:
            st.markdown("<h3 style='color: var(--neon-blue);'>Possible Conditions</h3>", unsafe_allow_html=True)
            for cause in assessment["possible_causes"][:5]:
                st.markdown(f"""<div class="glow-box">
                    <strong style='color: var(--neon-cyan);'>•</strong> {cause}
                </div>""", unsafe_allow_html=True)
        
        # Recommendations
        st.markdown("<h3 style='color: var(--neon-purple);'>Recommendations</h3>", unsafe_allow_html=True)
        
        recommendations = get_risk_recommendation(risk_level)
        for rec in recommendations.split("•")[1:]:
            if rec.strip():
                st.markdown(f"""<div class="glow-box">
                    <span style='color: var(--neon-green);'>✓</span> {rec.strip()}
                </div>""", unsafe_allow_html=True)
        
        # Warning
        if risk_level == "high":
            st.markdown("""
                <div class="alert-emergency">
                    ⚠️ HIGH RISK: If you're experiencing a medical emergency, please call emergency services immediately.
                </div>
            """, unsafe_allow_html=True)
    
    else:
        st.markdown("""
            <div class="glow-box" style='text-align: center;'>
                <p style='color: var(--neon-cyan); font-size: 16px;'>👆 Select symptoms above to begin analysis</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
        <div style='color: var(--text-tertiary); font-size: 12px; text-align: center; padding: 20px;'>
            <p>⚠️ DISCLAIMER: This tool provides health information only and is not a diagnosis.</p>
            <p>Always consult with a healthcare professional for proper diagnosis and treatment.</p>
        </div>
    """, unsafe_allow_html=True)

render_symptom_checker()
