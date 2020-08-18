# Purpose: Looks at the coverage of ech data sources of the categorical variables of the subgroup of completed chart reviewed patients
# Corresponding Graph:"chartedAnalysis.pdf Page 7"
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

#excel_file='Minimal Phenotype Fields - Dev Window Fields Separated_2020-06-25.xlsx'
excel_file= "Minimal Phenotype Fields - Dev Window Fields Separated_071020.xlsx"
vals=pd.read_excel(excel_file, sheet_name=0)
def isNaN(num):
    return num != num

valuePresent=0
totalValues=0
T=0
group_labels1=['Race','Ethnicity', 
'Communi-\ncation', 'MRI','EEG','DD',"ID",'Epi Type']
#all the possible columns
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
# for the total coverage of the variables except epi type
for group in range(0,len(variables)-1,1):
    i+=1
    uniqueID=set()
    for j in variables[group]:
        valuePresent=0
        for col in vals.columns:
            if col=="Cohort":
                
                for ind in vals.index:
                    if vals[col][ind]=="ASD,Epi":
                        for col1 in vals.columns:
                            if col1=="Chart Review Complete":
                                if vals[col1][ind]=="Complete":
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

# for the total coverage epi type
uniqueID=set()
for j in variables[len(variables)-1]:
    valuePresent=0
    for col in vals.columns:
            if col=="Cohort":
                
                for ind in vals.index:
                    if vals[col][ind]=="ASD,Epi":
                        for col1 in vals.columns:
                            if col1=="Chart Review Complete":
                                if vals[col1][ind]=="Complete":
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
# for the total coverage of the data sources of the categorical variables except epi type
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
                        for col1 in vals.columns:
                            if col1=="Chart Review Complete":
                                if vals[col1][ind]=="Complete":
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
        #print(valuePresent,end=", ")
        T=totalValues                
        coveragePercent=(valuePresent/totalValues)*100
        if typeSource!="":
            graphPlot.append([typeSource,group_labels1[i],coveragePercent])
#calculates the coverage of each type of source for epi type           
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
                        for col1 in vals.columns:
                            if col1=="Chart Review Complete":
                                if vals[col1][ind]=="Complete":
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
#make the graph
df = pd.DataFrame(graphPlot,columns=['Sources','Category','Percent coverage'])

ax=df.pivot('Category','Sources','Percent coverage').plot(kind='bar',colormap='Paired')
for p in ax.patches[0:]:
    h = p.get_height()
    x = p.get_x()+p.get_width()/2.
    if h != 0:
        ax.annotate("{:.1f}".format(p.get_height()), xy=(x,h), xytext=(0,4), rotation=90, 
                   textcoords="offset points", ha="center", va="bottom", fontsize=6)
plt.title("\nPercent Coverage of Variables N={}".format(T))
plt.ylim(ymax=100)
plt.legend(bbox_to_anchor=(0,1.02,1,0.102),loc='lower left',ncol=10,fontsize='small')
plt.show()