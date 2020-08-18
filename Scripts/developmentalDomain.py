#Purpose: Looks at the developmental Delay domains:Practical,Social,Conceptual and their correlation within the two data sources: chart and interview
#Corresponding graphs: "DDChartvInterview.png" "DDIntractable.png" "DD-PracticalSocialConceptual-Chart.png" "DD-PracticalSocialConceptual-Interviewt.png" 
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib_venn import venn2
from matplotlib_venn import venn3
#excel_file='Minimal Phenotype Fields - Dev Window Fields Separated_2020-06-25.xlsx'
excel_file= "Minimal Phenotype Fields - Dev Window Fields Separated_DevDelDomainsAdded.xlsx"
vals=pd.read_excel(excel_file, sheet_name=0)
def isNaN(num):
    return num != num

#chart vs interview venn diagram
fromChart=[]
fromInterview=[]
for col in vals.columns:
    if(col=="Cohort"):
        for ind in vals.index:
            pid=""
            if(vals[col][ind])=="ASD,Epi":
                for col2 in vals.columns:
                                      
                    if col2=="Subject ID":
                        pid=vals[col2][ind]
                    if col2=="DD domains (Chart)": 
                        if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                            fromChart.append(str(pid))
                    if col2=="DD domains (Interview)": 
                        if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                            fromInterview.append(str(pid))

set1 = set(fromChart)
set2 = set(fromInterview)
interviewStr=""
chartStr=""
bothStr=""
s1=list(set1-set2)
s2=list(set2-set1)
s3=list(set1&set2)



plt.figure()
ax = plt.gca()
v=venn2([set1, set2], ('DD Domain(Chart)', 'DD Domain (Interview)'))

plt.title("Developmental Domain: Chart vs. Interview")

plt.show()
########################################################################333
#filters the 3 skills domains for chart
intDict={}
conceptual=[]
practical=[]
social=[]
for col in vals.columns:
    if(col=="Cohort"):
        for ind in vals.index:
            pid=""
            if(vals[col][ind])=="ASD,Epi":
                for col2 in vals.columns:
                                      
                    if col2=="Subject ID":
                        pid=vals[col2][ind]
                    if col2=="DD domains (Chart)": 
                        if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                            domains=vals[col2][ind].split(";")
                            intDict[pid]=domains
for i in intDict:
    print(i,end=", ")
    print(intDict[i])
    if "Conceptual Skills" in intDict[i]:
        conceptual.append(str(i))
    if "Practical Skills" in intDict[i]:
        practical.append(str(i))
    if "Social Skills" in intDict[i]:
        social.append(str(i))
print(conceptual)
print(practical)
print(social)
a=['1','2','3','4','5','16','17','19','20']
b=['6','7','8','9','10','16','18','19','20']
c=['11','12','13','14','15','17','18','19','20']

set1 = set(a)
set2 = set(b)
set3 = set(c)

A=set(conceptual)
B=set(practical)
C=set(social)
plt.figure()
ax = plt.gca()
v = venn3([set1,set2,set3], ('Conceptual', 'Practical', 'Social'))
vennList=[]
a1=(list(A-B-C))
vennList.append(a1)
a2=(list(A&B-C))
vennList.append(a2)
a3=(list(A&C-B))
vennList.append(a3)
a4=(list(A&C-B))
vennList.append(a4)
a5=(list(A&B&C))
vennList.append(a5)
a6=(list(B&C-A))
vennList.append(a6)
a7=(list(C-A-B))
vennList.append(a7)
h=[]
l=[]
ids=['100','110','010','101','111','011','001']
for i in range(0,len(ids)):
    h.append(v.get_patch_by_id(ids[i]))
    l.append(len(vennList[i]))
    ctr=1
    strVal=""
    if len(vennList[i])==0:
        v.get_label_by_id(ids[i]).set_text("")
    else:
        strVal=len(vennList[i])
                    
          
    v.get_label_by_id(ids[i]).set_text(strVal)   
    v.get_label_by_id(ids[i]).set_fontsize(7)   


plt.title("Developmental Domains- Practical, Social, Conceptual: Chart")

plt.show()
########################################################
#filters the 3 skills domains for interview
intDict={}
conceptual=[]
practical=[]
social=[]
for col in vals.columns:
    if(col=="Cohort"):
        for ind in vals.index:
            pid=""
            if(vals[col][ind])=="ASD,Epi":
                for col2 in vals.columns:
                                      
                    if col2=="Subject ID":
                        pid=vals[col2][ind]
                    if col2=="DD domains (Interview)": 
                        if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown" :
                            domains=vals[col2][ind].split(";")
                            intDict[pid]=domains
for i in intDict:
    print(i,end=", ")
    print(intDict[i])
    if "Conceptual" in intDict[i]:
        conceptual.append(str(i))
    if "Practical" in intDict[i]:
        practical.append(str(i))
    if "Social" in intDict[i]:
        social.append(str(i))
print(conceptual)
print(practical)
print(social)
a=['1','2','3','4','5','16','17','19','20','21','22','23','24','25']
b=['6','7','8','9','10','16','18','19','20','21','22','23','24','25']
c=['11','12','13','14','15','17','18','19','20','21','22','23','24','25']

set1 = set(a)
set2 = set(b)
set3 = set(c)

A=set(conceptual)
B=set(practical)
C=set(social)
plt.figure()
ax = plt.gca()
v = venn3([set1,set2,set3], ('Conceptual', 'Practical', 'Social'))
vennList=[]
a1=(list(A-B-C))
vennList.append(a1)
a2=(list(A&B-C))
vennList.append(a2)
a3=(list(A&C-B))
vennList.append(a3)
a4=(list(A&C-B))
vennList.append(a4)
a5=(list(A&B&C))
vennList.append(a5)
a6=(list(B&C-A))
vennList.append(a6)
a7=(list(C-A-B))
vennList.append(a7)
h=[]
l=[]
ids=['100','110','010','101','111','011','001']
for i in range(0,len(ids)):
    h.append(v.get_patch_by_id(ids[i]))
    l.append(len(vennList[i]))
    ctr=1
    strVal=""
    if len(vennList[i])==0:
        v.get_label_by_id(ids[i]).set_text("")
    else:
        strVal=len(vennList[i])
        

    v.get_label_by_id(ids[i]).set_text(strVal)   
    v.get_label_by_id(ids[i]).set_fontsize(7)   


plt.title("Developmental Domains- Practical, Social, Conceptual: Interview")
#ax.legend(handles=h, labels=l, title="counts")
plt.show()