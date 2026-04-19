import streamlit as st
import pandas as pd


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Hyderabad Real Estate Dashboard",
    layout="wide",
)

st.title("Hyderabad Real Estate Buyer Dashboard")
st.markdown("Buyer-focused analysis using embedded property data")

# ---------------------------------------------------------
# EMBEDDED DATA (NO FILE UPLOAD REQUIRED)
# ---------------------------------------------------------
@st.cache_data
def load_data():
    data = [
        [50001, "Banjara Hills", "Apartment", 1283, 7461, 3, 3, 9572463, 4.77, 10],
        [50002, "Kondapur", "Independent House", 1263, 9473, 3, 1, 11964399, 5.58, 10],
        [50003, "Nizampet", "Apartment", 2598, 8933, 3, 2, 23207934, 4.17, 10],
        [50004, "Jubilee Hills", "Apartment", 2231, 8277, 4, 1, 18465987, 2.53, 7.5],
        [50005, "Kukatpally", "Independent House", 2095, 7369, 2, 1, 15438055, 2.56, 10],
        [50008, "HITEC City", "Apartment", 2120, 5456, 3, 3, 11566720, 2.90, 10],
        [50014, "Kondapur", "Villa", 2760, 8487, 3, 2, 23424120, 3.40, 10],
        [50020, "Madhapur", "Villa", 2359, 7604, 2, 2, 17937836, 4.70, 10],
        [50027, "Gachibowli", "Villa", 2295, 6193, 3, 2, 14212935, 2.47, 10],
        [50032, "Manikonda", "Apartment", 802, 4725, 1, 2, 3789450, 4.78, 10],
        [50037, "LB Nagar", "Apartment", 2927, 5315, 3, 2, 15557005, 4.33, 10],
        [50041, "Banjara Hills", "Villa", 2791, 7620, 4, 3, 21267420, 2.35, 6.6],
        [50055, "Madhapur", "Villa", 2334, 7670, 3, 3, 17901780, 4.44, 10],
        [50064, "Banjara Hills", "Independent House", 3120, 7827, 1, 2, 24420240, 4.46, 9.6],
        [50070, "Madhapur", "Apartment", 2387, 9942, 1, 2, 23731554, 2.37, 10],
        [50085, "Jubilee Hills", "Apartment", 1754, 8841, 1, 1, 15507114, 6.48, 10],
        [50093, "Jubilee Hills", "Villa", 2043, 8631, 1, 3, 17633133, 4.08, 10],
        [50100, "Gachibowli", "Villa", 2800, 5471, 4, 1, 15318800, 6.44, 10],
    ]

    columns = [
        "Property ID",
        "Locality",
        "Property Type",
        "Built-up Area (sqft)",
        "Price per Sqft",
        "Bedrooms (BHK)",
        "Bathrooms",
        "Estimated Sale Price",
        "Rental Yield (%)",
        "Buyer Attraction Score",
    ]

    return pd.DataFrame(data, columns=columns)


df = load_data()

# ---------------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------------
st.sidebar.header("🔎 Filters")

locality = st.sidebar.multiselect(
    "Select Locality",
    sorted(df["Locality"].unique()),
    default=df["Locality"].unique(),
)

property_type = st.sidebar.multiselect(
    "Property Type",
    df["Property Type"].unique(),
    default=df["Property Type"].unique(),
)

bhk = st.sidebar.multiselect(
    "Bedrooms (BHK)",
    sorted(df["Bedrooms (BHK)"].unique()),
    default=df["Bedrooms (BHK)"].unique(),
)

budget = st.sidebar.slider(
    "Budget (INR)",
    int(df["Estimated Sale Price"].min()),
    int(df["Estimated Sale Price"].max()),
    (
        int(df["Estimated Sale Price"].min()),
        int(df["Estimated Sale Price"].max()),
    ),
)

# ---------------------------------------------------------
# FILTER DATA
# ---------------------------------------------------------
filtered_df = df[
    (df["Locality"].isin(locality)) &
    (df["Property Type"].isin(property_type)) &
    (df["Bedrooms (BHK)"].isin(bhk)) &
    (df["Estimated Sale Price"].between(budget[0], budget[1]))
]

# ---------------------------------------------------------
# KPI METRICS
# ---------------------------------------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Properties", len(filtered_df))
col2.metric("Avg Price / Sqft", f"₹ {int(filtered_df['Price per Sqft'].mean())}")
col3.metric("Avg Sale Price", f"₹ {int(filtered_df['Estimated Sale Price'].mean()):,}")
col4.metric("Avg Rental Yield", f"{filtered_df['Rental Yield (%)'].mean():.2f} %")

# ---------------------------------------------------------
# CHARTS
# ---------------------------------------------------------
st.subheader("📈 Visual Analysis")

col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(
        filtered_df,
        x="Locality",
        y="Estimated Sale Price",
        color="Property Type",
        title="Average Sale Price by Locality",
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.scatter(
        filtered_df,
        x="Built-up Area (sqft)",
        y="Estimated Sale Price",
        color="Bedrooms (BHK)",
        size="Buyer Attraction Score",
        title="Area vs Price Relationship",
    )
    st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------------------------
# DATA TABLE
# ---------------------------------------------------------
st.subheader("📋 Property Details")

st.dataframe(
    filtered_df.sort_values("Buyer Attraction Score", ascending=False),
    use_container_width=True,
)
