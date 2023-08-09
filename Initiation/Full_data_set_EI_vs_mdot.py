from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


##################################################
#                     Shot Data                  #
##################################################
##Nonel
#Clap
nonel_clap = pd.read_csv("NONELCLAP.csv")
mdot_nonel_clap = nonel_clap.mdot
IE_nonel_clap = nonel_clap.IE
plt.plot(mdot_nonel_clap,IE_nonel_clap, marker = "s", markeredgecolor = "k", color="w", label = "Clapping")
#4 waves
nonel_4w = pd.read_csv("NONEL4WAV.csv")
mdot_nonel_4w = nonel_4w.mdot
IE_nonel_4w = nonel_4w.IE
plt.plot(mdot_nonel_4w,IE_nonel_4w, marker = "o", markeredgecolor = "k", color="w", label = "Co-rotating")
# 3 waves
nonel_3w = pd.read_csv("NONEL3WAV.csv")
mdot_nonel_3w = nonel_3w.mdot
IE_nonel_3w = nonel_3w.IE
plt.plot(mdot_nonel_3w,IE_nonel_3w, marker = "o", markeredgecolor = "k", color="w")
# # 1 Wave
# nonel_1w = pd.read_csv("NONEL1wav.csv")
# mdot_nonel_1w = nonel_1w.mdot
# IE_nonel_1w = nonel_1w.IE
# plt.plot(mdot_nonel_1w,IE_nonel_1w, marker = "o", markeredgecolor = "k", color="w")

## Low Energy spark igniter
LE_fail = pd.read_csv("LE FAIL.csv")
mdot_LE_fail = LE_fail.mdot
IE_LE_fail = LE_fail.IE
plt.plot(mdot_LE_fail,IE_LE_fail, marker = "x", markeredgecolor = "k", color="w", label = "Fail")
#1 Wave
LE_1w = pd.read_csv("LE SINGLE.csv")
mdot_LE_1w = LE_1w.mdot
IE_LE_1w = LE_1w.IE
plt.plot(mdot_LE_1w,IE_LE_1w, marker = "o", markeredgecolor = "k", color="w")

#2 Wave
LE_2w = pd.read_csv("LE 2WAV.csv")
mdot_LE_2w = LE_2w.mdot
IE_LE_2w = LE_2w.IE
plt.plot(mdot_LE_2w,IE_LE_2w, marker = "o", markeredgecolor = "k", color="w")

#CLAP
LE_clap = pd.read_csv("LE CLAP.csv")
mdot_LE_clap = LE_clap.mdot
IE_LE_clap = LE_clap.IE
plt.plot(mdot_LE_clap,IE_LE_clap, marker = "s", markeredgecolor = "k", color="w")


##High energy spark igniter
HE_fail = pd.read_csv("HEFAIL.csv")
mdot_HE_fail = HE_fail.mdot
IE_HE_fail = HE_fail.IE
plt.plot(mdot_HE_fail,IE_HE_fail, marker = "x", markeredgecolor = "k", color="w")
#1 Wave
HE_1w = pd.read_csv("HE1WAV.csv")
mdot_HE_1w = HE_1w.mdot
IE_HE_1w = HE_1w.IE
plt.plot(mdot_HE_1w,IE_HE_1w, marker = "o", markeredgecolor = "k", color="w")
#CLAP
HE_clap = pd.read_csv("HECLAP.csv")
mdot_HE_clap = HE_clap.mdot
IE_HE_clap = HE_clap.IE
plt.plot(mdot_HE_clap,IE_HE_clap, marker = "s", markeredgecolor = "k", color="w")

plt.legend(loc="upper right")
plt.savefig("IE_vs_mdot.svg")
plt.show()
