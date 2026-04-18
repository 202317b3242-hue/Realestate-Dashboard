import streamlit as st
import pandas as pd

st.title("Hyderabad Real Estate – Data")

# -------------------------------------------------
# Embedded data (sample        "Property ID": 50001,# Embedded data (sample from your dataset)
        "Locality": "Banjara Hills",
        "Property Type": "Apartment",
        "Built-up Area (sqft)": 1283,
        "Price per Sqft (INR)": 7461,
        "Bedrooms (BHK)": 3,
        "Estimated Sale Price (INR)": 9572463,
        "Buyer Attraction Score": 10
    },
    {
        "Property ID": 50002,
        "Locality": "Kondapur",
        "Property Type": "Independent House",
        "Built-up Area (sqft)": 1263,
        "Price per Sqft (INR)": 9473,
        "Bedrooms (BHK)": 3,
        "Estimated Sale Price (INR)": 11964399,
        "Buyer Attraction Score": 10
    },
    {
        "Property ID": 50003,
        "Locality": "Nizampet",
        "Property Type": "Apartment",
        "Built-up Area (sqft)": 2598,
        "Price per Sqft (INR)": 8933,
        "Bedrooms (BHK)": 3,
        "Estimated Sale Price (INR)": 23207934,
        "Buyer Attraction Score": 10
    },
    {
        "Property ID": 50004,
        "Locality": "Jubilee Hills",
        "Property Type": "Apartment",
        "Built-up Area (sqft)": 2231,
        "Price per Sqft (INR)": 8277,
        "Bedrooms (BHK)": 4,
        "Estimated Sale Price (INR)": 18465987,
        "Buyer Attraction Score": 7.5
    }
]

df = pd.DataFrame(data)

# -------------------------------------------------
# Locality filter
# -------------------------------------------------
localities = sorted(df["Locality"].unique())

selected_locality = st.selectbox(
    "Select Locality",
    options=["All"] + localities
)

if selected_locality != "All":
    df_filtered = df[df["Locality"] == selected_locality]
else:
    df_filtered = df

st.write(f"Showing **{len(df_filtered)}** records")

# -------------------------------------------------
# Data preview
# -------------------------------------------------
st.dataframe(df_filtered, use_container_width=True)
# -------------------------------------------------
data = [
    {
