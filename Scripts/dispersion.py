#Purpose: Looks at the range (mos) and CV (ratio) for ASD AOO and EPIAOO, ASD AOD and EpiAOD as a scatter plot
# Corresponding graphs: "AoD_rangeCV.png" "AoO_rangeCV.png" 
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import statistics
import collections
import math
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
#excel_file='Minimal Phenotype Fields - Dev Window Fields Separated_2020-05-28.xlsx'
excel_file= "Minimal Phenotype Fields - Dev Window Fields Separated_2020-06-25_16-04-37.xlsx"
vals=pd.read_excel(excel_file, sheet_name=0)
def isNaN(num):
    return num != num

def coeffVar(data):
    mean= sum(data)/len(data)
    result= statistics.pstdev(data)
    result= result/mean
    return round(result,2)
def getrange(data):
    return max(data)-min(data)
def CountFrequency(my_list): 
 
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    return freq


# first go through and put everything in dict
probandDict={}
cvDict={}
rangeDict={}
i=0
for col in vals.columns:
    if(col=="Cohort"):
        for ind in vals.index:
            
            pid=""
            eachProband=[]
            if(vals[col][ind])=="ASD,Epi":
                i+=1
                for col2 in vals.columns:
                                      
                    if col2=="Subject ID":
                        pid=vals[col2][ind]
                    if col2=="Proband's ASD Ao O (mos) (Referral)": 
                        if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                            eachProband.append(vals[col2][ind])
                    elif col2=="ASD Ao O (mos) (Interview)" :
                        if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                            eachProband.append(vals[col2][ind])
                    elif col2=="ASD Ao O (mos) (Chart)": 
                        if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                            eachProband.append(vals[col2][ind])
                    elif col2=="ASD Ao O (mos) (Self Assess)": 
                        if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                            eachProband.append(vals[col2][ind])


                if len(eachProband)>1:
                    probandDict[pid]=eachProband
       
for i in probandDict:
    if len(probandDict[i])>1:
        rangeDict[i]=getrange(probandDict[i])
    if len(probandDict[i])>2:
        cvDict[i]=coeffVar(probandDict[i])
           


# ############################
#ASD AoO: Range and CV
rangex=[]
rangey=[]
cvx=[]
cvy=[]
for i in rangeDict:
    rangex.append(i)
    rangey.append(rangeDict[i])

for i in cvDict:
    cvx.append(i)
    cvy.append(cvDict[i])


xvals=[]
for j in cvx:
    for i in range(0,len(rangex)):
        if rangex[i]== j:
            xvals.append(i)

x=np.arange(len(rangex))
x1=np.array(xvals)

print(len(rangex))
print(len(cvx))
fig,ax1=plt.subplots()
ax1.set_xlabel("Subject Id")
ax1.set_ylabel("Range",color='b')
ax1.tick_params(axis='x', rotation=90,labelsize=6)
#other axis
ax1.plot(x,rangey,'bo',label='Range')
ax2=ax1.twinx()
ax2.set_ylabel('CV',color='g')
ax2.plot(x1,cvy,'go',label='CV')
ax1.set_xticks(range(0,len(rangex)))
ax1.set_xticklabels(rangex)

fig.tight_layout()

ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.title("Dispersion per individual for ASD AoO: Range and CV")
plt.xticks(rotation=90)

plt.show()

# ########################################################################################
probandDict={}
cvDict={}
rangeDict={}
i=0
for col in vals.columns:
    if(col=="Cohort"):
        for ind in vals.index:
            
            pid=""
            eachProband=[]
            if(vals[col][ind])=="ASD,Epi":
                i+=1
                for col2 in vals.columns:
                                      
                    if col2=="Subject ID":
                        pid=vals[col2][ind]
                    if col2=="Proband's ASD Ao D (mos) (Referral)": 
                        if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                            eachProband.append(vals[col2][ind])
                    elif col2=="ASD Ao D (mos) (Interview)" :
                        if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                            eachProband.append(vals[col2][ind])
                    elif col2=="ASD Ao D (mos) (Chart)": 
                        if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                            eachProband.append(vals[col2][ind])
                    elif col2=="ASD Ao D (mos) (Self Assess)": 
                        if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                            eachProband.append(vals[col2][ind])


                if len(eachProband)>1:
                    probandDict[pid]=eachProband
       
for i in probandDict:
    if len(probandDict[i])>1:
        rangeDict[i]=getrange(probandDict[i])
    if len(probandDict[i])>2:
        cvDict[i]=coeffVar(probandDict[i])
           


# ############################
rangex=[]
rangey=[]
cvx=[]
cvy=[]
for i in rangeDict:
    rangex.append(i)
    rangey.append(rangeDict[i])

for i in cvDict:
    cvx.append(i)
    cvy.append(cvDict[i])


xvals=[]
for j in cvx:
    for i in range(0,len(rangex)):
        if rangex[i]== j:
            xvals.append(i)

x=np.arange(len(rangex))
x1=np.array(xvals)
print(len(rangex))
print(len(cvx))
fig,ax1=plt.subplots()
ax1.set_xlabel("Subject Id")
ax1.set_ylabel("Range",color='b')
ax1.tick_params(axis='x', rotation=90,labelsize=8)

ax1.plot(x,rangey,'bo',label='Range')
ax2=ax1.twinx()
ax2.set_ylabel('CV',color='g')
ax2.plot(x1,cvy,'go',label='CV')
ax1.set_xticks(range(0,len(rangex)))
ax1.set_xticklabels(rangex)

fig.tight_layout()

ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.title("Dispersion per individual for ASD AoD: Range and CV")
plt.xticks(rotation=90)

plt.show()