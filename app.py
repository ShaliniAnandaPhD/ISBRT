import streamlit as st
from content_generator import ContentGenerator
from error_logger import ErrorLogger
from analytics_insights import AnalyticsInsights

# Initialize modules
content_gen = ContentGenerator()
logger = ErrorLogger()
analytics = AnalyticsInsights()

st.title('ISBRT Project Dashboard')

# Display generated content
st.header('Generated Content')
scenario = content_gen.generate_scenario_content()
persona = content_gen.generate_persona_content()
st.write('Scenario:', scenario)
st.write('Persona:', persona)

# Display controls for simulation (placeholder)
st.header('Simulation Controls')
if st.button('Start Simulation'):
    logger.log_info("Simulation started")
    # Start simulation code
if st.button('Stop Simulation'):
    logger.log_info("Simulation stopped")
    # Stop simulation code

# Display logs (placeholder)
st.header('System Logs')
st.text_area('Logs', value='Here the logs will be displayed...', height=150)

# Display analytics (placeholder)
st.header('Analytics & Insights')
st.write('Analytics data will be displayed here...')
