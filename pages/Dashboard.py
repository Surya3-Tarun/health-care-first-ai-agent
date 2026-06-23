"""⊕ HEALTHFIRST AI - Dashboard | UFO Analytics Hub"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import datetime

def render_dashboard():
    """📊 Analytics dashboard with real-time metrics."""
    
    st.markdown("""
        <div class="hero-section">
            <div class="hero-title">📊 ANALYTICS HUB</div>
            <div class="hero-subtitle">REAL-TIME SYSTEM METRICS & INSIGHTS</div>
        </div>
    """, unsafe_allow_html=True)
    
    # KPI Metrics
    st.markdown("<h3 style='color: var(--neon-cyan);'>📈 KEY PERFORMANCE INDICATORS</h3>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("💬 Total Chats", st.session_state.conversation_count, delta=None)
    with col2:
        st.metric("🔍 Symptom Scans", st.session_state.symptom_assessments, delta=None)
    with col3:
        st.metric("⚖️ BMI Calculations", st.session_state.bmi_calculations, delta=None)
    with col4:
        st.metric("⚠️ Emergency Alerts", st.session_state.emergency_alerts, delta=None)
    
    st.markdown("---")
    
    # Activity Trends
    st.markdown("<h3 style='color: var(--neon-blue);'>📈 ACTIVITY TRENDS</h3>", unsafe_allow_html=True)
    
    dates = pd.date_range(end=datetime.datetime.now(), periods=7)
    data = {
        'Date': dates,
        'Chats': [5, 8, 6, 10, 12, 9, st.session_state.conversation_count],
        'Scans': [3, 4, 5, 6, 7, 8, st.session_state.symptom_assessments],
    }
    df = pd.DataFrame(data)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Chats'], mode='lines+markers', 
                             name='Conversations', line=dict(color='#00E5FF')))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Scans'], mode='lines+markers',
                             name='Assessments', line=dict(color='#00BFFF')))
    
    fig.update_layout(
        template='plotly_dark',
        hovermode='x unified',
        plot_bgcolor='rgba(5, 8, 22, 0.8)',
        paper_bgcolor='rgba(5, 8, 22, 0.8)',
        font=dict(color='#B0B8C8'),
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Activity Distribution
    st.markdown("<h3 style='color: var(--neon-purple);'>📊 ACTIVITY DISTRIBUTION</h3>", unsafe_allow_html=True)
    
    activity_data = {
        'Activity': ['AI Chats', 'Symptom Scans', 'BMI Calculations', 'Emergency Protocols', 'Dashboard Views'],
        'Count': [
            st.session_state.conversation_count,
            st.session_state.symptom_assessments,
            st.session_state.bmi_calculations,
            st.session_state.emergency_alerts,
            5
        ]
    }
    
    fig_pie = go.Figure(data=[go.Pie(
        labels=activity_data['Activity'],
        values=activity_data['Count'],
        marker=dict(colors=['#00E5FF', '#00BFFF', '#8A2BE2', '#FF006E', '#00FF41'])
    )])
    
    fig_pie.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(5, 8, 22, 0.8)',
        paper_bgcolor='rgba(5, 8, 22, 0.8)',
        font=dict(color='#B0B8C8'),
    )
    
    st.plotly_chart(fig_pie, use_container_width=True)
    
    st.markdown("---")
    
    # System Status
    st.markdown("<h3 style='color: var(--neon-green);'>🔧 SYSTEM STATUS</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""<div class="glow-box">
            <strong style='color: var(--neon-cyan);'>AI MODEL STATUS</strong><br>
            <span style='color: var(--neon-green); font-size: 18px;'>✓ OPERATIONAL</span>
        </div>""", unsafe_allow_html=True)
    
    with col2:
        st.markdown("""<div class="glow-box">
            <strong style='color: var(--neon-blue);'>PROCESSING SPEED</strong><br>
            <span style='color: var(--neon-green); font-size: 18px;'>✓ OPTIMAL</span>
        </div>""", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
        <div style='color: var(--text-tertiary); font-size: 12px; text-align: center; padding: 20px;'>
            <p>📊 Real-time analytics powered by Streamlit and Plotly</p>
            <p>Last updated: """ + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + """</p>
        </div>
    """, unsafe_allow_html=True)

render_dashboard()
