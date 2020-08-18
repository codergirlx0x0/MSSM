#purpose: looks at the epi types and how they are spread and correlate with intractable epi
#corresponding graphs: intractableEpiAnalysis.pdf Page 1
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from matplotlib.offsetbox import AnchoredText
#excel_file='Minimal Phenotype Fields - Dev Window Fields Separated_2020-06-25.xlsx'
excel_file= "Minimal Phenotype Fields - Dev Window Fields Separated_2020-07-30_11-17-39_Referral_2020-07-30_10-33-09.xlsx"
vals=pd.read_excel(excel_file, sheet_name=0)
def isNaN(num):
    return num != num
def parseData(index,colName):
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
                                            if col2==colName:
                                                for col3 in vals.columns:
                                                    if col3== "Dxreferral Aed":
                                                        if index==0:
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                                    subjects[sid]=[vals[col2][ind],vals[col3][ind]]
                                                       
    return subjects

   
def createGraph(s):                 
    labels=['Intractable Epi',"Not Intractable Epi"]
    eeL=[]
    igeL=[]
    lfeL=[]
    nafeL=[]
    ee=0
    ige=0
    lfe=0
    nafe=0
    tot=0
    for i in s:
        print(i,end=", ")
        print(s[i])
        if s[i][1]==True:
            tot+=1
        if ";" in s[i][0]:
            types=s[i][0].split(";")
            for j in types:
                
                if (s[i][1]==True and j=="Epileptic Encephalopathy"):
                    ee+=1
                elif (s[i][1]==True and j=="Idiopathic generalized epilepsy"):
                    ige+=1
                elif (s[i][1]==True and j=="Lesional focal epilepsy"):
                    lfe+=1
                elif (s[i][1]==True and j=="Non-acquired focal epilepsy"):
                    nafe+=1
        else:
            if (s[i][1]==True and s[i][0]=="Epileptic Encephalopathy"):
                ee+=1
            elif (s[i][1]==True and s[i][0]=="Idiopathic generalized epilepsy"):
                ige+=1
            elif (s[i][1]==True and s[i][0]=="Lesional focal epilepsy"):
                lfe+=1
            elif (s[i][1]==True and s[i][0]=="Non-acquired focal epilepsy"):
                nafe+=1

                
    eeL.append(ee/len(s)*100)
    igeL.append(ige/len(s)*100)
    lfeL.append(lfe/len(s)*100)
    nafeL.append(nafe/len(s)*100)
    labels[0]+=" N= {}".format(tot)
    ee=0
    ige=0
    lfe=0
    nafe=0
    tot=0
    for i in s:
        if s[i][1]==False:
            tot+=1
        if ";" in s[i][0]:
            types=s[i][0].split(";")
            for j in types:
                
                if (s[i][1]==False and j=="Epileptic Encephalopathy"):
                    ee+=1
                elif (s[i][1]==False and j=="Idiopathic generalized epilepsy"):
                    ige+=1
                elif (s[i][1]==False and j=="Lesional focal epilepsy"):
                    lfe+=1
                elif (s[i][1]==False and j=="Non-acquired focal epilepsy"):
                    nafe+=1
        else:
            if (s[i][1]==False and s[i][0]=="Epileptic Encephalopathy"):
                ee+=1
            elif (s[i][1]==False and s[i][0]=="Idiopathic generalized epilepsy"):
                ige+=1
            elif (s[i][1]==False and s[i][0]=="Lesional focal epilepsy"):
                lfe+=1
            elif (s[i][1]==False and s[i][0]=="Non-acquired focal epilepsy"):
                nafe+=1

                
    eeL.append(ee/len(s)*100)
    igeL.append(ige/len(s)*100)
    lfeL.append(lfe/len(s)*100)
    nafeL.append(nafe/len(s)*100)
    labels[1]+=" N= {}".format(tot)
    
       
            
    
    barWidth =0.12
    r1=np.arange(len(eeL))
    r2=[x+barWidth for x in r1]
    r3=[x + barWidth for x in r2]
    r4=[x + barWidth for x in r3]
    p1=plt.bar(r1, eeL, color='#7f6d5f', width=barWidth, edgecolor='white', label="EE")
    p2=plt.bar(r2, igeL, color='#557f2d', width=barWidth, edgecolor='white', label="IGE")
    p3=plt.bar(r3, lfeL, color='#2d7f5e', width=barWidth, edgecolor='white', label="LFE")    
    p4=plt.bar(r4, nafeL, color='#5f3f5e', width=barWidth, edgecolor='white', label="NAFE")
    


    plt.ylabel('%')
    plt.xticks([r + barWidth for r in range(len(eeL))], labels)
    plt.legend()
    plt.title('Epi Types vs Intractable Epi N={}'.format(len(s)))
    plt.ylim(top=100)
    plt.ylim(bottom=0)

    for rect in p1+p2+p3+p4:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
   
    
    plt.show()

var="Epi type (Referral)"
s=parseData(0,var) 
# print(len(s))
# t=parseData(1,var)
# print(len(t))
createGraph(s) 