def get_treatment(disease):

    treatments = {

        "Tomato Early Blight":
        """Spray Mancozeb fungicide.
Remove infected leaves.
Avoid overhead irrigation.
Monitor plants regularly.""",

        "Healthy":
        """No disease detected.
Maintain regular watering.
Continue normal crop care."""
    }

    return treatments.get(
        disease,
        "Consult an agricultural expert."
    )