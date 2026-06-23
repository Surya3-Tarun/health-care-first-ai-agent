"""⊕ HEALTHFIRST AI - First Aid | UFO Emergency Response"""

import streamlit as st
from utils.emergency_detector import get_first_aid_guide, get_first_aid_condition_names

def render_first_aid():
    """🚑 Emergency protocols and first aid procedures."""
    
    st.markdown("""
        <div class="hero-section">
            <div class="hero-title">🚑 EMERGENCY RESPONSE CENTER</div>
            <div class="hero-subtitle">FIRST AID PROTOCOLS & EMERGENCY GUIDANCE</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="alert-emergency">
            🚨 IF EXPERIENCING A LIFE-THREATENING EMERGENCY, CALL 911 (USA) OR 112 (INTERNATIONAL) IMMEDIATELY 🚨
        </div>
    """, unsafe_allow_html=True)
    
    # Emergency numbers
    st.markdown("<h3 style='color: var(--neon-cyan);'>📞 Emergency Contacts</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div class="card-neon">
            <strong style='color: var(--neon-pink);'>USA</strong><br>
            <span style='color: var(--neon-cyan); font-size: 20px; font-weight: 900;'>911</span>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="card-neon">
            <strong style='color: var(--neon-pink);'>UK</strong><br>
            <span style='color: var(--neon-cyan); font-size: 20px; font-weight: 900;'>999</span>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="card-neon">
            <strong style='color: var(--neon-pink);'>INTERNATIONAL</strong><br>
            <span style='color: var(--neon-cyan); font-size: 20px; font-weight: 900;'>112</span>
        </div>""", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # First aid selection
    first_aid_names = get_first_aid_condition_names()
    selected_condition = st.selectbox(
        "🔍 Select First Aid Topic:",
        list(first_aid_names.keys())
    )
    
    if selected_condition:
        guide = get_first_aid_guide(selected_condition)
        
        st.markdown(f"""
            <div class="card-neon">
                <h2 style='color: var(--neon-blue);'>{guide['title']}</h2>
                <p style='color: var(--text-secondary); font-size: 16px;'>{guide.get('description', '')}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Steps
        st.markdown("<h3 style='color: var(--neon-cyan);'>📋 STEP-BY-STEP PROCEDURE</h3>", unsafe_allow_html=True)
        
        for i, step in enumerate(guide.get("steps", []), 1):
            st.markdown(f"""
                <div class="glow-box">
                    <strong style='color: var(--neon-cyan); font-size: 18px;'>Step {i}</strong><br>
                    <span style='color: var(--text-secondary);'>{step}</span>
                </div>
            """, unsafe_allow_html=True)
        
        # Do's
        if guide.get("dos"):
            st.markdown("<h3 style='color: var(--neon-green);'>✅ DO</h3>", unsafe_allow_html=True)
            for do in guide["dos"]:
                st.markdown(f"""<div class="glow-box">
                    <span style='color: var(--neon-green);'>✓</span> {do}
                </div>""", unsafe_allow_html=True)
        
        # Don'ts
        if guide.get("donts"):
            st.markdown("<h3 style='color: var(--neon-pink);'>❌ DON'T</h3>", unsafe_allow_html=True)
            for dont in guide["donts"]:
                st.markdown(f"""<div class="glow-box">
                    <span style='color: var(--neon-pink);'>✗</span> {dont}
                </div>""", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
        <div style='color: var(--text-tertiary); font-size: 12px; text-align: center; padding: 20px;'>
            <p>⚠️ IMPORTANT: This guide is for educational purposes only.</p>
            <p>Always seek professional emergency medical help when needed.</p>
        </div>
    """, unsafe_allow_html=True)

render_first_aid()
