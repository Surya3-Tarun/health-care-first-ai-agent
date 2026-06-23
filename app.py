"""
HEALTHFIRST AI - FUTURISTIC MEDICAL COMMAND CENTER
⊕ Advanced AI-Powered Healthcare Assistant ⊕
Groq Llama 3.3 70B | UFO-Inspired AI Control Room
"""

import streamlit as st
from pathlib import Path
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# 🌌 FUTURISTIC PAGE CONFIGURATION
st.set_page_config(
    page_title="⊕ HEALTHFIRST AI - Medical Command Center ⊕",
    page_icon="⊕",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "⊕ HEALTHFIRST AI - Futuristic Medical Intelligence System ⊕"
    }
)

# 🎨 Load custom CSS with neon dark theme
css_path = Path(__file__).parent / "styles" / "custom.css"
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 🔧 Hide Streamlit default page navigation (multipage nav)
st.markdown("""
    <style>
        /* Comprehensive hide for Streamlit default navigation */
        [data-testid="stSidebarNav"] { display: none !important; }
        [data-testid="stSidebarNavItems"] { display: none !important; }
        [data-testid="stSidebarNavSeparator"] { display: none !important; }
        section[data-testid="stSidebarNav"] { display: none !important; }
        .stSidebar nav { display: none !important; }
        .stSidebar [role="navigation"] { display: none !important; }
        div[data-testid*="NavLink"] { display: none !important; }
        li[data-testid*="NavLink"] { display: none !important; }
    </style>
""", unsafe_allow_html=True)

# 💾 Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'Home'
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'conversation_count' not in st.session_state:
    st.session_state.conversation_count = 0
if 'symptom_assessments' not in st.session_state:
    st.session_state.symptom_assessments = 0
if 'bmi_calculations' not in st.session_state:
    st.session_state.bmi_calculations = 0
if 'emergency_alerts' not in st.session_state:
    st.session_state.emergency_alerts = 0


def render_sidebar():
    """🎛️ Render futuristic command center sidebar."""
    with st.sidebar:
        # 🌌 COMPACT HEADER WITH NEON GLOW
        st.markdown("""
            <div class="nav-header-compact">
                <div class="nav-logo-compact">⊕ HEALTHFIRST AI</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div class='divider-neon'></div>", unsafe_allow_html=True)
        
        # 🎛️ COMMAND CENTER NAVIGATION
        st.markdown("<div class='nav-section-label'>⚙️ COMMAND INTERFACE</div>", unsafe_allow_html=True)
        
        nav_items = [
            ("🌟 Home", "Home", "Launch command center"),
            ("🤖 AI Chat Agent", "Health_Chat", "Activate health advisor"),
            ("🔍 Symptom Detector", "Symptom_Checker", "Scan medical condition"),
            ("⚖️ BMI Analysis", "BMI_Calculator", "Body metrics analyzer"),
            ("🚑 Emergency Response", "First_Aid", "Critical alert protocols"),
            ("📡 Analytics Hub", "Dashboard", "System analytics"),
            ("ℹ️ System Info", "About", "Platform information"),
        ]
        
        for label, page_name, tooltip in nav_items:
            is_active = st.session_state.page == page_name
            col1, col2 = st.columns([0.9, 0.1])
            
            with col1:
                if st.button(
                    label,
                    key=f"nav_{page_name}",
                    use_container_width=True,
                    help=tooltip
                ):
                    st.session_state.page = page_name
                    st.rerun()
        
        st.markdown("<div class='divider-neon'></div>", unsafe_allow_html=True)
        
        # 📊 SYSTEM STATUS METRICS
        st.markdown("<div class='nav-section-label'>📊 SYSTEM STATUS</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("🤖 Chats", st.session_state.conversation_count, delta=None)
        with col2:
            st.metric("🔍 Scans", st.session_state.symptom_assessments, delta=None)
        with col3:
            st.metric("⚠️ Alerts", st.session_state.emergency_alerts, delta=None)
        
        st.markdown("<div class='divider-neon'></div>", unsafe_allow_html=True)
        
        # 🔧 SYSTEM INFORMATION
        st.markdown("""
            <div class='status-panel'>
                <div class='status-item'>
                    <span class='status-label'>AI MODEL</span>
                    <span class='status-value'>Llama 3.3 70B</span>
                </div>
                <div class='status-item'>
                    <span class='status-label'>PROCESSING</span>
                    <span class='status-value'>LIVE</span>
                </div>
                <div class='status-item'>
                    <span class='status-label'>SECURITY</span>
                    <span class='status-value'>ENCRYPTED</span>
                </div>
            </div>
        """, unsafe_allow_html=True)


def main():
    """🚀 Main application entry point."""
    render_sidebar()
    
    # Route to pages based on session state
    page_map = {
        'Home': ('pages.Home', 'render_home'),
        'Health_Chat': ('pages.Health_Chat', 'render_health_chat'),
        'Symptom_Checker': ('pages.Symptom_Checker', 'render_symptom_checker'),
        'BMI_Calculator': ('pages.BMI_Calculator', 'render_bmi_calculator'),
        'First_Aid': ('pages.First_Aid', 'render_first_aid'),
        'Dashboard': ('pages.Dashboard', 'render_dashboard'),
        'About': ('pages.About', 'render_about'),
    }
    
    current_page = st.session_state.page
    
    if current_page in page_map:
        module_name, func_name = page_map[current_page]
        try:
            module = __import__(module_name, fromlist=[func_name])
            render_func = getattr(module, func_name)
            render_func()
        except Exception as e:
            st.error(f"⚠️ Error loading page: {str(e)}")


if __name__ == "__main__":
    main()
