# Purpose: Looks at AoO and AoD spread within each age group
# Corresponding graph: ASD-EpiCohort.png
import pandas as pd
import csv
import matplotlib.pyplot as plt
excel_file='Minimal Phenotype Fields_2020-05-22_16-54-18.xlsx'
vals=pd.read_excel(excel_file, sheet_name=0, index_col=0)
def isNaN(num):
    return num != num
#Separates based on age
def checkAges(ageList, tallyStages):
    #print(type(months))
    n=0
    for months in ageList:
        n+=1
        
        
        
        if months.isdigit()==True:
            
            months=int(months)
            if months<=1:
                tallyStages[0]+=1
            elif months>1 and months<=24:
                tallyStages[1]+=1
            elif months>24 and months<=144:
                tallyStages[2]+=1
            elif months>144 and months <=216:
                tallyStages[3]+=1
            elif months>216:
                tallyStages[4]+=1
       
            
        else:
            if months=="Unknown" or months=="Not Specified":
                tallyStages[5]+=1
            elif months=="Infancy":
                tallyStages[1]+=1
            elif months=="Childhood":
                tallyStages[2]+=1
            elif months=="Birth":
                tallyStages[0]+=1
            else:
                months=(float(months))
                if months<=1:
                    tallyStages[0]+=1
                elif months>1 and months<=24:
                    tallyStages[1]+=1
                elif months>24 and months<=144:
                    tallyStages[2]+=1
                elif months>144 and months <=216:
                    tallyStages[3]+=1
                elif months>216:
                    tallyStages[4]+=1
    return tallyStages

months_onset=[]
months_diagnosis=[]
for col in vals.columns:
    if(col=="Cohort"):
        for ind in vals.index:
            if((vals[col][ind])=="ASD,Epi"):
                for col2 in vals.columns:
                                      
                    if(col2=="Proband's ASD Ao O (mos) (Referral)"):
                        #print(vals[col2][ind])
                        if(isNaN(vals[col2][ind])==True):
                           
                            months_onset.append("Not Specified")
                        else:

                            months_onset.append(vals[col2][ind])
                        
                    if(col2=="Proband's ASD Ao D (mos) (Referral)"):
                        if(isNaN(vals[col2][ind])==True):
                           
                            months_diagnosis.append("Not Specified")
                        else:

                            months_diagnosis.append(vals[col2][ind])
                      

tallyonset=[0,0,0,0,0,0]
tallydiagnosis=[0,0,0,0,0,0]
#print(months_onset)
onset=checkAges(months_onset,tallyonset)
diagnosis=checkAges(months_diagnosis,tallydiagnosis)
onset_percents=[]
diagnosis_percents=[]
tot_o=len(months_onset)
tot_d=len(months_diagnosis)
for i in onset:
    onset_percents.append((i/tot_o)*100)
for i in diagnosis:
    diagnosis_percents.append((i/tot_d)*100)
#creates the graph
print(diagnosis_percents)
print(onset_percents)
index=['Neonatal (0-30 days)','Infancy (1 month- 2 years',"Childhood (2 years-12 years)",
"Adolescent (12 years-18 years)","Adulthood (18+ years)","Unknown/Not Specified"]
df=pd.DataFrame({'Age of Onset':onset_percents,'Age of Diagnosis':diagnosis_percents},index=index)
ax=df.plot.barh()
ax.set_xlabel("% (out of {} )".format(tot_o))
ax.set_ylabel("Developmental Stages")
ax.set_title('ASD,Epi Cohort: Proband ASD Ao O (mos) (Referral) vs. Proband ASD Ao D (mos) (Referral)')  # or size, alternatively
plt.show()