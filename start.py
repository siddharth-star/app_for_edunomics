import pandas as pd
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
def number(s):
    c=0
    k=0
    l=[]
    t=[]
    for i in s:
        if i.isdigit():
            l.append(i)
            c=1
        elif i=='x' and c==1:
            l.append(i)
        elif i=='-' and c==1 and k!=1:
            l.append(i)
            k=1
        else:
            t.append(i)
            
    return ("".join(l),''.join(t))
def company(dis,data,data2,name,num,s):
    dis=[]
    for i in range(len(data2['new'])):
        if (fuzz.WRatio(num,data2['Company Dscription'][i])>=85.0):
            if (fuzz.WRatio(s,data2['new'][i])>=85.0):
                dis.append(data['Distributor Item code'][i])

    with open('distributor.txt', 'w') as file_handler:
        file_handler.write(f"Distributor with has name {name}\n")
        for item in dis:
            file_handler.write("{}\n".format(item))
    print(len(dis))
def distributor(data,name):
    l=[]
    for i in range(len(data['Distributor Item code'])):
        if name==data['Distributor Item code'][i]:
            l.append(data['Company Dscription'][i])
    with open('company.txt', 'w') as file_handler:
        file_handler.write(f"Distributor deal with company {name}\n")
        for item in l:
            file_handler.write("{}\n".format(item))
    print(len(l))
    
    
data = pd.read_csv('sku.csv')
data2=pd.read_csv('new.csv')
data["Distributor Item code"].fillna("Not Define", inplace = True) 
# name='Abreza Dk 600x300'
name='KKWD 300x600-06 PLAIN IVORY-P'
num,s=number(name)

company(dis,data,data2,name,num,s)
# distributor(data,name)
