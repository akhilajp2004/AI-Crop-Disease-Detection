def get_treatment(disease):

    treatments = {

    "🍂 Tomato Early Blight":
    "Spray Mancozeb or Chlorothalonil. Remove infected leaves and avoid overhead irrigation.",

    "🍂 Tomato Late Blight":
    "Apply Copper-based fungicide immediately. Remove infected plants and avoid excess moisture.",

    "🍂 Tomato Leaf Mold":
    "Improve air circulation, reduce humidity, and apply a recommended fungicide.",

    "🍂 Tomato Septoria Leaf Spot":
    "Remove infected leaves, rotate crops, and spray an appropriate fungicide.",

    "🌿 Healthy Tomato Leaf":
    "No disease detected. Continue regular watering, fertilization, and crop monitoring."

}
    return treatments.get(disease, "Consult an agricultural expert.")