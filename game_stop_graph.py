import plotly.graph_objects as go
import pandas as pd

# Load data
game_stock = pd.read_csv("gamestop_stock_data.csv")
stock_revenue = pd.read_csv("gamestop.csv")

# Line chart for Tesla stock
fig = go.Figure()
fig.add_trace(go.Scatter(x=game_stock["Date"], y=game_stock["Close"], mode="lines", name="Tesla Stock Price"))
fig.add_trace(go.Bar(x=stock_revenue["Year"], y=stock_revenue["Revenue"], name="Tesla Revenue"))
fig.update_layout(title="GameStop Stock Price and Revenue", xaxis_title="Date", yaxis_title="Value")
fig.show()
