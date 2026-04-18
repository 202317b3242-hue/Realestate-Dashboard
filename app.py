import streamlit as st
import pandas as pd

st.title("Hyderabad Real Estate – Data Preview")

# -------------------------------------------------
# Embedded dataset with multiple localities
# -------------------------------------------------
data = [
    {
        "Property ID": 50001,
        "Locality": "Banjara Hills",
        "Property Type": "Apartment",
        "Built-up Area (sqft)": 1283,
        "Price per Sqft (INR)": 7461,
        "Bedrooms (BHK)": 3,
        "Estimated Sale Price (INR)": 9572463
    },
    {
        "Property ID": 50002,
        "Locality": "Kondapur",
        "Property Type": "Independent House",
        "Built-up Area (sqft)": 1263,
        "Price per Sqft (INR)": 9473,
        "Bedrooms (BHK)": 3,
        "Estimated Sale Price (INR)": 11964399
    },
    {
        "Property ID": 50003,
        "Locality": "Nizampet",
        "Property Type": "Apartment",
        "Built-up Area (sqft)": 2598,
        "Price per Sqft (INR)": 8933,
        "Bedrooms (BHK)": 3,
        "Estimated Sale Price (INR)": 23207934
    },
    {
        "Property ID": 50004,
        "Locality": "Jubilee Hills",
        "Property Type": "Apartment",
        "Built-up Area (sqft)": 2231,
        "Price per Sqft (INR)": 8277,
        "Bedrooms (BHK)": 4,
        "Estimated Sale Price (INR)": 18465987
    },
    {
        "Property ID": 50005,
        "Locality": "HITEC City",
        "Property Type": "Apartment",
        "Built-up Area (sqft)": 2120,
        "Price per Sqft (INR)": 5456,
        "Bedrooms (BHK)": 3,
        "Estimated Sale Price (INR)": 11566720
    },
    {
        "Property ID": 50006,
        "Locality": "Madhapur",
        "Property Type": "Villa",
        "Built-up Area (sqft)": 2359,
        "Price per Sqft (INR)": 7604,
        "Bedrooms (BHK)": 2,
        "Estimated Sale Price (INR)": 17937836
    },
    {
        "Property ID": 50007,
        "Locality": "Gachibowli",
        "Property Type": "Villa",
        "Built-up Area (sqft)": 2295,
        "Price per Sqft (INR)": 6193,
        "Bedrooms (BHK)": 3,
        "Estimated Sale Price (INR)": 14212935
    },
    {
        "Property ID": 50008,
        "Locality": "Kukatpally",
        "Property Type": "Independent House",
        "Built-up Area (sqft)": 2095,
        "Price per Sqft (INR)": 7369,
        "Bedrooms (BHK)": 2,
        "Estimated Sale Price (INR)": 15438055
    },
    {
        "Property ID": 50009,
        "Locality": "LB Nagar",
        "Property Type": "Apartment",
        "Built-up Area (sqft)": 2307,
        "Price per Sqft (INR)": 7946,
        "Bedrooms (BHK)": 3,
        "Estimated Sale Price (INR)": 18331422
    },
    {
        "Property ID": 50010,
        "Locality": "Uppal",
        "Property Type": "Independent House",
        "Built-up Area (sqft)": 2453,
        "Price per Sqft (INR)": 8291,
        "Bedrooms (BHK)": 4,
        "Estimated Sale Price (INR)": 20337823
    }
]

df = pd.DataFrame(data)

# -------------------------------------------------
# Locality filter
# -------------------------------------------------
localities = sorted(df["Locality"].unique())

selected_locality = st.selectbox(
    "Select Locality",
    ["All"] + localities
)

if selected_locality != "All":
    df = df[df["Locality"] == selected_locality]

st.write(f"Showing **{len(df)}** records")
st.dataframe(df, use_container_width=True)
