#C:\\Users\\thoma\\anaconda3\\envs\\codetesting python 3.11.5
# -*- coding: utf-8 -*-

""" Extract and Plot Data TMS

   This script extract a .csv files for each patients data located in the specified INPUT folder.
   Then it processes the data using an exclusion mask and plot for each subject barplot graphs.
   Different plotting functions are called and all plots are savec in the OUPUT folder.

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


####################
# Libraries        #
####################

import os # version python 3.11.5
import pandas as pd # version 2.1.0
import numpy as np # version 1.25.2
import seaborn as sns # version 0.12.2
import matplotlib.pyplot as plt # version 3.7.3

# Internal imports ### (Put here imports that are related to internal codes from the lab)


##### Please remove any patient/subject identifier from the code
##### Please use English (i.e. replace comments in Dutch or other languages)
##### Please include packages-libraries versions with a hashtag next to each of them (as numpy example above).
##### Please consider leaving a pip freeze requirements file in your projects folder so that we can keep track of all package versions used at the time the project was being executed. (https://blog.usejournal.com/why-and-how-to-make-a-requirements-txt-f329c685181e)
##### The comments in this file (e.g. ### Put here built-in..) do not need to be propagated to your code. They are only to give instructions in this template file.
##### Please consider using sections divisions such as the ones above enclosed by hashtags. 
##### Please also have a look at https://www.python.org/dev/peps/pep-0008/. This will explain how to follow the Python community standards. E.g. i=i+1 is wrong, should be i = i + 1
##### Please consider limiting all lines to 72 characters (instructions on how to do that correctly can be found in PEP-0008 Maximum Line Length section).
##### Have a look at black.vercel.app (this is a browser link). This app will help you quickly format you code (basic formatting). Then you can proceed with manual enrichment.
##### Please document your functions to create docstrings (https://www.python.org/dev/peps/pep-0257/). Example:





#### Variables
path = r"C:\Users\tpaul\Documents\12_06_2023_Collab_NHP_to_HP"  # Path to folder containing different subjects
os.chdir(path)
cwd = os.getcwd()
print(os.getcwd())
xmin = 0.45
xmax = 0.55
offset = 0.096
sampling_freq = 5000 #Hz
interval = 1/sampling_freq
mask = True

# Subjects

sub = ["P01SS", "P02CL", "P03SS", "P04TP", "P05ER", "P06CL", "P07ER", "P08TP", "P09SS"]


# Mask
# Writing the frame number from CED --> Then the algo will take the frame number - 1 (as in the table it goes starting form 0
P01SS_mask = [27, 29, 37, 51, 113]
P02CL_mask = [24, 42 ,46, 59, 87, 88, 101, 102, 103, 104, 105, 111, 116, 160]
P03SS_mask = [9, 11, 50, 51, 82, 84, 86, 88, 89, 111, 118, 130, 138]
P04TP_mask = [1, 31, 32, 33, 61, 62, 63, 66, 74, 81, 83, 84, 85, 86, 87, 89, 123, 124, 125, 133, 134, 135]
P05ER_mask = [8, 10, 23, 82, 83, 84, 85, 86,87]

P06CL_mask = [1, 2, 9, 11, 14, 24, 34, 36,  38, 39, 40, 48, 60, 61, 68, 70, 81, 83, 87, 91, 92]
P07ER_mask = [81, 82, 83]
P08TP_mask = [5, 15, 25, 27, 39, 40, 41, 46, 47, 48, 50, 59, 64, 65, 66, 70, 72, 73, 76, 77, 78, 79, 88, 90]
P09SS_mask = [1, 4, 5, 19, 23, 24, 31, 34, 35, 36, 40, 92]

def subject_mask(subject):
    if subject == "P01SS":
        return P01SS_mask
    if subject == "P02CL":
        return P02CL_mask
    if subject == "P03SS":
        return P03SS_mask
    if subject == "P04TP":
        return P04TP_mask
    if subject == "P05ER":
        return P05ER_mask

    # Session 11.07.2023
    if subject == "P06CL":
        return P06CL_mask
    if subject == "P07ER":
        return P07ER_mask
    if subject == "P08TP":
        return P08TP_mask
    if subject == "P09SS":
        return P09SS_mask

def rename_states(df):
    """
    measured -> str
    """
    df = df.rename(columns={df.columns[0]: "State", df.columns[1]: "MEP (mV)"})
    for ite, state in enumerate(df["State"]):
        if int(state) == 0:
            df = df.drop(ite)
        if int(state) == 1:
            df.loc[ite, "State"] = "Pre_01"
        if int(state) == 2:
            df.loc[ite, "State"] = "Pre_02"
        if int(state) == 3:
            df.loc[ite, "State"] = "Pre_03"
        if int(state) == 4:
            df.loc[ite, "State"] = "T05"
        if int(state) == 5:
            df.loc[ite, "State"] = "T10"
        if int(state) == 6:
            df.loc[ite, "State"] = "T15"
        if int(state) == 7:
            df.loc[ite, "State"] = "T20"
        if int(state) == 8:
            df.loc[ite, "State"] = "T25"
        if int(state) == 9:
            df.loc[ite, "State"] = "T30"
        if int(state) == 10:
            df.loc[ite, "State"] = "T35"
        if int(state) == 11:
            df.loc[ite, "State"] = "T40"
        if int(state) == 12:
            df.loc[ite, "State"] = "T45"
        if int(state) == 13:
            df.loc[ite, "State"] = "T50"
        if int(state) == 14:
            df.loc[ite, "State"] = "T55"
        if int(state) == 15:
            df.loc[ite, "State"] = "T60"
        if int(state) == 16:
            df.loc[ite, "State"] = "T70"
    return df

def compute_data_Nakajima(subject, path, mask=False, save=False):
    """
    :param subject:
    :param channel:
    :param path:
    :return:
    """
    df = pd.read_csv(path + r"\{a}\{a}.txt".format(a=subject.split("_")[0]), sep="\t", dtype=np.float64)
    if mask == True:
        length = len(df)
        mask_lst = [True for k in range(0, length)]
        for k in subject_mask(subject):
            mask_lst[k-1] = False
        df["Mask"] = mask_lst
        df["Original_Frame_Number"] = [k for k in range(0, length)]
    ######################################################################

    df = df.reset_index(drop=True)
    df = rename_states(df)

    ######################################################################
    ######################################################################
    # Only for P02CL
    # Deletion of Pre_01 and Pre_02
    if subject == "P02CL":
        data = pd.DataFrame(columns=df.columns)
        for timepoint in list(dict.fromkeys(df["State"])):
            if timepoint == "Pre_01":
                pass
            elif timepoint == "Pre_02":
                pass
            else:
                interim_df = df[df["State"] == timepoint].copy()
                first = interim_df.index[0]
                interim_df.loc[first, "Mask"] = False
                # print(interim_df.index, first, last)
                data = pd.concat([data, interim_df], axis=0)
        df = data
    ######################################################################
    ######################################################################


    ######################################################################
    ######################################################################
    # Only for P03SS
    # Deletion of Pre_01 and Pre_02
    if subject == "P03SS":
        data = pd.DataFrame(columns=df.columns)
        for timepoint in list(dict.fromkeys(df["State"])):
            if timepoint == "T20":
                interim_df = df[df["State"] == timepoint].copy()
                state_list = []
                for ite, state in enumerate(interim_df["State"]):
                    if ite < 10:
                        state_list.append("T20")
                    if ite >= 10:
                        state_list.append("T25")
                interim_df["State"]=state_list
            else:
                interim_df = df[df["State"] == timepoint].copy()
                first = interim_df.index[0]
                interim_df.loc[first, "Mask"] = False
                # print(interim_df.index, first, last)
            data = pd.concat([data, interim_df], axis=0)
        df = data
    ######################################################################
    ######################################################################

    ######################################################################
    ######################################################################
    # Only for P07ER
    # T10 was registered in T05
    if subject == "P07ER":
        data = pd.DataFrame(columns=df.columns)
        for timepoint in list(dict.fromkeys(df["State"])):
            if timepoint == "T05":
                interim_df = df[df["State"] == timepoint].copy()
                state_list = []
                for ite, state in enumerate(interim_df["State"]):
                    if ite < 10:
                        state_list.append("T05")
                    if ite >= 10:
                        state_list.append("T10")
                interim_df["State"]=state_list
            else:
                interim_df = df[df["State"] == timepoint].copy()
                first = interim_df.index[0]
                interim_df.loc[first, "Mask"] = False
                # print(interim_df.index, first, last)
            data = pd.concat([data, interim_df], axis=0)
        df = data
    ######################################################################
    ######################################################################

    if mask == True:
        df = df[df["Mask"] == True]
    return df
def compute_mean_sd(subject, path, mask=False, save=False, add_60=False):
    data = compute_data_Nakajima(subject=subject, path=path, mask=mask, save=save)

    df = pd.DataFrame(index=(["Pre_01", "Pre_02", "Pre_03", "T05", "T10","T15", "T20","T25", "T30","T35", "T40","T45", "T50", "T55", "T60"]))
    mean_list = []
    sd_list = []
    for post_fus in df.index:

        if post_fus == "Pre_01":
            p01 = [k for k in data[data["State"] == 'Pre_01']["MEP (mV)"].values]
            mean_list.append(np.mean(p01))
            sd_list.append(np.std(p01))

        if post_fus == "Pre_02":
            p02 = [k for k in data[data["State"] == 'Pre_02']["MEP (mV)"].values]
            mean_list.append(np.mean(p02))
            sd_list.append(np.std(p02))

        if post_fus == "Pre_02":
            p03 = [k for k in data[data["State"] == 'Pre_03']["MEP (mV)"].values]
            mean_list.append(np.mean(p03))
            sd_list.append(np.std(p03))

        if post_fus == "T05":
            t05 = [k for k in data[data["State"] == 'T05']["MEP (mV)"].values]
            mean_list.append(np.mean(t05))
            sd_list.append(np.std(t05))

        if post_fus == "T10":
            t10 = [k for k in data[data["State"] == 'T10']["MEP (mV)"].values]
            mean_list.append(np.mean(t10))
            sd_list.append(np.std(t10))

        if post_fus == "T15":
            t15 = [k for k in data[data["State"] == 'T15']["MEP (mV)"].values]
            mean_list.append(np.mean(t15))
            sd_list.append(np.std(t15))

        if post_fus == "T20":
            t20 = [k for k in data[data["State"] == 'T20']["MEP (mV)"].values]
            mean_list.append(np.mean(t20))
            sd_list.append(np.std(t20))

        if post_fus == "T25":
            t25 = [k for k in data[data["State"] == 'T25']["MEP (mV)"].values]
            mean_list.append(np.mean(t25))
            sd_list.append(np.std(t25))

        if post_fus == "T30":
            t30 = [k for k in data[data["State"] == 'T30']["MEP (mV)"].values]
            mean_list.append(np.mean(t30))
            sd_list.append(np.std(t30))

        if add_60:
            if post_fus == "T35":
                t35 = [k for k in data[data["State"] == 'T35']["MEP (mV)"].values]
                mean_list.append(np.mean(t35))
                sd_list.append(np.std(t35))

            if post_fus == "T40":
                t40 = [k for k in data[data["State"] == 'T40']["MEP (mV)"].values]
                mean_list.append(np.mean(t40))
                sd_list.append(np.std(t40))

            if post_fus == "T45":
                t45 = [k for k in data[data["State"] == 'T45']["MEP (mV)"].values]
                mean_list.append(np.mean(t45))
                sd_list.append(np.std(t45))

            if post_fus == "T50":
                t50 = [k for k in data[data["State"] == 'T50']["MEP (mV)"].values]
                mean_list.append(np.mean(t50))
                sd_list.append(np.std(t50))

            if post_fus == "T55":
                t55 = [k for k in data[data["State"] == 'T55']["MEP (mV)"].values]
                mean_list.append(np.mean(t55))
                sd_list.append(np.std(t55))

            if post_fus == "T60":
                t60 = [k for k in data[data["State"] == 'T60']["MEP (mV)"].values]
                mean_list.append(np.mean(t60))
                sd_list.append(np.std(t60))

            if post_fus == "T70":
                t70 = [k for k in data[data["State"] == 'T70']["MEP (mV)"].values]
                mean_list.append(np.mean(t70))
                sd_list.append(np.std(t70))

    pre_01 = [k for k in data[data["State"] == 'Pre_01']["MEP (mV)"].values]
    pre_02 = [k for k in data[data["State"] == 'Pre_02']["MEP (mV)"].values]
    pre_03 = [k for k in data[data["State"] == 'Pre_03']["MEP (mV)"].values]
    pre = pre_01 + pre_02 + pre_03
    mean_baseline = np.mean(pre)

    df["Mean - MEP (mV)"] = mean_list
    df["sd"] = sd_list
    return df, mean_baseline

def compute_normalization(mean_dataframe, mean_overbaseline):
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

def mean_between_subject(subject, path, mask, add_60, save=False):
    # subject as a list
    list_data =[]
    for s in sub:
        df_mean, mean_baseline = compute_mean_sd(subject=s, path=path, mask=mask, save=False, add_60=add_60)
        df_mean = df_mean.dropna() # drop lines with NaN (in case of too much noise)
        data, mean_normalization_baseline = compute_normalization(df_mean, mean_baseline)
        list_data.append(data)

    data = pd.concat(list_data, axis=0)
    mean_between = pd.DataFrame(index=list(dict.fromkeys(data["State"])), columns=["Normalized MEP Amplitude", "Normalized MEP SD"])
    for timepoint in list(dict.fromkeys(data["State"])):
        mean_tp = np.mean(data[data["State"] == timepoint]["Normalized MEP Amplitude"].values)
        std_tp = np.std(data[data["State"] == timepoint]["Normalized MEP sd"].values)

        if len(data[data["State"] == timepoint]) == 1:
            mean_tp = np.NaN
            std_tp = np.NaN

        mean_between.loc[timepoint]["Normalized MEP Amplitude"] = mean_tp
        mean_between.loc[timepoint]["Normalized MEP SD"] = std_tp
    mean_between = mean_between.dropna()
    return mean_between

def plot_nakajima(subject, path, add_60, mask=False, save=False):
    df_mean, mean_baseline = compute_mean_sd(subject=subject, path=path, mask=mask, save=False, add_60=add_60)
    df_mean = df_mean.dropna() # drop lines with NaN (in case of too much noise)
    data, mean_normalization_baseline = compute_normalization(df_mean, mean_baseline)

    plt.figure(figsize=(10,8))
    fig = sns.stripplot(data=data, x=data.index, y="Normalized MEP Amplitude", zorder=0, legend=False, jitter=False,
                        dodge=True)
    fig2 = sns.boxplot(data=data, x=data.index, y="Normalized MEP Amplitude", zorder=1, dodge=True)
    x_coords = []

    for point_pair in fig2.collections:
        for x, y in point_pair.get_offsets():
            x_coords.append(x)
    xcoords = list(dict.fromkeys(x_coords).keys())
    ymin = data["Normalized MEP Amplitude"].values - data["Normalized MEP sd"].values
    ymax = data["Normalized MEP Amplitude"].values + data["Normalized MEP sd"].values
    xmin = [k - 0.25 for k in xcoords]
    xmax = [k + 0.25 for k in xcoords]
    plt.vlines(x=xcoords, ymin=ymin, ymax=ymax, colors="black", zorder=1, alpha=0.25, linestyles=":")
    plt.hlines(xmin=xmin, xmax=xmax, y=ymin, colors="black", zorder=1, alpha=0.25)
    plt.hlines(xmin=xmin, xmax=xmax, y=ymax, colors="black", zorder=1, alpha=0.25)

    # Plot hline as norma baseline
    xmin, xmax, ymin, ymax = plt.axis()
    plt.hlines(mean_normalization_baseline, xmin=xmin, xmax=xmax, colors="black", linestyles=":")
    # Separation of the baseline
    #plt.vlines(x=(xcoords[2] + xcoords[3]) / 2, ymin=ymin, ymax=ymax, colors="orange", zorder=1, linestyles=":")
    plt.xticks(rotation=45, ha="right", rotation_mode="anchor")
    plt.title(subject)

    if save == True:
        plt.savefig(r"C:\Users\tpaul\Documents\12_06_2023_Collab_NHP_to_HP\{}".format(subject), dpi=300)

    plt.show()

def plot_nakajima_between_subject(mean_between, save=False):
    data = mean_between.copy()
    data["State"] = data.index
    mean_normalization_baseline = []
    for timepoint in ["Pre_01", "Pre_02", "Pre_03"]:
        mean_normalization_baseline.append(data[data["State"] == timepoint]["Normalized MEP Amplitude"])
    mean_normalization_baseline = np.mean(mean_normalization_baseline)
    plt.figure(figsize=(10,8))

    fig = sns.stripplot(data=data, x=data.index, y="Normalized MEP Amplitude", zorder=0, legend=False, jitter=False,
                        dodge=True)
    fig2 = sns.boxplot(data=data, x=data.index, y="Normalized MEP Amplitude", zorder=1, dodge=True)
    x_coords = []

    for point_pair in fig2.collections:
        for x, y in point_pair.get_offsets():
            x_coords.append(x)
    xcoords = list(dict.fromkeys(x_coords).keys())
    ymin = data["Normalized MEP Amplitude"].values - data["Normalized MEP SD"].values
    ymax = data["Normalized MEP Amplitude"].values + data["Normalized MEP SD"].values
    xmin = [k - 0.25 for k in xcoords]
    xmax = [k + 0.25 for k in xcoords]
    plt.vlines(x=xcoords, ymin=ymin, ymax=ymax, colors="black", zorder=1, alpha=0.25, linestyles=":")
    plt.hlines(xmin=xmin, xmax=xmax, y=ymin, colors="black", zorder=1, alpha=0.25)
    plt.hlines(xmin=xmin, xmax=xmax, y=ymax, colors="black", zorder=1, alpha=0.25)

    # Plot hline as norma baseline
    xmin, xmax, ymin, ymax = plt.axis()
    plt.hlines(mean_normalization_baseline, xmin=xmin, xmax=xmax, colors="black", linestyles=":")
    # Separation of the baseline
    #plt.vlines(x=(xcoords[2] + xcoords[3]) / 2, ymin=ymin, ymax=ymax, colors="orange", zorder=1, linestyles=":")
    plt.xticks(rotation=45, ha="right", rotation_mode="anchor")
    plt.title("Four Subjects")

    if save == True:
        plt.savefig(r"C:\Users\tpaul\Documents\12_06_2023_Collab_NHP_to_HP\{}".format("All"), dpi=300)

    plt.show()

for s in sub:
    data = compute_data_Nakajima(subject=s, path=path, mask=mask, save=False)
    plot_nakajima(subject=s, path=path, mask=mask, save=True, add_60=True)

#mean_between = mean_between_subject(subject=sub, path=path, mask=mask, save=False, add_60=True)
#plot_nakajima_between_subject(mean_between=mean_between, save=True)

# Stat (paired t test apparently)