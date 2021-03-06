import csv
l = []
lb = []
with open('assets/binary.csv','r')as file:
    reader = csv.reader(file)
    for row in reader:
        l.append(row)

l = list(l[0])

l1 = list(l[:len(l)//2])
l2 = list(l[len(l)//2:])

out1 = list()
out2 = list()
iter_limit = min(len(l1), len(l2))

for i in range(0, iter_limit):
    var1 = list(l1[i])
    var2 = list(l2[i])

    ostr1 = str()
    ostr2 = str()
    
    for j in range(2, min(len(l1[i]), len(l2[i])), 8):    ## 01001011
        tmp = var1[j]
        var1[j] = var2[j]
        var2[j] = tmp

    for j in range(3, min(len(l1[i]), len(l2[i])), 8):
        tmp = var1[j]
        var1[j] = var2[j]
        var2[j] = tmp

    for j in range(5, min(len(l1[i]), len(l2[i])), 8):
        tmp = var1[j]
        var1[j] = var2[j]
        var2[j] = tmp

    for j in range(7, min(len(l1[i]), len(l2[i])), 8):
        tmp = var1[j]
        var1[j] = var2[j]
        var2[j] = tmp

    for items in var1:
        ostr1 += items
    for items in var2:
        ostr2 += items

    out1.append(ostr1)
    out2.append(ostr2)

if(len(l1) != len(l2)):
    out2.append(l2[iter_limit])

with open('assets/cross_out.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(out1)
with open('assets/cross_out2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(out2)
print("crossover done")
