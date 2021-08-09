import csv

def get_column(tab, num):
    result = []
    for row in tab:
        try:
            result.append(float(row[num]))
        except:
            print("Info: can't parse to numeric: ", row[num], " skipping")
    return result

def get_csv(filename):
    with open(filename, newline='') as csvfile:
        csvdata= csv.reader(csvfile, delimiter=',', quotechar='\n')
        table =[ ]
        for row in csvdata:
            table.append(row)
    return table