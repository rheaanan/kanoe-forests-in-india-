import csv

f1 = open('latlong1.csv')
csv_f1 = csv.reader(f1)

nf = open('append1.csv','w')
csv_w = csv.writer(nf,delimiter = ",")

for i in csv_f1:
	print i
	if('.' not in i[1]):
		i[1] = int(i[1])+0.5
	if('.' not in i[2]):
		i[2] = int(i[2]) + 0.5
	
	csv_w.writerow(i)