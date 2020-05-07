#!/usr/bin/env python3

"""

postprocess.py

Due Date: May 6th, 2020

This portion of the program takes the analyzed csv files and prepares
them for visualization

"""

# Header Variables

__author__      = "Adrian Vasu"
__copyright__   = "Copyright 2020, Adrian Vasu"
__email__       = "vasuad2019@mountunion.edu"
__status__      = "Educational"

# Global Import Statements
import helper as h
import csv
from datetime import datetime

# Post process method which calls the helper on the files created
#   during the analyze phase
def postprocess():
    print('Postprocessing Data\n')
    rep_data = "csv_files/rep_data_analyzed.csv"
    rep_out = "csv_files/rep_data_visualization.csv"
    dem_data = "csv_files/dem_data_analyzed.csv"
    dem_out = "csv_files/dem_data_visualization.csv"
    ind_data = "csv_files/ind_data_analyzed.csv"
    ind_out = "csv_files/ind_data_visualization.csv"

    postprocess_helper(rep_data, rep_out)
    postprocess_helper(dem_data, dem_out)
    postprocess_helper(ind_data, ind_out)
    print('Done Postprocessing Data\n')

# Helper method created to ensure that code did not need to be
#   duplicated because this runs on all 3 data sets
def postprocess_helper(data, outfile):
    # Variables to store information in
    results = dict()
    output = dict()
    final = dict()
    count = dict()

    # open input file and create csv reader
    i = open(data, 'r')
    rdr = csv.reader(i)

    # loop over input file filling in information
    for r in rdr:
        tmp = datetime.strptime(r[0], '%Y-%m-%d %H:%M:%S')
        results[tmp] = float(r[1])

    # sort the dates from the results dict
    dates = sorted(results)

    # loop over dates and determine how many tweets per date
    for d in dates:
        day = datetime(d.year, d.month, d.day)
        if day in count:
            count[day] += 1
        else:
            count[day] = 1

    # loop over dates and populate tweet values using a sum
    for d in dates:
        day = datetime(d.year, d.month, d.day)
        if day in output:
            output[day] += results[d]
        else:
            output[day] = results[d]

    # Loop over the output dict normalizing the relative
    #   positivity due to the number of tweets on that date
    for key, val in output.items():
        final[key] = val / count[key]

    # Open the output file and create the csv writer
    o = open(outfile, 'w', newline='')
    wtr = csv.writer(o)

    # loop over final dict and output to the csv
    for key, val in final.items():
        wtr.writerow((key, val))


"""

====================================================================================

Main Function and Calls:

------------------------------------------------------------------------------------

"""

def main():
    postprocess()

if __name__ == '__main__':
    main()

"""

------------------------------------------------------------------------------------

End of Main.

====================================================================================

"""
