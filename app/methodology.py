import streamlit as st
import pandas as pd
import numpy as np


with st.container(border=True):

    left, middle, right = st.columns([1, 2, 1])

    with middle: 
        st.title("How does our tool work?")
    
    st.write("Models")

    left, middle, right = st.columns([1, 1, 1])

    with left:
        st.write("Logistic Regression")
    with middle: 
        st.write("Random Forest")
    with right:
        st.write("Neural Network")

    left, middle, right = st.columns([1, 1, 1])

    with left:
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse facilisis eros ac neque pulvinar, in convallis leo ullamcorper. Vestibulum aliquam ut eros ut placerat. Integer ullamcorper eros ut odio venenatis sollicitudin. Cras pulvinar augue eget tortor mollis dapibus. Aenean a nisl diam. Fusce imperdiet risus augue. In eu dui vel justo dictum congue vitae ac ante. Aenean lacinia felis lectus, in luctus leo dignissim vel. Vestibulum sollicitudin eleifend dui, volutpat luctus augue pellentesque eget. In semper enim massa, nec dictum risus ornare ut. Quisque ut mattis est. Interdum et malesuada fames ac ante ipsum primis in faucibus. ")
    with middle: 
        st.write("Cras id augue nisl. Pellentesque ut nisi nec ipsum accumsan aliquam congue sed neque. Nullam purus lorem, viverra vel viverra at, iaculis eu lorem. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse potenti. Donec nec odio volutpat, sollicitudin orci vel, interdum tellus. Donec felis quam, tempor interdum posuere eu, varius in nulla. Fusce elementum mauris vel nulla rhoncus porttitor. Cras commodo sagittis augue sed sagittis. Curabitur efficitur efficitur risus in pharetra. Proin volutpat convallis lorem in eleifend. Etiam ut auctor neque. Aenean tincidunt, enim in eleifend malesuada, diam leo hendrerit diam, vitae rhoncus leo risus eget massa. Suspendisse at ante pellentesque, consectetur arcu at, semper nibh. Etiam a metus massa. ")
    with right:
        st.write("Nullam convallis urna non leo sollicitudin, non suscipit massa molestie. Vivamus mollis semper viverra. Integer condimentum libero et neque imperdiet, non efficitur mi posuere. Morbi vel eros fringilla, aliquam enim ut, mollis elit. Ut pharetra hendrerit ornare. Aenean et ipsum id augue ultricies consectetur at et nisl. Quisque mauris neque, blandit id mauris eget, luctus lobortis urna. Aenean eu nisi vitae leo commodo laoreet. ")

    st.write("Training dataset")
    st.write("Nullam convallis urna non leo sollicitudin, non suscipit massa molestie. Vivamus mollis semper viverra. Integer condimentum libero et neque imperdiet, non efficitur mi posuere. Morbi vel eros fringilla, aliquam enim ut, mollis elit. Ut pharetra hendrerit ornare. Aenean et ipsum id augue ultricies consectetur at et nisl. Quisque mauris neque, blandit id mauris eget, luctus lobortis urna. Aenean eu nisi vitae leo commodo laoreet. ")

    st.write("Description and metadata")
    st.write("Nullam convallis urna non leo sollicitudin, non suscipit massa molestie. Vivamus mollis semper viverra. Integer condimentum libero et neque imperdiet, non efficitur mi posuere. Morbi vel eros fringilla, aliquam enim ut, mollis elit. Ut pharetra hendrerit ornare. Aenean et ipsum id augue ultricies consectetur at et nisl. Quisque mauris neque, blandit id mauris eget, luctus lobortis urna. Aenean eu nisi vitae leo commodo laoreet. ")


    

