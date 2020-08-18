import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import statistics
import collections
import math
import csv
from collections import defaultdict
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


rows=[]
flags={} 
filename = "flags.csv"
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
rangex=[]
rangey=[]
cvx=[]
cvy=[]
fields = ["SubjectID","ASD AoO range","ASD AoD range","Epi AoO range","Epi AoD range"] 
for i in rangeDict:
    rangex.append(i)
    rangey.append(rangeDict[i])
    if(rangeDict[i]>0):
        flags[i]=["","","",""]
        flags[i][0]=rangeDict[i]
    

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



# # ########################################################################################
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
    if(rangeDict[i]>0 and i in flags):
        flags[i][1]=rangeDict[i]
    elif rangeDict[i]>0 and i not in flags:
        flags[i]=["","","",""]
        flags[i][1]=rangeDict[i]
    

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


# ##############################################################################

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
                    if col2=="Proband's Epi Ao O (mos) (Referral)": 
                        if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                            eachProband.append(vals[col2][ind])
                    elif col2=="Age at first seizure (mos) (Interview)" :
                        if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                            eachProband.append(vals[col2][ind])
                    elif col2=="Epi Ao O (mos) (Chart)": 
                        if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                            eachProband.append(vals[col2][ind])
                    elif col2=="Age at 1st seizure (mos) (Self Assess)": 
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
    if(rangeDict[i]>0 and i in flags):
        flags[i][2]=rangeDict[i]
    elif rangeDict[i]>0 and i not in flags:
        flags[i]=["","","",""]
        flags[i][2]=rangeDict[i]

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


######################################################################################
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
                    if col2=="Proband's Epi Ao D (mos) (Referral)": 
                        if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                            eachProband.append(vals[col2][ind])
                    elif col2=="Epi Ao D (mos) (Interview)" :
                        if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                            eachProband.append(vals[col2][ind])
                    elif col2=="Epi Ao D (mos) (Chart)": 
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
    if(rangeDict[i]>0 and i in flags):
        flags[i][3]=rangeDict[i]
    elif rangeDict[i]>0 and i not in flags:
        flags[i]=["","","",""]
        flags[i][3]=rangeDict[i]

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
rows=[]
for i in flags:
    row=[]
    
    row.append(i)
    for j in flags[i]:
        row.append(j)
    rows.append(row)
    
for i in rows:
    print(i)
# # writing to csv file  
# with open(filename, 'w') as csvfile:  
#     # creating a csv writer object  
#     csvwriter = csv.writer(csvfile)  
        
#     # writing the fields  
#     csvwriter.writerow(fields)  
        
#     # writing the data rows  
#     csvwriter.writerows(rows)
