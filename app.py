import io

import streamlit as st

from generator import generate_decoder_image

# Create simple Streamlit App for Decoder image generation

st.set_page_config(
    page_title="Decoder Image Generator",
    page_icon="🔎",
    layout="centered",
)

st.title("🔎 Secret Text Generator")

text = st.text_input("Secret Text", value="Top Secret!", icon="📝")

col1, col2 = st.columns(2)

with col1:
    width = st.number_input("Width of Image", min_value=0, step=1, icon="↔", value=1000)

with col2:
    height = st.number_input(
        "Height of Image", min_value=0, step=1, icon="↕", value=500
    )

font_size = st.number_input("Font Size", min_value=0, step=5, icon="🅰", value=100)

alpha = st.slider("🔅 Opacity of Text", min_value=0, max_value=100, value=10)

img = generate_decoder_image(
    text=text, width=width, height=height, alpha=alpha, font_size=font_size
)

st.image(img)

buf = io.BytesIO()
img.save(buf, format="PNG")
byte_im = buf.getvalue()

if st.download_button(
    "**Save image**",
    data=byte_im,
    mime="image/png",
    icon="💾",
    file_name="secret_text.png",
):
    st.success("✅ Image downloaded successfully!")
    st.balloons()
