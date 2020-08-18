#Purpose: Looks at the associativity between ASD Aoo and ID statuses and splits into two categories: ID status (3 types) percents fo Age 2 or less and mri percents for Age 2+
#Corresponding Graphs: associativityAnalysisUpdated.pdf page 1
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
                                
                                                        if col3== "ID? (Chart)":
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
                                
                                                        if col3== "ID? (Chart)":
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
                                
                                                        if col3== "ID? (Chart)":
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
                                
                                                        if col3== "ID? (Chart)":
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
                                
                                                        if col3== "ID? (Chart)":
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
                                
                                                        if col3== "ID? (Chart)":
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
                                
                                                        if col3== "ID? (Chart)":
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
                                            
                                            if col2=="ASD Ao O (approx) (Interview)":
                                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                    count+=1
                                                    for col3 in vals.columns:
                                
                                                        if col3== "ID? (Chart)":
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
    return subjects
s=parseData(0)
t=parseData(1)
labels=['<= 2 years',"> 2 years"]
id=[]
noid=[]
unknown=[]
fishers=[[1,1],[1,1]]
ict=0
nict=0
uct=0
for i in t:
    print(i,end=", ")
    print(t[i][0])
    if isinstance(t[i][0], str):
        if t[i][0]=='Infancy' or t[i][0]=="Birth":
            if t[i][1]=="Yes":
                ict+=1
            elif t[i][1]=="No" or isNaN(t[i][1]):
                nict+=1
            elif t[i][1]=="Unknown":
                uct+=1
    else:
        if t[i][0]<=24.0:
            if t[i][1]=="Yes":
                ict+=1
            elif t[i][1]=="No" or isNaN(t[i][1]):
                nict+=1
            elif t[i][1]=="Unknown":
                uct+=1
fishers[0][0]=nict
fishers[0][1]=ict
id.append(ict/len(t)*100)
noid.append(nict/len(t)*100)
unknown.append(uct/len(t)*100)
labels[0]+=" N= {}".format(nict+ict+uct)
ict=0
nict=0
uct=0
for i in t:
    if isinstance(t[i][0], str):
        if t[i][0]!='Infancy' and t[i][0]!="Birth":
            if t[i][1]=="Yes":
                ict+=1
            elif t[i][1]=="No" or isNaN(t[i][1]):
                nict+=1
            elif t[i][1]=="Unknown":
                uct+=1
    else:
        if t[i][0]>24.0:
            if t[i][1]=="Yes":
                ict+=1
            elif t[i][1]=="No" or isNaN(t[i][1]):
                nict+=1
            elif t[i][1]=="Unknown":
                uct+=1
fishers[1][0]=nict
fishers[1][1]=ict
id.append(ict/len(t)*100)
noid.append(nict/len(t)*100)
unknown.append(uct/len(t)*100)
labels[1]+=" N= {}".format(nict+ict+uct)    
        
plt.subplot(2,1,1)
barWidth =0.25
r1=np.arange(len(id))
r2=[x+barWidth for x in r1]
r3=[x + barWidth for x in r2]
p1=plt.bar(r1, id, color='#7f6d5f', width=barWidth, edgecolor='white', label='ID')
p2=plt.bar(r2, noid, color='#557f2d', width=barWidth, edgecolor='white', label='No ID')
p3=plt.bar(r3, unknown, color='#2d7f5e', width=barWidth, edgecolor='white', label='Unknown')    

  


oddsratio, pvalue = stats.fisher_exact(fishers)

plt.ylabel('%')
plt.xticks([r + barWidth for r in range(len(id))], labels)
plt.legend()
plt.title('ASD AoO vs ID Status N={}'.format(len(t)))
plt.ylim(top=100)
plt.ylim(bottom=0)

for rect in p1+p2+p3:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
txt="Odds Ratio: {} \nP Value: {}".format(oddsratio,pvalue)
plt.text(0,80, txt,fontsize=6)

############
labels=['<= 2 years',"> 2 years"]
id=[]
noid=[]
unknown=[]
fishers=[[1,1],[1,1]]
ict=0
nict=0
uct=0
for i in s:
    print(i,end=", ")
    print(s[i][0])
    if isinstance(s[i][0], str):
        if s[i][0]=='Infancy' or s[i][0]=="Birth":
            if s[i][1]=="Yes":
                ict+=1
            elif s[i][1]=="No":
                nict+=1
            elif s[i][1]=="Unknown":
                uct+=1
    else:
        if s[i][0]<=24.0:
            if s[i][1]=="Yes":
                ict+=1
            elif s[i][1]=="No":
                nict+=1
            elif s[i][1]=="Unknown":
                uct+=1
fishers[0][0]=nict
fishers[0][1]=ict
id.append(ict/len(s)*100)
noid.append(nict/len(s)*100)
unknown.append(uct/len(s)*100)
labels[0]+=" N= {}".format(nict+ict+uct)
ict=0
nict=0
uct=0
for i in s:
    if isinstance(s[i][0], str):
        if s[i][0]!='Infancy' and s[i][0]!="Birth":
            if s[i][1]=="Yes":
                ict+=1
            elif s[i][1]=="No":
                nict+=1
            elif s[i][1]=="Unknown":
                uct+=1
    else:
        if s[i][0]>24.0:
            if s[i][1]=="Yes":
                ict+=1
            elif s[i][1]=="No":
                nict+=1
            elif s[i][1]=="Unknown":
                uct+=1
fishers[1][0]=nict
fishers[1][1]=ict
id.append(ict/len(s)*100)
noid.append(nict/len(s)*100)
unknown.append(uct/len(s)*100)
labels[1]+=" N= {}".format(nict+ict+uct)    
        
plt.subplot(2,1,2)
barWidth =0.25
r1=np.arange(len(id))
r2=[x+barWidth for x in r1]
r3=[x + barWidth for x in r2]
p1=plt.bar(r1, id, color='#7f6d5f', width=barWidth, edgecolor='white', label='ID')
p2=plt.bar(r2, noid, color='#557f2d', width=barWidth, edgecolor='white', label='No ID')
p3=plt.bar(r3, unknown, color='#2d7f5e', width=barWidth, edgecolor='white', label='Unknown')    

  


oddsratio, pvalue = stats.fisher_exact(fishers)

plt.ylabel('%')
plt.xticks([r + barWidth for r in range(len(id))], labels)
plt.legend()
plt.title('ASD AoO vs ID Status N={}'.format(len(s)))
plt.ylim(top=100)
plt.ylim(bottom=0)

for rect in p1+p2+p3:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
txt="Odds Ratio: {} \nP Value: {}".format(oddsratio,pvalue)
plt.text(0,80, txt,fontsize=6)
plt.show()