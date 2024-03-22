import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Extract values from relevant columns
    years = df['Year'].values
    sea_level_CSIRO = df['CSIRO Adjusted Sea Level'].values

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(years, sea_level_CSIRO)

    # Extract line of best fit parameters from raw data using linear regression
    slope, intercept, r_value, p_value, std_err = linregress(years, sea_level_CSIRO)
    # Plot first best fit line (extended to the year 2050)
    years_extended = np.concatenate((years, np.arange(years[-1] + 1, 2051, 1)))
    ax.plot(years_extended, slope*years_extended+intercept, color='red', label='Line of Best Fit (all data)')
   
    # Create second line of best fit using data from 2000 onwards
    years_since2000 = df[df['Year'] >= 2000]['Year'].values
    sea_level_CSIRO_since2000 = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'].values

    # Extract line of best fit parameters from raw data using linear regression
    slope, intercept, r_value, p_value, std_err = linregress(years_since2000, sea_level_CSIRO_since2000)
    # Plot first best fit line, extending it to the year 2050
    years_since2000_extended = np.concatenate((years_since2000, np.arange(years_since2000[-1] + 1, 2051, 1)))
    ax.plot(years_since2000_extended , slope*years_since2000_extended+intercept, color='green', label='Line of Best Fit (data since 2000)')
   
    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()