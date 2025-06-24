import streamlit as st
from routes.dashboard import dashboard
from routes.prediction import prediction
from routes.history import history
from routes.methodology import methodology
from routes.team import team
from routes.resources import resources

st.set_page_config(
    page_title="Multi-Page App",
    layout="wide",
    initial_sidebar_state="expanded"
)

if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Dashboard'

st.sidebar.title("Navigation Menu")
st.sidebar.markdown("---")

if st.sidebar.button("Dashboard", use_container_width=True):
    st.session_state.current_page = 'Dashboard'

if st.sidebar.button("Prediction", use_container_width=True):
    st.session_state.current_page = 'Prediction'

if st.sidebar.button("History", use_container_width=True):
    st.session_state.current_page = 'History'

if st.sidebar.button("Methodology", use_container_width=True):
    st.session_state.current_page = 'Methodology'

if st.sidebar.button("Team", use_container_width=True):
    st.session_state.current_page = 'Team'

if st.sidebar.button("Resources", use_container_width=True):
    st.session_state.current_page = 'Resources'

# Page routing
if  st.session_state.current_page == "Dashboard":
    dashboard(st)
elif  st.session_state.current_page == "Prediction":
    prediction(st)
elif  st.session_state.current_page == "History":
    history(st)
elif  st.session_state.current_page == "Methodology":
    methodology(st)
elif  st.session_state.current_page == "Team":
    team(st)
elif  st.session_state.current_page == "Resources":
    resources(st)
