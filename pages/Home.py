"""⊕ HEALTHFIRST AI - Home Page | UFO Command Center Landing"""

import streamlit as st
import datetime

def render_home():
    """🌌 Futuristic UFO-themed landing page."""
    
    st.markdown("""
        <div class="hero-section">
            <div class="hero-title">⊕ HEALTHFIRST AI ⊕</div>
            <div class="hero-subtitle">FUTURISTIC MEDICAL COMMAND CENTER</div>
            <div style='color: var(--neon-cyan); font-size: 14px; letter-spacing: 2px; margin-top: 20px;'>
                🤖 AI-POWERED MEDICAL INTELLIGENCE 🤖
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div class="stat-box"><div class="stat-box-label">🤖 AI MODEL</div>
            <div class="stat-box-value" style="color: var(--neon-green);">LLAMA 3.3</div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="stat-box"><div class="stat-box-label">⚡ STATUS</div>
            <div class="stat-box-value" style="color: var(--neon-cyan);">LIVE</div></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="stat-box"><div class="stat-box-label">🔒 SECURITY</div>
            <div class="stat-box-value" style="color: var(--neon-green);">ENCRYPTED</div></div>""", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>⚙️ COMMAND CENTER MODULES</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    features = [
        ("🤖", "AI HEALTH AGENT", "Real-time healthcare conversations with Groq Llama 3.3 70B", "var(--neon-cyan)"),
        ("🔍", "SYMPTOM DETECTOR", "Interactive health condition scanner with risk assessment", "var(--neon-blue)"),
        ("⚖️", "BMI ANALYZER", "Body composition analysis with personalized metrics", "var(--neon-purple)"),
    ]
    
    for icon, title, desc, color in features:
        with st.columns(3)[features.index((icon, title, desc, color))]:
            st.markdown(f"""
                <div class="card-neon"><div style='font-size: 40px; text-align: center; margin-bottom: 15px;'>{icon}</div>
                <h3 style='text-align: center; color: {color};'>{title}</h3>
                <p style='text-align: center; color: var(--text-secondary); font-size: 14px;'>{desc}</p></div>
            """, unsafe_allow_html=True)

render_home()
