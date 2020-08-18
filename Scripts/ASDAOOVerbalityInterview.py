# Purpose: Looks at the correlation of AoO ASD and Verbality by looking at the break up of 5 types of verbality statuses from Interview 
# Corresponding Graph:"ASDAOOInterviewVerbality.png"

#import statements
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

#Excel file
#excel_file='Minimal Phenotype Fields - Dev Window Fields Separated_2020-06-25.xlsx'
excel_file= "Minimal Phenotype Fields - Dev Window Fields Separated_071020.xlsx"
vals=pd.read_excel(excel_file, sheet_name=0)
#Check if cell is nan
def isNaN(num):
    return num != num

#We are prioritizing by referral, chart,self assess, interview
# index of 0:don't include NAN 
#index of 1: Include nan values
def parseData(index):
    subjects={}
    count=0
    # get the columns
    for col in vals.columns:
        if col=="Cohort":
            #get values in the column
            for ind in vals.index:
                if vals[col][ind]=="ASD,Epi":
                    # Repeat to get the complete chart review
                    for col1 in vals.columns:
                        if col1=="Chart Review Complete":
                            if vals[col1][ind]=="Complete":
                                # store subject id
                                for col4 in vals.columns:   
                                    if col4=="Subject ID":
                                        sid=vals[col4][ind] 
                                        for col2 in vals.columns:
                                            if col2=="Proband's ASD Ao O (mos) (Referral)":
                                                # get the AOO
                                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                    count+=1
                                                    for col3 in vals.columns:
                                                        if col3== "Nonverbal (Interview)":
                                                            # Check if age is less than 2 yrs
                                                            if vals[col2][ind]<=24.0:
                                                                if index==0:
                                                                    if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                        subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                                elif index==1:
                                                                    subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                            # Check if age is more than 2 yrs
                                                            if vals[col2][ind]>24.0:
                                                                if index==0:
                                                                    if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                        subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                                elif index==1:
                                                                    subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                            # Repeat for the ordinal column
                                            if col2=="Proband's ASD Ao O (approx) (Referral)":
                                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                    count+=1
                                                    for col3 in vals.columns:
                                
                                                        if col3== "Nonverbal (Interview)":
                                                            if vals[col2][ind]=="Infancy":
                                                                if index==0:
                                                                    if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                        subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                                elif index==1:
                                                                    subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                            if vals[col2][ind]!="Infancy":
                                                                if index==0:
                                                                    if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                        subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                                elif index==1:
                                                                    subjects[sid]=(vals[col2][ind],vals[col3][ind])
    # repeat for interview                                                            
    for col in vals.columns:
        if col=="Cohort":
            for ind in vals.index:
                if vals[col][ind]=="ASD,Epi":
                    for col1 in vals.columns:
                        if col1=="Chart Review Complete":
                            if vals[col1][ind]=="Complete":
                                for col4 in vals.columns:   
                                    if col4=="Subject ID":
                                        sid=vals[col4][ind] 
                                        for col2 in vals.columns:
                                            if col2=="ASD Ao O (mos) (Chart)":
                                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                    count+=1
                                                    for col3 in vals.columns:
                                
                                                        if col3== "Nonverbal (Interview)":
                                                            if vals[col2][ind]<=24.0:
                                                                if index==0:
                                                                    if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                        subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                                elif index==1:
                                                                    subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                            if vals[col2][ind]>24.0:
                                                                if index==0:
                                                                    if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                        subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                                elif index==1:
                                                                    subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                            
                                            if col2=="ASD Ao O (approx) (Chart)":
                                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                    count+=1
                                                    for col3 in vals.columns:
                                
                                                        if col3== "Nonverbal (Interview)":
                                                            if vals[col2][ind]=="Infancy":
                                                                if index==0:
                                                                    if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                        subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                                elif index==1:
                                                                    subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                            if vals[col2][ind]!="Infancy":
                                                                if index==0:
                                                                    if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                        subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                                elif index==1:
                                                                    subjects[sid]=(vals[col2][ind],vals[col3][ind])

    # repeat for self assess
    for col in vals.columns:
        if col=="Cohort":
            for ind in vals.index:
                if vals[col][ind]=="ASD,Epi":
                    for col1 in vals.columns:
                        if col1=="Chart Review Complete":
                            if vals[col1][ind]=="Complete":
                                for col4 in vals.columns:   
                                    if col4=="Subject ID":
                                        sid=vals[col4][ind] 
                                        for col2 in vals.columns:
                                            if col2=="ASD Ao O (mos) (Self Assess)":
                                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                    count+=1
                                                    for col3 in vals.columns:
                                
                                                        if col3== "Nonverbal (Interview)":
                                                            if vals[col2][ind]<=24.0:
                                                                if index==0:
                                                                    if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                        subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                                elif index==1:
                                                                    subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                            if vals[col2][ind]>24.0:
                                                                if index==0:
                                                                    if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                        subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                                elif index==1:
                                                                    subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                            
                                            if col2=="ASD Ao O (approx) (Self Assess)":
                                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                    count+=1
                                                    for col3 in vals.columns:
                                
                                                        if col3== "Nonverbal (Interview)":
                                                            if vals[col2][ind]=="Infancy":
                                                                if index==0:
                                                                    if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                        subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                                elif index==1:
                                                                    subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                            if vals[col2][ind]!="Infancy":
                                                                if index==0:
                                                                    if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                        subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                                elif index==1:
                                                                    subjects[sid]=(vals[col2][ind],vals[col3][ind])

    # repeat for interview
    for col in vals.columns:
        if col=="Cohort":
            for ind in vals.index:
                if vals[col][ind]=="ASD,Epi":
                    for col1 in vals.columns:
                        if col1=="Chart Review Complete":
                            if vals[col1][ind]=="Complete":
                                for col4 in vals.columns:   
                                    if col4=="Subject ID":
                                        sid=vals[col4][ind] 
                                        for col2 in vals.columns:
                                            if col2=="ASD Ao O (mos) (Interview)":
                                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                    count+=1
                                                    for col3 in vals.columns:
                                
                                                        if col3== "Nonverbal (Interview)":
                                                            if vals[col2][ind]<=24.0:
                                                                if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                    subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                            if vals[col2][ind]>24.0:
                                                                if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                    subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                            
                                            if col2=="ASD Ao O (approx) (Interview)":
                                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                    count+=1
                                                    for col3 in vals.columns:
                                
                                                        if col3== "Nonverbal (Interview)":
                                                            if vals[col2][ind]=="Infancy":
                                                                if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                    subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                            if vals[col2][ind]!="Infancy":
                                                                if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                    subjects[sid]=(vals[col2][ind],vals[col3][ind])
    return subjects


t=parseData(1)
labels=['<= 2 years',"> 2 years"]
sd=0
nvl3w=0
nvnw=0
lv=0
sdL=[]
v=0
ot=0
nvl3wL=[]
nvnwL=[]
lvL=[]
verbal=[]
other=[]
tot=0
# Go through the dictionary and count the number of less than 2years and speech delay
#less than 2years and less than 3 words
# less than 2years and no words
#less than 2years and limited
#less than 2years and other
# Go through the dictionary and count the number of more than 2years and speech delay
#more than 2years and less than 3 words
# more than 2years and no words
#more than 2years and limited
#more than 2years and other
for i in t:
    print(i,end=", ")
    print(t[i])
    
    if isinstance(t[i][0], str):
        if t[i][0]=='Infancy' or t[i][0]=='Birth':
            tot+=1
            if isNaN(t[i][1]):
                v+=1
            if not isNaN(t[i][1]) and ";" in t[i][1]:
                types=t[i][1].split(";")
                for j in types:
                    if j=="Speech delay":
                        sd+=1
                    elif j ==  'Nonverbal - less than 3 words':
                        nvl3w+=1
                    elif j ==  'Nonverbal - no words':
                        nvnw+=1
                    elif j ==  'Limited vocabulary - 3 or more words':
                        lv+=1
                    elif "Other" in j:
                        ot+=1
            elif not isNaN(t[i][1]) and ";" not in t[i][1] :
                if t[i][1]=="Speech delay":
                    sd+=1
                elif t[i][1] ==  'Nonverbal - less than 3 words':
                    nvl3w+=1
                elif t[i][1] ==  'Nonverbal - no words':
                    nvnw+=1
                elif t[i][1] ==  'Limited vocabulary - 3 or more words':
                    lv+=1
                elif "Other" in j:
                        ot+=1
    else:
        
        if t[i][0]<=24.0:
            tot+=1
            if isNaN(t[i][1]):
                v+=1
            if not isNaN(t[i][1]) and ";" in t[i][1]:
                types=t[i][1].split(";")
                for j in types:
                    if j=="Speech delay":
                        sd+=1
                    elif j ==  'Nonverbal - less than 3 words':
                        nvl3w+=1
                    elif j ==  'Nonverbal - no words':
                        nvnw+=1
                    elif j ==  'Limited vocabulary - 3 or more words':
                        lv+=1
                    elif "Other" in j:
                        ot+=1
            elif not isNaN(t[i][1]) and ";" not in t[i][1] :
                if t[i][1]=="Speech delay":
                    sd+=1
                elif t[i][1] ==  'Nonverbal - less than 3 words':
                    nvl3w+=1
                elif t[i][1] ==  'Nonverbal - no words':
                    nvnw+=1
                elif t[i][1] ==  'Limited vocabulary - 3 or more words':
                    lv+=1
                elif "Other" in j:
                        ot+=1

sdL.append(sd/len(t)*100)
nvl3wL.append(nvl3w/len(t)*100)
nvnwL.append(nvnw/len(t)*100)
lvL.append(lv/len(t)*100)
verbal.append(v/len(t)*100)
other.append(ot/len(t)*100)
labels[0]+=" N= {}".format(tot)
sd=0
nvl3w=0
nvnw=0
lv=0
v=0
ot=0
tot=0
for i in t:
    print(i,end=", ")
    print(t[i])
    
    if isinstance(t[i][0], str):
        if t[i][0]!='Infancy' or t[i][0]!='Birth':
            tot+=1
            if isNaN(t[i][1]):
                v+=1
            if not isNaN(t[i][1]) and ";" in t[i][1]:
                types=t[i][1].split(";")
                for j in types:
                    if j=="Speech delay":
                        sd+=1
                    elif j ==  'Nonverbal - less than 3 words':
                        nvl3w+=1
                    elif j ==  'Nonverbal - no words':
                        nvnw+=1
                    elif j ==  'Limited vocabulary - 3 or more words':
                        lv+=1
                    elif "Other" in j:
                        ot+=1
            elif not isNaN(t[i][1]) and ";" not in t[i][1] :
                if t[i][1]=="Speech delay":
                    sd+=1
                elif t[i][1] ==  'Nonverbal - less than 3 words':
                    nvl3w+=1
                elif t[i][1] ==  'Nonverbal - no words':
                    nvnw+=1
                elif t[i][1] ==  'Limited vocabulary - 3 or more words':
                    lv+=1
                elif "Other" in j:
                        ot+=1
    else:
        
        if t[i][0]>24.0:
            tot+=1
            if isNaN(t[i][1]):
                v+=1
            if not isNaN(t[i][1]) and ";" in t[i][1]:
                types=t[i][1].split(";")
                for j in types:
                    if j=="Speech delay":
                        sd+=1
                    elif j ==  'Nonverbal - less than 3 words':
                        nvl3w+=1
                    elif j ==  'Nonverbal - no words':
                        nvnw+=1
                    elif j ==  'Limited vocabulary - 3 or more words':
                        lv+=1
                    elif "Other" in j:
                        ot+=1
            elif not isNaN(t[i][1]) and ";" not in t[i][1] :
                if t[i][1]=="Speech delay":
                    sd+=1
                elif t[i][1] ==  'Nonverbal - less than 3 words':
                    nvl3w+=1
                elif t[i][1] ==  'Nonverbal - no words':
                    nvnw+=1
                elif t[i][1] ==  'Limited vocabulary - 3 or more words':
                    lv+=1
                elif "Other" in j:
                        ot+=1

sdL.append(sd/len(t)*100)
nvl3wL.append(nvl3w/len(t)*100)
nvnwL.append(nvnw/len(t)*100)
lvL.append(lv/len(t)*100)
verbal.append(v/len(t)*100)
other.append(ot/len(t)*100)
labels[1]+=" N= {}".format(tot)
        
# make the graph by setting the colors, bar width, y labels, x ticks
barWidth =0.12
r1=np.arange(len(sdL))
r2=[x+barWidth for x in r1]
r3=[x + barWidth for x in r2]
r4=[x + barWidth for x in r3]
r5=[x + barWidth for x in r4]
r6=[x + barWidth for x in r5]
p1=plt.bar(r1, sdL, color='#7f6d5f', width=barWidth, edgecolor='white', label='Speech Delay')
p2=plt.bar(r2, nvl3wL, color='#557f2d', width=barWidth, edgecolor='white', label='NV:Less than 3 words')
p3=plt.bar(r3, nvnwL, color='#2d7f5e', width=barWidth, edgecolor='white', label='NV: No Words')  
p4=plt.bar(r4, lvL, color='#5f3f5e', width=barWidth, edgecolor='white', label="Limited Vocabulary")
p5=plt.bar(r5, other, color='#8F3C4F', width=barWidth, edgecolor='white', label='Other')  
p6=plt.bar(r6, verbal, color='#9EA8C7', width=barWidth, edgecolor='white', label="Verbal")



plt.ylabel('%')
plt.xticks([r + barWidth for r in range(len(verbal))], labels)
plt.legend()
plt.title('ASD AoO vs Verbality Interview Status N={}'.format(len(t)+1))
plt.ylim(top=100)
plt.ylim(bottom=0)
#labels for the bar heights
for rect in p1+p2+p3+p4+p5+p6:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')


plt.show()