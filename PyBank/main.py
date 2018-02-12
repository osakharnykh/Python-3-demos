import os
import csv

file2=os.path.join('budget_data_1.csv')
file1=os.path.join('budget_data_2.csv')

dates=[]
rev=[]

with open(file1,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
#    print (csvreader)
    next(csvreader)
    for row in csvreader:
        dates.append(row[0][0:4]+row[0][6:8])
        rev.append(int(row[1]))

with open(file2,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
#    print (csvreader)
    next(csvreader)
    for row in csvreader:
        dates.append(row[0])
        rev.append(int(row[1]))

budget={}
for i in range(0,len(dates)):
    if dates[i] in budget.keys():
        budget[dates[i]]+=rev[i]
    else:
        budget[dates[i]]=rev[i]

#1 Total months
#2 Total revenue
m_sum = 0
rev_sum=0
for key, value in budget.items():
    m_sum+=1
    rev_sum+=value

#3 Average change

av_ch=(budget[dates[-1]]-budget[dates[0]])/(m_sum-1)
    
#4 Greatest Increase
#5 Greatest Decrease

gr_inc=0
gr_dec=0
m_inc=''
m_dec=''

dates1=[]
rev1=[]

for key, value in budget.items():
    dates1.append(key)
    rev1.append(value)

for i in range(0,len(rev1)-1):
    if rev1[i+1]-rev1[i]>gr_inc:
        gr_inc=rev1[i+1]-rev1[i]
        m_inc=dates1[i+1]
    if rev1[i+1]-rev1[i]<gr_dec:
        gr_dec=rev1[i+1]-rev1[i]
        m_dec=dates[i+1]

print("Financial Analysis")
print("------------------")
print("Total months:  "+str(m_sum))
print("Total revenue:  $"+str(rev_sum))
print("Average revenue change:  $"+str(int(av_ch)))
print("Greatest increase in revenue:   "+str(m_inc)+"  $"+str(gr_inc))
print("Greatest decrease in revenue:   "+str(m_dec)+"  $"+str(gr_dec))

output_path=os.path.join('results.csv')
with open(output_path,'w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=',')
    csvwriter.writerow(['Total months',str(m_sum)])
    csvwriter.writerow(['Total revenue',str(rev_sum)])
    csvwriter.writerow(['Average revenue change',str(int(av_ch))])
    csvwriter.writerow(['Greatest increase',str(m_inc),str(gr_inc)])
    csvwriter.writerow(['Greatest decrease',str(m_dec),str(gr_dec)])
    
