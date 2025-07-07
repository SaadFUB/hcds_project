import streamlit as st
import pandas as pd
import numpy as np
from fileloader import find_file

st.markdown("<h2 style='text-align: center; margin-bottom: 0.9em'>Helpful resources</h2>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center; font-size: 1.1em; color: #3d3a2a; margin-bottom: 2em;'>Helpful information and tools to guide you, your patients, and their relatives after an Alzheimer's risk assessment.</div>",
    unsafe_allow_html=True
)

# --- SEARCH & FILTER ROW ---
search_col, filter_col = st.columns([2.4, 1.6])  # Make filter_col wider

# Add this before your search bar
st.markdown("""
    <style>
    div[data-testid="stTextInput"] input {
        font-size: 1.1em;
        text-align: left;
        box-sizing: border-box;
    }
    </style>
""", unsafe_allow_html=True)

with search_col:
    # Your search bar
    search_query = st.text_input("Search resources", "", placeholder="Type to search...", label_visibility="collapsed")

with filter_col:
    with st.expander("Filter resources", expanded=False):
        col1, col2 = st.columns(2)
        # Audience filter
        with col1:
            audience_options = ["Patients", "Doctors", "Relatives"]
            selected_audiences = []
            st.markdown("**Audience**")
            for audience in audience_options:
                if st.checkbox(audience, value=True, key=f"aud_{audience}"):
                    selected_audiences.append(audience)
        # Risk severity filter
        with col2:
            severity_options = ["Low (0-20%)", "Medium (21-50%)", "High (51-100%)"]
            selected_severities = []
            st.markdown("**Risk severity of patient**")
            for severity in severity_options:
                if st.checkbox(severity, value=True, key=f"sev_{severity}"):
                    selected_severities.append(severity)

# --- RESOURCE DATA ---
resources = [
    {
        "title": "Memory Support Groups",
        "desc": "Find local and online support groups for memory care.",
        "audience": "Patients",
        "risk_severity": "Low",
        "type": "Website",
        "link": "https://www.example.com/memory-support"
    },
    {
        "title": "Caregiver Tips",
        "desc": "Advice for caregivers supporting loved ones with Alzheimer's.",
        "audience": "Relatives",
        "risk_severity": "Medium",
        "type": "PDF",
        "link": "https://www.example.com/caregiver-tips.pdf"
    },
    {
        "title": "Legal Planning",
        "desc": "Guidance on legal and financial planning after diagnosis.",
        "audience": "Patients",
        "risk_severity": "High",
        "type": "PDF",
        "link": "https://www.example.com/legal-planning.pdf"
    },
    {
        "title": "Clinical Guidelines",
        "desc": "Latest clinical guidelines for Alzheimer's risk management.",
        "audience": "Doctors",
        "risk_severity": "High",
        "type": "Website",
        "link": "https://www.example.com/clinical-guidelines"
    },
    {
        "title": "Communication Strategies",
        "desc": "How to talk to patients and families about risk.",
        "audience": "Doctors",
        "risk_severity": "Medium",
        "type": "Video",
        "link": "https://www.example.com/communication-strategies.mp4"
    },
    {
        "title": "Family Counseling",
        "desc": "Support for relatives coping with a diagnosis.",
        "audience": "Relatives",
        "risk_severity": "Low",
        "type": "Photo",
        "link": "https://www.example.com/family-counseling.jpg"
    },
]

# --- FILTERING ---
def severity_label_to_value(label):
    # Extracts "Low", "Medium", or "High" from the label
    return label.split()[0]

selected_severity_values = [severity_label_to_value(s) for s in selected_severities]

filtered_resources = [
    res for res in resources
    if (search_query.lower() in res["title"].lower() or search_query.lower() in res["desc"].lower())
    and (not selected_audiences or res["audience"] in selected_audiences)
    and (not selected_severity_values or res["risk_severity"] in selected_severity_values)
]

# --- DISPLAY ---
st.markdown("---")
for idx, res in enumerate(filtered_resources):
    img_col, text_col, btn_col = st.columns([1, 4, 1])
    with img_col:
        st.image(str(find_file("placeholder.svg")), width=60)
    with text_col:
        if res.get("type") == "Website" and res.get("link"):
            title_html = f"<a href='{res['link']}' target='_blank' style='text-decoration:underline; color:inherit;'><b>{res['title']}</b></a>"
        else:
            title_html = f"<b>{res['title']}</b>"
        st.markdown(
            f"{title_html} "
            f"<span style='background-color:#ecebe4; color:#3d3a2a; border-radius:6px; padding:2px 10px; font-size:0.9em; margin-left:8px;'>{res['type']}</span><br>"
            f"<em>Severity: {res['risk_severity']} | Audience: {res['audience']}</em>",
            unsafe_allow_html=True
        )
        st.write(res["desc"])
    with btn_col:
        btn_key = f"open_{idx}"
        if res.get("link"):
            st.link_button("Open link", res["link"])
        else:
            st.button("Open", disabled=True, key=btn_key)





