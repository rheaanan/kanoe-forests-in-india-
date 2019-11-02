import csv
import re
f2 = open('2005.csv')
csv_f2 = csv.reader(f2)
l = []
k = []
lal = []
ll = []

for i in csv_f2:
	len = len(i)
	break
print len
f2.seek(0)


for j in range (2,len):
	f2.seek(0)

	for i in csv_f2:
		if(i[j] == 'LAT.'):
			break
		l.append(i[j])
	
	k.append(l)
	l = []
#k - list of columns
nf = open("2005n.csv",'w')
csv_w = csv.writer(nf,delimiter = ",")
f2.seek(0)
l2 = []
for i in csv_f2:
	l2.append(i[0])
	l2.append(i[1])
	ll.append(l2)
	l2 = []
# ll contains month and latitude 
ll = ll[1: ]
for i in ll:
	for j in k:
		lal.append(i[0])
		lal.append(i[1])
		for w in j:
			lal.append(w)
		#print i,j
		csv_w.writerow(lal)
	
		
	lal = []
	
		
	
'''ll = []
lal = []	
for i in csv_f2:
	ll.append(i[0])

for j in range(2,len):	
	for i in csv_f2:
		if(re.match('??012012'):
			cnt = i[j]+cnt
	cnt  = cnt /31
	
	lal[0].append(cnt)
	cnt = 0'''
	
	
	