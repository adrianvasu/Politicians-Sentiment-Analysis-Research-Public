#!/usr/bin/env python3

"""

FinalProjectController.py

Due Date: May 6th, 2020

This program was written to complete the final project requirement for PHY 299
This program utilizes the Twitter API (tweepy) to pull tweets from all 100 senators
and determine the relative positivity or sentiment of the senators in a party. The
results are then reported for the republican, democratic, and independent parties
showcasing their sentiment over each senator's past 100 tweets.

"""

# Header Variables

__author__      = "Adrian Vasu"
__copyright__   = "Copyright 2020, Adrian Vasu"
__email__       = "vasuad2019@mountunion.edu"
__status__      = "Educational"

# Global Import Statements to bring in classes and execute program

import createCSV
import preprocess
import analyze
import postprocess
import visualize
from timer import Timer

"""

====================================================================================

Main Function and Calls:

------------------------------------------------------------------------------------

"""

def main():
    # Define a timer
    t = Timer()
    # Start the timer
    t.start()
    # Start by getting all the data from twitter
    # Note that this should be commented out if there is no API keys
    # Note max is 100 tweets per senator due to twitter limits
    createCSV.getData(100)
    # Preprocess the data and create new CSV files
    preprocess.preprocess()
    # Analyze the data and generate new CSV files
    analyze.analyze()
    # Postprocess the data and create new CSV files
    postprocess.postprocess()
    # Generate the visualizations of the data
    visualize.visualize()
    # Stop the timer and display runtime
    elapsed_time = t.stop()

if __name__ == '__main__':
    main()

"""

------------------------------------------------------------------------------------

End of Main.

====================================================================================

"""
