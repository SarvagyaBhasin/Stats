import csv
with open('HeightWeight.csv', newline='')as f:
    r=csv.reader(f)
    df=list(r)

df.pop(0)
height=[]
weight=[]
totalheight, totalweight=0,0
count=0
for i in range(len(df)):
    height.append(float(df[i][1]))
    weight.append(float(df[i][2]))
    count+=1

for i in height:
    totalheight+=i 

for i in weight:
    totalweight+=i 

meanheight=totalheight/count
meanweight=totalweight/count
print("Average height: ", meanheight)
print("Average weight: ", meanweight)