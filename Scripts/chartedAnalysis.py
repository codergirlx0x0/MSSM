# Purpose: Looks at the counts of ech variable with non nan and non unknown values of the subgroup of completed chart reviewed patients
# Corresponding Graph:"chartedAnalysis.pdf Page 1-5"

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
group_labels1=['DD',"ID"]

variables=[

["DD dx (Interview)","DD? (Chart)", "DD? (Pt Qstr)"],
["ID dx (Interview)","ID? (Chart)", "ID ICD codes"],

]
icdcodes=[['IGE/GGE ICD codes','NAFE/LFE ICD codes','EE ICD codes','Other G40 ICD codes']]

graphPlot=[]



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
        # goes through columns
        for col in vals.columns:
            if col=="Cohort":
                for ind in vals.index:
                    #filter the asd epi
                    if vals[col][ind]=="ASD,Epi":
                        for col1 in vals.columns:
                            # filters the completed chart reviews
                            if col1=="Chart Review Complete":
                                if vals[col1][ind]=="Complete":
                                    for col2 in vals.columns:   
                                        if col2==var:
                                            if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" and vals[col2][ind]!="No":
                                                valuePresent+=1
                                                totalValues+=1
                                                eachVar+=1
                                                # store the sources
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
        coveragePercent=valuePresent
        if typeSource!="":
            graphPlot.append([typeSource,group_labels1[i],coveragePercent])
           



# make graph
df = pd.DataFrame(graphPlot,columns=['Sources','Category','Percent coverage'])

ax=df.pivot('Category','Sources','Percent coverage').plot(kind='bar',colormap='Paired')
for p in ax.patches[0:]:
    h = p.get_height()
    x = p.get_x()+p.get_width()/2.
    if h != 0:
        ax.annotate("{:.1f}".format(p.get_height()), xy=(x,h), xytext=(0,4), rotation=90, 
                   textcoords="offset points", ha="center", va="bottom", fontsize=6)
plt.title("Counts for DD and ID N={}".format(T))

plt.legend(bbox_to_anchor=(0,1.02,1,0.102),loc='lower left',ncol=10,fontsize='small')
plt.show()
###########################################################
# this is for mri status
normal=0
abnormal=0
noresults=0
counts=0
awaiting=0
sidlist=[]
idfound=[]
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
                                    sidlist.append(sid)  
                                    for col2 in vals.columns:
                                         
                                        if col2=="MRI status (Chart)":
                                            
                                            if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                idfound.append(sid)
                                                counts+=1
                                                if vals[col2][ind]=="No MRI results":
                                                    noresults+=1
                                                if vals[col2][ind]=="Normal":
                                                    normal+=1
                                                if vals[col2][ind]=="Abnormal":
                                                    abnormal+=1
                                                if vals[col2][ind]=="Awaiting results":
                                                    awaiting+=1
labels=['Abnormal','Normal','No MRI Results',"Awaiting Results"]
graphs_=[abnormal,normal,noresults,awaiting]
df=pd.DataFrame({'Status':labels,'counts':graphs_})
ax=df.plot.bar(x='Status',y='counts',rot=0)
for j in range(0,len(sidlist)):
    print(j,end=", ")
    print(sidlist[j])
print("=============")
for j in range(0,len(idfound)):
    print(j,end=", ")
    print(idfound[j])
print(set(sidlist)-set(idfound))
for p in ax.patches[0:]:
    h = p.get_height()
    x = p.get_x()+p.get_width()/2.
    if h != 0:
        ax.annotate("{:.1f}".format(p.get_height()), xy=(x,h), xytext=(0,4), rotation=90, 
                   textcoords="offset points", ha="center", va="bottom", fontsize=6)
plt.title("MRI Status (Chart) counts N={}".format(counts))
plt.show()
############################################################
# verbality
no=0
yes=0
unknown=0 

plot=[]
counts=0
for col in vals.columns:
    if col=="Cohort":
        for ind in vals.index:
            if vals[col][ind]=="ASD,Epi":
                for col1 in vals.columns:
                    if col1=="Chart Review Complete":
                        if vals[col1][ind]=="Complete":
                            for col2 in vals.columns:
                                  
                                if col2=="Nonverbal (Chart)":
                                    if not isNaN(vals[col2][ind]):
                                        counts+=1
                                        if vals[col2][ind]=="No":
                                            no+=1
                                        if vals[col2][ind]=="Unknown":
                                            unknown+=1
                                        if vals[col2][ind]=="Yes":
                                            yes+=1
                                       
plot.append(['Nonverbal \n (Chart)','Yes',yes])
plot.append(['Nonverbal \n (Chart)','No',no])
plot.append(['Nonverbal \n (Chart)','Unknown',unknown])
no=0
yes=0
unknown=0 
for col in vals.columns:
    if col=="Cohort":
        for ind in vals.index:
            if vals[col][ind]=="ASD,Epi":
                for col1 in vals.columns:
                    if col1=="Chart Review Complete":
                        if vals[col1][ind]=="Complete":
                            for col2 in vals.columns:
                                  
                                if col2=="Nonverbal (Self Assess)":
                                    if not isNaN(vals[col2][ind]):
                                        counts+=1
                                        if vals[col2][ind]=="No":
                                            no+=1
                                        if vals[col2][ind]=="Unknown":
                                            unknown+=1
                                        if vals[col2][ind]=="Yes":
                                            yes+=1
                                       
plot.append(['Nonverbal \n (Self Assess)','Yes',yes])
plot.append(['Nonverbal \n (Self Assess)','No',no])
plot.append(['Nonverbal \n (Self Assess)','Unknown',unknown])  

nvl3=0
nvn=0
sd=0
limited=0
other=0

for col in vals.columns:
    if col=="Cohort":
        for ind in vals.index:
            if vals[col][ind]=="ASD,Epi":
                for col1 in vals.columns:
                    if col1=="Chart Review Complete":
                        if vals[col1][ind]=="Complete":
                            for col2 in vals.columns:
                                  
                                if col2=="Nonverbal (Interview)":
                                    if not isNaN(vals[col2][ind]):
                                        values=vals[col2][ind].split(";")
                                        counts+=1
                                        for i in values:
                                            if "less than 3 words" in i:
                                                nvn+=1
                                            if "no words" in i:
                                                nvn+=1
                                            if "Limited" in i:
                                                limited+=1
                                            if "Speech delay" in i:
                                                sd+=1
                                            if "Other" in i:
                                                other+=1
print(counts)
plot.append(['Nonverbal \n (Interview)','NV: Less than \n 3 words or \n no words',nvn])
plot.append(['Nonverbal \n (Interview)','Limited vocab',limited])
plot.append(['Nonverbal \n (Interview)','Speech delay',sd])

plot.append(['Nonverbal \n (Interview)','Other',other])
for i in plot:
    print(i)
df = pd.DataFrame(plot,columns=['Status','Source','Counts'])

ax=df.pivot('Status','Source','Counts').plot(kind='bar',colormap='Paired')
for p in ax.patches[0:]:
    h = p.get_height()
    x = p.get_x()+p.get_width()/2.
    if h != 0:
        ax.annotate("{:.1f}".format(p.get_height()), xy=(x,h), xytext=(0,4), rotation=90, 
                   textcoords="offset points", ha="center", va="bottom", fontsize=6)
plt.title("Nonverbal-Verbal Status Counts")
plt.legend(loc='upper left')
plt.show()
#########################################################################################################
#Race
sources=["Proband's Race (Referral)",'Race (Demo)','Race (Epic SP)',]
plot=[]
counts=0
for s in sources:
    caucasian=0
    Asian=0
    Mixed=0
    AfricanAmerican=0
    Unknown=0
    hispanic=0
    other=0
    unknown=0
    for col in vals.columns:
        if col=="Cohort":
            for ind in vals.index:
                if vals[col][ind]=="ASD,Epi":
                    for col1 in vals.columns:
                        if col1=="Chart Review Complete":
                            if vals[col1][ind]=="Complete":
                                for col2 in vals.columns:
                                    
                                    if col2==s:
                                        if not isNaN(vals[col2][ind]):
                                            counts+=1
                                            if vals[col2][ind]=="Caucasian/White" or vals[col2][ind]=="White" :
                                                caucasian+=1
                                            if vals[col2][ind]=="Mixed":
                                                Mixed+=1
                                            if vals[col2][ind]=="Asian":
                                                Asian+=1
                                            if vals[col2][ind]=="African American/Black" or vals[col2][ind]=="Black":
                                                AfricanAmerican+=1
                                            if vals[col2][ind]=="HISPANIC":
                                                hispanic+=1
                                            if "Other" in vals[col2][ind]:
                                                other+=1
                                            if "Unknown" in vals[col2][ind]:
                                                unknown+=1
                                        
    plot.append(['Caucasian/\nWhite',s,caucasian])
    plot.append(['Mixed',s,Mixed])
    plot.append(['Asian',s,Asian])
    plot.append(['African \n American/\nBlack',s,AfricanAmerican])
    plot.append(['Hispanic',s,hispanic])
    plot.append(['Other',s,other])
    plot.append(['Unknown',s,unknown])
for i in plot:
    print(i)
df = pd.DataFrame(plot,columns=['Race','Source','Counts'])

ax=df.pivot('Race','Source','Counts').plot(kind='bar',colormap='Paired')
for p in ax.patches[0:]:
    h = p.get_height()
    x = p.get_x()+p.get_width()/2.
    if h != 0:
        ax.annotate("{:.1f}".format(p.get_height()), xy=(x,h), xytext=(0,4), rotation=90, 
                   textcoords="offset points", ha="center", va="bottom", fontsize=6)
plt.title("Race Counts")
plt.legend(loc='upper left')
plt.show()
#############################################################
#Ethnicity
sources=["Proband's Ethnicity (Referral)", "Ethnicity (Demo)"]
plot=[]
counts=0
for s in sources:
    nHispanic=0
    hispanic=0
    other=0
    unknown=0
    for col in vals.columns:
        if col=="Cohort":
            for ind in vals.index:
                if vals[col][ind]=="ASD,Epi":
                    for col1 in vals.columns:
                        if col1=="Chart Review Complete":
                            if vals[col1][ind]=="Complete":
                                for col2 in vals.columns:
                                    
                                    if col2==s:
                                        if not isNaN(vals[col2][ind]):
                                            counts+=1
                                            if vals[col2][ind]=="Not Hispanic":
                                                nHispanic+=1
                                            if vals[col2][ind]=="Hispanic":
                                                hispanic+=1
                                           
                                            if "Unknown" in vals[col2][ind]:
                                                unknown+=1
                                        
    plot.append(['Not \n Hispanic',s,nHispanic])
    plot.append(['Hispanic',s,hispanic])
    plot.append(['Unknown',s,unknown])
for i in plot:
    print(i)
df = pd.DataFrame(plot,columns=['Ethnicity','Source','Counts'])

ax=df.pivot('Ethnicity','Source','Counts').plot(kind='bar',colormap='Paired')
for p in ax.patches[0:]:
    h = p.get_height()
    x = p.get_x()+p.get_width()/2.
    if h != 0:
        ax.annotate("{:.1f}".format(p.get_height()), xy=(x,h), xytext=(0,4), rotation=90, 
                   textcoords="offset points", ha="center", va="bottom", fontsize=6)
plt.title("Ethnicity Counts")
plt.legend(loc='upper left')
plt.show()