import streamlit as st
from function import (
    transcribe_arabic_to_english,
    load_mapping,
    contains_english,
)
from streamlit_pdf_viewer import pdf_viewer


mapping = load_mapping(r"rules.json")
col1,center,col2 = st.columns(3)
with center:
    st.image(r"logo.jpg",width=200)

# Input text box for Arabic text
arabic_text = st.text_area(
    "أدخِل نصا مشكولا باللغة العربية، ليظهر لك مرومنا بنظام الباز للعرمنة", height=200
)

# Button to translate
if st.button("عرمِن/transliterate"):
    if arabic_text.strip() != "":
        if contains_english(arabic_text):
            st.warning("النص يحوي على احرف انجليزية او ارقام الرجاء حذفهم")
        else:
            english_text = transcribe_arabic_to_english(arabic_text, mapping)
            st.text_area("Translation", value=english_text, height=200)
    else:
        st.warning("النص فارغ")

pdf = r'dict.pdf'

pdf_viewer(input = pdf,width = 700)
