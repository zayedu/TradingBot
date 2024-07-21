# Pocket Trader

## Overview
Po is a Machine Learning-based trading algorithm that utilizes PyTorch and Hugging Face's Transformers Library for sentiment analysis to make trading decisions. It processes stock data from the Alpaca Trading API over the past three days, performs sentiment analysis, and then makes informed trading decisions. The trading operations are executed by Lumibot, with accurate stock market data sourced from YahooFinance. This full-stack application is built using Flask, allowing users to select backtesting dates, view detailed tradesheets, and tear sheets of the algorithm's performance.

## Table of Contents
- [Overview](#overview)
- [Demo](#demo)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)
- [License](#license)
## Demo
![Pocket Trader Demo](Assets/PocketTraderDemo.gif)

## Features
- **Sentiment Analysis:** Utilizes Hugging Face's Transformers Library for sentiment analysis on stock data.
- **Data Integration:** Pulls stock data from Alpaca Trading API and YahooFinance.
- **Trading Decisions:** Executes trades based on sentiment analysis using Lumibot.
- **Backtesting:** Configured to backtest using historical stock market data.
- **User Interface:** Flask-based web application for selecting backtesting dates and viewing detailed tradesheets and tear sheets.
- **Live Deployment:** Under construction at [tradingbot-esp2.onrender.com](http://tradingbot-esp2.onrender.com/).

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/zayedu/TradingBot.git
   cd Pocket Trader
   ```
2. **Set up a virtual environment:**
   ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up the environment variables:**
   ```sh
   ALPACA_API_KEY=<your_alpaca_api_key>
   ALPACA_SECRET_KEY=<your_alpaca_secret_key>
    ```
## Usage
1. **Run the Flask application:**
```sh
flask run
```
2. **Access the web application:**
   Open your browser and navigate to `http://127.0.0.1:5000/`
3. **Backtest the algorithm:**
   Select the desired backtesting dates and run the algorithm to view the tradesheet and tear sheet.
## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to follow the coding standards and include relevant tests for your code.

## Contact
Email: [umerz@mcmaster.ca](mailto:umerz@mcmaster.ca)

LinkedIn: [Zayed Umer](https://www.linkedin.com/in/zayed-umer/)

GitHub: [zayedu](https://github.com/zayedu)

Personal Portfolio: [notzayed.me](http://notzayed.me/)

## License
This project is licensed under the MIT License. See the LICENSE file for details.