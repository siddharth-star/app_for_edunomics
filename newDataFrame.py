import pandas as pd
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

data = pd.read_csv('sku.csv',)
data["Distributor Item code"].fillna("Not Define", inplace = True) 
data['new']=data['Company Dscription']
for i in range(len(data["Company Dscription"])):
    data["Company Dscription"][i],data['new'][i]=number(data["Company Dscription"][i])
data.to_csv('new.csv')
print('done')