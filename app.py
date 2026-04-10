import streamlit as st
import pandas as pd

# Base recipe from the book
# Original yields 1807g total dough (enough for approx. 5.16 x 350g balls)
BASE_RECIPE = {
    "Bread flour": 1000,
    "Cold water": 590,
    "Poolish": 150,
    "Dry yeast": 2,
    "Salt": 25,
    "Olive oil": 40
}

# The book's stated baker's percentages (relative to 1075g total flour)
BAKERS_PERCENTAGES = {
    "Bread flour": "93%",
    "Cold water": "59%",
    "Poolish": "15%",
    "Dry yeast": "0.18%",
    "Salt": "2.3%",
    "Olive oil": "3.7%"
}

BASE_TOTAL_WEIGHT = sum(BASE_RECIPE.values())

# --- Page Setup ---
st.set_page_config(page_title="NY Pizza Dough Scaler", page_icon="🍕", layout="centered")

st.title("🍕 NY-Style Dough Calculator")
st.markdown("Adjust your ingredient weights automatically based on your desired yield.")

# --- Input Section ---
st.subheader("Yield Requirements")
col1, col2 = st.columns(2)
with col1:
    num_balls = st.number_input("Number of Dough Balls", min_value=1, value=4, step=1)
with col2:
    ball_weight = st.number_input(
        "Weight per Ball (grams)", 
        min_value=50, 
        value=350, 
        step=10, 
        help="The recipe recommends 350g for 14-inch pies or 250g for 12-inch pies."
    )

target_total_weight = num_balls * ball_weight
scaling_factor = target_total_weight / BASE_TOTAL_WEIGHT

# --- Calculation Section ---
st.markdown("---")
st.subheader(f"Scaled Ingredients (Target: {target_total_weight}g total dough)")

# Calculate scaled ingredients and round to 1 decimal place
scaled_data = []
for ingredient, weight in BASE_RECIPE.items():
    adjusted_weight = round(weight * scaling_factor, 1)
    scaled_data.append({
        "Ingredient": ingredient,
        "Weight (g)": adjusted_weight,
        "Baker's % (Image)": BAKERS_PERCENTAGES[ingredient]
    })

# Display as a clean table
df = pd.DataFrame(scaled_data)
st.dataframe(df, hide_index=True, use_container_width=True)

# --- Instructions Section ---
st.markdown("### 📝 Quick Prep Reminder")
st.markdown("""
1. **Water Split:** Divide your scaled water into two batches. 
2. **First Mix:** Combine first water, yeast, and poolish on slow speed. 
3. **Flour Mix:** Add flour, mix on slow for 5 mins until no dry bits remain. Rest 1-2 mins.
4. **Salt & Second Water:** Add salt and the rest of the water. Mix on medium for 2 mins. Rest 2 mins.
5. **Oil Integration:** Restart on medium, gradually adding oil until combined. Rest 5 mins.
6. **Fermentation:** Ball up, leave at room temp for 1-2 hours, then cold ferment in the fridge for 24-48 hours.
""")
