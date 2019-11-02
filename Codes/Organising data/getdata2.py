import csv
import re
f2 = open('MeanT_2010.TXT.csv')
csv_f2 = csv.reader(f2)
lat = []

nf = open("2010.csv",'w')
csv_w = csv.writer(nf,delimiter = ",")

for i in csv_f2:
	lat.append(i[1])
nod = 31
l = list(set(lat))
#l = l[1: ]
pop = []
cnt = [0.0]*33
print cnt
print l
for k in range(1,13):
	if(k < 10):
		mon = '0'+str(k)
	for j in l:
		f2.seek(0)
		for i in csv_f2:
			
			z = re.match('..'+str(mon)+'2010',i[0])
			q = re.match('.'+str(mon)+'2010',i[0])
			o = (q or z)
			
			if(o and i[1] == j):
				if(k == 1 or k == 3 or k == 5 or k == 7 or k ==8 or k == 10 or k == 12):
						nod = 31
				elif(k == 2):
						nod = 28
				else:
						nod = 30
				for m in range(2,33):
					#print(m,i[m])
					cnt[m] = float(i[m]) + cnt[m]


				
				
		f2.seek(0)

		pop.append(k)
		pop.append(j)
		for g in cnt:
			pop.append(g/nod)
		csv_w.writerow(pop)
		cnt = [0.0]*33

		pop = []
		
	