#Purpose: This looks at the correlation between each pair of the (total 3) different sources of epi types: We look at the line of best fit and r2 value
#Corresponding graphs: "EERefvschart.png" "LFEChartvsInt.png" "NAFEChartvsInt.png" "IGEChartvsInt.png" "EEChartvsInt.png" "LFERefvsInt.png" "NAFERefvsInt.png" "IGERefvsInt.png" "EERefvsInt.png" "LFERefvsChart.png" "NAFERefvsChart.png" "IGERefvsChart.png" 
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
#excel_file='Minimal Phenotype Fields - Dev Window Fields Separated_2020-05-28.xlsx'
excel_file= "Minimal Phenotype Fields - Dev Window Fields Separated_2020-06-25_16-04-37.xlsx"
vals=pd.read_excel(excel_file, sheet_name=0)
def isNaN(num):
    return num != num
def removekey(d, key):
    r = dict(d)
    del r[key]
    return r
isThere={}
data=[]
epiTypes=['Epileptic Encephalopathy','Idiopathic generalized epilepsy','Non-acquired focal epilepsy',
'Lesional focal epilepsy']
#ref vs chart
for etype in epiTypes:
    refDict={}
    for col in vals.columns:
        if col=="Cohort":
            
            for ind in vals.index:
                if vals[col][ind]=="ASD,Epi":
                    for col2 in vals.columns:
                        
                        if col2=="Subject ID":
                            pid=vals[col2][ind]
                            #eachProband.append(pid)
                        if col2=="Proband's Epi type (Referral)": 
                            if not isNaN(vals[col2][ind]) and "Unknown" not in vals[col2][ind] :
                                if ";" in vals[col2][ind]:
                                    new=vals[col2][ind].split(";")
                                    refDict[pid]=new
                                    
                                else:
                                    refDict[pid]=[vals[col2][ind]]

    
    for i in refDict:
        
        for j in refDict[i]:
            if j==etype:
                isThere[i]=[1]
                break
            else:
                isThere[i]=[0]

    chartDict={}
    for col in vals.columns:
        if col=="Cohort":
            
            for ind in vals.index:
                if vals[col][ind]=="ASD,Epi":
                    for col2 in vals.columns:
                        
                        if col2=="Subject ID":
                            pid=vals[col2][ind]
                            #eachProband.append(pid)
                        if col2=="Epi type (Chart)": 
                            if not isNaN(vals[col2][ind]) and "Unknown" not in vals[col2][ind] :
                                if ";" in vals[col2][ind]:
                                    new=vals[col2][ind].split(";")
                                    chartDict[pid]=new
                                    
                                else:
                                    chartDict[pid]=[vals[col2][ind]]
    # true=1 and false=0          
    for i in chartDict:
        if i in isThere:
            for j in chartDict[i]:
                if j==etype:
                    isThere[i].append(1)
                    break
                else:
                    isThere[i].append(0)
                    break
    for i in isThere:
        if len(isThere[i])==1:
            isThere=removekey(isThere,i)

    x=[]
    y=[]
    for i in isThere:
        x.append(isThere[i][0])
        y.append(isThere[i][1])
    print(len(x))
    x_=np.array(x)
    y_=np.array(y)

    m_, b = np.polyfit(x_, y_, 1)
    correlation_matrix = np.corrcoef(x, y)
    correlation_xy = correlation_matrix[0,1]
    r_squared = correlation_xy**2
    #find r2 and line of best fit
    if round(b,2)>0:

        lineEq="y="+str(round(m_,2))+"x+"+str(round(b,2))
    elif round(b,2)==0:
        lineEq="y="+str(round(m_,2))+"x"
    else:
        lineEq="y="+str(round(m_,2))+"x"+str(round(b,2))
    plt.plot(x_,m_*x_+b,'r', label=lineEq+", R2=" +str(round(r_squared,2)))

    plt.legend(loc='upper left')

    jittered_y = y + 0.1 * np.random.rand(len(y)) -0.04
    jittered_x = x + 0.1 * np.random.rand(len(x)) -0.05
    plt.scatter(jittered_x,jittered_y,color='b',s=3)
    plt.ylabel('Chart')
    plt.xlabel('Referral')
    plt.ylim(ymax=1.3,ymin=-0.3)
    plt.xlim(xmax=1.3,xmin=-0.3)
    my_xticks=[0,1]
    my_yticks=[0,1]
    plt.xticks([my_xticks[0], my_xticks[-1]], visible=True, rotation="horizontal")
    plt.yticks([my_yticks[0], my_yticks[-1]], visible=True, rotation="horizontal")
    plt.title("{} Epi Type Correlation Referral vs. Chart".format(etype))
    plt.show()


##################################################################################################################
#Ref vs Interview
isThere={}
data=[]
epiTypes=['Epileptic Encephalopathy','Idiopathic generalized epilepsy','Non-acquired focal epilepsy',
'Lesional focal epilepsy']

for etype in epiTypes:
    refDict={}
    for col in vals.columns:
        if col=="Cohort":
            
            for ind in vals.index:
                if vals[col][ind]=="ASD,Epi":
                    for col2 in vals.columns:
                        
                        if col2=="Subject ID":
                            pid=vals[col2][ind]
                            #eachProband.append(pid)
                        if col2=="Proband's Epi type (Referral)": 
                            if not isNaN(vals[col2][ind]) and "Unknown" not in vals[col2][ind] :
                                if ";" in vals[col2][ind]:
                                    new=vals[col2][ind].split(";")
                                    refDict[pid]=new
                                    
                                else:
                                    refDict[pid]=[vals[col2][ind]]

    
    for i in refDict:
        
        for j in refDict[i]:
            if j==etype:
                isThere[i]=[1]
                break
            else:
                isThere[i]=[0]

    intDict={}
    for col in vals.columns:
        if col=="Cohort":
            
            for ind in vals.index:
                if vals[col][ind]=="ASD,Epi":
                    for col2 in vals.columns:
                        
                        if col2=="Subject ID":
                            pid=vals[col2][ind]
                            #eachProband.append(pid)
                        if col2=="Epi type (Interview)": 
                            if not isNaN(vals[col2][ind]) and "Unknown" not in vals[col2][ind] :
                                if ";" in vals[col2][ind]:
                                    new=vals[col2][ind].split(";")
                                    intDict[pid]=new
                                    
                                else:
                                    intDict[pid]=[vals[col2][ind]]
               
    for i in intDict:
        if i in isThere:
            for j in intDict[i]:
                if j==etype:
                    isThere[i].append(1)
                    break
                else:
                    isThere[i].append(0)
                    break
    for i in isThere:
        if len(isThere[i])==1:
            isThere=removekey(isThere,i)
    # for i in isThere:
    #     print(i,end=", ")
    #     print(isThere[i])
    # print("===================")
    x=[]
    y=[]
    for i in isThere:
        x.append(isThere[i][0])
        y.append(isThere[i][1])
 
    x_=np.array(x)
    y_=np.array(y)

    m_, b = np.polyfit(x_, y_, 1)
    correlation_matrix = np.corrcoef(x, y)
    correlation_xy = correlation_matrix[0,1]
    r_squared = correlation_xy**2

    if round(b,2)>0:

        lineEq="y="+str(round(m_,2))+"x+"+str(round(b,2))
    elif round(b,2)==0:
        lineEq="y="+str(round(m_,2))+"x"
    else:
        lineEq="y="+str(round(m_,2))+"x"+str(round(b,2))
    plt.plot(x_,m_*x_+b,'r', label=lineEq+", R2=" +str(round(r_squared,2)))

    plt.legend(loc='upper left')

    jittered_y = y + 0.1 * np.random.rand(len(y)) -0.04
    jittered_x = x + 0.1 * np.random.rand(len(x)) -0.05
    plt.scatter(jittered_x,jittered_y,color='b',s=3)
    plt.ylabel('Interview')
    plt.xlabel('Referral')
    plt.ylim(ymax=1.3,ymin=-0.3)
    plt.xlim(xmax=1.3,xmin=-0.3)
    my_xticks=[0,1]
    my_yticks=[0,1]
    plt.xticks([my_xticks[0], my_xticks[-1]], visible=True, rotation="horizontal")
    plt.yticks([my_yticks[0], my_yticks[-1]], visible=True, rotation="horizontal")
    plt.title("{} Epi Type Correlation Referral vs. Interview".format(etype))
    plt.show()



##################################################################################################

#int vs chart
isThere={}
data=[]
epiTypes=['Epileptic Encephalopathy','Idiopathic generalized epilepsy','Non-acquired focal epilepsy',
'Lesional focal epilepsy']

for etype in epiTypes:
    chartDict={}
    for col in vals.columns:
        if col=="Cohort":
            
            for ind in vals.index:
                if vals[col][ind]=="ASD,Epi":
                    for col2 in vals.columns:
                        
                        if col2=="Subject ID":
                            pid=vals[col2][ind]
                            #eachProband.append(pid)
                        if col2=="Epi type (Chart)": 
                            if not isNaN(vals[col2][ind]) and "Unknown" not in vals[col2][ind] :
                                if ";" in vals[col2][ind]:
                                    new=vals[col2][ind].split(";")
                                    chartDict[pid]=new
                                    
                                else:
                                    chartDict[pid]=[vals[col2][ind]]

    
    for i in chartDict:
        
        for j in chartDict[i]:
            if j==etype:
                isThere[i]=[1]
                break
            else:
                isThere[i]=[0]

    intDict={}
    for col in vals.columns:
        if col=="Cohort":
            
            for ind in vals.index:
                if vals[col][ind]=="ASD,Epi":
                    for col2 in vals.columns:
                        
                        if col2=="Subject ID":
                            pid=vals[col2][ind]
                            #eachProband.append(pid)
                        if col2=="Epi type (Interview)": 
                            if not isNaN(vals[col2][ind]) and "Unknown" not in vals[col2][ind] :
                                if ";" in vals[col2][ind]:
                                    new=vals[col2][ind].split(";")
                                    intDict[pid]=new
                                    
                                else:
                                    intDict[pid]=[vals[col2][ind]]
               
    for i in intDict:
        if i in isThere:
            for j in intDict[i]:
                if j==etype:
                    isThere[i].append(1)
                    break
                else:
                    isThere[i].append(0)
                    break
    for i in isThere:
        if len(isThere[i])==1:
            isThere=removekey(isThere,i)
  
    x=[]
    y=[]
    for i in isThere:
        x.append(isThere[i][0]+0.1)
        y.append(isThere[i][1]+0.1)
    if all(y[v]==0 for v in range(0,len(y))):
        y[v]+=0.05
        x[v]+=0.05

    print(len(x))
        
    x_=np.array(x)
    y_=np.array(y)

    m_, b = np.polyfit(x_, y_, 1)
    correlation_matrix = np.corrcoef(x, y)
    correlation_xy = correlation_matrix[0,1]
    r_squared = correlation_xy**2

    if round(b,2)>0:

        lineEq="y="+str(round(m_,2))+"x+"+str(round(b,2))
    elif round(b,2)==0:
        lineEq="y="+str(round(m_,2))+"x"
    else:
        lineEq="y="+str(round(m_,2))+"x"+str(round(b,2))
    plt.plot(x_,m_*x_+b,'r', label=lineEq+", R2=" +str(round(r_squared,2)))

    plt.legend(loc='upper left')

    jittered_y = y + 0.1 * np.random.rand(len(y)) -0.05
    jittered_x = x + 0.1 * np.random.rand(len(x)) -0.05
    plt.scatter(jittered_x,jittered_y,color='b',s=3)
    plt.ylabel('Interview')
    plt.xlabel('Chart')
    plt.ylim(ymax=1.3,ymin=-0.3)
    plt.xlim(xmax=1.3,xmin=-0.3)
    my_xticks=[0,1]
    my_yticks=[0,1]
    plt.xticks([my_xticks[0], my_xticks[-1]], visible=True, rotation="horizontal")
    plt.yticks([my_yticks[0], my_yticks[-1]], visible=True, rotation="horizontal")
    plt.title("{} Epi Type Correlation Chart vs. Interview".format(etype))
    plt.show()

