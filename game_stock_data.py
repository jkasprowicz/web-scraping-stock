import yfinance as yf



gamestop_data = yf.Ticker("GME").history(period="max")
gamestop_data.reset_index(inplace=True)
gamestop_data.to_csv("gamestop_stock_data.csv", index=False)  # Save for sharing
print(gamestop_data.head())
