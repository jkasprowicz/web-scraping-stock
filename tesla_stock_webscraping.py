import yfinance as yf

tesla_data = yf.Ticker("TSLA").history(period="max")
tesla_data.reset_index(inplace=True)
tesla_data.to_csv("tesla_stock_data.csv", index=False)  # Save for sharing
print(tesla_data.head())  # Display the first few rows
