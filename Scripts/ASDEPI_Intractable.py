# Purpose: Looks at the correlation of Intractable Epi and other variables such as ID,DD,Verbality
# Corresponding Graphs:"intractableEpiAnalysis.pdf Page 2-5"

#import statements
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from matplotlib.offsetbox import AnchoredText
#excel_file='Minimal Phenotype Fields - Dev Window Fields Separated_2020-06-25.xlsx'
excel_file= "Minimal Phenotype Fields - Dev Window Fields Separated_2020-07-30_11-17-39_Referral_2020-07-30_10-33-09.xlsx"
vals=pd.read_excel(excel_file, sheet_name=0)
#Check if cell is nan
def isNaN(num):
    return num != num

# index of 0:don't include NAN 
#index of 1: Include nan values
def parseData(index,colName):
    subjects={}
    count=0
    #go through columns
    for col in vals.columns:
        if col=="Cohort":
            #filter out ASD Epi
            for ind in vals.index:
                if vals[col][ind]=="ASD,Epi":
                    for col1 in vals.columns:
                        # filter out completed chart reviews
                        if col1=="Chart Review Complete":
                            if vals[col1][ind]=="Complete":
                                for col4 in vals.columns:   
                                    #store subject ids
                                    if col4=="Subject ID":
                                        sid=vals[col4][ind] 
                                        for col2 in vals.columns:
                                            #gets the column name your are comparing with: ex: Verbality, ID,DD
                                            if col2==colName:
                                                for col3 in vals.columns:
                                                    # get the intractable epi column
                                                    if col3== "Dxreferral Aed":
                                                        if index==0:
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                subjects[sid]=(vals[col2][ind],vals[col3][ind])
                                                        elif index==1:
                                                            if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                                if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                    subjects[sid]=(vals[col2][ind],vals[col3][ind])
    return subjects

# function to build graph  
def createGraph(s,t,variable,pos,neg,nr):                 
    labels=['Intractable Epi',"Not Intractable Epi"]
    affected=[]
    notaffected=[]
    unknown=[]
    fishers=[[1,1],[1,1]]
    a=0
    n=0
    u=0
    for i in s:
        if s[i][1]==True and s[i][0]==pos:
            a+=1
        elif (s[i][1]==True and s[i][0]==neg) or (s[i][1]==True and isNaN(s[i][0])):
            n+=1
        elif s[i][1]==True and s[i][0]==nr:
            u+=1

    fishers[0][0]=a
    fishers[0][1]=n
    affected.append(a/len(s)*100)
    notaffected.append(n/len(s)*100)
    unknown.append(u/len(s)*100)
    labels[0]+=" N= {}".format(a+n+u)
    a=0
    n=0
    u=0
    for i in s:
        if s[i][1]==False and s[i][0]==pos:
            a+=1
        elif (s[i][1]==False and s[i][0]==n) or (s[i][1]==False and isNaN(s[i][0])):
            n+=1
        elif s[i][1]==False and s[i][0]==nr:
            u+=1
    #for fishers test
    fishers[0][0]=a
    fishers[0][1]=n
    affected.append(a/len(s)*100)
    notaffected.append(n/len(s)*100)
    unknown.append(u/len(s)*100)
    labels[1]+=" N= {}".format(a+n+u)    
            
    plt.subplot(2,1,1)
    barWidth =0.25
    r1=np.arange(len(affected))
    r2=[x+barWidth for x in r1]
    r3=[x + barWidth for x in r2]
    p1=plt.bar(r1, affected, color='#7f6d5f', width=barWidth, edgecolor='white', label=pos)
    p2=plt.bar(r2, notaffected, color='#557f2d', width=barWidth, edgecolor='white', label=neg)
    p3=plt.bar(r3, unknown, color='#2d7f5e', width=barWidth, edgecolor='white', label=nr)    

    


    oddsratio, pvalue = stats.fisher_exact(fishers)

    plt.ylabel('%')
    plt.xticks([r + barWidth for r in range(len(affected))], labels)
    plt.legend()
    plt.title('{} vs Intractable Epi N={}'.format(variable,len(s)))
    plt.ylim(top=100)
    plt.ylim(bottom=0)

    for rect in p1+p2+p3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    txt="Odds Ratio: {} \nP Value: {}".format(oddsratio,pvalue)
    plt.text(0,80, txt,fontsize=6)
    ####################
    labels=['Intractable Epi',"Not Intractable Epi"]
    affected=[]
    notaffected=[]
    unknown=[]
    fishers=[[1,1],[1,1]]
    a=0
    n=0
    u=0
    for i in t:
        if t[i][1]==True and t[i][0]==pos:
            a+=1
        elif t[i][1]==True and t[i][0]==n:
            n+=1
        elif t[i][1]==True and t[i][0]==nr:
            u+=1

    fishers[0][0]=a
    fishers[0][1]=n
    affected.append(a/len(t)*100)
    notaffected.append(n/len(t)*100)
    unknown.append(u/len(t)*100)
    labels[0]+=" N= {}".format(a+n+u)
    a=0
    n=0
    u=0
    for i in t:
        if t[i][1]==False and t[i][0]==pos:
            a+=1
        elif t[i][1]==False and t[i][0]==neg:
            n+=1
        elif t[i][1]==False and t[i][0]==nr:
            u+=1

    fishers[0][0]=a
    fishers[0][1]=n
    affected.append(a/len(t)*100)
    notaffected.append(n/len(t)*100)
    unknown.append(u/len(t)*100)
    labels[1]+=" N= {}".format(a+n+u)    
            
    plt.subplot(2,1,2)
    barWidth =0.25
    r1=np.arange(len(affected))
    r2=[x+barWidth for x in r1]
    r3=[x + barWidth for x in r2]
    p1=plt.bar(r1, affected, color='#7f6d5f', width=barWidth, edgecolor='white', label=pos)
    p2=plt.bar(r2, notaffected, color='#557f2d', width=barWidth, edgecolor='white', label=neg)
    p3=plt.bar(r3, unknown, color='#2d7f5e', width=barWidth, edgecolor='white', label=nr)    

    


    oddsratio, pvalue = stats.fisher_exact(fishers)

    plt.ylabel('%')
    plt.xticks([r + barWidth for r in range(len(affected))], labels)
    plt.legend()
    plt.title('{} vs Intractable Epi N={}'.format(variable,len(t)))
    plt.ylim(top=100)
    plt.ylim(bottom=0)

    for rect in p1+p2+p3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    txt="Odds Ratio: {} \nP Value: {}".format(oddsratio,pvalue)
    plt.text(0,80, txt,fontsize=6)
    plt.show()

# Here, swap the Pos, neg, nr, and var with the corresponding columns to what you are looking for
# for example, if we are looking at DD (Chart)
# pos would be "No", neg would be "Yes", nr would be"No results" and var would be "DD? (Chart)"
pos="Normal"
neg="Abnormal"
nr="No MRI results"
var="MRI status (Chart)"
s=parseData(0,var) 
print(len(s))
t=parseData(1,var)
print(len(t))
createGraph(s,t,var,pos,neg,nr) 