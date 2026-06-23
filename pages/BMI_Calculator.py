"""⊕ HEALTHFIRST AI - BMI Calculator | UFO Body Analysis"""

import streamlit as st
from utils.bmi_utils import calculate_bmi, get_bmi_category, get_ideal_weight_range

def render_bmi_calculator():
    """⚖️ Body Mass Index analysis with animated visualizations."""
    
    st.markdown("""
        <div class="hero-section">
            <div class="hero-title">⚖️ BMI ANALYZER</div>
            <div class="hero-subtitle">BODY COMPOSITION ANALYSIS</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Unit selection
    unit = st.radio("Select Unit System:", ["Metric (cm, kg)", "Imperial (inches, lbs)"], horizontal=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if "Metric" in unit:
            height = st.number_input("Height (cm):", min_value=50, max_value=300, value=170, step=1)
        else:
            height = st.number_input("Height (inches):", min_value=20, max_value=120, value=67, step=1)
    
    with col2:
        if "Metric" in unit:
            weight = st.number_input("Weight (kg):", min_value=20, max_value=500, value=70, step=1)
        else:
            weight = st.number_input("Weight (lbs):", min_value=44, max_value=1100, value=154, step=1)
    
    if height and weight:
        st.session_state.bmi_calculations += 1
        
        # Calculate BMI
        bmi = calculate_bmi(height, weight, "metric" if "Metric" in unit else "imperial")
        category = get_bmi_category(bmi)
        
        # Display result
        color = {
            "Underweight": "var(--neon-blue)",
            "Normal": "var(--neon-green)",
            "Overweight": "var(--neon-blue)",
            "Obese": "var(--neon-pink)"
        }.get(category["category"], "var(--neon-cyan)")
        
        st.markdown(f"""
            <div class="card-neon" style='border-color: {color};'>
                <div style='font-size: 48px; font-weight: 900; color: {color}; text-align: center;'>{bmi:.1f}</div>
                <div style='color: {color}; text-align: center; font-size: 20px; margin-top: 10px;'>{category["category"].upper()}</div>
                <div style='color: var(--text-secondary); text-align: center; margin-top: 10px;'>{category["health_status"]}</div>
            </div>
        """, unsafe_allow_html=True)
        
        # Ideal weight range
        if "Metric" in unit:
            ideal = get_ideal_weight_range(height, "metric")
            st.markdown(f"""
                <div class="glow-box">
                    <strong style='color: var(--neon-cyan);'>Ideal Weight Range:</strong><br>
                    {ideal['min']:.1f} - {ideal['max']:.1f} kg
                </div>
            """, unsafe_allow_html=True)
        
        # Health risks
        if category["risks"]:
            st.markdown("<h3 style='color: var(--neon-blue);'>Health Considerations</h3>", unsafe_allow_html=True)
            for risk in category["risks"][:4]:
                st.markdown(f"""<div class="glow-box">
                    <span style='color: var(--neon-pink);'>⚠️</span> {risk}
                </div>""", unsafe_allow_html=True)
        
        # Recommendations
        if category["recommendations"]:
            st.markdown("<h3 style='color: var(--neon-green);'>Recommendations</h3>", unsafe_allow_html=True)
            for rec in category["recommendations"][:3]:
                st.markdown(f"""<div class="glow-box">
                    <span style='color: var(--neon-green);'>✓</span> {rec}
                </div>""", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
        <div style='color: var(--text-tertiary); font-size: 12px; text-align: center; padding: 20px;'>
            <p>📊 BMI is a screening tool and does not diagnose health conditions.</p>
            <p>Consult a healthcare professional for personalized health advice.</p>
        </div>
    """, unsafe_allow_html=True)

render_bmi_calculator()
