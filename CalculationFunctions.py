# C:\\Users\\thoma\\anaconda3\\envs\\codetesting python 3.8
# -*- coding: utf-8 -*-

""" Calculation Mean and SD

   This script is used to compute mean and sd from the preprocessed files

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
import pandas as pd # version 2.1.0
import numpy as np # version 1.25.2


def compute_mean_sd(data_to_analyse):
    """
        Compute the mean and the standard deviation for each timepoint

        :param data_to_analyse: Processed data ready to be analysed as computed in PreProcessingFucntions.py

        :return: data_analysis : Analysed data.
        :return: mean_baseline : The value of the mean amongst baseline to compute the normalization
        """

    # Code snippet to extract the timepoint without using the set function from python
    timepoint_list = [timepoint for timepoint in data_to_analyse["State"]]
    timepoint_unique = []
    for timepoint in timepoint_list:
        if timepoint not in timepoint_unique:
            timepoint_unique.append(timepoint) # Order of timepoint is kept

    data_analysis = pd.DataFrame(index=(timepoint_unique))
    mean_list = []
    sd_list = []
    # Compute the mean for each timepoint.
    # /!\ Need to later on be generalized
    for post_fus in data_analysis.index:
        if post_fus == "Pre_01":
            p01 = [k for k in data_to_analyse[data_to_analyse["State"] == 'Pre_01']["MEP (mV)"].values]
            mean_list.append(np.mean(p01))
            sd_list.append(np.std(p01))

        if post_fus == "Pre_02":
            p02 = [k for k in data_to_analyse[data_to_analyse["State"] == 'Pre_02']["MEP (mV)"].values]
            mean_list.append(np.mean(p02))
            sd_list.append(np.std(p02))

        if post_fus == "Pre_02":
            p03 = [k for k in data_to_analyse[data_to_analyse["State"] == 'Pre_03']["MEP (mV)"].values]
            mean_list.append(np.mean(p03))
            sd_list.append(np.std(p03))

        if post_fus == "T05":
            t05 = [k for k in data_to_analyse[data_to_analyse["State"] == 'T05']["MEP (mV)"].values]
            mean_list.append(np.mean(t05))
            sd_list.append(np.std(t05))

        if post_fus == "T10":
            t10 = [k for k in data_to_analyse[data_to_analyse["State"] == 'T10']["MEP (mV)"].values]
            mean_list.append(np.mean(t10))
            sd_list.append(np.std(t10))

        if post_fus == "T15":
            t15 = [k for k in data_to_analyse[data_to_analyse["State"] == 'T15']["MEP (mV)"].values]
            mean_list.append(np.mean(t15))
            sd_list.append(np.std(t15))

        if post_fus == "T20":
            t20 = [k for k in data_to_analyse[data_to_analyse["State"] == 'T20']["MEP (mV)"].values]
            mean_list.append(np.mean(t20))
            sd_list.append(np.std(t20))

        if post_fus == "T25":
            t25 = [k for k in data_to_analyse[data_to_analyse["State"] == 'T25']["MEP (mV)"].values]
            mean_list.append(np.mean(t25))
            sd_list.append(np.std(t25))

        if post_fus == "T30":
            t30 = [k for k in data_to_analyse[data_to_analyse["State"] == 'T30']["MEP (mV)"].values]
            mean_list.append(np.mean(t30))
            sd_list.append(np.std(t30))

        if post_fus == "T35":
            t35 = [k for k in data_to_analyse[data_to_analyse["State"] == 'T35']["MEP (mV)"].values]
            mean_list.append(np.mean(t35))
            sd_list.append(np.std(t35))

        if post_fus == "T40":
            t40 = [k for k in data_to_analyse[data_to_analyse["State"] == 'T40']["MEP (mV)"].values]
            mean_list.append(np.mean(t40))
            sd_list.append(np.std(t40))

        if post_fus == "T45":
            t45 = [k for k in data_to_analyse[data_to_analyse["State"] == 'T45']["MEP (mV)"].values]
            mean_list.append(np.mean(t45))
            sd_list.append(np.std(t45))

        if post_fus == "T50":
            t50 = [k for k in data_to_analyse[data_to_analyse["State"] == 'T50']["MEP (mV)"].values]
            mean_list.append(np.mean(t50))
            sd_list.append(np.std(t50))

        if post_fus == "T55":
            t55 = [k for k in data_to_analyse[data_to_analyse["State"] == 'T55']["MEP (mV)"].values]
            mean_list.append(np.mean(t55))
            sd_list.append(np.std(t55))

        if post_fus == "T60":
            t60 = [k for k in data_to_analyse[data_to_analyse["State"] == 'T60']["MEP (mV)"].values]
            mean_list.append(np.mean(t60))
            sd_list.append(np.std(t60))

        if post_fus == "T70":
            t70 = [k for k in data_to_analyse[data_to_analyse["State"] == 'T70']["MEP (mV)"].values]
            mean_list.append(np.mean(t70))
            sd_list.append(np.std(t70))

    # Collecting values for the three baseline pre 01 02 and  03
    pre_01 = [k for k in data_to_analyse[data_to_analyse["State"] == 'Pre_01']["MEP (mV)"].values]
    pre_02 = [k for k in data_to_analyse[data_to_analyse["State"] == 'Pre_02']["MEP (mV)"].values]
    pre_03 = [k for k in data_to_analyse[data_to_analyse["State"] == 'Pre_03']["MEP (mV)"].values]
    pre = pre_01 + pre_02 + pre_03
    # TO compute its mean
    mean_baseline = np.mean(pre)

    # Reattribute to the new table
    data_analysis["Mean - MEP (mV)"] = mean_list
    data_analysis["sd"] = sd_list
    return data_analysis, mean_baseline

def compute_normalization(mean_dataframe, mean_overbaseline):
    """
        Normalize the data with the mean extracted from the baselines

        :param: mean_dataframe : Analysed data that will be normalized
        :param: mean_overbaseline : The value of the mean amongst baseline to compute the normalization

        :return:  mean_dataframe. For each data, the values after baseline normalization
        :return: mean_normalization_baseline. Baseline normalized
    """
    mean_norma = [val/mean_overbaseline for val in mean_dataframe["Mean - MEP (mV)"]]
    sd = [val/mean_overbaseline for val in mean_dataframe["sd"]]
    mean_dataframe["Normalized MEP Amplitude"] = mean_norma
    mean_dataframe["Normalized MEP sd"] = sd

    mean_dataframe["State"] = mean_dataframe.index
    pre_01 = [k for k in mean_dataframe[mean_dataframe["State"] == 'Pre_01']["Normalized MEP Amplitude"].values]
    pre_02 = [k for k in mean_dataframe[mean_dataframe["State"] == 'Pre_02']["Normalized MEP Amplitude"].values]
    pre_03 = [k for k in mean_dataframe[mean_dataframe["State"] == 'Pre_03']["Normalized MEP Amplitude"].values]
    pre = pre_01 + pre_02 + pre_03
    mean_normalization_baseline = np.mean(pre)
    return mean_dataframe, mean_normalization_baseline