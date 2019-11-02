import csv

f2 = open('2005.csv')
csv_f2 = csv.reader(f2)
l = []
m = []
for i in csv_f2:
	l.append(i)

m = l[0]
l = l[1: ]

nf = open("2005try.csv",'w')
csv_w = csv.writer(nf,delimiter = ",")

ll = []

for i in l:
		for k in range(2,33):
			ll.append(i[0])
			ll.append(i[1])
			ll.append(m[k])
			ll.append(i[k])
			csv_w.writerow(ll)
			ll = []

	