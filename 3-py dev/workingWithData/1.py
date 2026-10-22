#import needed modules and data
import csv

columns=["bookId","name","author","year"]
fileName="bookStore.csv"
newData=[]
oldData=[]         

#load old data
with open(fileName,"r"):     
    reader=csv.DictReader(fileName)

#save old data 
for i in reader:
    oldData.append(dict(i))

#check the current ID and create new ID     
if len(oldData)>0:
    currentID=oldData[-1].get("bookId")        #({id:"xv001",name:"vikash",age:19,country:"LK"},{id:"xv002",name:"piyu",age:16,country:"LK"})
    newId=int(currentID)+1


    


    
    




