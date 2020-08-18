#Purpose: Looks at the correlation between mri and DD by looking at percent of chart review complete population that has/doesn't have DD in each of the mri status categories
#Corresponding graphs: mriAnalysis.pdf page2
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

excel_file= "Minimal Phenotype Fields - Dev Window Fields Separated_071020.xlsx"
vals=pd.read_excel(excel_file, sheet_name=0)
subjects={}
def isNaN(num):
    return num != num
def delKey(subjects,val):
    del subjects[val]
    return subjects

def findValue(columnValue):
    ret=""
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
                                            if col2=="MRI status (Chart)":
                                                if not isNaN(vals[col2][ind]) and vals[col2][ind]!="Unknown":
                                                    #count+=1
                                                    for col3 in vals.columns:
                                
                                                        if col3== columnValue:
                                                            if not isNaN(vals[col3][ind]) and vals[col3][ind]!="Unknown":
                                                                ret=vals[col3][ind]
                                                                if sid in subjects and len(subjects[sid])==2:
                                                                    if subjects[sid][1]=="renew":
                                                                        subjects[sid][1]=ret
                                                                    
                                                                else:
                                                                    subjects[sid]=[vals[col2][ind],ret] 
                                                            else:
                                                                ret="renew"
                                                                subjects[sid]=[vals[col2][ind],ret]
                                                                
                                                                

                                                        
    # return ret                                                       



findValue("DD? (Chart)")
findValue("DD dx (Interview)")
# if value=="renew":
#     value=findValue("dd (Self Assess)")
subjects2={}
for i in subjects:
    if subjects[i][1]!="renew":
        subjects2[i]=subjects[i]
for i in subjects2:
    print(i,end=", ")
    print(subjects2[i]) 

labels=['Normal',"Abnormal","No Results","Awaiting"]
nodd=[]
dd=[]
ct=0
nct=0
dct=0
for i in subjects2:

    if subjects2[i][0]=='Normal':
        ct+=1
        if subjects[i][1]=="Yes":
            nct+=1
        elif subjects[i][1]=="No":
            dct+=1
nodd.append(nct/len(subjects2)*100)
dd.append(dct/len(subjects2)*100)
labels[0]+= " N= {}".format(ct)
nct=0
dct=0
ct=0
for i in subjects2:
    if subjects2[i][0]=='Abnormal':
        ct+=1
        if subjects2[i][1]=="Yes":
            nct+=1
        elif subjects2[i][1]=="No":
            dct+=1
nodd.append(nct/len(subjects2)*100)
dd.append(dct/len(subjects2)*100)
labels[1]+= " N= {}".format(ct)
nct=0
dct=0  
ct=0
for i in subjects2:
    
    if subjects2[i][0]=='No MRI results':
        ct+=1
        if subjects2[i][1]=="Yes":
            nct+=1
        elif subjects2[i][1]=="No":
            dct+=1
nodd.append(nct/len(subjects2)*100)
dd.append(dct/len(subjects2)*100)
labels[2]+= " N= {}".format(ct)
nct=0
dct=0 
ct=0
for i in subjects2:
    
    if subjects2[i][0]=='Awaiting results':
        ct+=1
        if subjects2[i][1]=="Yes":
            nct+=1
        elif subjects2[i][1]=="No":
            dct+=1
nodd.append(nct/len(subjects2)*100)
dd.append(dct/len(subjects2)*100)
labels[3]+= " N= {}".format(ct)


# nodd.append(nct/len(subjects2)*100)
# dd.append(dct/len(subjects)*100)
   
        



x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, nodd, width, label='no DD')
rects2 = ax.bar(x + width/2, dd, width, label='DD')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('%')
ax.set_title('MRI vs DD N={}'.format(len(subjects2)))
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        height=round(height, 2)
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

ax.set_ylim(0, 100)
fig.tight_layout()

plt.show()                                               