#Purpose: Looks at the coverage resultes of all the variables of each sources without taking into consideration completed chart reviews
#Corresponding graphs: coverageResults_2variables.png and coverageResultsASD-AOO.png
# same code as chartedCategoricalVariables.py" and "chartedASD-Epi.py" but removes the check for completed chart reviews
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

#excel_file='Minimal Phenotype Fields - Dev Window Fields Separated_2020-06-25.xlsx'
excel_file= "Minimal Phenotype Fields - Dev Window Fields Separated_DevDelDomainsAdded.xlsx"
vals=pd.read_excel(excel_file, sheet_name=0)
def isNaN(num):
    return num != num

valuePresent=0
totalValues=0

group_labels1=['Race','Ethnicity', 
'Communi-\ncation', 'MRI','EEG','DD',"ID",'Epi Type']

variables=[
["Proband's Race (Referral)","Race (Demo)","Race (Epic SP)"],
["Proband's Ethnicity (Referral)", "Ethnicity (Demo)"],
["Nonverbal (Chart)", "Nonverbal (Self Assess)","Nonverbal (Interview)"],
["MRI status (Chart)","MRI review (Epic SP)"],
["Has EEG (Chart)"],
["DD dx (Interview)","DD? (Chart)", "DD? (Pt Qstr)"],
["ID dx (Interview)","ID? (Chart)", "ID ICD codes"],
["Proband's Epi type (Referral)", "Epi type (Interview)","Epi type (Chart)"],
]
icdcodes=[['IGE/GGE ICD codes','NAFE/LFE ICD codes','EE ICD codes','Other G40 ICD codes']]

graphPlot=[]
i=-1
for group in range(0,len(variables)-1,1):
    i+=1
    uniqueID=set()
    for j in variables[group]:
        valuePresent=0
        for col in vals.columns:
            if col=="Cohort":
                
                for ind in vals.index:
                    if vals[col][ind]=="ASD,Epi":
       
                        subjectid=""
                        for col2 in vals.columns: 
                            if(col2=="Subject ID"):
                                subjectid=vals[col2][ind]
                                valuePresent+=1
                            if col2==j :
                                
                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                                   
                                    uniqueID.add(subjectid)
                           


    print(valuePresent)                
    coveragePercent=(len(uniqueID)/valuePresent)*100
    graphPlot.append(["Total Coverage",group_labels1[i],coveragePercent])


uniqueID=set()
for j in variables[len(variables)-1]:
    valuePresent=0
    for col in vals.columns:
            if col=="Cohort":
                
                for ind in vals.index:
                    if vals[col][ind]=="ASD,Epi":
   
                        subjectid=""
                        for col2 in vals.columns: 
                            if(col2=="Subject ID"):
                                subjectid=vals[col2][ind]
                                valuePresent+=1
                            if col2==j :
                                #print(j)
                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                                    #print(subjectid)
                                    uniqueID.add(subjectid)
for k in icdcodes[0]:
    if col2==k:
        if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
            #print(subjectid)
            uniqueID.add(subjectid)

coveragePercent=(len(uniqueID)/valuePresent)*100
graphPlot.append(["Total Coverage",'Epi Type',coveragePercent])

i=-1
for group in variables:
    i+=1
    valuePresent=0
    totalValues=0
    eachVar=0
    
    for var in group:
        #print(var)
        typeSource=""
        valuePresent=0
        totalValues=0
        for col in vals.columns:
            if col=="Cohort":
                
                for ind in vals.index:
                    if vals[col][ind]=="ASD,Epi":
        
                        for col2 in vals.columns:   
                            if col2==var:
                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                                    valuePresent+=1
                                    totalValues+=1
                                    eachVar+=1
                                
                                    if "Referral" in var and "approx" not in var:
                                        typeSource="Referral"
                                    elif "Demo" in var:
                                        typeSource="Demo"
                                    elif "Epic SP" in var:
                                        typeSource="Epic SP"
                                    elif "Interview" in var and "approx" not in var:
                                        typeSource="Interview"
                                    elif "Chart" in var and "approx" not in var:
                                        typeSource="Chart"
                                    elif "Self Assess" in var and "approx" not in var:
                                        typeSource="Self Assess"
                                    elif "Behav" in var:
                                        typeSource="Behaviour Obs"
                                    elif "IEP" in var:
                                        typeSource="IEP"
                                    elif "Composite" in var:
                                        typeSource="Composite"
                                    elif "Qstr" in var:
                                        typeSource="Pt QStr"
                                    elif var == 'ID ICD codes':
                                        typeSource=" ID Code"
                                    
                                else:
                                    totalValues+=1
                        
        coveragePercent=(valuePresent/totalValues)*100
        if typeSource!="":
            graphPlot.append([typeSource,group_labels1[i],coveragePercent])
           
for group in icdcodes:
    valuePresent=0
    totalValues=0
    eachVar=0
    
    for var in group:
        #print(var)
        typeSource=""
        valuePresent=0
        totalValues=0
        for col in vals.columns:
            if col=="Cohort":
                
                for ind in vals.index:
                    if vals[col][ind]=="ASD,Epi":
        
                        for col2 in vals.columns:   
                            if col2=='IGE/GGE ICD codes':
                                if not isNaN(vals[col2][ind]) and "Unknown" not in vals[col2][ind] :
                                    valuePresent+=1
                                    totalValues+=1
                                    typeSource='Epi ICD code'
                                else:
                                    totalValues+=1
                            if col2=='NAFE/LFE ICD codes':
                                if not isNaN(vals[col2][ind]) and "Unknown" not in vals[col2][ind] :
                                    valuePresent+=1
                                    totalValues+=1
                                    typeSource='Epi ICD code'
                                else:
                                    totalValues+=1
                            if col2=='EE ICD codes':
                                if not isNaN(vals[col2][ind]) and "Unknown" not in vals[col2][ind] :
                                    valuePresent+=1
                                    totalValues+=1
                                    typeSource='Epi ICD code'
                                else:
                                    totalValues+=1
                            if col2=='Other G40 ICD codes':
                                if not isNaN(vals[col2][ind]) and "Unknown" not in vals[col2][ind] :
                                    valuePresent+=1
                                    totalValues+=1
                                    typeSource='Epi ICD code'      
                                    
                            
                                    
                                    
                                else:
                                    totalValues+=1
                      
    coveragePercent=(valuePresent/totalValues)*100

    if typeSource!="":
        graphPlot.append([typeSource,"Epi Type",coveragePercent])  
for i in graphPlot:
    print(i)

df = pd.DataFrame(graphPlot,columns=['Sources','Category','Percent coverage'])

ax=df.pivot('Category','Sources','Percent coverage').plot(kind='bar',colormap='Paired')
for p in ax.patches[0:]:
    h = p.get_height()
    x = p.get_x()+p.get_width()/2.
    if h != 0:
        ax.annotate("{:.1f}".format(p.get_height()), xy=(x,h), xytext=(0,4), rotation=90, 
                   textcoords="offset points", ha="center", va="bottom", fontsize=6)
plt.title("Percent Coverage of Variables")
plt.ylim(ymax=100)
plt.legend(loc='upper left')
plt.show()
######################################################################################
group_labels2=['ASD AoO','ASD AoD','Epi AoO','Epi AoD']
group_labels3=['ASD AoO \n with Approx','ASD AoD \n with Approx','Epi AoO \n with Approx',
'Epi AoD \n with Approx']
varAOOD=[
["Proband's ASD Ao O (mos) (Referral)","ASD Ao O (mos) (Interview)","ASD Ao O (mos) (Chart)","ASD Ao O (mos) (Self Assess)"],
["Proband's ASD Ao O (mos) (Referral)","Proband's ASD Ao O (approx) (Referral)","ASD Ao O (mos) (Interview)","ASD Ao O (approx) (Interview)",
"ASD Ao O (mos) (Chart)","ASD Ao O (approx) (Chart)","ASD Ao O (mos) (Self Assess)","ASD Ao O (approx) (Self Assess)"],

["Proband's ASD Ao D (mos) (Referral)","ASD Ao D (mos) (Interview)","ASD Ao D (mos) (Chart)","ASD Ao D (mos) (Self Assess)"],
["Proband's ASD Ao D (mos) (Referral)","Proband's ASD Ao D (approx) (Referral)","ASD Ao D (mos) (Interview)","ASD Ao D (approx) (Interview)",
"ASD Ao D (mos) (Chart)","ASD Ao D (approx) (Chart)","ASD Ao D (mos) (Self Assess)","ASD Ao D (approx) (Self Assess)"],

["Proband's Epi Ao O (mos) (Referral)","Age at first seizure (mos) (Interview)","Epi Ao O (mos) (Chart)","Age at 1st seizure (mos) (Self Assess)"],
["Proband's Epi Ao O (mos) (Referral)","Proband's Epi Ao O (approx) (Referral)","Age at first seizure (mos) (Interview)","Age at first seizure (mos) (Interview)",
"Epi Ao O (mos) (Chart)","Epi Ao O (approx) (Chart)","Age at 1st seizure (mos) (Self Assess)","Age at 1st seizure (approx) (Self Assess)"],

["Proband's Epi Ao D (mos) (Referral)","Epi Ao D (mos) (Interview)","Epi Ao D (mos) (Chart)","Age at 1st seizure (mos) (Self Assess)"],
["Proband's Epi Ao D (mos) (Referral)","Proband's Epi Ao D (approx) (Referral)","Epi Ao OD (mos) (Chart)","Epi Ao D (approx) (Chart)","Age at 1st seizure (mos) (Self Assess)","Age at 1st seizure (approx) (Self Assess)"]
]
graphPlot=[]
i=-1

counts=[]

for group in range(0,len(varAOOD),2):
    i+=1
    uniqueID=set()
    for j in varAOOD[group]:
        valuePresent=0
        for col in vals.columns:
            if col=="Cohort":
                
                for ind in vals.index:
                    if vals[col][ind]=="ASD,Epi":
                        subjectid=""
                        for col2 in vals.columns: 
                            if(col2=="Subject ID"):
                                subjectid=vals[col2][ind]
                                valuePresent+=1
                            if col2==j:
                            
                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                                    #print(subjectid)
                                    uniqueID.add(subjectid)

                        

    coveragePercent=(len(uniqueID)/valuePresent)*100
    graphPlot.append(["Total Coverage",group_labels2[i],coveragePercent])

i=-1
for group in range(1,len(varAOOD),2):
    i+=1
    uniqueID=set()
    for j,k in zip(varAOOD[group][0::2],varAOOD[group][1::2]):
        valuePresent=0
        for col in vals.columns:
            if col=="Cohort":
                
                for ind in vals.index:
                    if vals[col][ind]=="ASD,Epi":
        
                        subjectid=""
                        for col2 in vals.columns: 
                            if(col2=="Subject ID"):
                                subjectid=vals[col2][ind]
                                valuePresent+=1
                            if col2==k:
                            
                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                                    #print(subjectid)
                                    uniqueID.add(subjectid)
                            if col2==j:
                            
                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                                    #print(subjectid)
                                    uniqueID.add(subjectid)

    print(valuePresent)                
    coveragePercent=(len(uniqueID)/valuePresent)*100
    graphPlot.append(["Total Coverage",group_labels3[i],coveragePercent])

i=-1
for group in range(0,len(varAOOD),2):
    valuePresent=0
    totalValues=0
    i+=1
    for var in varAOOD[group]:
        typeSource=""
        valuePresent=0
        totalValues=0
        for col in vals.columns:
            if col=="Cohort":
                
                for ind in vals.index:
                    if vals[col][ind]=="ASD,Epi":
        
                        for col2 in vals.columns:   
                            if col2==var:
                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                                    valuePresent+=1
                                    totalValues+=1
                                    
                                
                                    if "Referral" in var and "approx" not in var:
                                        typeSource="Referral"
                                    elif "Demo" in var:
                                        typeSource="Demo"
                                    elif "Epic SP" in var:
                                        typeSource="Epic SP"
                                
                                    elif "Interview" in var and "approx" not in var:
                                        typeSource="Interview"
                                    
                                    elif "Chart" in var and "approx" not in var:
                                        typeSource="Chart"
                                    
                                    elif "Self Assess" in var and "approx" not in var:
                                        typeSource="Self Assess"
                                    
                                    
                                else:
                                    totalValues+=1
                      
        coveragePercent=(valuePresent/totalValues)*100
       
        if typeSource!="":
            counts.append((var,valuePresent))
            graphPlot.append([typeSource,group_labels2[i],coveragePercent])


# # ###########################################
i=-1
for group in range(1,len(varAOOD),2):
    i+=1
    totalValues=0
    
    for j,k in zip(varAOOD[group][0::2],varAOOD[group][1::2]):
        typeSource=""
        valuePresent=0
        totalValues=0
        for col in vals.columns:
            if col=="Cohort":
                
                for ind in vals.index:
                    if vals[col][ind]=="ASD,Epi":
        
            
                        for col2 in vals.columns:   
                            if col2==j:
                                
                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                                    valuePresent+=1
                                    if "Referral" in k and "approx" in k:
                                        typeSource="Referral"
                                    
                                    elif "Demo" in k:
                                        typeSource="Demo"
                                    
                                    elif "Interview" in k and "approx" in k:
                                        typeSource="Interview"
                                
                                    elif "Chart" in k and "approx" in k:
                                        typeSource="Chart"
                                    
                                    elif "Self Assess" in k and "approx" in k:
                                        typeSource="Self Assess"

                        for col2 in vals.columns:
                            if col2==k:
                                
                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                                    valuePresent+=1
                                    totalValues+=1
                                    
                                    
                                    if "Referral" in k and "approx" in k:
                                        typeSource="Referral"
                                    
                                    elif "Demo" in k:
                                        typeSource="Demo"
                                    
                                    elif "Interview" in k and "approx" in k:
                                        typeSource="Interview"
                                
                                    elif "Chart" in k and "approx" in k:
                                        typeSource="Chart"
                                    
                                    elif "Self Assess" in k and "approx" in k:
                                        typeSource="Self Assess"
                                
                                    
                                    
                                else:
                                    totalValues+=1

                      
        coveragePercent=(valuePresent/totalValues)*100
        if typeSource!="":
            counts.append((k,valuePresent))
            graphPlot.append([typeSource,group_labels3[i],coveragePercent])
    
for i in graphPlot:
    print(i)

df = pd.DataFrame(graphPlot,columns=['Sources','Category','Percent coverage'])

ax=df.pivot('Category','Sources','Percent coverage').plot(kind='bar',colormap='Paired')
for p in ax.patches[0:]:
    h = p.get_height()
    x = p.get_x()+p.get_width()/2.
    if h != 0:
        ax.annotate("{:.1f}".format(p.get_height()), xy=(x,h), xytext=(0,4), rotation=90, 
                   textcoords="offset points", ha="center", va="bottom", fontsize=7)
plt.title("Percent Coverage of Variables")
plt.ylim(ymax=100)
plt.legend(loc='upper left')
plt.show()