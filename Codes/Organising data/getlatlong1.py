import csv
f2 = open('latlonggg.csv')
csv_f2 = csv.reader(f2)

nf = open("latlong2.csv",'w')
csv_w = csv.writer(nf,delimiter = ",")

lolal = []
l = []
for i in csv_f2:

	if('.' in i[1] and '.' in i[2]):
		i1=i[1].split('.')
		f1=i1[0]
		f1=int(f1)
		s1=float(i1[1])
		s1 = s1/60
		res1 = f1+s1
		res1 = round(res1,2)
		
		
		i2=i[2].split('.')
		f2=i2[0]
		f2=int(f2)
		print(i2[1])
		s2=float(i2[1])
		s2 = s2/60
		res2 = f2+s2
		res2 = round(res2,2)
		

		l.append(i[0])
		l.append(res1)
		l.append(res2)
		csv_w.writerow(l)
	
	elif('.' in i[1] and '.' not in i[2]):
		i1=i[1].split('.')
		f1=i1[0]
		f1=int(f1)
		s1=float(i1[1])
		s1 = s1/60
		res1 = f1+s1
		res1 = round(res1,2)
		f2=i[2]
		f2=int(f2)

		l.append(i[0])
		l.append(res1)
		l.append(f2)
		csv_w.writerow(l)

	elif('.' not in i[1] and '.' in i[2]):
		f1=i1[0]
		f1=int(f1)

		i2=i[2].split('.')
		f2=i2[0]
		f2=int(f2)
		s2=float(i2[1])
		s2 = s2/60
		res2 = f2+s2
		res2 = round(res2,2)


		l.append(i[0])
		l.append(f1)
		l.append(res2)
		csv_w.writerow(l)



	else:
		f1=i[1]
		f1=int(f1)
		f2=i[2]
		f2=int(f2)
		l.append(i[0])

		l.append(f1)
		l.append(f2)
		csv_w.writerow(l)
		



	l=[]

		


	
