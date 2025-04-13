# Stock-Price-Predictor

## Project Overview
This project predicts the future stock prices of companies listed in the National Stock Exchange (NSE) of India using historical stock data. The prediction is based on a Linear Regression model that is trained on one year's worth of stock data. The project uses a GUI for user interaction, where users can input the company name and a future date, and receive the predicted stock price for that date.

## Features
- **Stock Price Prediction**: Uses historical stock price data to predict future prices.
- **GUI Interface**: Simple and intuitive Tkinter-based interface for user interaction.
- **Stock Symbol Matching**: Allows users to input the company name, and the application matches it with the closest stock symbol from a pre-loaded CSV file.
- **Graphical Representation**: Displays historical stock prices along with the predicted price for the future date.

## Technologies Used
- **Python**: Main programming language.
- **yfinance**: To fetch historical stock data from Yahoo Finance.
- **Pandas**: For data manipulation and analysis.
- **Scikit-learn**: For building the Linear Regression model.
- **Tkinter**: For creating the graphical user interface.
- **Matplotlib**: For plotting the stock price graph.

## Requirements
- Python 3.x
- Required Python libraries:
  - `yfinance`
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `tkinter`
  - `matplotlib`

You can install the required libraries by running:

```bash
pip install yfinance pandas numpy scikit-learn matplotlib
```

How to Run the Project
Follow these steps to run the project on your local machine:

Step 1: Clone the Repository
To get the project files, you need to clone the repository to your local machine. Open your terminal or command prompt and run the following command:

```bash
git clone https://github.com/shreeyamane/Stock-Price-Predictor.git
cd Stock-Price-Predictor
```
This will download the project and navigate to the project folder.

Step 2: Install Dependencies
Make sure you have Python 3.x installed on your system. Then, you need to install the required Python libraries. You can do this using pip by running the following command:

```bash
pip install yfinance pandas numpy scikit-learn matplotlib
```

Step 3: Prepare the EQUITY_L.csv File
Ensure the EQUITY_L.csv file is in the same directory as the Python script (stock_predictor.py). The CSV file contains stock symbols and corresponding company names, which are necessary for the application to function.

You can obtain the file from the appropriate source or use your own dataset with the correct format.

Step 4: Run the Project
Now you are ready to run the project. In your terminal or command prompt, run the following command:

```bash
python stock_predictor.py
```

This will start the project and open a GUI window where you can:

Enter the company name (e.g., RELIANCE INDUSTRIES LIMITED).

Enter the future date in the format YYYY-MM-DD.

Click on the Predict button to get the predicted stock price for the selected date.

Step 5: Interact with the GUI
Once the GUI is open:

Enter the company name in the text box (it will attempt to match the company name with available symbols).

Enter the future date you want the prediction for (in YYYY-MM-DD format).

Click on Predict to view the predicted stock price and a graph displaying historical stock data and the predicted price.

CSV File Format (EQUITY_L.csv)
The EQUITY_L.csv file should have the following columns:

SYMBOL: The stock symbol for the company.

NAME OF COMPANY: The full name of the company.

Example:

SYMBOL	NAME OF COMPANY
RELIANCE	RELIANCE INDUSTRIES LIMITED
INFY	INFOSYS TECHNOLOGIES LIMITED
Example Usage
Enter the company name: RELIANCE.

Enter the future date: 2025-05-01.

The predicted stock price for RELIANCE on the given date will be displayed along with a graph showing the historical prices and the predicted price.

Acknowledgements
yfinance for fetching the stock data.

Scikit-learn for the machine learning tools.

Tkinter for building the user interface.

Matplotlib for data visualization.
