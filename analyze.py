#!/usr/bin/env python3

"""

analyze.py

Due Date: May 6th, 2020

This file analyzes the data sets and determines the relative positivity
of a tweet and logs it to CSV

"""

# Header Variables

__author__      = "Adrian Vasu"
__copyright__   = "Copyright 2020, Adrian Vasu"
__email__       = "vasuad2019@mountunion.edu"
__status__      = "Educational"

# Global Import Statements
import helper as h
import csv

def analyze():
    print('Analyzing Data\n')
    # Bring in negative and positive wordlists
    negwords, poswords = h.buildWordLists()
    # define the names for the input and output data files
    rep_data = "csv_files/republican_data.csv"
    rep_out = "csv_files/rep_data_analyzed.csv"
    dem_data = "csv_files/democrat_data.csv"
    dem_out = "csv_files/dem_data_analyzed.csv"
    ind_data = "csv_files/independent_data.csv"
    ind_out = "csv_files/ind_data_analyzed.csv"

    # Helper function used so that same steps don't need
    #   repeated 3 times
    analyze_helper(rep_data, rep_out, negwords, poswords)
    analyze_helper(dem_data, dem_out, negwords, poswords)
    analyze_helper(ind_data, ind_out, negwords, poswords)
    print('Done Analyzing Data\n')

def analyze_helper(data, output, negwords, poswords):
    # Open input file
    i = open(data, 'r')
    # Create CSV reader
    rdr = csv.reader(i)
    # Open output file
    o = open(output, 'w', newline='')
    # Create CSV writer
    wtr = csv.writer(o)
    # Loop over the data in the input file
    for r in rdr:
        # Create variables
        count, val = 0, 0
        # Use tmp variable as container for tweet text
        tmp = r[1]
        # Replace mentions and hashtags
        tmp.replace('@', ' ')
        tmp.replace('#', ' ')
        # Split on whitespace
        tmp = tmp.split()
        # Compare each word in a tweet to the wordlists
        #   if there is a negative word subtract from count
        #   if positive add
        for s in tmp:
            if s in negwords:
                count -= 1
            elif s in poswords:
                count += 1
        # Create divisor to account for the url at the end
        #   of the tweet object
        divisor = len(tmp) - 1
        # If one word tweet divisor will be 0
        if divisor == 0:
            divisor = 1
        # Normalize to 1 for ease of viewership
        val = count / divisor
        # Output the data to the new CSV
        wtr.writerow((r[0], val))

    # Close files
    i.close()
    o.close()

"""

====================================================================================

Main Function and Calls:

------------------------------------------------------------------------------------

"""

def main():
    analyze()

if __name__ == '__main__':
    main()

"""

------------------------------------------------------------------------------------

End of Main.

====================================================================================

"""
