import streamlit as st

# App setup
st.set_page_config(page_title="Health Info Assistant", layout="centered")
st.title("🩺 Health Info Assistant")
st.write("Ask a health-related question to receive basic info and suggestions.")

# Input
query = st.text_input("Your question:")

# Health response logic
def get_health_response(question):
    question = question.lower()

    if "fever" in question:
        return (
            "Fever often indicates an infection and may come with chills or fatigue.\n"
            "Stay hydrated and take adequate rest.\n"
            "You may use Paracetamol 500mg every 4–6 hours (max 4/day) to reduce fever.\n"
            "If temperature exceeds 102°F or lasts more than 2 days, consult a doctor.\n"
            "Avoid antibiotics without a medical prescription."
        )

    elif "headache" in question:
        return (
            "Headaches may result from stress, dehydration, or screen exposure.\n"
            "Rest in a quiet room, reduce screen time, and stay hydrated.\n"
            "Paracetamol or Ibuprofen (if not allergic) can help relieve pain.\n"
            "If frequent or severe, it may be migraine — seek medical advice.\n"
            "Avoid excessive caffeine and get enough sleep."
        )

    elif "diet" in question:
        return (
            "A balanced diet helps maintain energy and immunity.\n"
            "Include fruits, vegetables, whole grains, lean protein, and healthy fats.\n"
            "Limit sugar, fried foods, and processed snacks.\n"
            "Drink at least 2–3 liters of water daily.\n"
            "Supplements like multivitamins can help if prescribed by a doctor."
        )

    elif "mental health" in question or "stress" in question:
        return (
            "Mental health matters as much as physical health.\n"
            "Practice mindfulness, take breaks, and engage in hobbies or exercise.\n"
            "Talk to a counselor if feeling persistently anxious or low.\n"
            "Sleep aids like melatonin or herbal teas can help relax.\n"
            "Avoid alcohol or self-medication — seek support when needed."
        )

    else:
        return (
            "Sorry, I don't have information on that topic.\n"
            "Try asking about fever, headache, diet, stress, or mental health.\n"
            "For specific medical concerns, consult a certified healthcare provider.\n"
            "This tool offers general guidance, not personalized medical advice.\n"
            "Avoid taking medications without medical supervision."
        )

# Output
if query:
    response = get_health_response(query)
    st.subheader("Health Info:")
    st.write(response)
    st.markdown("⚠️ _Disclaimer: This assistant provides general information only. Always consult a qualified doctor for diagnosis and treatment._")
