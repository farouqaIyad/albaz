import streamlit as st
from function import (
    transcribe_arabic_to_english,
    load_mapping,
    contains_english,
)
from dairect import get_tashkeel
from streamlit_pdf_viewer import pdf_viewer
from streamlit_autorefresh import st_autorefresh
import ast
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

st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

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
# st.markdown(
#         """
#         <style>
#         .footer {
#             position: fixed;
#             left: 0;
#             bottom: 0;
#             width: 100%;
#             background-color: #f1f1f1;
#             color: black;
#             text-align: center;
#             padding: 10px;
#             font-size: 14px;
#         }
#         </style>
#         <div class="footer">
#             <p>إذا وجدت خطأ ما نرجو التواصل لنحل المشكلة    
#             <a href="https://wa.me/+966567203053" target="_blank"> +966567203053</a></p>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )