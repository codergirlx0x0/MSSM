#Purpose: Looks at the associativity between ASD Aoo and Epi types and splits into two categories: epi types (4 types) percents fo Age 2 or less and epi types percents for Age 2+
#Corresponding Graphs: associativityAnalysis.pdf page 6
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

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
                                        if col2=="Proband's ASD Ao O (mos) (Referral)":
                                            if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                count+=1
                                                for col3 in vals.columns:
                            
                                                    if col3== "Proband's Epi type (Referral)":
                                                        if vals[col2][ind]<=24.0:
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                if ";" in vals[col3][ind]:
                                                                    types=vals[col3][ind].split(";")
                                                                else:
                                                                    types=[vals[col3][ind]]
                                                                subjects[sid]=(vals[col2][ind],types)
                                                        if vals[col2][ind]>24.0:
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                if ";" in vals[col3][ind]:
                                                                    types=vals[col3][ind].split(";")
                                                                else:
                                                                    types=[vals[col3][ind]]
                                                                subjects[sid]=(vals[col2][ind],types)
                                        
                                        if col2=="Proband's ASD Ao O (approx) (Referral)":
                                            if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                count+=1
                                                for col3 in vals.columns:
                            
                                                    if col3== "Proband's Epi type (Referral)":
                                                        if vals[col2][ind]=="Infancy":
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                if ";" in vals[col3][ind]:
                                                                    types=vals[col3][ind].split(";")
                                                                else:
                                                                    types=[vals[col3][ind]]
                                                                subjects[sid]=(vals[col2][ind],types)
                                                        if vals[col2][ind]!="Infancy":
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                if ";" in vals[col3][ind]:
                                                                    types=vals[col3][ind].split(";")
                                                                else:
                                                                    types=[vals[col3][ind]]
                                                                subjects[sid]=(vals[col2][ind],types)
                                                            
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
                            
                                                    if col3== "Proband's Epi type (Referral)":
                                                        if vals[col2][ind]<=24.0:
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                if ";" in vals[col3][ind]:
                                                                    types=vals[col3][ind].split(";")
                                                                else:
                                                                    types=[vals[col3][ind]]
                                                                subjects[sid]=(vals[col2][ind],types)
                                                        if vals[col2][ind]>24.0:
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                if ";" in vals[col3][ind]:
                                                                    types=vals[col3][ind].split(";")
                                                                else:
                                                                    types=[vals[col3][ind]]
                                                                subjects[sid]=(vals[col2][ind],types)
                                        
                                        if col2=="ASD Ao O (approx) (Chart)":
                                            if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                count+=1
                                                for col3 in vals.columns:
                            
                                                    if col3== "Proband's Epi type (Referral)":
                                                        if vals[col2][ind]=="Infancy":
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                if ";" in vals[col3][ind]:
                                                                    types=vals[col3][ind].split(";")
                                                                else:
                                                                    types=[vals[col3][ind]]
                                                                subjects[sid]=(vals[col2][ind],types)
                                                        if vals[col2][ind]!="Infancy":
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                if ";" in vals[col3][ind]:
                                                                    types=vals[col3][ind].split(";")
                                                                else:
                                                                    types=[vals[col3][ind]]
                                                                subjects[sid]=(vals[col2][ind],types)


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
                            
                                                    if col3== "Proband's Epi type (Referral)":
                                                        if vals[col2][ind]<=24.0:
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                if ";" in vals[col3][ind]:
                                                                    types=vals[col3][ind].split(";")
                                                                else:
                                                                    types=[vals[col3][ind]]
                                                                subjects[sid]=(vals[col2][ind],types)
                                                        if vals[col2][ind]>24.0:
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                if ";" in vals[col3][ind]:
                                                                    types=vals[col3][ind].split(";")
                                                                else:
                                                                    types=[vals[col3][ind]]
                                                                subjects[sid]=(vals[col2][ind],types)
                                        
                                        if col2=="ASD Ao O (approx) (Self Assess)":
                                            if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                count+=1
                                                for col3 in vals.columns:
                            
                                                    if col3== "Proband's Epi type (Referral)":
                                                        if vals[col2][ind]=="Infancy":
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                if ";" in vals[col3][ind]:
                                                                    types=vals[col3][ind].split(";")
                                                                else:
                                                                    types=[vals[col3][ind]]
                                                                subjects[sid]=(vals[col2][ind],types)
                                                        if vals[col2][ind]!="Infancy":
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                if ";" in vals[col3][ind]:
                                                                    types=vals[col3][ind].split(";")
                                                                else:
                                                                    types=[vals[col3][ind]]
                                                                subjects[sid]=(vals[col2][ind],types)


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
                            
                                                    if col3== "Proband's Epi type (Referral)":
                                                        if vals[col2][ind]<=24.0:
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                if ";" in vals[col3][ind]:
                                                                    types=vals[col3][ind].split(";")
                                                                else:
                                                                    types=[vals[col3][ind]]
                                                                subjects[sid]=(vals[col2][ind],types)
                                                        if vals[col2][ind]>24.0:
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                if ";" in vals[col3][ind]:
                                                                    types=vals[col3][ind].split(";")
                                                                else:
                                                                    types=[vals[col3][ind]]
                                                                subjects[sid]=(vals[col2][ind],types)
                                        
                                        if col2=="ASD Ao O (approx) (Interview)":
                                            if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                count+=1
                                                for col3 in vals.columns:
                            
                                                    if col3== "Proband's Epi type (Referral)":
                                                        if vals[col2][ind]=="Infancy":
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                if ";" in vals[col3][ind]:
                                                                    types=vals[col3][ind].split(";")
                                                                else:
                                                                    types=[vals[col3][ind]]
                                                                subjects[sid]=(vals[col2][ind],types)
                                                        if vals[col2][ind]!="Infancy":
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                if ";" in vals[col3][ind]:
                                                                    types=vals[col3][ind].split(";")
                                                                else:
                                                                    types=[vals[col3][ind]]
                                                                subjects[sid]=(vals[col2][ind],types)


labels=['<= 2 years',"> 2 years"]
NAFE=[]
IGE=[]
EE=[]
LFE=[]
nct=0
ict=0
ect=0
lct=0
for i in subjects:
    print(i,end=", ")
    print(subjects[i])
    if isinstance(subjects[i][0], str):
        if subjects[i][0]=='Infancy':
            for j in subjects[i][1]:
                if j=="Non-acquired focal epilepsy":
                    nct+=1
                if j=="Idiopathic generalized epilepsy":
                    ict+=1
                if j=="Epileptic Encephalopathy":
                    ect+=1
                if j=="Lesional focal epilepsy":
                    lct+=1
    else:
        if subjects[i][0]<=24.0:
            for j in subjects[i][1]:
                if j=="Non-acquired focal epilepsy":
                    nct+=1
                if j=="Idiopathic generalized epilepsy":
                    ict+=1
                if j=="Epileptic Encephalopathy":
                    ect+=1
                if j=="Lesional focal epilepsy":
                    lct+=1
NAFE.append(nct)
LFE.append(lct)
EE.append(ect)
IGE.append(ict)
nct=0
ict=0
ect=0
lct=0
for i in subjects:
    if isinstance(subjects[i][0], str):
        if subjects[i][0]!='Infancy':
            for j in subjects[i][1]:
                if j=="Non-acquired focal epilepsy":
                    nct+=1
                if j=="Idiopathic generalized epilepsy":
                    ict+=1
                if j=="Epileptic Encephalopathy":
                    ect+=1
                if j=="Lesional focal epilepsy":
                    lct+=1
    else:
        if subjects[i][0]>24.0:
            for j in subjects[i][1]:
                if j=="Non-acquired focal epilepsy":
                    nct+=1
                if j=="Idiopathic generalized epilepsy":
                    ict+=1
                if j=="Epileptic Encephalopathy":
                    ect+=1
                if j=="Lesional focal epilepsy":
                    lct+=1
NAFE.append(nct)
LFE.append(lct)
EE.append(ect)
IGE.append(ict)
    
        
print(NAFE)
print(LFE)
print(EE)
print(IGE)
print(len(subjects))

df = pd.DataFrame({'NAFE': NAFE,
                   'LFE': LFE,
                   'IGE': IGE,
                   'EE':EE}, index=labels)
ax = df.plot.bar(rot=0)




ax.set_ylabel('Number of Subjects')
ax.set_title('ASD AoO vs Epi Type N={}'.format(len(subjects)))
for p in ax.patches[0:]:
    h = p.get_height()
    x = p.get_x()+p.get_width()/2.
    if h != 0:
        ax.annotate("{:.1f}".format(p.get_height()), xy=(x,h), xytext=(0,4), rotation=90, 
                   textcoords="offset points", ha="center", va="bottom", fontsize=7)

plt.show()