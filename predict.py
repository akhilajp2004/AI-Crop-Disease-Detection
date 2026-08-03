import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Load trained model
model = load_model("models/crop_model.keras")

# IMPORTANT: Must match train_generator.class_indices
class_names = [
    "🍂 Tomato Early Blight",
    "🍂 Tomato Late Blight",
    "🍂 Tomato Leaf Mold",
    "🍂 Tomato Septoria Leaf Spot",
    "🌿 Healthy Tomato Leaf"
]

def predict_disease(image):

    # Convert to RGB (important for uploaded images)
    image = image.convert("RGB")

    # Resize image
    image = image.resize((128, 128))

    # Convert to NumPy array
    image = np.array(image)

    # Normalize
    image = image / 255.0

    # Add batch dimension
    image = np.expand_dims(image, axis=0)

    # Predict
    prediction = model.predict(image, verbose=0)

    predicted_class = np.argmax(prediction)

    confidence = float(np.max(prediction) * 100)

    disease = class_names[predicted_class]

    return disease, round(confidence, 2)