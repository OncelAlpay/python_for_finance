# 📈 Hedge Fund Strategy Performance Visualization

This project shows how a €1,000 investment would have grown over time under different hedge fund strategies, using historical return data.

## 📁 Files

- `edhec-hedgefundindices.csv`: Contains monthly returns of various hedge fund strategies (data from EDHEC Business School).
- `strategy_plot.py`: A Python script that calculates cumulative performance and visualizes the investment growth for selected strategies.

## 📊 What it does

- Loads hedge fund index data from the CSV file
- Calculates the cumulative wealth index (how €1,000 would grow)
- Plots investment performance by strategy
- Allows flexible selection of:
  - Time period (`start_year`, `end_year`)
  - Strategies to compare
  - X-axis interval (year steps)

## ▶️ How to run

1. Make sure the following packages are installed:

```bash
pip install pandas matplotlib
