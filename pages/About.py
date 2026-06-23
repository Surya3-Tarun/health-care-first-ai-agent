"""⊕ HEALTHFIRST AI - About | UFO System Information"""

import streamlit as st

def render_about():
    """ℹ️ Platform information and architecture."""
    
    st.markdown("""
        <div class="hero-section">
            <div class="hero-title">ℹ️ ABOUT HEALTHFIRST AI</div>
            <div class="hero-subtitle">FUTURISTIC MEDICAL INTELLIGENCE PLATFORM</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Platform Overview
    st.markdown("<h2 style='color: var(--neon-cyan);'>🌟 PLATFORM OVERVIEW</h2>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="glow-box">
            <p style='color: var(--text-secondary); line-height: 1.8;'>
            HEALTHFIRST AI is a cutting-edge medical command center powered by Groq's Llama 3.3 70B model. 
            Designed with a futuristic UFO-inspired interface, it provides real-time healthcare intelligence, 
            symptom analysis, emergency protocols, and comprehensive health analytics. Built for production-ready 
            deployment with enterprise-grade security and reliability.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Key Features
    st.markdown("<h2 style='color: var(--neon-blue);'>✨ KEY FEATURES</h2>", unsafe_allow_html=True)
    
    features = [
        ("🤖", "AI HEALTH AGENT", "Real-time conversations with Groq Llama 3.3 70B streaming"),
        ("🔍", "SYMPTOM DETECTOR", "Interactive symptom analysis with risk assessment"),
        ("⚖️", "BMI ANALYZER", "Body composition analysis with personalized metrics"),
        ("🚑", "EMERGENCY RESPONSE", "8 first aid guides with step-by-step procedures"),
        ("📊", "ANALYTICS HUB", "Real-time metrics with Plotly visualizations"),
        ("🔐", "HEALTHCARE SAFETY", "Domain filtering, emergency detection, medical disclaimers"),
    ]
    
    cols = st.columns(3)
    for i, (icon, title, desc) in enumerate(features):
        with cols[i % 3]:
            st.markdown(f"""<div class="card-neon">
                <div style='font-size: 32px; text-align: center; margin-bottom: 10px;'>{icon}</div>
                <h4 style='color: var(--neon-cyan); text-align: center;'>{title}</h4>
                <p style='color: var(--text-secondary); font-size: 13px; text-align: center;'>{desc}</p>
            </div>""", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Technology Stack
    st.markdown("<h2 style='color: var(--neon-purple);'>⚙️ TECHNOLOGY STACK</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="glow-box">
                <h4 style='color: var(--neon-cyan);'>Frontend</h4>
                <ul style='color: var(--text-secondary); font-size: 14px;'>
                    <li>✓ Streamlit 1.28.1</li>
                    <li>✓ Plotly 5.16.1</li>
                    <li>✓ Custom CSS Dark Theme</li>
                    <li>✓ Neon Glassmorphism</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="glow-box">
                <h4 style='color: var(--neon-blue);'>Backend & AI</h4>
                <ul style='color: var(--text-secondary); font-size: 14px;'>
                    <li>✓ Python 3.8+</li>
                    <li>✓ Groq API</li>
                    <li>✓ Llama 3.3 70B</li>
                    <li>✓ Streaming Responses</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="glow-box">
                <h4 style='color: var(--neon-green);'>Data & Analytics</h4>
                <ul style='color: var(--text-secondary); font-size: 14px;'>
                    <li>✓ Pandas 2.0.3</li>
                    <li>✓ NumPy 1.24.3</li>
                    <li>✓ Session State</li>
                    <li>✓ Real-time Metrics</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="glow-box">
                <h4 style='color: var(--neon-pink);'>Infrastructure</h4>
                <ul style='color: var(--text-secondary); font-size: 14px;'>
                    <li>✓ Deployment Ready</li>
                    <li>✓ Cloud Agnostic</li>
                    <li>✓ Scalable Design</li>
                    <li>✓ Security First</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Architecture
    st.markdown("<h2 style='color: var(--neon-cyan);'>🏗️ SYSTEM ARCHITECTURE</h2>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="glow-box" style='text-align: center; color: var(--neon-cyan);'>
            <p style='font-family: monospace; font-size: 14px;'>
                USER INPUT<br>
                ↓<br>
                VALIDATION (Healthcare Check)<br>
                ↓<br>
                EMERGENCY DETECTION<br>
                ↓<br>
                GROQ API / LOCAL LOGIC<br>
                ↓<br>
                STREAMING RESPONSE<br>
                ↓<br>
                SESSION STATE STORAGE<br>
                ↓<br>
                ANALYTICS TRACKING<br>
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Safety & Ethics
    st.markdown("<h2 style='color: var(--neon-green);'>🔒 SAFETY & ETHICS</h2>", unsafe_allow_html=True)
    
    safety_items = [
        "Healthcare domain filtering (50+ topics supported)",
        "Emergency keyword detection (7 critical conditions)",
        "Medical safety disclaimers on all responses",
        "Doctor recommendation protocols",
        "Professional consultation guidance",
        "HIPAA-compliant architecture",
        "No personal data storage",
        "Transparent AI responses",
    ]
    
    for item in safety_items:
        st.markdown(f"""<div class="glow-box">
            <span style='color: var(--neon-green);'>✓</span> {item}
        </div>""", unsafe_have_html=True)
    
    st.markdown("---")
    
    # Future Roadmap
    st.markdown("<h2 style='color: var(--neon-blue);'>🚀 FUTURE ROADMAP</h2>", unsafe_have_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="glow-box">
                <h4 style='color: var(--neon-cyan);'>Q1-Q2 2024</h4>
                <ul style='color: var(--text-secondary); font-size: 13px;'>
                    <li>Mobile app deployment</li>
                    <li>Multi-language support</li>
                    <li>Voice input/output</li>
                </ul>
            </div>
        """, unsafe_have_html=True)
    
    with col2:
        st.markdown("""
            <div class="glow-box">
                <h4 style='color: var(--neon-purple);'>Q3-Q4 2024</h4>
                <ul style='color: var(--text-secondary); font-size: 13px;'>
                    <li>Wearable integration</li>
                    <li>Predictive analytics</li>
                    <li>Clinical partnerships</li>
                </ul>
            </div>
        """, unsafe_have_html=True)
    
    st.markdown("---")
    
    # Version & Credits
    st.markdown("""
        <div style='text-align: center; color: var(--text-tertiary); font-size: 12px; padding: 30px;'>
            <p style='color: var(--neon-cyan); font-weight: bold;'>⊕ HEALTHFIRST AI ⊕</p>
            <p>Version 1.0.0 | Enterprise-Ready Healthcare AI Platform</p>
            <p>Powered by Groq Llama 3.3 70B | Built with Streamlit | Production-Grade Code</p>
            <p style='margin-top: 20px; color: var(--neon-green);'>🔒 Security: ENCRYPTED | 🤖 AI: OPERATIONAL | 📊 Status: LIVE</p>
        </div>
    """, unsafe_have_html=True)

render_about()
