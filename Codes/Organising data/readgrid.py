import csv
s = 'MeanT_'
t = '.TXT'

fi = s+'2013'+t
#print fi
txt = open(fi)
l = []
m = []
for line in txt:
	#print line
	l = line.strip().split(" ")
	nl=filter(lambda x: len(x)>0, l) 
	m.append(nl)
	l = []
	nl = []  
m2 = []
for i in m[1: ]:
	nl1 = []
	if(i[0]=='DTMTYEAR'): 
		m2.append(i)
		continue
	nl1= map((lambda x: float(x)),i)
	m2.append(nl1)

nf = open(fi+'1'+'.csv','w')
csv_w = csv.writer(nf,delimiter = ",")

for row in m2:
	csv_w.writerow(row)
	

