import csv
l = []
lb = []
# interim = []

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

    for j in range(2, min(len(l1[i]), len(l2[i])), 8):
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

    for j in range(6, min(len(l1[i]), len(l2[i])), 8):
        tmp = var1[j]
        var1[j] = var2[j]
        var2[j] = tmp

    for items in var1:
        ostr1 += items
    for items in var2:
        ostr2 += items
    
    out1.append(ostr1)
    out2.append(ostr2)
        # print(row)
# for i in range(len(l)):
#     for j in range(len(l[0])):
#         # interim.append(''.join(format(i, '08b') for i in bytearray(l[i][j], encoding ='utf-8')))
    
#         #var = ('1''0''1''0') | ('1010')
#         var = list(l[i][j])
#         out = str()
#         for h in range(2, len(var), 16):
#             try:
#                 tmp = var[h]
#                 var[h] = var[h+8]
#                 var[h+8] = tmp
#             except IndexError:
#                 if(var[h] == '0'):
#                     var[h] = '1'
#                 else:
#                     var[h] = '0'
#                 break
#         for v in range(3, len(var), 16):
#             try:
#                 tmp = var[h]
#                 var[h] = var[h+8]
#                 var[h+8] = tmp
#             except IndexError:
#                 if(var[v] == '0'):
#                     var[v] = '1'
#                 else:
#                     var[v] = '0'
#                 break
#         for s in range(5, len(var), 16):
#             try:
#                 tmp = var[h]
#                 var[h] = var[h+8]
#                 var[h+8] = tmp
#             except IndexError:
#                 if(var[s] == '0'):
#                     var[s] = '1'
#                 else:
#                     var[s] = '0'
#                 break
#         for a in range(7, len(var), 16):
#             try:
#                 tmp = var[h]
#                 var[h] = var[h+8]
#                 var[h+8] = tmp
#             except IndexError:
#                 if(var[a] == '0'):
#                     var[a] = '1'
#                 else:
#                     var[a] = '0'
#                 break
#         for items in var:
#             out += items
#         lb.append(out)

# # print(lb[0])

with open('cross_out.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(l1)
with open('cross_out2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(l2)
print("crossover done")
