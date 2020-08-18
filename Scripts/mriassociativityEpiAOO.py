#Purpose: Looks at the associativity between Epi Aoo and Mri statuses and splits into two categories: mri status (3 types) percents fo Age 3 or less and mri percents for Age 3+
#Corresponding Graphs: associativityAnalysis.pdf page 3
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from matplotlib.offsetbox import AnchoredText
#excel_file='Minimal Phenotype Fields - Dev Window Fields Separated_2020-06-25.xlsx'
excel_file= "Minimal Phenotype Fields - Dev Window Fields Separated_071020.xlsx"
vals=pd.read_excel(excel_file, sheet_name=0)
def isNaN(num):
    return num != num

subjects={}
count=0
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
                                        if col2=="Proband's Epi Ao O (mos) (Referral)":
                                            if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                count+=1
                                                for col3 in vals.columns:
                            
                                                    if col3== "MRI status (Chart)":
                                                        if vals[col2][ind]<=24.0:
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                        if vals[col2][ind]>24.0:
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                        
                                        if col2=="Proband's Epi Ao O (approx) (Referral)":
                                            if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                count+=1
                                                for col3 in vals.columns:
                            
                                                    if col3== "MRI status (Chart)":
                                                        if vals[col2][ind]=="Infancy":
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                        if vals[col2][ind]!="Infancy":
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                            
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
                                        if col2=="Epi Ao O (mos) (Chart)":
                                            if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                count+=1
                                                for col3 in vals.columns:
                            
                                                    if col3== "MRI status (Chart)":
                                                        if vals[col2][ind]<=24.0:
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                        if vals[col2][ind]>24.0:
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                        
                                        if col2=="Epi Ao O (approx) (Chart)":
                                            if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                count+=1
                                                for col3 in vals.columns:
                            
                                                    if col3== "MRI status (Chart)":
                                                        if vals[col2][ind]=="Infancy":
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                        if vals[col2][ind]!="Infancy":
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                subjects[sid]=(vals[col2][ind],vals[col3][ind])


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
                                        if col2=="Age at 1st seizure (mos) (Self Assess)":
                                            if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                count+=1
                                                for col3 in vals.columns:
                            
                                                    if col3== "MRI status (Chart)":
                                                        if vals[col2][ind]<=24.0:
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                        if vals[col2][ind]>24.0:
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                        
                                        if col2=="Age at 1st seizure (approx) (Self Assess)":
                                            if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                count+=1
                                                for col3 in vals.columns:
                            
                                                    if col3== "MRI status (Chart)":
                                                        if vals[col2][ind]=="Infancy":
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                        if vals[col2][ind]!="Infancy":
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                subjects[sid]=(vals[col2][ind],vals[col3][ind])


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
                                        if col2=="Age at first seizure (mos) (Interview)":
                                            if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                count+=1
                                                for col3 in vals.columns:
                            
                                                    if col3== "MRI status (Chart)":
                                                        if vals[col2][ind]<=24.0:
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                        if vals[col2][ind]>24.0:
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                        
                                        if col2=="Age at first seizure (mos) (Interview)":
                                            if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                count+=1
                                                for col3 in vals.columns:
                            
                                                    if col3== "MRI status (Chart)":
                                                        if vals[col2][ind]=="Infancy":
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                        if vals[col2][ind]!="Infancy":
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                subjects[sid]=(vals[col2][ind],vals[col3][ind])


labels=['<= 2 years',"> 2 years"]
abnormal=[]
normal=[]
noresults=[]
awaiting=[]
fishers=[[1,1],[1,1]]
act=0
nct=0
nrct=0
wct=0
for i in subjects:
    print(i,end=", ")
    print(subjects[i][0])
    if isinstance(subjects[i][0], str):
        if subjects[i][0]=='Infancy':
            if subjects[i][1]=="Abnormal":
                act+=1
            if subjects[i][1]=="Normal":
                nct+=1
            if subjects[i][1]=="No MRI results":
                nrct+=1
            if subjects[i][1]=="Awaiting results":
                wct+=1
    else:
        if subjects[i][0]<=24.0:
            if subjects[i][1]=="Abnormal":
                act+=1
            if subjects[i][1]=="Normal":
                nct+=1
            if subjects[i][1]=="No MRI results":
                nrct+=1
            if subjects[i][1]=="Awaiting results":
                wct+=1
fishers[0][0]=act
fishers[0][1]=nct
abnormal.append(act/len(subjects)*100)
normal.append(nct/len(subjects)*100)
noresults.append(nrct/len(subjects)*100)
awaiting.append(wct/len(subjects)*100)
labels[0]+=" N= {}".format(act+nct+nrct+wct)
act=0
nct=0
nrct=0
wct=0
for i in subjects:
    if isinstance(subjects[i][0], str):
        if subjects[i][0]!='Infancy':
            if subjects[i][1]=="Abnormal":
                act+=1
            if subjects[i][1]=="Normal":
                nct+=1
            if subjects[i][1]=="No MRI results":
                nrct+=1
            if subjects[i][1]=="Awaiting results":
                wct+=1
    else:
        if subjects[i][0]>24.0:
            if subjects[i][1]=="Abnormal":
                act+=1
            if subjects[i][1]=="Normal":
                nct+=1
            if subjects[i][1]=="No MRI results":
                nrct+=1
            if subjects[i][1]=="Awaiting results":
                wct+=1
fishers[1][0]=act
fishers[1][1]=nct
abnormal.append(act/len(subjects)*100)
normal.append(nct/len(subjects)*100)
noresults.append(nrct/len(subjects)*100)
awaiting.append(wct/len(subjects)*100)
labels[1]+=" N= {}".format(act+nct+nrct+wct)    
        
print(abnormal)
print(normal)
print(noresults)
print(awaiting)
print(len(subjects))

oddsratio, pvalue = stats.fisher_exact(fishers)
anchored_text = AnchoredText("Odds Ratio: {} \n p value: {}".format(oddsratio,pvalue), loc=2)
df = pd.DataFrame({'Abnormal': abnormal,
                   'Normal': normal,
                   'No Results': noresults,
                   'Awaiting Results':awaiting}, index=labels)
ax = df.plot.bar(rot=0)




ax.set_ylabel('%')
ax.set_title('Epi AoO vs MRI Status N={}'.format(len(subjects)))
for p in ax.patches[0:]:
    h = p.get_height()
    x = p.get_x()+p.get_width()/2.
    if h != 0:
        ax.annotate("{:.1f}".format(p.get_height()), xy=(x,h), xytext=(0,4), rotation=90, 
                   textcoords="offset points", ha="center", va="bottom", fontsize=7)
ax.add_artist(anchored_text)
ax.set_ylim(0, 100)
plt.show()