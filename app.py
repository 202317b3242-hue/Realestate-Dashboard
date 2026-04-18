import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="Hyderabad Real Estate Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏙️ Hyderabad Real Estate – Buyer Focused Dashboard")

# ----------------------------------------------------
# Data Loading
# ----------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_excel("Hyderabad_Real_Estate_Buyer_Focused_Dataset (1).xlsx")

df = load_data()

# ----------------------------------------------------
# Sidebar Filters
# ----------------------------------------------------
st.sidebar.header("🔍 Filter Properties")

localities = sorted(df["Locality"].unique())
property_types = sorted(df["Property Type"].unique())
bhk_options = sorted(df["Bedrooms (BHK)"].unique())

selected_locality = st.sidebar.multiselect(
    "Select Locality",
    localities,
    default=localities
)

selected_property_type = st.sidebar.multiselect(
    "Select Property Type",
    property_types,
    default=property_types
)

selected_bhk = st.sidebar.multiselect(
    "Select BHK",
    bhk_options,
    default=bhk_options
)

price_range = st.sidebar.slider(
    "Budget Range (INR)",
    int(df["Estimated Sale Price (INR)"].min()),
    int(df["Estimated Sale Price (INR)"].max()),
    (
        int(df["Estimated Sale Price (INR)"].min()),
        int(df["Estimated Sale Price (INR)"].max())
    )
)

# ----------------------------------------------------
# Apply Filters
# ----------------------------------------------------
filtered_df = df[
    (df["Locality"].isin(selected_locality)) &
    (df["Property Type"].isin(selected_property_type)) &
    (df["Bedrooms (BHK)"].isin(selected_bhk)) &
    (df["Estimated Sale Price (INR)"].between(price_range[0], price_range[1]))
]

# ----------------------------------------------------
# KPI Metrics
# ----------------------------------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Properties",
    len(filtered_df)
)

col2.metric(
    "Avg Price (INR)",
    f"{int(filtered_df['Estimated Sale Price (INR)'].mean()):,}"
)

col3.metric(
    "Avg Price / Sqft (INR)",
    f"{int(filtered_df['Price per Sqft (INR)'].mean()):,}"
)

col4.metric(
    "Avg Buyer Score",
    round(filtered_df["Buyer Attraction Score (1-10)"].mean(), 2)
)

# ----------------------------------------------------
# Charts Row 1
# ----------------------------------------------------
st.subheader("📈 Market Insights")

col1, col2 = st.columns(2)

with col1:
    fig_price_locality = px.bar(
        filtered_df.groupby("Locality", as_index=False)["Estimated Sale Price (INR)"].mean(),
        x="Locality",
        y="Estimated Sale Price (INR)",
        title="Average Property Price by Locality",
        color="Locality"
    )
    st.plotly_chart(fig_price_locality, use_container_width=True)

with col2:
    fig_property_type = px.pie(
        filtered_df,
        names="Property Type",
        title="Property Type Distribution"
    )
    st.plotly_chart(fig_property_type, use_container_width=True)

# ----------------------------------------------------
# Charts Row 2
# ----------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    fig_price_sqft = px.box(
        filtered_df,
        x="Property Type",
        y="Price per Sqft (INR)",
        title="Price per Sqft by Property Type"
    )
    st.plotly_chart(fig_price_sqft, use_container_width=True)

with col2:
    fig_buyer_score = px.scatter(
        filtered_df,
        x="Estimated Sale Price (INR)",
        y="Buyer Attraction Score (1-10)",
        color="Locality",
        title="Price vs Buyer Attraction Score",
        size="Built-up Area (sqft)"
    )
    st.plotly_chart(fig_buyer_score, use_container_width=True)

# ----------------------------------------------------
# Amenities & Distance Insights
# ----------------------------------------------------
st.subheader("📍 Location & Amenities Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    fig_metro_dist = px.histogram(
        filtered_df,
        x="Distance to Metro (km)",
        title="Distance to Metro Distribution"
    )
    st.plotly_chart(fig_metro_dist, use_container_width=True)

with col2:
    fig_it_dist = px.histogram(
        filtered_df,
        x="Distance to IT Hub (km)",
        title="Distance to IT Hub Distribution"
    )
    st.plotly_chart(fig_it_dist, use_container_width=True)

with col3:
    fig_amenities = px.histogram(
        filtered_df,
        x="Amenities Count",
        title="Amenities Count Distribution"
    )
    st.plotly_chart(fig_amenities, use_container_width=True)

# ----------------------------------------------------
# Data Table
# ----------------------------------------------------
st.subheader("📋 Filtered Property Data")

st.dataframe(
    filtered_df.sort_values("Buyer Attraction Score (1-10)", ascending=False),
    use_container_width=True
)
