import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
excel_file='Minimal Phenotype Fields - Dev Window Fields Separated_2020-05-28.xlsx'
vals=pd.read_excel(excel_file, sheet_name=0)
def isNaN(num):
    return num != num


data=[]
for ind in vals.index:
    pid=""
    eachProband=[]
    for col2 in vals.columns:
        
        if col2=="Subject ID":
            pid=vals[col2][ind]
            eachProband.append(pid)
        if col2=="Proband's Epi type (Referral)": 
            if not isNaN(vals[col2][ind]) and "Unknown" not in vals[col2][ind] :
                if ";" in vals[col2][ind]:
                    new=vals[col2][ind].split(";")
                    for i in new:

                        eachProband.append(i)
                else:
                    eachProband.append(vals[col2][ind])
        elif col2=="Epi type (Interview)" :
            if not isNaN(vals[col2][ind]) and "Unknown" not in vals[col2][ind] :
                if ";" in vals[col2][ind]:
                    new=vals[col2][ind].split(";")
                    for i in new:

                        eachProband.append(i)
                else:
                    eachProband.append(vals[col2][ind])
        elif col2=="Epi type (Chart)" :
            if not isNaN(vals[col2][ind]) and "Unknown" not in vals[col2][ind] :
                if ";" in vals[col2][ind]:
                    new=vals[col2][ind].split(";")
                    for i in new:

                        eachProband.append(i)
                else:
                    eachProband.append(vals[col2][ind])
    #print(eachProband)
    # if len(eachProband)>1:
    #     for y in eachProband[1:]:
    #         if "Other" in y:
    #             y="Other"
    #         z=(eachProband[0],y)
    #         data.append(z)
    if len(eachProband)>1:
        for y in eachProband[1:]:
            if "Other" in y:
                y="Other"
        l=eachProband[1:]
        myset = set(l)
        if len(myset)==1:
            z=(eachProband[0],1)
            data.append(z)
        else:
            z=(eachProband[0],len(myset))
            data.append(z)


            
     
subjects=[]
for i in data:
    if(i[1]>=3):
        subjects.append(i[0])
        print(i[0])

xval=[x[0] for x in data]
yval=[x[1] for x in data]
plt.scatter(xval,yval,s=5)

plt.xticks(np.arange(min(xval), max(xval)+20, 20.0),rotation=90)
plt.title("Recorded Epi Type Frequency for each Proband")

plt.show()