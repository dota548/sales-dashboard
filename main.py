import streamlit as st
import pandas as pd
import plotly.express as px

# Dashboard title
st.title("Sales Dashboard")

# Load sales data
df = pd.read_excel("sales.xlsx")

# Filter by region
region = st.selectbox(
    "Select Region",
    ["ALL"] + list(df["Region"].unique())
)

if region != "ALL":
    df = df[df["Region"] == region]

# Key sales metrics
st.metric("Total Sales", f"${df['Sales'].sum():,.0f}")
st.metric("Total Orders", len(df))

# Sales by product
sales = df.groupby("Product")["Sales"].sum().reset_index()

# Bar chart
fig = px.bar(
    sales,
    x="Product",
    y="Sales",
    title="Sales by Product"
)

# Display results
st.plotly_chart(fig, use_container_width=True)
st.dataframe(df)
