import streamlit as st
import sys
from pathlib import Path


sys.path.append(str(Path(__file__).parent.parent))

st.set_page_config(
    page_title="Multi-Page App",
    layout="wide",
    initial_sidebar_state="expanded"
)

pg = st.navigation(
    {
        "General": [
            st.Page("./dashboard.py", title="Dashboard", icon=":material/dashboard:", url_path="/"),
            st.Page("prediction.py", title="Prediction", icon=":material/psychology:", url_path="/prediction"),
        ],
        "Misc.": [
            # st.Page("history.py", title="History", icon=":material/history:", url_path="/history"),
            st.Page("methodology.py", title="Methodology", icon=":material/science:", url_path="/methodology"),
            st.Page("team.py", title="Team", icon=":material/groups:", url_path="/team"),
            st.Page("resources.py", title="Resources", icon=":material/menu_book:", url_path="/resources"),
        ],
    }
)

pg.run()