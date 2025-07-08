import streamlit as st
import pandas as pd
import numpy as np
from fileloader import find_file

st.markdown("<h2 style='text-align: center; margin-bottom: 0.9em'>Helpful resources</h2>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center; font-size: 1.1em; color: #3d3a2a; margin-bottom: 2em;'>Helpful information and tools to guide you, your patients, and their relatives after an Alzheimer's risk assessment.</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style='background-color:#fff8e1; border:1px solid #ffe082; border-radius:8px; padding:1em; margin-bottom:1.5em; color:#6d4c1b; font-size:1em;'>
        <b>Disclaimer:</b> The resources listed on this page are <b>only placeholders</b> for the purpose of demonstration and do not represent actual clinical or informational content. Please do not use these links for real medical or patient guidance.
    </div>
    """,
    unsafe_allow_html=True
)

# --- SEARCH & FILTER ROW ---
search_col = st.container()

with search_col:
    search_query = st.text_input("Search resources", "", placeholder="Type to search...", label_visibility="collapsed")

# --- FILTER & SORT ROW ---
filter_col, sort_col = st.columns([3, 1])

with filter_col:
    st.markdown(
        "<span style='font-size:0.85em; color:#3d3a2a; margin-bottom:-2em; display:block;'>Filter resources by</span>",
        unsafe_allow_html=True
    )

    audience_options = ["Patients", "Doctors", "Relatives"]
    severity_options = ["Low (0-20%)", "Medium (21-50%)", "High (51-100%)"]
    type_options = ["Website", "PDF", "Video", "Photo"]

    if "selected_audiences" not in st.session_state:
        st.session_state.selected_audiences = audience_options.copy()
    if "selected_severities" not in st.session_state:
        st.session_state.selected_severities = severity_options.copy()
    if "selected_types" not in st.session_state:
        st.session_state.selected_types = type_options.copy()

    with st.expander("Show filters", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Audience**")
            updated_audiences = []
            for audience in audience_options:
                if st.checkbox(
                    audience,
                    value=audience in st.session_state.selected_audiences,
                    key=f"aud_{audience}"
                ):
                    updated_audiences.append(audience)
        with col2:
            st.markdown("**Risk severity of patient**")
            updated_severities = []
            for severity in severity_options:
                if st.checkbox(
                    severity,
                    value=severity in st.session_state.selected_severities,
                    key=f"sev_{severity}"
                ):
                    updated_severities.append(severity)

        st.markdown("**Resource type**")
        updated_types = []
        for t in type_options:
            if st.checkbox(
                t,
                value=t in st.session_state.selected_types,
                key=f"type_{t}"
            ):
                updated_types.append(t)
        st.session_state.selected_audiences = updated_audiences
        st.session_state.selected_severities = updated_severities
        st.session_state.selected_types = updated_types

    # currently selected filters bar
    audience_str = ", ".join(st.session_state.selected_audiences) if st.session_state.selected_audiences else "None"
    severity_str = ", ".join(st.session_state.selected_severities) if st.session_state.selected_severities else "None"
    type_str = ", ".join(st.session_state.selected_types) if st.session_state.selected_types else "None"
    st.markdown(
        f"<div style='padding:0.3em 0.3em; margin-top:-1em; font-size:0.8em;'>"
        f"<b>Audience:</b> {audience_str} &nbsp;|&nbsp; <b>Severity:</b> {severity_str} &nbsp;|&nbsp; <b>Type:</b> {type_str}"
        f"</div>",
        unsafe_allow_html=True
    )

    selected_audiences = st.session_state.selected_audiences
    selected_severities = st.session_state.selected_severities
    selected_types = st.session_state.selected_types
with sort_col:
    sort_options = {
        "Title (A-Z)": ("title", False),
        "Title (Z-A)": ("title", True),
        "Audience (A-Z)": ("audience", False),
        "Audience (Z-A)": ("audience", True),
        "Risk severity (Low-High)": ("risk_severity", False),
        "Risk severity (High-Low)": ("risk_severity", True),
        "Type (A-Z)": ("type", False),
        "Type (Z-A)": ("type", True),
    }
    sort_choice = st.selectbox(
        "Sort resources by",
        list(sort_options.keys()),
        index=0,
        key="sort_resources"
    )
    sort_key, sort_reverse = sort_options[sort_choice]

# --- RESOURCE DATA ---
resources = [
    {
        "title": "Memory Support Groups",
        "desc": "Find local and online support groups for memory care.",
        "audience": ["Patients", "Relatives"],
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
        "audience": ["Patients", "Relatives"],
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
        "type": "PDF",
        "link": "https://www.example.com/communication-strategies.pdf"
    },
    {
        "title": "Family Counseling",
        "desc": "Support for relatives coping with a diagnosis.",
        "audience": "Relatives",
        "risk_severity": "Low",
        "type": "Photo",
        "link": "https://www.example.com/family-counseling.jpg"
    },
    {
        "title": "Establishing Safety Measures at Home",
        "desc": "As symptoms progress, make environmental adjustments such as labeling drawers, using reminder notes, installing safety locks, and minimizing trip hazards to promote safe, independent living...",
        "audience": ["Patients", "Relatives"],
        "risk_severity": "Medium",
        "type": "Video",
        "link": "https://www.example.com/safety-measures.mp4"
    },
    {
        "title": "Healthy Lifestyle and Mental Stimulation",
        "desc": "Encourage regular physical activity, a balanced diet (e.g., Mediterranean), social interaction, and brain-stimulating activities like reading or puzzles. These can help slow cognitive decline in the early stages or even as a preventive measure...",
        "audience": ["Patients", "Relatives"],
        "risk_severity": "Low",
        "type": "Video",
        "link": "https://www.example.com/healthy-lifestyle-and-mental-stimulation.mp4"
    },
    {
        "title": "Routine Monitoring and Medication Review",
        "desc": "Schedule periodic check-ups to monitor memory and cognitive function. Consider discussing medications like cholinesterase inhibitors (e.g., donepezil) with a specialist to potentially manage early symptoms...",
        "audience": ["Patients", "Relatives"],
        "risk_severity": "Medium",
        "type": "Website",
        "link": "https://www.example.com/routine-monitoring-and-medication-review"
    },
]

# --- FILTERING ---
def severity_label_to_value(label):
    # extracts "Low", "Medium", or "High" from the label
    return label.split()[0]

selected_severity_values = [severity_label_to_value(s) for s in selected_severities]

filtered_resources = [
    res for res in resources
    if (search_query.lower() in res["title"].lower() or search_query.lower() in res["desc"].lower())
    and (not selected_audiences or (
        isinstance(res["audience"], list) and any(aud in selected_audiences for aud in res["audience"])
        or isinstance(res["audience"], str) and res["audience"] in selected_audiences
    ))
    and (not selected_severity_values or res["risk_severity"] in selected_severity_values)
    and (not selected_types or res["type"] in selected_types)
]

# --- SORTING ---
severity_order = {"Low": 0, "Medium": 1, "High": 2}

if sort_key == "risk_severity":
    sorted_resources = sorted(
        filtered_resources,
        key=lambda x: severity_order.get(x["risk_severity"], 99),
        reverse=sort_reverse
    )
else:
    sorted_resources = sorted(
        filtered_resources,
        key=lambda x: (x[sort_key], x["title"]),
        reverse=sort_reverse
    )

# --- DISPLAY ---
st.markdown("---")
for idx, res in enumerate(sorted_resources):
    if idx > 0:
        st.markdown("<hr style='border: 1px solid #ecebe4; margin: 2em 0;'>", unsafe_allow_html=True)
    with st.container():
        img_col, text_col, btn_col = st.columns([1, 4, 2])
        with img_col:
            st.image(str(find_file("placeholder.svg")), width=60)
        with text_col:
            if res.get("link"):
                title_html = f"<a href='{res['link']}' target='_blank' style='text-decoration:underline; color:inherit;'><b>{res['title']}</b></a>"
            else:
                title_html = f"<b>{res['title']}</b>"
            if isinstance(res['audience'], list):
                audience_display = ", ".join(res['audience'])
            else:
                audience_display = res['audience']
            st.markdown(
                f"{title_html} "
                f"<span style='background-color:#ecebe4; color:#3d3a2a; border-radius:6px; padding:2px 10px; font-size:0.9em; margin-left:8px;'>{res['type']}</span><br>"
                f"Audience: {audience_display} | Severity: {res['risk_severity']}",
                unsafe_allow_html=True
            )
            st.markdown(
                f"<span style='color: #888; margin-top: -0.7em; display: block;'>{res['desc']}</span>",
                unsafe_allow_html=True
            )
        with btn_col:
            btn_key = f"open_{idx}"
            if res.get("link"):
                st.markdown(
                    f"""
                    <br>
                    <div style="display: flex; justify-content: center;">
                        <div style="margin-left: 1.2em; margin-right: 1.2em;">
                            <a href="{res['link']}" target="_blank" style="
                                display: inline-block;
                                padding: 0.5em 1.2em;
                                background-color: #ecebe4;
                                color: #000 !important;
                                border-radius: 6px;
                                text-decoration: none;
                                font-weight: 600;
                                font-size: 1em;
                                border: 1px solid #bdbdbd;
                            ">
                                Open
                            </a>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.button("Open", disabled=True, key=btn_key)




