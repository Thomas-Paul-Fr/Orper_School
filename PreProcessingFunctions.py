# C:\\Users\\thoma\\anaconda3\\envs\\codetesting python 3.8
# -*- coding: utf-8 -*-

""" Script to preprocess the data

   This script is used to compute rename some elements in the data .txt and exclude outliers

"""

__author__ = "Thomas Paul"
__contact__ = "thomas.paul@epfl.ch"
__date__ = "2023/06/01"  ### Date it was created
__status__ = "Under Development"  ### Production = still being developed. Else: Concluded/Finished.

####################
# Review History   #
####################

# Written on 2023/09/14 -> Thomas Paul

####################
# Libraries        #
####################
import pandas as pd  # version 2.1.0
import numpy as np  # version 1.25.2

def rename_cols_and_rows(data_to_extract):
    """
    This function is used to rename my .txt file
    Cf NOTE in OpenCsvAndExtractData for .txt structure.
    :param data_to_extract: .txt Dataframe read in OpenFileAndExtractData.
    :return: data_extracted : pandas.DataFrame. DataFrame with or without the outliers.
    """
    # First we rename the first and second columns
    data_to_extract = data_to_extract.rename(columns={data_to_extract.columns[0]: "State", data_to_extract.columns[1]: "MEP (mV)"})

    # For each state we rename with the equivalent timepoint
    for ite, state in enumerate(data_to_extract["State"]):
        if int(state) == 0:
            data_to_extract = data_to_extract.drop(ite)
        if int(state) == 1:
            data_to_extract.loc[ite, "State"] = "Pre_01"
        if int(state) == 2:
            data_to_extract.loc[ite, "State"] = "Pre_02"
        if int(state) == 3:
            data_to_extract.loc[ite, "State"] = "Pre_03"
        if int(state) == 4:
            data_to_extract.loc[ite, "State"] = "T05"
        if int(state) == 5:
            data_to_extract.loc[ite, "State"] = "T10"
        if int(state) == 6:
            data_to_extract.loc[ite, "State"] = "T15"
        if int(state) == 7:
            data_to_extract.loc[ite, "State"] = "T20"
        if int(state) == 8:
            data_to_extract.loc[ite, "State"] = "T25"
        if int(state) == 9:
            data_to_extract.loc[ite, "State"] = "T30"
        if int(state) == 10:
            data_to_extract.loc[ite, "State"] = "T35"
        if int(state) == 11:
            data_to_extract.loc[ite, "State"] = "T40"
        if int(state) == 12:
            data_to_extract.loc[ite, "State"] = "T45"
        if int(state) == 13:
            data_to_extract.loc[ite, "State"] = "T50"
        if int(state) == 14:
            data_to_extract.loc[ite, "State"] = "T55"
        if int(state) == 15:
            data_to_extract.loc[ite, "State"] = "T60"
        if int(state) == 16:
            data_to_extract.loc[ite, "State"] = "T70"
    return data_to_extract

def OpenFileAndExtractData(subject, path, mask=False):
    """
    Open a .txt data file obtained from the Signal software and extracts or not its outliers.

    NOTE: the subject and path lead to the .csv file. This format of the .csv should be as follows:
    ##################################
    |Frame state|Channel	|Mask    |
    |1	        |0.94604492	|    1   |
    |1	        |1.0586548	|    1   |
    The file is a .txt file with a coma delimiter.

    :param subject: Name of the subject from subject_list.
    :param path: Path to the folder containing the subject data.
    :param mask: Boolean. If False or 0 then the binary mask will be used to exclude the trials to remove

    :return: data_extracted : pandas.DataFrame. DataFrame with or without the outliers.
    """
    data_to_extract = pd.read_csv(path + r"\{a}\{a}.txt".format(a=subject.split("_")[0]), sep=",", dtype=np.float64)

    # Processing to renaming of the Data columns and rows
    data_extracted = rename_cols_and_rows(data_to_extract)

    if mask == True:
        data_extracted = data_extracted[data_extracted["Mask"] == True]
        data_extracted = data_extracted.reset_index(drop=True)
    return data_extracted


