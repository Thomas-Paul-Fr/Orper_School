#C:\\Users\\thoma\\anaconda3\\envs\\codetesting python 3.8
# -*- coding: utf-8 -*-

""" Extract Data TMS

   This script extract a .csv files for each patients data located in the specified INPUT folder.
   Then it processes the data using an exclusion mask via the set of function written in CalculationFucntions.py.
   In the future, different plotting functions will be called.

"""

__author__ = "Thomas Paul"
__contact__ = "thomas.paul@epfl.ch"
__date__ = "2023/06/01"   ### Date it was created
__status__ = "Under Development" ### Production = still being developed. Else: Concluded/Finished.

####################
# Review History   #
####################

# Written on 2023/06/01 -> Thomas Paul
# First Draft correction 2023/09/13 -> Thomas Paul
# Second Draft correction 2023/09/14 -> Thomas Paul

####################
# Libraries        #
####################

import os # version python 3.11.5
import pandas as pd # version 2.1.0
import numpy as np # version 1.25.2
import seaborn as sns # version 0.12.2
import matplotlib.pyplot as plt # version 3.7.3

# Internal imports
import PreProcessingFunctions as preprocess
import CalculationFunctions as calcfunct

#### Variables
# Path to the folder containing files to be analyzed
path = r"C:\Users\thoma\Desktop\code\CODE_GIT\INPUT"
os.chdir(path)
print("The directory containing the file is:", os.getcwd())

# List Containing the subjects in the path folder from which we want to run the analysis
subject_list = ["P04TP"]

# If mask is true then the outliers are excluded
mask = True

# Dictionnary to have each subject attributed to its data frame
dict_subject = {}
for subject in subject_list:
    dict_subject[subject + "_data"] = preprocess.OpenFileAndExtractData(subject=subject, path=path, mask=mask)
    data_analysis, mean_baseline = calcfunct.compute_mean_sd(data_to_analyse=dict_subject[subject + "_data"])
    normalized_dataframe, _ = calcfunct.compute_normalization(mean_dataframe=data_analysis,
                                                              mean_overbaseline=mean_baseline)
print("--END")











