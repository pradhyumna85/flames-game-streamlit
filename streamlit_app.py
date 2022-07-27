import pandas as pd
import streamlit as st
from flames import flames_game

st.set_page_config(page_title='FLAMES Game', page_icon='🔥')

"""
# Welcome to 🔥FLAMES❤️ game app!

Enter Name 1 and Name 2 below to see the result!
"""

## hide menu and original footer
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

## customize footer
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: transparent;
color: white;
text-align: center;
}

a:link, a:visited {
color: yellow;
}

a:hover {
color: red;
}

</style>
<div class="footer">
<p>Developed with ❤️ by <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/pradyumnasingh/" target="_blank">Pradyumna Singh Rathore</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

name1 = st.text_input("Name 1")
name2 = st.text_input("Name 2")

if st.button('Show Result!'):
    if len(name1) and len(name2):
        result = flames_game(name1,name2)
        
        if result in ['Love','Affection','Marriage']:
            st.success(result)
        else:
            st.error(result)


