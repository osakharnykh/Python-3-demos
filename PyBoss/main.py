import os
import csv

file1=os.path.join('employee_data1.csv')
file2=os.path.join('employee_data1.csv')

empid=[]
name=[]
dob=[]
ssn=[]
state=[]

with open(file1,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader)
    for row in csvreader:
        empid.append(row[0])
        name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])
#    print(csvreader)
with open(file2,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader)
    for row in csvreader:
        empid.append(row[0])
        name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])
#    print(csvreader)

#Name split

first=[]
last=[]
for i in range (0, len(name)):
    namedata=name[i].split(' ')
    first.append(namedata[0])
    last.append(namedata[1])

#DOB format
dob_new=[]
for i in range (0,len(dob)):
    dobdata=dob[i].split('-')
    dob_new.append(dobdata[2]+'/'+dobdata[1]+'/'+dobdata[0])

#SSN format
ssn_new=[]
for i in range(0,len(ssn)):
    ssndata=ssn[i].split('-')
    ssn_new.append('***-**-'+ssndata[2])

#State
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
state_new=[]
for i in range(0,len(state)):
    state_new.append(us_state_abbrev[state[i]])


#Export

output_path=os.path.join('results.csv')
with open(output_path,'w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=',')
    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
    for i in range(0,len(empid)):
        csvwriter.writerow([empid[i],first[i],last[i],dob_new[i],ssn_new[i],state_new[i]])
        
    
