import csv,os
os.makedirs('headerRemoved',exist_ok=True)
for filename in os.listdir():
    if not filename.endswith('.csv'):
        continue
    rows = []
    csvFile = open(filename, 'r')
    readerObj = csv.reader(csvFile)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        rows.append(row)
    csvFile.close()
    csvwriteFile = open(os.path.join('headerRemoved', filename),'w',newline='')
    writer=csv.writer(csvwriteFile)
    for row in rows:
        writer.writerow(row)
    csvwriteFile.close()