# Reading article details from input text file.
"""This script reads the text file and make a python list out of it."""
import pandas as pd

data = pd.read_csv('/Users/jeevananthamganesan/\
Inputdata_github/Articlev1.csv', sep=",", header=True)

# print data.head(10)
