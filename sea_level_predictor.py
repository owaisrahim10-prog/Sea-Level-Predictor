import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Import data
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data')

    # 3. Create first line of best fit (using all data from 1880 to the latest year)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred_all = pd.Series([i for i in range(df['Year'].min(), 2050)])
    y_pred_all = res_all.intercept + res_all.slope * x_pred_all
    ax.plot(x_pred_all, y_pred_all, color='red', label='Best Fit Line (1880-2050)')

    # 4. Create second line of best fit (using data from year 2000 to the latest year)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series([i for i in range(2000, 2050)])
    y_pred_recent = res_recent.intercept + res_recent.slope * x_pred_recent
    ax.plot(x_pred_recent, y_pred_recent, color='green', label='Best Fit Line (2000-2050)')

    # 5. Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()