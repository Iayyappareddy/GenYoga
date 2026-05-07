import pickle
import os
from .preprocess import clean_text

# ===============================
# Load Models (once)
# ===============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

body_model = pickle.load(open(os.path.join(BASE_DIR, '..', 'models', 'body_model.pkl'), 'rb'))
body_vectorizer = pickle.load(open(os.path.join(BASE_DIR, '..', 'models', 'body_vectorizer.pkl'), 'rb'))

level_model = pickle.load(open(os.path.join(BASE_DIR, '..', 'models', 'level_model.pkl'), 'rb'))
level_vectorizer = pickle.load(open(os.path.join(BASE_DIR, '..', 'models', 'level_vectorizer.pkl'), 'rb'))


# ===============================
# MAIN FUNCTION FOR DJANGO
# ===============================
def predict(description, duration_choice):
    
    # Map duration input
    duration_map = {
        "1": "1–3 days",
        "2": "About 1 week",
        "3": "More than 2 weeks"
    }

    duration = duration_map.get(duration_choice, "1–3 days")

    # Preprocess
    cleaned_input = clean_text(description)

    # ML Prediction
    body_input = body_vectorizer.transform([cleaned_input])
    level_input = level_vectorizer.transform([cleaned_input])

    predicted_body = body_model.predict(body_input)[0]
    predicted_level = level_model.predict(level_input)[0]

    # Adjust level based on duration
    if duration == "1–3 days":
        if predicted_level == "advanced":
            predicted_level = "intermediate"

    elif duration == "About 1 week":
        if predicted_level == "beginner":
            predicted_level = "intermediate"

    elif duration == "More than 2 weeks":
        if predicted_level == "beginner":
            predicted_level = "intermediate"
        elif predicted_level == "intermediate":
            predicted_level = "advanced"

    return predicted_body, predicted_level