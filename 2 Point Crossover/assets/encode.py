import csv
l =[]
lb=[]

with open('iothingslocationdata.csv','r')as file:
    reader = csv.reader(file)
    for row in reader:
        l.append(row)
        #print(row)
for i in range(len(l)):
    for j in range(len(l[0])):
        lb.append(''.join(format(i, '08b') for i in bytearray(l[i][j], encoding ='utf-8')))


with open('iotsample_encoded.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(lb)
print("File converted to Binary")
