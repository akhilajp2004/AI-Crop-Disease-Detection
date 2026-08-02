import streamlit as st
from PIL import Image
import time
from predict import predict_disease
from treatment import get_treatment

st.set_page_config(
    page_title="AI Crop Disease Detection",
    page_icon="🌿",
    layout="centered"
)

st.title("🌿 AI Crop Disease Detection")

st.write(
    "Upload a crop leaf image to identify the disease and receive treatment recommendations."
)

st.divider()

st.subheader("Upload Leaf Image")

uploaded_file = st.file_uploader(
    "Choose a leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is None:

    st.info("Please upload a leaf image.")

else:

    image = Image.open(uploaded_file)

    st.success("Image uploaded successfully!")

    st.image(
        image,
        caption="Uploaded Leaf Image",
        use_container_width=True
    )

    if st.button("Predict Disease"):

        with st.spinner("Analyzing leaf image..."):

            time.sleep(2)

            disease, confidence = predict_disease(image)

        st.success("Prediction completed!")

        st.subheader("Prediction Result")

        st.write(f"### Disease")
        st.success(disease)

        st.write(f"### Confidence")
        st.info(f"{confidence}%")

        treatment = get_treatment(disease)

        st.write("### Recommended Treatment")

        st.warning(treatment)