#!/usr/bin/env python3

"""

visualize.py

Due Date: May 6th, 2020

This file takes the final csv files and visualizes the data

"""

# Header Variables

__author__      = "Adrian Vasu"
__copyright__   = "Copyright 2020, Adrian Vasu"
__email__       = "vasuad2019@mountunion.edu"
__status__      = "Educational"

# Global Import Statements
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib

# Method to call the helper on all 3 data sets to avoid duplicate code
def visualize():
    rep_data = "csv_files/rep_data_visualization.csv"
    dem_data = "csv_files/dem_data_visualization.csv"
    ind_data ="csv_files/ind_data_visualization.csv"

    visualize_helper(rep_data)
    visualize_helper(dem_data)
    visualize_helper(ind_data)
    visualize_all3(rep_data, dem_data, ind_data)

# Helper to avoid duplicate code
def visualize_helper(data):
    # Instantiating x and y variable holders
    dates = list()
    vals = list()

    # Open the datafile and create the reader
    i = open(data, 'r')
    rdr = csv.reader(i)

    # Loop over reader reading information into the variable holders
    for r in rdr:
        dates.append(datetime.strptime(r[0], '%Y-%m-%d %H:%M:%S'))
        vals.append(float(r[1]))

    # Create plot (to handle dates nicely)
    fig, ax = plt.subplots()
    ax.plot(dates, vals)
    fig.autofmt_xdate()
    ax.fmt_xdata = matplotlib.dates.DateFormatter('%Y-%m-%d')

    # labels based on data
    lowdate = dates[0].strftime('%m-%d-%Y')
    plt.xlabel("Date since " + lowdate)

    if 'rep' in data:
        ylabel = 'Degree of Positivity in Republican Senator Tweets'
        title = 'Republican Senator Tweet Positivity Over Time'
    elif 'dem' in data:
        ylabel = 'Degree of Positivity in Democrat Senator Tweets'
        title = 'Democrat Senator Tweet Positivity Over Time'
    elif 'ind' in data:
        ylabel = 'Degree of Positivity in Independent Senator Tweets'
        title = 'Independent Senator Tweet Positivity Over Time'

    plt.ylabel(ylabel)
    plt.title(title)
    
# Helper to plot all 3 on the same graph
def visualize_all3(rep, dem, ind):
    # Instantiates x and y variable holders for all 3
    rep_dates = list()
    rep_vals = list()
    dem_dates = list()
    dem_vals = list()
    ind_dates = list()
    ind_vals = list()

    # Open the datafiles and create the readers
    i = open(rep, 'r')
    rep_rdr = csv.reader(i)
    i = open(dem, 'r')
    dem_rdr = csv.reader(i)
    i = open(ind, 'r')
    ind_rdr = csv.reader(i)

    # Loop over readers reading information into the variable holders
    for r in rep_rdr:
        rep_dates.append(datetime.strptime(r[0], '%Y-%m-%d %H:%M:%S'))
        rep_vals.append(float(r[1]))
    for r in dem_rdr:
        dem_dates.append(datetime.strptime(r[0], '%Y-%m-%d %H:%M:%S'))
        dem_vals.append(float(r[1]))
    for r in ind_rdr:
        ind_dates.append(datetime.strptime(r[0], '%Y-%m-%d %H:%M:%S'))
        ind_vals.append(float(r[1]))

    # Create plot (to handle dates nicely)
    fig, ax = plt.subplots()
    ax.plot(rep_dates, rep_vals, dem_dates, dem_vals, ind_dates, ind_vals)
    fig.autofmt_xdate()
    ax.fmt_xdata = matplotlib.dates.DateFormatter('%Y-%m-%d')

    # labels based on data
    lowdate = min(rep_dates[0], dem_dates[0], ind_dates[0]).strftime('%m-%d-%Y')
    plt.xlabel("Date since " + lowdate)

    ylabel = 'Degree of Positivity in Senator Tweets'
    title = 'Senator Tweet Positivity Over Time'

    plt.legend(['Republican', 'Democratic', 'Independent'])
    plt.ylabel(ylabel)
    plt.title(title)

"""

====================================================================================

Main Function and Calls:

------------------------------------------------------------------------------------

"""

def main():
    visualize()

if __name__ == '__main__':
    main()

"""

------------------------------------------------------------------------------------

End of Main.

====================================================================================

"""
