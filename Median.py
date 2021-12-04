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

height.sort()
weight.sort()
if count %2==0:
    Hm1=height[count//2]
    Wm1=weight[count//2]
    Hm2=height[count//2-1]
    Wm2=weight[count//2-1]
    medianheight=(Hm1+Hm2)/2
    medianweight=(Wm1+Wm2)/2
else: 
    medianheight=height[n//2]
    medianweight=weight[n//2]

print("Median height: ", medianheight)
print("Median weight: ", medianweight)