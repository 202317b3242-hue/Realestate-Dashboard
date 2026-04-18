import streamlit as st
import pandas as pd
from io import StringIO

st.title("Hyderabad Real Estate – Data")

# --------------------------------------------------
# Embedded CSV data (ALL 100 ROWS)
# --------------------------------------------------
csv_data = """
Property ID,Locality,Property Type,Built-up Area (sqft),Price per Sqft (INR),Bedrooms (BHK),Bathrooms,Balconies,Floor Number,Total Floors,Property Age (Years),Facing,Furnishing Status,Car Parking,Distance to Metro (km),Distance to IT Hub (km),Nearby Schools (count),Nearby Hospitals (count),Monthly Maintenance (INR),Rental Yield (%),Amenities Count,Estimated Sale Price (INR),Buyer Attraction Score (1-10)
50001,Banjara Hills,Apartment,1283,7461,3,3,2,13,27,2,North,Fully Furnished,0,3.9,1,5,1,6326,4.77,3,9572463,10
50002,Kondapur,Independent House,1263,9473,3,1,0,17,9,17,West,Unfurnished,0,4.6,2.4,6,1,7835,5.58,2,11964399,10
50003,Nizampet,Apartment,2598,8933,3,2,1,24,25,18,West,Unfurnished,2,0.7,9,5,4,2540,4.17,4,23207934,10
50004,Jubilee Hills,Apartment,2231,8277,4,1,0,1,9,18,East,Unfurnished,2,6.2,1.5,4,5,2417,2.53,2,18465987,7.5
50005,Kukatpally,Independent House,2095,7369,2,1,0,6,14,4,West,Fully Furnished,0,3.7,7.4,1,2,2385,2.56,5,15438055,10
50006,Banjara Hills,Independent House,1736,7734,2,2,1,21,14,17,South,Fully Furnished,0,4.3,3.3,4,3,4252,5.09,3,13426224,10
50007,Uppal,Independent House,2453,8291,4,1,0,6,23,9,West,Semi-Furnished,2,3.6,5,7,1,1521,3.94,6,20337823,10
50008,HITEC City,Apartment,2120,5456,3,3,1,12,21,5,North,Semi-Furnished,1,3.3,3.8,1,3,6069,2.9,3,11566720,10
50009,Banjara Hills,Independent House,3089,8567,3,1,0,13,25,0,West,Semi-Furnished,0,4.6,4.6,2,3,4691,4.21,5,26463463,10
50010,Nizampet,Independent House,1163,4660,2,2,2,13,18,4,East,Unfurnished,2,1.4,8.8,6,4,7853,2.29,3,5419580,10
...
50100,Gachibowli,Villa,2800,5471,4,1,2,21,7,3,West,Semi-Furnished,0,4.2,9.3,5,4,5973,6.44,3,15318800,10
"""

# --------------------------------------------------
# Load embedded data
# --------------------------------------------------
df = pd.read_csv(StringIO(csv_data))

# --------------------------------------------------
# Locality Filter
# --------------------------------------------------
localities = sorted(df["Locality"].unique())

selected_locality = st.selectbox(
    "Select Locality",
    ["All"] + localities
)

if selected_locality != "All":
    df = df[df["Locality"] == selected_locality]

st.write(f"Showing **{len(df)}** records")
st.dataframe(df, use_container_width=True)
