import csv

def get_column(tab, num):
    result = []
    for row in tab:
        try:
            result.append(float(row[num]))
        except:
            print("error", row[num])
    return result

def get_csv(filename):
    with open(filename, newline='') as csvfile:
        csvdata= csv.reader(csvfile, delimiter=',', quotechar='\n')
        table =[ ]
        for row in csvdata:
            table.append(row)
    return table