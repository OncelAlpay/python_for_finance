import pandas as pd
import matplotlib.pyplot as plt


# Load EDHEC hedge fund index returns
def get_hfi_returns():
    """
    Load the EDHEC Hedge Fund Index returns.
    Make sure the CSV file 'edhec-hedgefundindices.csv' is in the same folder.
    """
    hfi = pd.read_csv("edhec-hedgefundindices.csv", index_col=0, parse_dates=True, dayfirst=True)
    hfi = hfi / 100  # Convert percentages to decimals
    hfi.index = hfi.index.to_period('M')  # Monthly period index
    return hfi


# Plotting function
def plot_strategies(returns, strategies, start_year=2000, end_year=2020, step=5):
    """
    Plots the cumulative wealth index for selected strategies over a given time frame.

    Parameters:
    - returns: DataFrame with strategy returns
    - strategies: list of strategy names (columns in the DataFrame)
    - start_year: first year to include in the plot
    - end_year: last year to include in the plot
    - step: interval in years for x-axis labels
    """
    if not all(col in returns.columns for col in strategies):
        print("❌ The file does not contain all required columns.")
        print("Available Columns:", list(returns.columns))
        return

    # Slice data to selected date range
    returns = returns[(returns.index >= pd.Period(f"{start_year}-01")) &
                      (returns.index <= pd.Period(f"{end_year}-12"))]

    # Calculate wealth index
    wealth_index = (1 + returns[strategies]).cumprod()

    # Plot
    fig, ax = plt.subplots(figsize=(12, 6), dpi=100)
    wealth_index.plot(ax=ax, linewidth=2)

    # Titles and labels
    ax.set_title("Wealth Accumulation: 1,000€ Invested in Hedge Fund Strategies", fontsize=14, fontweight="bold")
    ax.set_ylabel("Wealth", fontsize=12)
    ax.set_xlabel("Year", fontsize=12)  # Sets x-axis label to "Year"
    ax.grid(True, linestyle='--', alpha=0.5)

    # Custom x-axis ticks
    years = list(range(start_year, end_year + 1, step))
    ax.set_xticks([pd.Period(str(y)).to_timestamp() for y in years])
    ax.set_xticklabels([str(y) for y in years])

    plt.tight_layout()
    plt.show()


# Main function
def main():
    hfi = get_hfi_returns()
    strategies = ["Global Macro", "Event Driven", "Long/Short Equity"]

    # Change these to customize time frame
    plot_strategies(hfi, strategies, start_year=2005, end_year=2019, step=2)


if __name__ == "__main__":
    main()

