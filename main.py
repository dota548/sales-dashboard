import streamlit as st
import pandas as pd 
import plotly.express as px

# dashboard title 
st.title(" Sales Dashboard")

# load sales data
df = pd.read_excel("sales.xlsx")

# filter by region 
region = st.selectbox(
    "Select Region",
    ["ALL"] + list(df["Region"].unique())
)

if region != "All":
    df = df[df["Regio"] == region]

# key sales metrics
st.metric("Total Sales", f"${df['Sales'].sum():,.0f}")
st.metric("Total Orders". len(df))

# sales by product 
sales = df.groupby("product")["Sales"].sum().reset_index()

fig = px.bar(
    sales, 
    x="Product",
    y="Sales",
    titles="Sales by Prdocut"
)

# display results
st.plotly_chart(fig, use_container_width=True)
st.dataframe(df)