import os
import csv

file1=os.path.join('election_data_1.csv')
file2=os.path.join('election_data_2.csv')

cand=[]

with open(file1,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
#    print(csvreader)
    next(csvreader)
    for row in csvreader:
        cand.append(row[2])

with open(file2,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
#    print (csvreader)
    next(csvreader)
    for row in csvreader:
        cand.append(row[2])
poll={}
for i in range(0,len(cand)):
    if cand[i] in poll.keys():
        poll[cand[i]]+=1
    else:
        poll[cand[i]]=1


#1 Total number of votes
tvotes=len(cand)

#2 Complete list of candidates
candidates=[]
for key in poll.keys():
    candidates.append(key)

#3 Percentage
perc={}
for key in poll.keys():
    perc[key]=poll[key]/tvotes

#4 Total votes for each already stored
#5 The winner
voice=0
winner=''
for key in poll.keys():
    if poll[key]>voice:
        voice=poll[key]
        winner=key

print("Election Results")
print("----------------")
print("Total Votes: "+str(tvotes))
print("----------------")
for key in perc.keys():
    print(key+':  '+str("%.2f" % (perc[key]*100))+'%   ('+str(poll[key])+')')
print("----------------")
print("Winner: "+winner)

output_path=os.path.join('results.csv')
with open(output_path,'w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=',')
    csvwriter.writerow(['Candidate','Percentage','Voice count'])
    for key in perc.keys():
        csvwriter.writerow([key,str("%.2f" % (perc[key]*100)),str(poll[key])])

