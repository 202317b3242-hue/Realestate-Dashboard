import streamlit as st
import pandas as pd

# Page titlest.title("Hyderabad Real Estate – Data")

# Load data
@st.cache_data
def load_data():
    return pd.read_excel("Hyderabad_Real_Estate_Buyer_Focused_Dataset (1).xlsx")

df = load_data()

# Sidebar filter
st.sidebar.header("Filter")
localities = sorted(df["Locality"].unique())

selected_locality = st.sidebar.selectbox(
    "Select Locality",
    options=["All"] + localities
)

# Apply filter
if selected_locality != "All":
    filtered_df = df[df["Locality"] == selected_locality]
else:
    filtered_df = df

# Show row count
st.write(f"Showing **{len(filtered_df)}** properties")

# Preview data
st.dataframe(filtered_df, use_container_width=True)
