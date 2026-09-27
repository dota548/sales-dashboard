# Sales Dashboard

This is a simple Streamlit dashboard I built to visualise sales data. It reads data from an Excel file, lets you filter by region, and shows a few useful stats and charts. I mainly made this to practise Streamlit and get better at building dashboards in Python.

## What it does

- Loads sales data from an Excel file
- Lets you pick a region from a dropdown
- Shows total sales and total orders
- Groups sales by product
- Displays an interactive bar chart
- Shows the filtered data in a table

## Important note about the data

I didn’t upload a real `sales.xlsx` file in this repo.

If you want to run this dashboard yourself, you’ll need to **create your own Excel file** called `sales.xlsx` with columns similar to:

- `Region`
- `Product`
- `Sales`

As long as your file has those columns, the dashboard will work.

Put your `sales.xlsx` file in the same folder as `main.py`.

## How it works (explained simply)

The app reads the Excel file into a Pandas DataFrame.  
You choose a region, and the dashboard updates the numbers and the chart based on your selection.

It shows:
- how much money was made  
- how many orders there were  
- which products sold the most  

The bar chart is made with Plotly, so you can hover over it and interact with it.  
At the bottom, you can see the actual filtered data.

## How to run it

Here are the commands you need to install the required packages:
pip install streamlit
pip install pandas
pip install plotly
pip install openpyxl

Then run the app with:
streamlit run main.py

Make sure your `sales.xlsx` file is in the same folder as the script.

## File structure
project-folder/
│
├── main.py
├── sales.xlsx   <-- you need to add this yourself
└── README.md

## Extra notes

This is just a basic dashboard, but you can expand it however you like — more charts, more filters, or even turning it into a multi‑page Streamlit app.
