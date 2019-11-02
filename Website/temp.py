import csv
f1 = open('lol2.csv')
csv_f1 = csv.reader(f1)
l = []
for i in csv_f1:
	l.append(i[0])
l = set(l)
print(l)