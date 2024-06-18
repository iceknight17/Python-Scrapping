import csv

def checkStr(str):
   return str if str else '-'

with open('ech0.csv', 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    
    results = []
    count = 0
    for row in csv_reader:
        count += 1
        filteredRow = []
        filteredRow = [
            checkStr(row[0]),
            checkStr(row[1]),
            checkStr(row[6]), # mailing street
            checkStr(row[7]), # mailing city
            checkStr(row[8]), # mailing state
            checkStr(row[9]), # mailing zip
            checkStr(row[10]), # mailing country
            checkStr(row[16]), # phone
            checkStr(row[20]), # email
            checkStr(row[40]), # DOB not matched
            checkStr(row[70]), # ssn full
            checkStr(row[71]), # ssn last 5
        ]
        if not any(item == '-' for item in filteredRow):
            results.append('|'.join(filteredRow))
        if(count%100 == 0):
            with open('result.txt', 'a', encoding='utf-8') as file:
                file.write('\n'.join(results) + '\n')
                results = []
    with open('result.txt', 'a', encoding='utf-8') as file:
        file.write('\n'.join(results))
    print(count)