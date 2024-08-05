import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    plt.figure(figsize=(10,10))
    plt.scatter(x, y, alpha=0.7)

    # Create first line of best fit
    stats = linregress(x, y)
    a = stats.slope
    b = stats.intercept
    i = range(1880, 2051)
    plt.plot(i, a * i + b, color="black")

    # Create second line of best fit
    df_year2000 = df[df["Year"] >= 2000]
    x = df_year2000["Year"]
    y = df_year2000["CSIRO Adjusted Sea Level"]
    
    stats = linregress(x, y)
    a = stats.slope
    b = stats.intercept
    j = range(2000, 2051)
    plt.plot(j, a * j + b, color="red")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()