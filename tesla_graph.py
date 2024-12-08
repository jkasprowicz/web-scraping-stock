import plotly.graph_objects as go
import pandas as pd

# Load data
tesla_stock = pd.read_csv("tesla_stock_data.csv")
tesla_revenue = pd.read_csv("tesla_revenue_data.csv")

# Line chart for Tesla stock
fig = go.Figure()
fig.add_trace(go.Scatter(x=tesla_stock["Date"], y=tesla_stock["Close"], mode="lines", name="Tesla Stock Price"))
fig.add_trace(go.Bar(x=tesla_revenue["Year"], y=tesla_revenue["Revenue"], name="Tesla Revenue"))
fig.update_layout(title="Tesla Stock Price and Revenue", xaxis_title="Date", yaxis_title="Value")
fig.show()
