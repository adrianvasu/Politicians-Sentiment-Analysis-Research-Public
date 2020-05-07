#!/usr/bin/env python3

"""

createCSV.py

Due Date: May 6th, 2020

This file works with the final project for PHY 299 to create the CSV file
which the rest of the project will work on.

"""

# Header Variables

__author__      = "Adrian Vasu"
__copyright__   = "Copyright 2020, Adrian Vasu"
__email__       = "vasuad2019@mountunion.edu"
__status__      = "Educational"

# Global Import Statements

import getTweets

# Method to pull in tweets from each senator
#   default number of tweets per senator is 10
def getData(N=10):
    print("\nPulling Twitter Data\n")
    getTweets.getTweets(N)
    print("\nDone Pulling Twitter Data\n")


"""

====================================================================================

Main Function and Calls:

------------------------------------------------------------------------------------

"""

def main():
    getData()

if __name__ == '__main__':
    main()

"""

------------------------------------------------------------------------------------

End of Main.

====================================================================================

"""
