import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime
import matplotlib.pyplot as plt
from difflib import get_close_matches
import os
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Check if EQUITY_L.csv exists, else warn the user
csv_file = 'EQUITY_L.csv'
if not os.path.exists(csv_file):
    print("Error: The file 'EQUITY_L.csv' was not found in the current directory.")
    print("Please ensure the file is available for mapping company names to stock symbols.")
    exit()

# Load NSE stock list (pre-downloaded CSV from NSE website)
nse_data = pd.read_csv(csv_file)
nse_data['SYMBOL'] = nse_data['SYMBOL'].astype(str).str.upper()
nse_data['NAME OF COMPANY'] = nse_data['NAME OF COMPANY'].astype(str)

# Create name-to-symbol mapping
company_name_list = nse_data['NAME OF COMPANY'].tolist()

def get_symbol_from_name(company_name):
    # Standardize input (upper case and strip)
    company_name = company_name.strip().upper()

    # First, try to find an exact match
    exact_match = nse_data[nse_data['NAME OF COMPANY'].str.upper() == company_name]
    
    if not exact_match.empty:
        match = exact_match.iloc[0]
        symbol = match['SYMBOL'] + '.NS'
        return symbol, match['NAME OF COMPANY']
    
    # If no exact match, fall back to fuzzy matching
    matches = get_close_matches(company_name, company_name_list, n=1, cutoff=0.9)
    
    if matches:
        match = matches[0]
        print(f"Closest match found: '{match}'")  # Debug print
        row = nse_data[nse_data['NAME OF COMPANY'] == match].iloc[0]
        symbol = row['SYMBOL'] + '.NS'
        return symbol, match
    else:
        print(f"No match found for '{company_name}'")  # Debug print
        return None, None

# Predict using Linear Regression
def predict_stock_price(symbol, future_date_str):
    df = yf.download(symbol, period='1y')
    df = df.reset_index()
    df['Date_Ordinal'] = pd.to_datetime(df['Date']).map(datetime.toordinal)
    X = df[['Date_Ordinal']]
    y = df['Close']

    model = LinearRegression()
    model.fit(X, y)

    future_date = datetime.strptime(future_date_str, '%Y-%m-%d')
    future_ordinal = np.array([[future_date.toordinal()]])  # Ensure it is a 2D array
    predicted_price_array = model.predict(future_ordinal)  # This is an array
    print(f"Predicted price array: {predicted_price_array}")  # Debugging: see the array

    predicted_price = predicted_price_array[0][0]  # Extract the scalar value from the 2D array

    return predicted_price, df

# GUI using Tkinter
def run_gui():
    def on_predict():
        company = entry_company.get().strip()
        future_date = entry_date.get().strip()

        symbol, match_name = get_symbol_from_name(company)
        if not symbol:
            messagebox.showerror("Error", "Company name not recognized.")
            return

        try:
            price, df = predict_stock_price(symbol, future_date)
            result_label.config(text=f"Predicted price for {match_name} on {future_date} ₹{price:.2f}")

            # Plotting
            fig, ax = plt.subplots(figsize=(5, 3))
            ax.plot(df['Date'], df['Close'], label='Historical Close')
            ax.axhline(y=price, color='r', linestyle='--', label='Predicted')
            ax.set_title(f"{match_name} Price Prediction")
            ax.set_xlabel('Date')
            ax.set_ylabel('Price')
            ax.legend()

            canvas = FigureCanvasTkAgg(fig, master=window)
            canvas.draw()
            canvas.get_tk_widget().pack()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    window = tk.Tk()
    window.title("Indian Stock AI Predictor")
    window.geometry("600x600")

    tk.Label(window, text="Enter Company Name (e.g., RELIANCE)").pack(pady=5)
    entry_company = tk.Entry(window, width=40)
    entry_company.pack(pady=5)

    tk.Label(window, text="Enter Future Date (YYYY-MM-DD)").pack(pady=5)
    entry_date = tk.Entry(window, width=40)
    entry_date.pack(pady=5)

    tk.Button(window, text="Predict", command=on_predict).pack(pady=10)
    result_label = tk.Label(window, text="")
    result_label.pack(pady=10)

    window.mainloop()

if __name__ == '__main__':
    run_gui()