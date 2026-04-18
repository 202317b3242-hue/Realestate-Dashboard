import streamlit as st

st.set_page_config(
    page_title="Hyderabad Property Details",
    layout="centered"
)

st.title("Hyderabad Property Details")
st.caption("Buyer-focused property entry form")

locality = st.text_input("Locality")
property_type = st.selectbox(
    "Property Type",
    ["Apartment", "Independent House", "Villa"]
)

built_up_area = st.number_input(
    "Built-up Area (sqft)", min_value=100, step=10
)

price_per_sqft = st.number_input(
    "Price per Sqft (INR)", min_value=1000, step=100
)

bedrooms = st.selectbox("Bedrooms (BHK)", [1, 2, 3, 4])
bathrooms = st.selectbox("Bathrooms", [1, 2, 3, 4])
balconies = st.selectbox("Balconies", [0, 1, 2, 3])

property_age = st.number_input("Property Age (Years)", min_value=0)
facing = st.selectbox(
    "Facing",
    ["North", "South", "East", "West",
     "North-East", "North-West", "South-East", "South-West"]
)

furnishing_status = st.selectbox(
    "Furnishing Status",
    ["Unfurnished", "Semi-Furnished", "Fully Furnished"]
)

car_parking = st.selectbox("Car Parking", [0, 1, 2])

estimated_price = st.number_input(
    "Estimated Sale Price (INR)", min_value=0, step=10000
)

buyer_score = st.slider(
    "Buyer Attraction Score (1–10)", 1.0, 10.0, 5.0, 0.1
)

if st.button("Submit"):
    st.success("Property details captured successfully")
    st.json({
        "Locality": locality,
        "Property Type": property_type,
        "Built-up Area (sqft)": built_up_area,
        "Price per Sqft (INR)": price_per_sqft,
        "Bedrooms (BHK)": bedrooms,
        "Bathrooms": bathrooms,
        "Balconies": balconies,
        "Property Age (Years)": property_age,
        "Facing": facing,
        "Furnishing Status": furnishing_status,
        "Car Parking": car_parking,
        "Estimated Sale Price (INR)": estimated_price,
        "Buyer Attraction Score": buyer_score
    })
