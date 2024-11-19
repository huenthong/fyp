import streamlit as st
import openai

# Define product categories, features, benefits, and additional criteria
product_categories = [
    "Smartphones",
    "Laptops",
    "Smartwatches",
    "Headphones",
    "Gaming Consoles",
    "Tablets",
    "Monitors",
    "Smart Home Devices"
]
product_features = [
    "Long battery life",
    "High-resolution display",
    "Fast charging",
    "Lightweight design",
    "Advanced noise cancellation",
    "Water resistance",
    "High performance",
    "Large storage capacity"
]
product_benefits = [
    "Improved productivity",
    "Seamless entertainment",
    "Enhanced health tracking",
    "Immersive gaming",
    "Clearer communication",
    "Convenience for work and travel",
    "Efficient multitasking",
    "Smart home integration"
]
use_cases = ["Work from home", "Fitness tracking", "Travel", "Gaming", "Daily communication", "Streaming", "Content creation"]
budget_options = ["Budget-friendly", "Mid-range", "Premium", "Luxury"]
tones = ["Professional", "Friendly", "Tech-savvy", "Enthusiastic"]

# Function to generate product recommendation
def generate_recommendation(category, features, benefits, use_case, budget, tone):
    prompt = f"""
    You're an expert product recommender. Suggest the best {category} based on the following user preferences:
    
    **Key Features:** {', '.join(features)}
    **Desired Benefits:** {', '.join(benefits)}
    **Use Case:** {use_case}
    **Budget Preference:** {budget}
    **Tone:** {tone}

    Provide a detailed and tailored product recommendation explaining why it matches their preferences.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a knowledgeable product recommendation expert."},
            {"role": "user", "content": prompt}
        ]
    )
    recommendation = response['choices'][0]['message']['content']
    return recommendation

# Streamlit UI
st.title("Virtual Electronic Product Recommender System")
st.markdown("""
This tool helps you find the best electronic products tailored to your needs and preferences. 
Simply select your preferences, and we'll recommend the perfect product for you.
""")

# User inputs
selected_category = st.selectbox("Product Category:", product_categories)
selected_features = st.multiselect("Key Features:", product_features)
selected_benefits = st.multiselect("Desired Benefits:", product_benefits)
selected_use_case = st.selectbox("Use Case:", use_cases)
selected_budget = st.selectbox("Budget Preference:", budget_options)
selected_tone = st.selectbox("Tone of Recommendation:", tones)

# Generate recommendation on button click
if st.button("Get Recommendation"):
    if not selected_features or not selected_benefits:
        st.warning("Please select at least one feature and one benefit.")
    else:
        recommendation = generate_recommendation(
            selected_category,
            selected_features,
            selected_benefits,
            selected_use_case,
            selected_budget,
            selected_tone
        )
        st.subheader("Recommended Product:")
        st.write(recommendation)

# Sidebar with additional information
st.sidebar.title("About This Tool")
st.sidebar.markdown("""
This product recommender is powered by AI and provides suggestions for electronic products based on your preferences.
- **Categories** include a wide range of electronic devices.
- **Features** and **benefits** help refine the search for a perfect match.
- Select your **use case** and **budget** to personalize results further.

Built using Streamlit and OpenAI's GPT model.
""")
