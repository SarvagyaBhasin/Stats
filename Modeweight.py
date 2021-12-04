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

d=Counter(weight)
modeforrange={"75-85": 0, "85-95": 0, "95-105": 0,"105-115": 0, "115-125": 0, "125-135": 0, "135-145": 0, "145-155": 0, "155-165": 0, "165-175": 0}
for h, occurence in d.items():
    if 75<h<85: 
        modeforrange["75-85"]+=occurence
    elif 85<h<95:
        modeforrange["85-95"]+=occurence
    elif 95<h<105:
        modeforrange["95-105"]+=occurence
    elif 105<h<115:
        modeforrange["105-115"]+=occurence
    elif 115<h<125:
        modeforrange["115-125"]+=occurence
    elif 125<h<135:
        modeforrange["125-135"]+=occurence
    elif 135<h<145:
        modeforrange["135-145"]+=occurence
    elif 145<h<155:
        modeforrange["145-155"]+=occurence
    elif 155<h<165:
        modeforrange["155-165"]+=occurence
    elif 165<h<175:
        modeforrange["165-175"]+=occurence

moderange, modeoccurence=0, 0
for range, occurence in modeforrange.items():
    if occurence>modeoccurence:
        moderange, modeoccurence=[int(range.split("-")[0]), int(range.split("-")[1])], occurence

mode=float((moderange[0]+moderange[1])/2)
print ("Mode for weight: ", mode)