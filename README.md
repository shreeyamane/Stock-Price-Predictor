# Stock-Price-Predictor

Project Overview
This project predicts the future stock prices of companies listed in the National Stock Exchange (NSE) of India using historical stock data. The prediction is based on a Linear Regression model that is trained on one year's worth of stock data. The project uses a GUI for user interaction, where users can input the company name and a future date, and receive the predicted stock price for that date.

Features
Stock Price Prediction: Uses historical stock price data to predict future prices.

GUI Interface: Simple and intuitive Tkinter-based interface for user interaction.

Stock Symbol Matching: Allows users to input the company name, and the application matches it with the closest stock symbol from a pre-loaded CSV file.

Graphical Representation: Displays historical stock prices along with the predicted price for the future date.

Technologies Used

Python: Main programming language.

yfinance: To fetch historical stock data from Yahoo Finance.

Pandas: For data manipulation and analysis.

Scikit-learn: For building the Linear Regression model.

Tkinter: For creating the graphical user interface.

Matplotlib: For plotting the stock price graph.

Requirements
Python 3.x

Required Python libraries:

yfinance

pandas

numpy

scikit-learn

tkinter

matplotlib

You can install the required libraries by running:

bash
Copy
Edit
pip install yfinance pandas numpy scikit-learn matplotlib
How to Run the Project
Clone the repository:

bash
Copy
Edit
git clone https://github.com/shreeyamane/Stock-Price-Predictor.git
cd Stock-Price-Predictor
Make sure the EQUITY_L.csv file is in the same directory as the script. This file contains the stock symbols and company names used for matching.

Run the project:

bash
Copy
Edit
python stock_predictor.py
The GUI will open, where you can enter the company name and the future date (in the format YYYY-MM-DD). Click on Predict to get the predicted stock price for the selected date.

CSV File Format (EQUITY_L.csv)
The EQUITY_L.csv file should have the following columns:

SYMBOL: The stock symbol for the company.

NAME OF COMPANY: The full name of the company.

Example:

SYMBOL	NAME OF COMPANY
RELIANCE	RELIANCE INDUSTRIES LIMITED
INFY	INFOSYS TECHNOLOGIES LIMITED
Example Usage
Enter the company name: RELIANCE INDUSTRIES LIMITED

Enter the future date: 2026-01-01.

The predicted stock price for RELIANCE on the given date will be displayed along with a graph showing the historical prices and the predicted price.

Acknowledgements
yfinance for fetching the stock data.

Scikit-learn for the machine learning tools.

Tkinter for building the user interface.

Matplotlib for data visualization.
