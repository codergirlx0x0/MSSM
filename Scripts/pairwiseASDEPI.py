#Purpose: This looks at the correlation between each pair of the (total 4) different sources of ASD-EPI aoo and aod types: We look at the line of best fit and r2 value
#Corresponding graphs: Correlations_ASDEPI.pdf
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations
import numpy.ma as ma
from scipy.stats.stats import pearsonr 
from matplotlib.backends.backend_pdf import PdfPages
#excel_file='Minimal Phenotype Fields - Dev Window Fields Separated_2020-05-28.xlsx'
excel_file= "Minimal Phenotype Fields - Dev Window Fields Separated_DevDelDomainsAdded.xlsx"
vals=pd.read_excel(excel_file, sheet_name=0)
def isNaN(num):
    return num != num
def removekey(d, key):
    r = dict(d)
    del r[key]
    return r
def formPairs(source):
    result=list(combinations(source,2))
    return result
pdf = PdfPages('out.pdf')

sources=["Proband's ASD Ao O (mos) (Referral)","ASD Ao O (mos) (Interview)","ASD Ao O (mos) (Chart)","ASD Ao O (mos) (Self Assess)"]
sourcePairs=formPairs(sources)


for s in sourcePairs:
    source1={}
    isThere={}
    print(s)
    print("++++++++++++++++++++++++")
    for col in vals.columns:
        if col=="Cohort":
            for ind in vals.index:
                found=0
                mosList=[]
                pid=""
                if vals[col][ind]=="ASD,Epi":
                    for col2 in vals.columns:
                        if col2=="Subject ID":
                            pid=vals[col2][ind]
                        if col2==s[0]: 
                            #print(vals[col2][ind])
                            if not isNaN(vals[col2][ind]) and "Unknown" != vals[col2][ind] :
                                    mosList.append(vals[col2][ind])
                                    found=1
                                    
                        if col2==s[1] and found==1:
                           
                            if not isNaN(vals[col2][ind]) and "Unknown" != vals[col2][ind] :
                                    mosList.append(vals[col2][ind])
                    if len(mosList)==2:
                        source1[pid]=mosList                    
                                    
                               
    for i in source1:
        print(i,end=", ")
        print(source1[i])
    
    x=[]
    y=[]
    for i in source1:
        x.append(source1[i][0])
        y.append(source1[i][1])
    
    # x.append(1)
    # y.append(0)
    x_=np.array(x)
    y_=np.array(y)

    total=len(x)
    
    #find the line of best fit and r2
    m_, b = np.polyfit(x_, y_, 1)
    correlation_matrix=np.corrcoef(x,y)
    correlation_xy = correlation_matrix[0,1]
    r_squared = correlation_xy**2
    print(r_squared)
    if round(b,2)>0:

        lineEq="y="+str(round(m_,2))+"x+"+str(round(b,2))
    elif round(b,2)==0:
        lineEq="y="+str(round(m_,2))+"x"
    else:
        lineEq="y="+str(round(m_,2))+"x"+str(round(b,2))
    fig=plt.figure()
    plt.plot(x_,m_*x_+b,'r', label=lineEq+", R2=" +str(round(r_squared,2)))

    plt.legend(loc='upper left')

   
    plt.scatter(x,y,color='b',s=3)
    plt.xlabel('{}'.format(s[0]))
    plt.ylabel('{}'.format(s[1]))

    plt.title("ASD AoO Correlation {} vs. {} N={}".format(s[0],s[1],total))
    pdf.savefig(fig,bbox_inches='tight')
    plt.clf
############################################################    
sources=["Proband's ASD Ao D (mos) (Referral)","ASD Ao D (mos) (Interview)","ASD Ao D (mos) (Chart)","ASD Ao D (mos) (Self Assess)"]
sourcePairs=formPairs(sources)


for s in sourcePairs:
    source1={}
    isThere={}
    print(s)
    print("++++++++++++++++++++++++")
    for col in vals.columns:
        if col=="Cohort":
            for ind in vals.index:
                found=0
                mosList=[]
                pid=""
                if vals[col][ind]=="ASD,Epi":
                    for col2 in vals.columns:
                        if col2=="Subject ID":
                            pid=vals[col2][ind]
                        if col2==s[0]: 
                            #print(vals[col2][ind])
                            if not isNaN(vals[col2][ind]) and "Unknown" != vals[col2][ind] :
                                    mosList.append(vals[col2][ind])
                                    found=1
                                    
                        if col2==s[1] and found==1:
                           
                            if not isNaN(vals[col2][ind]) and "Unknown" != vals[col2][ind] :
                                    mosList.append(vals[col2][ind])
                    if len(mosList)==2:
                        source1[pid]=mosList                    
                                    
                               
    for i in source1:
        print(i,end=", ")
        print(source1[i])
    
    x=[]
    y=[]
    for i in source1:
        x.append(source1[i][0])
        y.append(source1[i][1])
    
    # x.append(1)
    # y.append(0)
    x_=np.array(x)
    y_=np.array(y)

    total=len(x)
    

    m_, b = np.polyfit(x_, y_, 1)
    correlation_matrix=np.corrcoef(x,y)
    correlation_xy = correlation_matrix[0,1]
    r_squared = correlation_xy**2
    print(r_squared)
    if round(b,2)>0:

        lineEq="y="+str(round(m_,2))+"x+"+str(round(b,2))
    elif round(b,2)==0:
        lineEq="y="+str(round(m_,2))+"x"
    else:
        lineEq="y="+str(round(m_,2))+"x"+str(round(b,2))
    fig=plt.figure()
    plt.plot(x_,m_*x_+b,'r', label=lineEq+", R2=" +str(round(r_squared,2)))

    plt.legend(loc='upper left')

   
    plt.scatter(x,y,color='b',s=3)
    plt.xlabel('{}'.format(s[0]))
    plt.ylabel('{}'.format(s[1]))

    plt.title("ASD AoD Correlation {} vs. {} N={}".format(s[0],s[1],total))
    pdf.savefig(fig,bbox_inches='tight')
    plt.clf
    ###########################################################################################
sources=["Proband's Epi Ao O (mos) (Referral)","Epi Ao O (mos) (Chart)","Age at 1st seizure (mos) (Self Assess)","Age at first seizure (mos) (Interview)"]
sourcePairs=formPairs(sources)


for s in sourcePairs:
    source1={}
    isThere={}
    print(s)
    print("++++++++++++++++++++++++")
    for col in vals.columns:
        if col=="Cohort":
            for ind in vals.index:
                found=0
                mosList=[]
                pid=""
                if vals[col][ind]=="ASD,Epi":
                    for col2 in vals.columns:
                        if col2=="Subject ID":
                            pid=vals[col2][ind]
                        if col2==s[0]: 
                            #print(vals[col2][ind])
                            if not isNaN(vals[col2][ind]) and "Unknown" != vals[col2][ind] :
                                    mosList.append(vals[col2][ind])
                                    found=1
                                    
                        if col2==s[1] and found==1:
                           
                            if not isNaN(vals[col2][ind]) and "Unknown" != vals[col2][ind] :
                                    mosList.append(vals[col2][ind])
                    if len(mosList)==2:
                        source1[pid]=mosList                    
                                    
                               
    for i in source1:
        print(i,end=", ")
        print(source1[i])
    
    x=[]
    y=[]
    for i in source1:
        x.append(source1[i][0])
        y.append(source1[i][1])
    
    # x.append(1)
    # y.append(0)
    x_=np.array(x)
    y_=np.array(y)

    total=len(x)
    print(len(x))
    print(len(y))
    

    m_, b = np.polyfit(x_, y_, 1)
    correlation_matrix=np.corrcoef(x,y)
    correlation_xy = correlation_matrix[0,1]
    r_squared = correlation_xy**2
    print(r_squared)
    if round(b,2)>0:

        lineEq="y="+str(round(m_,2))+"x+"+str(round(b,2))
    elif round(b,2)==0:
        lineEq="y="+str(round(m_,2))+"x"
    else:
        lineEq="y="+str(round(m_,2))+"x"+str(round(b,2))
    fig=plt.figure()
    plt.plot(x_,m_*x_+b,'r', label=lineEq+", R2=" +str(round(r_squared,2)))

    plt.legend(loc='upper left')

   
    plt.scatter(x,y,color='b',s=3)
    plt.xlabel('{}'.format(s[0]))
    plt.ylabel('{}'.format(s[1]))

    plt.title("Epi AoO Correlation {} vs. {} N={}".format(s[0],s[1],total))
    pdf.savefig(fig,bbox_inches='tight')
    plt.clf 
# ########################################################################   
sources= ["Proband's Epi Ao D (mos) (Referral)","Epi Ao D (mos) (Interview)","Epi Ao D (mos) (Chart)"]
sourcePairs=formPairs(sources)


for s in sourcePairs:
    source1={}
    isThere={}
    print(s)
    print("++++++++++++++++++++++++")
    for col in vals.columns:
        if col=="Cohort":
            for ind in vals.index:
                found=0
                mosList=[]
                pid=""
                if vals[col][ind]=="ASD,Epi":
                    for col2 in vals.columns:
                        if col2=="Subject ID":
                            pid=vals[col2][ind]
                        if col2==s[0]: 
                            #print(vals[col2][ind])
                            if not isNaN(vals[col2][ind]) and "Unknown" != vals[col2][ind] :
                                    mosList.append(vals[col2][ind])
                                    found=1
                                    
                        if col2==s[1] and found==1:
                           
                            if not isNaN(vals[col2][ind]) and "Unknown" != vals[col2][ind] :
                                    mosList.append(vals[col2][ind])
                    if len(mosList)==2:
                        source1[pid]=mosList                    
                                    
                               
    for i in source1:
        print(i,end=", ")
        print(source1[i])
    
    x=[]
    y=[]
    print(len(source1))
    if len(source1)>1:
        for i in source1:
            x.append(source1[i][0])
            y.append(source1[i][1])
        
        # x.append(1)
        # y.append(0)
        x_=np.array(x)
        y_=np.array(y)

        total=len(x)
        

        m_, b = np.polyfit(x_, y_, 1)
        correlation_matrix=np.corrcoef(x,y)
        correlation_xy = correlation_matrix[0,1]
        r_squared = correlation_xy**2
        print(r_squared)
        if round(b,2)>0:

            lineEq="y="+str(round(m_,2))+"x+"+str(round(b,2))
        elif round(b,2)==0:
            lineEq="y="+str(round(m_,2))+"x"
        else:
            lineEq="y="+str(round(m_,2))+"x"+str(round(b,2))
        fig=plt.figure()
        plt.plot(x_,m_*x_+b,'r', label=lineEq+", R2=" +str(round(r_squared,2)))

        plt.legend(loc='upper left')

    
        plt.scatter(x,y,color='b',s=3)
        plt.xlabel('{}'.format(s[0]))
        plt.ylabel('{}'.format(s[1]))

        plt.title("Epi AoD Correlation {} vs. {} N={}".format(s[0],s[1],total))
        pdf.savefig(fig,bbox_inches='tight')
        plt.clf
pdf.close()