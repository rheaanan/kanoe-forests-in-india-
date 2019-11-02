import csv 
import matplotlib.pyplot as plt
f = open("allforest.csv")
csv_f = csv.reader(f)

l =  list(csv_f)
n1 = []
n2 = []
n3 = []
n1new = []
n2new = []
n3new = []
for i in l:
	n1.append(i[0])
	n2.append(i[1])
	n3.append(i[2])
for j in range(1,len(n2),3):
	for k in range(0,3):
		n1new.append(n1[j+k])
		n2new.append(n2[j+k])
		n3new.append(n3[j+k])
	
	'''plt.plot(n2new,n3new,'-o')
	plt.gca().set_xlim(left=2005)
	plt.gca().set_xlim(right=2015)
	plt.show()'''		
	if(n1[0]==n1[1]==n1[2]):
		

		
	n2new = []
	n3new = []

	
		




