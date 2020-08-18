# Purpose: Looks at the correlation of categorical variables such as ID,DD,Verbality among the different sources
# Corresponding Graphs:"Correlations_CategoricalVariables.pdf Page All"
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

#from the list of sources, make pairs of two sources
sources=["Nonverbal (Chart)","Nonverbal (Self Assess)","Nonverbal (Interview)"]
sourcePairs=formPairs(sources)


for s in sourcePairs:
    source1={}
    isThere={}
    print(s)
    print("++++++++++++++++++++++++")
    # go through each column
    for col in vals.columns:
        if col=="Cohort":
            for ind in vals.index:
                found=0
                boolList=[]
                pid=""
                # filter out Asd,epi
                if vals[col][ind]=="ASD,Epi":
                    for col2 in vals.columns:
                        # store subjects
                        if col2=="Subject ID":
                            pid=vals[col2][ind]
                        if col2==s[0]: 
                            if not isNaN(vals[col2][ind]) and "Unknown" not in vals[col2][ind] :
                                    boolList.append(vals[col2][ind])
                                    found=1
                                    
                        if col2==s[1] and found==1:
                           
                            if not isNaN(vals[col2][ind]) and "Unknown" not in vals[col2][ind] :
                                    boolList.append(vals[col2][ind])
                    if len(boolList)==2:
                        source1[pid]=boolList                    
                                    
    # if no, add a 0, otherwise add a 1                           
    for i in source1:
        if source1[i][0]=="No":
            isThere[i]=[0]
        elif source1[i][0]!="No":
            isThere[i]=[1]
        if source1[i][1]=="No":
            isThere[i].append(0)
        elif source1[i][1]!="No":
            isThere[i].append(1)
    
    x=[]
    y=[]
    for i in isThere:
        x.append(isThere[i][0])
        y.append(isThere[i][1])

    x_=np.array(x)
    y_=np.array(y)

    total=len(x)
    x.append(1)
    y.append(0)
    # find r2
    m_, b = np.polyfit(x_, y_, 1)
    correlation_matrix=np.corrcoef(x,y)
    correlation_xy = correlation_matrix[0,1]
    r_squared = correlation_xy**2

    if round(b,2)>0:

        lineEq="y="+str(round(m_,2))+"x+"+str(round(b,2))
    elif round(b,2)==0:
        lineEq="y="+str(round(m_,2))+"x"
    else:
        lineEq="y="+str(round(m_,2))+"x"+str(round(b,2))
    fig=plt.figure()
    plt.plot(x_,m_*x_+b,'r', label=lineEq+", R2=" +str(round(r_squared,2)))

    plt.legend(loc='upper left')
    # jitter the x and y
    jittered_y = y + 0.1 * np.random.rand(len(y)) +0.05
    jittered_x = x + 0.1 * np.random.rand(len(x)) +0.05
    plt.scatter(jittered_x,jittered_y,color='b',s=3)
    plt.xlabel('{}'.format(s[0]))
    plt.ylabel('{}'.format(s[1]))
    plt.ylim(ymax=1.3,ymin=-0.3)
    plt.xlim(xmax=1.3,xmin=-0.3)
    my_xticks=[0,1]
    my_yticks=[0,1]
    # plot
    plt.xticks([my_xticks[0], my_xticks[-1]], visible=True, rotation="horizontal")
    plt.yticks([my_yticks[0], my_yticks[-1]], visible=True, rotation="horizontal")
    plt.title("Communication Correlation {} vs. {} N={}".format(s[0],s[1],total))
    pdf.savefig(fig,bbox_inches='tight')
    plt.clf
# pdf.close()
######################################################################################
# repeat for ID
sources=["ID dx (Interview)","ID? (Chart)"]
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
                boolList=[]
                pid=""
                if vals[col][ind]=="ASD,Epi":
                    for col2 in vals.columns:
                        if col2=="Subject ID":
                            pid=vals[col2][ind]
                        if col2==s[0]: 
                            if not isNaN(vals[col2][ind]) and "Unknown" not in vals[col2][ind] :
                                    boolList.append(vals[col2][ind])
                                    found=1
                                    
                        if col2==s[1] and found==1:
                           
                            if not isNaN(vals[col2][ind]) and "Unknown" not in vals[col2][ind] :
                                    boolList.append(vals[col2][ind])
                    if len(boolList)==2:
                        source1[pid]=boolList                    
                                    
                               
    for i in source1:
        if source1[i][0]=="No":
            isThere[i]=[0]
        elif source1[i][0]!="No":
            isThere[i]=[1]
        if source1[i][1]=="No":
            isThere[i].append(0)
        elif source1[i][1]!="No":
            isThere[i].append(1)
    # for j in isThere:
    #     print(j,end=", ")
    #     print(isThere[j])
    x=[]
    y=[]
    for i in isThere:
        x.append(isThere[i][0])
        y.append(isThere[i][1])
    
    # x.append(1)
    # y.append(0)
    x_=np.array(x)
    y_=np.array(y)

    total=len(x)
    # x.append(1)
    # y.append(0)

    m_, b = np.polyfit(x_, y_, 1)
    correlation_matrix=np.corrcoef(x,y)
    correlation_xy = correlation_matrix[0,1]
    r_squared = correlation_xy**2

    if round(b,2)>0:

        lineEq="y="+str(round(m_,2))+"x+"+str(round(b,2))
    elif round(b,2)==0:
        lineEq="y="+str(round(m_,2))+"x"
    else:
        lineEq="y="+str(round(m_,2))+"x"+str(round(b,2))
    fig=plt.figure()
    plt.plot(x_,m_*x_+b,'r', label=lineEq+", R2=" +str(round(r_squared,2)))

    plt.legend(loc='upper left')

    jittered_y = y + 0.1 * np.random.rand(len(y)) +0.05
    jittered_x = x + 0.1 * np.random.rand(len(x)) +0.05
    plt.scatter(jittered_x,jittered_y,color='b',s=3)
    plt.xlabel('{}'.format(s[0]))
    plt.ylabel('{}'.format(s[1]))
    plt.ylim(ymax=1.3,ymin=-0.3)
    plt.xlim(xmax=1.3,xmin=-0.3)
    my_xticks=[0,1]
    my_yticks=[0,1]
    plt.xticks([my_xticks[0], my_xticks[-1]], visible=True, rotation="horizontal")
    plt.yticks([my_yticks[0], my_yticks[-1]], visible=True, rotation="horizontal")
    plt.title("Intellectual Disability Correlation \n {} vs. {} N={}".format(s[0],s[1],total))
    pdf.savefig(fig,bbox_inches='tight')
    plt.clf
##################################################
# repeat for DD
sources=["DD dx (Interview)","DD? (Chart)", "DD? (Pt Qstr)"]
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
                boolList=[]
                pid=""
                if vals[col][ind]=="ASD,Epi":
                    for col2 in vals.columns:
                        if col2=="Subject ID":
                            pid=vals[col2][ind]
                        if col2==s[0]: 
                            if not isNaN(vals[col2][ind]) and "Unknown" not in vals[col2][ind] :
                                    boolList.append(vals[col2][ind])
                                    found=1
                                    
                        if col2==s[1] and found==1:
                           
                            if not isNaN(vals[col2][ind]) and "Unknown" not in vals[col2][ind] :
                                    boolList.append(vals[col2][ind])
                    if len(boolList)==2:
                        source1[pid]=boolList                    
                                    
                               
    for i in source1:
        if source1[i][0]=="No":
            isThere[i]=[0]
        elif source1[i][0]!="No":
            isThere[i]=[1]
        if source1[i][1]=="No":
            isThere[i].append(0)
        elif source1[i][1]!="No":
            isThere[i].append(1)
    for j in isThere:
        print(j,end=", ")
        print(isThere[j])
    x=[]
    y=[]
    for i in isThere:
        x.append(isThere[i][0])
        y.append(isThere[i][1])
    
    # x.append(1)
    # y.append(0)
    x_=np.array(x)
    y_=np.array(y)

    total=len(x)
    # x.append(1)
    # y.append(0)

    m_, b = np.polyfit(x_, y_, 1)
    correlation_matrix=np.corrcoef(x,y)
    correlation_xy = correlation_matrix[0,1]
    r_squared = correlation_xy**2

    if round(b,2)>0:

        lineEq="y="+str(round(m_,2))+"x+"+str(round(b,2))
    elif round(b,2)==0:
        lineEq="y="+str(round(m_,2))+"x"
    else:
        lineEq="y="+str(round(m_,2))+"x"+str(round(b,2))
    fig=plt.figure()
    plt.plot(x_,m_*x_+b,'r', label=lineEq+", R2=" +str(round(r_squared,2)))

    plt.legend(loc='upper left')

    jittered_y = y + 0.1 * np.random.rand(len(y)) +0.05
    jittered_x = x + 0.1 * np.random.rand(len(x)) +0.05
    plt.scatter(jittered_x,jittered_y,color='b',s=3)
    plt.xlabel('{}'.format(s[0]))
    plt.ylabel('{}'.format(s[1]))
    plt.ylim(ymax=1.3,ymin=-0.3)
    plt.xlim(xmax=1.3,xmin=-0.3)
    my_xticks=[0,1]
    my_yticks=[0,1]
    plt.xticks([my_xticks[0], my_xticks[-1]], visible=True, rotation="horizontal")
    plt.yticks([my_yticks[0], my_yticks[-1]], visible=True, rotation="horizontal")
    plt.title("Intellectual Disability Correlation \n {} vs. {} N={}".format(s[0],s[1],total))
    pdf.savefig(fig,bbox_inches='tight')
    plt.clf
pdf.close()