import csv
from collections import Counter
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

d=Counter(height)
modeforrange={"50-60": 0, "60-70": 0, "70-80": 0}
for h, occurence in d.items():
    if 50<h<60: 
        modeforrange["50-60"]+=occurence
    elif 60<h<70:
        modeforrange["60-70"]+=occurence
    elif 70<h<80:
        modeforrange["70-80"]+=occurence

moderange, modeoccurence=0, 0
for range, occurence in modeforrange.items():
    if occurence>modeoccurence:
        moderange, modeoccurence=[int(range.split("-")[0]), int(range.split("-")[1])], occurence

mode=float((moderange[0]+moderange[1])/2)
print ("Mode for height: ", mode)