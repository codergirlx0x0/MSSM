#Purpose: Looks at the associativity between ASD Aoo and Verbality and splits into two categories: verbal/nonverbal percents fo Age 3 or less and verbal/nonverbal percents for Age 3+
#Corresponding Graphs: associativityAnalysis.pdf page 7
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
def parseData(index):
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
                                            if col2=="Proband's ASD Ao O (mos) (Referral)":
                                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                    count+=1
                                                    for col3 in vals.columns:
                                
                                                        if col3== "Nonverbal (Chart)":
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
                                            
                                            if col2=="Proband's ASD Ao O (approx) (Referral)":
                                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                    count+=1
                                                    for col3 in vals.columns:
                                
                                                        if col3== "Nonverbal (Chart)":
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
                                
                                                        if col3== "Nonverbal (Chart)":
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
                                
                                                        if col3== "Nonverbal (Chart)":
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
                                
                                                        if col3== "Nonverbal (Chart)":
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
                                
                                                        if col3== "Nonverbal (Chart)":
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
                                
                                                        if col3== "Nonverbal (Chart)":
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
                                
                                                        if col3== "Nonverbal (Chart)":
                                                            if vals[col2][ind]=="Infancy":
                                                                if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                    subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                            if vals[col2][ind]!="Infancy":
                                                                if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                    subjects[sid]=(vals[col2][ind],vals[col3][ind])
    return subjects

s=parseData(0)
t=parseData(1)
labels=['<= 2 years',"> 2 years"]
verbal=[]
nonverbal=[]
unknown=[]
fishers=[[1,1],[1,1]]
vct=0
nct=0
uct=0
for i in t:
    print(i,end=", ")
    print(t[i][0])
    if isinstance(t[i][0], str):
        if t[i][0]=='Infancy' or t[i][0]=='Birth':
            if t[i][1]=="Yes" or isNaN(t[i][1]):
                vct+=1
            elif t[i][1]=="No" :
                nct+=1
            elif t[i][1]=="Unknown":
                uct+=1
    else:
        if t[i][0]<=24.0:
            if t[i][1]=="Yes" or isNaN(t[i][1]):
                vct+=1
            elif t[i][1]=="No" :
                nct+=1
            elif t[i][1]=="Unknown":
                uct+=1
fishers[0][0]=nct
fishers[0][1]=vct
verbal.append(vct/len(t)*100)
nonverbal.append(nct/len(t)*100)
unknown.append(uct/len(t)*100)
labels[0]+=" N= {}".format(nct+vct+uct)
vct=0
nct=0
uct=0
for i in t:
    if isinstance(t[i][0], str):
        if t[i][0]!='Infancy' and t[i][0]!='Birth':
            if t[i][1]=="Yes" or isNaN(t[i][1]):
                vct+=1
            elif t[i][1]=="No" :
                nct+=1
            elif t[i][1]=="Unknown":
                uct+=1
    else:
        if t[i][0]>24.0:
            if t[i][1]=="Yes" or isNaN(t[i][1]):
                vct+=1
            elif t[i][1]=="No":
                nct+=1
            elif t[i][1]=="Unknown":
                uct+=1
fishers[1][0]=nct
fishers[1][1]=vct
unknown.append(uct/len(t)*100)
verbal.append(vct/len(t)*100)
nonverbal.append(nct/len(t)*100)
labels[1]+=" N= {}".format(nct+vct+uct)    
        
plt.subplot(2,1,1)
barWidth =0.25
r1=np.arange(len(verbal))
r2=[x+barWidth for x in r1]
r3=[x + barWidth for x in r2]
p1=plt.bar(r1, verbal, color='#7f6d5f', width=barWidth, edgecolor='white', label='Verbal')
p2=plt.bar(r2, nonverbal, color='#557f2d', width=barWidth, edgecolor='white', label='Non Verbal')
p3=plt.bar(r3, unknown, color='#2d7f5e', width=barWidth, edgecolor='white', label='Unknown')  

oddsratio, pvalue = stats.fisher_exact(fishers)

plt.ylabel('%')
plt.xticks([r + barWidth for r in range(len(verbal))], labels)
plt.legend()
plt.title('ASD AoO vs Verbality Status N={}'.format(len(t)))
plt.ylim(top=100)
plt.ylim(bottom=0)

for rect in p1+p2+p3:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
txt="Odds Ratio: {} \nP Value: {}".format(oddsratio,pvalue)
plt.text(0,80, txt,fontsize=6)
#############################################

labels=['<= 2 years',"> 2 years"]
verbal=[]
nonverbal=[]
unknown=[]
fishers=[[1,1],[1,1]]
vct=0
nct=0
uct=0
for i in s:
    print(i,end=", ")
    print(s[i][0])
    if isinstance(s[i][0], str):
        if s[i][0]=='Infancy' or s[i][0]=='Birth':
            if s[i][1]=="Yes":
                vct+=1
            elif s[i][1]=="No":
                nct+=1
            elif s[i][1]=="Unknown":
                uct+=1
    else:
        if s[i][0]<=24.0:
            if s[i][1]=="Yes":
                vct+=1
            elif s[i][1]=="No":
                nct+=1
            elif s[i][1]=="Unknown":
                uct+=1
fishers[0][0]=nct
fishers[0][1]=vct
verbal.append(vct/len(s)*100)
nonverbal.append(nct/len(s)*100)
unknown.append(uct/len(s)*100)
labels[0]+=" N= {}".format(nct+vct+uct)
vct=0
nct=0
uct=0
for i in s:
    if isinstance(s[i][0], str):
        if s[i][0]!='Infancy' and s[i][0]!='Birth':
            if s[i][1]=="Yes":
                vct+=1
            elif s[i][1]=="No":
                nct+=1
            elif s[i][1]=="Unknown":
                uct+=1
    else:
        if s[i][0]>24.0:
            if s[i][1]=="Yes":
                vct+=1
            elif s[i][1]=="No":
                nct+=1
            elif s[i][1]=="Unknown":
                uct+=1
fishers[1][0]=nct
fishers[1][1]=vct
unknown.append(uct/len(s)*100)
verbal.append(vct/len(s)*100)
nonverbal.append(nct/len(s)*100)
labels[1]+=" N= {}".format(nct+vct+uct)    
        
plt.subplot(2,1,2)
barWidth =0.25
r1=np.arange(len(verbal))
r2=[x+barWidth for x in r1]
r3=[x + barWidth for x in r2]
p1=plt.bar(r1, verbal, color='#7f6d5f', width=barWidth, edgecolor='white', label='Verbal')
p2=plt.bar(r2, nonverbal, color='#557f2d', width=barWidth, edgecolor='white', label='Non Verbal')
p3=plt.bar(r3, unknown, color='#2d7f5e', width=barWidth, edgecolor='white', label='Unknown')  

oddsratio, pvalue = stats.fisher_exact(fishers)

plt.ylabel('%')
plt.xticks([r + barWidth for r in range(len(verbal))], labels)
plt.legend()
plt.title('ASD AoO vs Verbality Status N={}'.format(len(s)))
plt.ylim(top=100)
plt.ylim(bottom=0)

for rect in p1+p2+p3:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
txt="Odds Ratio: {} \nP Value: {}".format(oddsratio,pvalue)
plt.text(0,80, txt,fontsize=6)
plt.show()