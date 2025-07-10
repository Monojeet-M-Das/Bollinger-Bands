# Bollinger Bands Trading Strategy with Backtrader

This project implements a **Bollinger Bands-based trading strategy** using the powerful [Backtrader](https://www.backtrader.com/) backtesting framework. It downloads historical stock data (IBM) via `yfinance` and evaluates the strategy using performance metrics like Sharpe Ratio, Returns, and Max Drawdown.

## 📈 Overview

**Bollinger Bands** are a technical analysis tool defined by a set of trendlines typically plotted two standard deviations (positively and negatively) away from a simple moving average (SMA).

This strategy:
- Buys when the price falls below the lower band
- Sells when the price rises above the upper band
- Closes positions when the price returns to the middle band (SMA)

## 🧠 Strategy Rules

- **Enter Long**: When the close price crosses below the lower band
- **Enter Short**: When the close price crosses above the upper band
- **Exit Long**: When the price crosses back above the middle band
- **Exit Short**: When the price crosses back below the middle band

## 🛠️ Requirements

Install dependencies with:
```bash
pip install backtrader yfinance pandas
```

## Example output:

Initial capital: $10000.00
Sharpe ratio: 0.76
Return: 45.20%
Max Drawdown: 18.30%
Capital: $14520.00

## 📌 Notes

  Strategy uses IBM stock data from 2010 to 2020.

  Capital is initialized at $10,000.

  Position size per trade is fixed (size=20 shares).
