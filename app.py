import streamlit as st
from keras.preprocessing import image # type: ignore
import numpy as np
from keras.models import model_from_json # type: ignore
from PIL import Image

# Initialize name_scope_stack as an empty list
name_scope_stack = []

# Load the CNN model architecture from JSON file
with open("cnn.json", "r") as json_file:
    loaded_model_json = json_file.read()
    
# Load the model architecture and weights
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights('model_weights.weights.h5')

# Function to make predictions on the test image
def predict(test_image):
    test_image = test_image.resize((64, 64))
    test_image = np.array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = loaded_model.predict(test_image)
    return result

st.sidebar.image(r"C:\Users\Ali\Downloads\transparent-stethoscope-serious-female-doctor-with-stethoscope-white-coat65ee80efa29936.918574981710129391666.png", width=320, use_column_width=True)
# Button to trigger the prediction
st.sidebar.title('🔒Instructions for Using the Web Application:')
st.sidebar.subheader('1. Upload Image')
st.sidebar.write('Click on the "Choose an image" button to select an image file (JPEG, PNG, or WebP format) from your device.')
st.sidebar.subheader('2. View Uploaded Image')
st.sidebar.write("Once you've uploaded an image, it will be displayed below the upload button.")
st.sidebar.subheader('3. Predict')
st.sidebar.write('Click on the "Check" button to analyze the uploaded image and get a prediction result.')
st.sidebar.subheader('4. Result Display')
st.sidebar.write('After clicking the "Check" button, the prediction result (either "Fractured" or "Normal") will be displayed below.')
st.sidebar.title(':memo: Author')
st.sidebar.subheader('Mohammad Ali')
st.title("Bone Fracture Predictor")
#st.sidebar.title('Description :scroll:')
#st.sidebar.write("This web application utilizes a Convolutional Neural Network (CNN) model to predict whether an uploaded medical image indicates a fractured bone or not. Users can easily upload an image of a bone scan or X-ray in JPEG, PNG, or WebP format. Once uploaded, the application processes the image and displays the prediction result, indicating whether the bone is fractured or normal. With a simple and intuitive interface, users can quickly assess the likelihood of bone fractures based on their medical images. This tool serves as a convenient aid for medical professionals and individuals seeking preliminary insights into bone health conditions..")
st.sidebar.title('Connect :link:')
st.sidebar.link_button(':large_blue_diamond: Linkdin', url='https://www.linkedin.com/in/mohdali02/')
st.sidebar.link_button(':black_large_square: Github ', url='github.com/Mohd-Ali2')



# User interface for uploading an image
upload_file = st.file_uploader('Choose an image', type=['jpeg', 'png', 'webp'])
if upload_file is None:
    st.image(r"C:\Users\Ali\Downloads\vecteezy_3d-robot-illustration-kawaii-friendly-suitable-for-tech-mascot_23220595.png",use_column_width=False, width=310)
# Display the uploaded image
if upload_file is not None:
    uploaded_image = Image.open(upload_file)
    st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)



if st.button('Check'):
    if upload_file is not None:
        # Make prediction using the uploaded image
        results = predict(uploaded_image)
        # Display the prediction result
        if results[0][0] == 0:
            st.write('Fractured :heavy_exclamation_mark:')
        else:
            st.write('Normal:white_check_mark:')
    else:
        st.write("Please upload an X-RAY image .")
