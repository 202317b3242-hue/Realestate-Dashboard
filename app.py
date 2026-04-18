import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------
# App Configuration
# ---------------------------
st.set_page_config(
    page_title="Hyderabad Real Estate Dashboard",
    layout="wide"
)

st.title("🏡 Hyderabad Real Estate Data Preview Dashboard")
st.markdown("A basic exploratory dashboard for buyer-focused real estate analytics")

# ---------------------------
# Load Data
# ---------------------------
@st.cache_data
def load_data():
    return pd.read_excel("Hyderabad_Real_Estate_Buyer_Focused_Dataset (1).xlsx")

df = load_data()

# ---------------------------
# Sidebar Filters
# ---------------------------
st.sidebar.header("🔎 Filters")

localities = st.sidebar.multiselect(
    "Select Locality",
    options=sorted(df["Locality"].unique()),
    default=sorted(df["Locality"].unique())
)

property_types = st.sidebar.multiselect(
    "Select Property Type",
    options=sorted(df["Property Type"].unique()),
    default=sorted(df["Property Type"].unique())
)

price_range = st.sidebar.slider(
    "Price Range (INR)",
    int(df["Estimated Sale Price (INR)"].min()),
    int(df["Estimated Sale Price (INR)"].max()),
    (
        int(df["Estimated Sale Price (INR)"].min()),
        int(df["Estimated Sale Price (INR)"].max())
    )
)

# Apply filters
filtered_df = df[
    (df["Locality"].isin(localities)) &
    (df["Property Type"].isin(property_types)) &
    (df["Estimated Sale Price (INR)"].between(price_range[0], price_range[1]))
]

# ---------------------------
# KPIs
# ---------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Properties", len(filtered_df))
col2.metric("Avg Price / Sqft", f"₹{int(filtered_df['Price per Sqft (INR)'].mean())}")
col3.metric("Avg Sale Price", f"₹{int(filtered_df['Estimated Sale Price (INR)'].mean()):,}")
col4.metric("Avg Buyer Score", round(filtered_df["Buyer Attraction Score (1-10)"].mean(), 2))

# ---------------------------
# Data Preview
# ---------------------------
st.subheader("📄 Data Preview")
st.dataframe(filtered_df, use_container_width=True)

# ---------------------------
# Visualizations
# ---------------------------
st.subheader("📊 Visual Insights")

col5, col6 = st.columns(2)

# Price vs Area
fig1 = px.scatter(
    filtered_df,
    x="Built-up Area (sqft)",
    y="Estimated Sale Price (INR)",
    color="Property Type",
    title="Built-up Area vs Sale Price",
    hover_data=["Locality"]
)
col5.plotly_chart(fig1, use_container_width=True)

# Avg Price by Locality
avg_price_locality = (
    filtered_df
    .groupby("Locality")["Estimated Sale Price (INR)"]
    .mean()
    .reset_index()
)

fig2 = px.bar(
    avg_price_locality,
    x="Locality",
    y="Estimated Sale Price (INR)",
    title="Average Sale Price by Locality"
)
col6.plotly_chart(fig2, use_container_width=True)

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.caption("📌 Built with Streamlit | Buyer-focused real estate data")
