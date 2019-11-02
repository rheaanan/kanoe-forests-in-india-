import csv
f1 = open('lol2.csv')
csv_f1 = csv.reader(f1)
l = []
for i in csv_f1:
	l.append(i[0])
l = list(set(l))
l.sort()
print(l)
for i in l :
	t = "<option value="+"'"+i+"'"+">"+i+"</option>"
	print t



#<option value="Northernmountains">Northern Mountains</option>