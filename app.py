import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Hyderabad Property Details",
    layout="centered"
)

st.title("Hyderabad Property Details")
st.caption("Enter buyer-focused property information")

st.subheader("Basic Property Information")

locality = st.text_input("Locality")

property_type = st.selectbox(
    "Property Type",
    ["Apartment", "Independent House", "Villa"]
)

built_up_area = st.number_input(
    "Built-up Area (sqft)",
    min_value=100,
    step=10
)

price_per_sqft = st.number_input(
    "Price per Sqft (INR)",
    min_value=1000,
    step=100
)

bedrooms = st.selectbox("Bedrooms (BHK)", [1, 2, 3, 4])
bathrooms = st.selectbox("Bathrooms", [1, 2, 3, 4])
balconies = st.selectbox("Balconies", [0, 1, 2, 3])

floor_number = st.number_input("Floor Number", min_value=0, step=1)
total_floors = st.number_input("Total Floors", min_value=0, step=1)

property_age = st.number_input(
    "Property Age (Years)",
    min_value=0,
    step=1
)

facing = st.selectbox(
    "Facing",
    ["North", "South", "East", "West", "North-East", "North-West", "South-East", "South-West"]
)

furnishing_status = st.selectbox(
    "Furnishing Status",
    ["Unfurnished", "Semi-Furnished", "Fully Furnished"]
)

car_parking = st.selectbox("Car Parking", [0, 1, 2])

st.subheader("Distance & Amenities")

distance_metro = st.number_input("Distance to Metro (km)", min_value=0.0)
distance_it_hub = st.number_input("Distance to IT Hub (km)", min_value=0.0)

nearby_schools = st.number_input("Nearby Schools (count)", min_value=0, step=1)
nearby_hospitals = st.number_input("Nearby Hospitals (count)", min_value=0, step=1)
amenities_count = st.number_input("Amenities Count", min_value=0, step=1)

st.subheader("Financial Details")

maintenance = st.number_input(
    "Monthly Maintenance (INR)",
    min_value=0,
    step=100
)

rental_yield = st.number_input(
    "Rental Yield (%)",
    min_value=0.0,
    step=0.1
)

estimated_price = st.number_input(
    "Estimated Sale Price (INR)",
    min_value=0,
    step=10000
)

buyer_score = st.slider(
    "Buyer Attraction Score (1–10)",
    1.0, 10.0, 5.0, 0.1
)

# Submit button
submitted = st.button("Submit Property Details")

# Output
if submitted:
    st.success("Property details submitted successfully")

    st.subheader("Property Summary")
    st.json({
        "Locality": locality,
        "Property Type": property_type,
        "Built-up Area (sqft)": built_up_area,
        "Price per Sqft (INR)": price_per_sqft,
        "Bedrooms (BHK)": bedrooms,
        "Bathrooms": bathrooms,
        "Balconies": balconies,
        "Floor Number": floor_number,
        "Total Floors": total_floors,
        "Property Age (Years)": property_age,
        "Facing": facing,
        "Furnishing Status": furnishing_status,
        "Car Parking": car_parking,
        "Distance to Metro (km)": distance_metro,
        "Distance to IT Hub (km)": distance_it_hub,
        "Nearby Schools": nearby_schools,
        "Nearby Hospitals": nearby_hospitals,
        "Amenities Count": amenities_count,
        "Monthly Maintenance (INR)": maintenance,
        "Rental Yield (%)": rental_yield,
        "Estimated Sale Price (INR)": estimated_price,
        "Buyer Attraction Score": buyer_score
    })
