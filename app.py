import pandas as pd
import streamlit as st

# Load CSV
df = pd.read_csv("backend/recipes1.csv")

# Streamlit UI
st.title("Kitchen coder🍇")
dish_name = st.text_input("Enter dish name:")

if dish_name:
    dish_name_lower = dish_name.lower()
    matched = df[df['Dish'].str.lower() == dish_name_lower]
    if not matched.empty:
        recipe_info = matched.iloc[0]
        st.write(f"**cuisine:** {recipe1_info['cooking style']}")
        st.write(f"**Dish:** {recipe1_info['Dish']}")
        st.write(f"**Time:** {recipe1_info['Time']} mins")
        st.write(f"**Tips:** {recipe1_info['Tips']}")
        st.write(f"**Recipe Steps:** {recipe1_info['Recipe']}")
    else:
        st.write("Sorry, recipe not found.")
