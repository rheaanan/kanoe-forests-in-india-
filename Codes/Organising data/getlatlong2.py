import csv
f2 = open('india.csv')
csv_f2 = csv.reader(f2)

nf = open("latlonggg.csv",'w')
csv_w = csv.writer(nf,delimiter = ",")

lolal = []
lal = []
for i in csv_f2:
	f = i[1][ :-5] 
	s = i[1][3:-2] 
	lal.append(i[0])
	lal.append(f+'.'+s)
	f = i[2][ :-5] 
	s = i[2][3:-2]
	lal.append(f+'.'+s)
	csv_w.writerow(lal)
	lal = []


	