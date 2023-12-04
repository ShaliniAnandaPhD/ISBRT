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

# Simulation controls with status updates
st.header('Simulation Controls')
if st.button('Start Simulation'):
    logger.log_info("Simulation started")
    st.write('Simulation Status: Started')
elif st.button('Stop Simulation'):
    logger.log_info("Simulation stopped")
    st.write('Simulation Status: Stopped')

# Display logs
st.header('System Logs')
# Assuming logs are written to 'error.log'
log_file = 'error.log'
with open(log_file, "r") as file:
    logs = file.read()
st.text_area('Logs', value=logs, height=150)

# Display analytics
st.header('Analytics & Insights')
# Example: display a simple analysis
st.write('Average Age in Personas:', analytics.average_age([persona]))


