# Reading article details from input text file.
"""This script reads the text file and make a python list out of it."""
import pandas as pd

articlelist = []
with open("/Users/jeevananthamganesan/Documents/\
Inputdata_github/Article.txt") as f:
    data = f.readlines()

articledata = pd.DataFrame(articlelist)
