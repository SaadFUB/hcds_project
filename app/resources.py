import streamlit as st
import pandas as pd
import numpy as np



left, middle, right = st.columns([2, 1, 2])

with middle:
    st.title("Resources")

left, middle, right = st.columns([5, 1, 5])

with left:
    with st.container(border=True):
        l, m, r = st.columns([2, 1, 2])
        with m:
            st.write("For Patients")
        l, m, r = st.columns([1, 5, 1])
        with m:
            st.divider()
        l, r = st.columns([1, 5])
        with l:
            st.image("static/img/placeholder.svg", width=100)
        with r:
            st.write("Nullam convallis urna non leo sollicitudin, non suscipit massa molestie. Vivamus mollis semper viverra. Integer condimentum libero et neque imperdiet, non efficitur mi posuere. Morbi vel eros fringilla, aliquam enim ut, mollis elit. Ut pharetra hendrerit ornare. Aenean et ipsum id augue ultricies consectetur at et nisl. Quisque mauris neque, blandit id mauris eget, luctus lobortis urna. Aenean eu nisi vitae leo commodo laoreet. ")
        l, r = st.columns([1, 5])
        with l:
            st.image("static/img/placeholder.svg", width=100)
        with r:
            st.write("Nullam convallis urna non leo sollicitudin, non suscipit massa molestie. Vivamus mollis semper viverra. Integer condimentum libero et neque imperdiet, non efficitur mi posuere. Morbi vel eros fringilla, aliquam enim ut, mollis elit. Ut pharetra hendrerit ornare. Aenean et ipsum id augue ultricies consectetur at et nisl. Quisque mauris neque, blandit id mauris eget, luctus lobortis urna. Aenean eu nisi vitae leo commodo laoreet. ")
        l, r = st.columns([1, 5])
        with l:
            st.image("static/img/placeholder.svg", width=100)
        with r:
            st.write("Nullam convallis urna non leo sollicitudin, non suscipit massa molestie. Vivamus mollis semper viverra. Integer condimentum libero et neque imperdiet, non efficitur mi posuere. Morbi vel eros fringilla, aliquam enim ut, mollis elit. Ut pharetra hendrerit ornare. Aenean et ipsum id augue ultricies consectetur at et nisl. Quisque mauris neque, blandit id mauris eget, luctus lobortis urna. Aenean eu nisi vitae leo commodo laoreet. ")

with right:
    with st.container(border=True):
        l, m, r = st.columns([2, 1, 2])
        with m:
            st.write("For Doctors")
        l, m, r = st.columns([1, 5, 1])
        with m:
            st.divider()
        l, r = st.columns([1, 5])
        with l:
            st.image("static/img/placeholder.svg", width=100)
        with r:
            st.write("Nullam convallis urna non leo sollicitudin, non suscipit massa molestie. Vivamus mollis semper viverra. Integer condimentum libero et neque imperdiet, non efficitur mi posuere. Morbi vel eros fringilla, aliquam enim ut, mollis elit. Ut pharetra hendrerit ornare. Aenean et ipsum id augue ultricies consectetur at et nisl. Quisque mauris neque, blandit id mauris eget, luctus lobortis urna. Aenean eu nisi vitae leo commodo laoreet. ")
        l, r = st.columns([1, 5])
        with l:
            st.image("static/img/placeholder.svg", width=100)
        with r:
            st.write("Nullam convallis urna non leo sollicitudin, non suscipit massa molestie. Vivamus mollis semper viverra. Integer condimentum libero et neque imperdiet, non efficitur mi posuere. Morbi vel eros fringilla, aliquam enim ut, mollis elit. Ut pharetra hendrerit ornare. Aenean et ipsum id augue ultricies consectetur at et nisl. Quisque mauris neque, blandit id mauris eget, luctus lobortis urna. Aenean eu nisi vitae leo commodo laoreet. ")
        l, r = st.columns([1, 5])
        with l:
            st.image("static/img/placeholder.svg", width=100)
        with r:
            st.write("Nullam convallis urna non leo sollicitudin, non suscipit massa molestie. Vivamus mollis semper viverra. Integer condimentum libero et neque imperdiet, non efficitur mi posuere. Morbi vel eros fringilla, aliquam enim ut, mollis elit. Ut pharetra hendrerit ornare. Aenean et ipsum id augue ultricies consectetur at et nisl. Quisque mauris neque, blandit id mauris eget, luctus lobortis urna. Aenean eu nisi vitae leo commodo laoreet. ")
        
        



