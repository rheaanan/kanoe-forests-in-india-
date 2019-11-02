import csv

f1 = open('append1.csv')
csv_f1 = csv.reader(f1)

f2 = open('2007try.csv')
csv_f2 = csv.reader(f2)

nf = open('try.csv','w')
csv_w = csv.writer(nf,delimiter = ",")

l = []

for i in csv_f2:
	for j in csv_f1:
		
		if(i[0] == j[1] and i[1] == j[2]):
			print j[0]
			l.append(j[0])
			l.append(i[0])
			l.append(j[1])
			l.append(i[1])
			l.append(j[2])
			for k in range(2,14):
				l.append(i[k])
			csv_w.writerow(l)
		l = []
			
	f1.seek(0)