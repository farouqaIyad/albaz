import streamlit as st
from function import (
    transcribe_arabic_to_english,
    load_mapping,
    contains_english,
)
from streamlit_pdf_viewer import pdf_viewer
from streamlit_autorefresh import st_autorefresh

import streamlit as st

st.set_page_config(layout="wide")


mapping = load_mapping(r"rules.json")
col1,center,col2 = st.columns([2,1,2])
with center:
    st.image(r"logo.jpg",width=250)


col1,col2,col3 = st.columns([1,6,1])
with col2:
    col1,col2,col3 = st.columns([4,2,4])
    with col1:
        arabic_text = st.text_area(
            "\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0 النص العربي مشكولا",
            height=200,key = 'text_ara'
        )
    english_text = transcribe_arabic_to_english(st.session_state.text_ara, mapping)

    with col2:   
        st.markdown("###")
        st.markdown("###")         
            
        if st.button("Transliterate عَـرمِـن"):
            with col3:
                    aa = st.text_area('\u00A0\u00A0\
                                      \u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\
                                      \u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\
                                      \u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\
                                      \u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\
                                      \u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\
                                      \u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0 (BAZ) حسب نظام الباز للعرمنة ',
                            value=english_text,height=200)
        else:
            with col3:
                    aa = st.text_area('\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0 (BAZ) حسب نظام الباز للعرمنة ',
                            value=english_text,height=200)



pdf = r'dict.pdf'
col1,center,col2 = st.columns([1,2,1])

with center:
    pdf_viewer(input = pdf)


# # if arabic_text.strip() != "":
# #     if contains_english(arabic_text):
# #         st.warning("النص يحوي على احرف انجليزية او ارقام الرجاء حذفهم")
# #     else:
# #         english_text = transcribe_arabic_to_english(arabic_text, mapping)
# #         st.text_area("Translation", value=english_text, height=200)
# # else:
# #     st.warning("النص فارغ")

# # pdf = r'dict.pdf'

# # pdf_viewer(input = pdf,width = 700)
