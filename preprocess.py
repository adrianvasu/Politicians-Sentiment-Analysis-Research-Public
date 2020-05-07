#!/usr/bin/env python3

"""

preprocess.py

Due Date: May 6th, 2020

This portion of the program prepares the CSV file for analysis

"""

# Header Variables

__author__      = "Adrian Vasu"
__copyright__   = "Copyright 2020, Adrian Vasu"
__email__       = "vasuad2019@mountunion.edu"
__status__      = "Educational"

# Global Import Statements

import helper as h
import csv

def preprocess():
    print("Preprocessing Data\n")

    # open and create the csv file reader
    source = open("csv_files/tweets.csv", 'r')
    rdr = csv.reader(source)

    # Create output files and writers for rep, dem, and ind senators
    routput = open("csv_files/republican_data.csv", 'w', newline='')
    doutput = open("csv_files/democrat_data.csv", 'w', newline='')
    ioutput = open("csv_files/independent_data.csv", 'w', newline='')
    rwtr = csv.writer(routput)
    dwtr = csv.writer(doutput)
    iwtr = csv.writer(ioutput)

    # pull in the twitter handles from the senators file to compare
    #   against the cspan data
    handles = h.getHandles()

    # Build the party relation dictionary
    partyRelations = h.buildPartyRelations()

    # Loop over the csv data file separating tweets by party and
    #   outputting date and tweet text
    for r in rdr:
        if r[0] in handles:
            if partyRelations[r[0]] == 'r':
                rwtr.writerow((r[3], r[2]))
            elif partyRelations[r[0]] == 'd':
                dwtr.writerow((r[3], r[2]))
            elif partyRelations[r[0]] == 'i':
                iwtr.writerow((r[3], r[2]))

    print("Done Preprocessing Data\n")

"""

====================================================================================

Main Function and Calls:

------------------------------------------------------------------------------------

"""

def main():
    preprocess()

if __name__ == '__main__':
    main()

"""

------------------------------------------------------------------------------------

End of Main.

====================================================================================

"""
