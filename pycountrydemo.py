import pycountry
import csv
from operator import itemgetter

dict={}
dictpercent={}
list2=[]

for i in range(249):
	country=list(pycountry.countries)[i]
	dict[country.name]=0
	list2.insert(i,country.name)
list3 = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado',
         'Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho', 
         'Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
         'Maine' 'Maryland','Massachusetts','Michigan','Minnesota',
         'Mississippi', 'Missouri','Montana','Nebraska','Nevada',
         'New Hampshire','New Jersey','New Mexico','New York',
         'North Carolina','North Dakota','Ohio',    
         'Oklahoma','Oregon','Pennsylvania','Rhode Island',
         'South  Carolina','South Dakota','Tennessee','Texas','Utah',
         'Vermont','Virginia','Washington','West Virginia',
         'Wisconsin','Wyoming']
#print('over')
#print(dict)

list2=list2+list3
print(list2)

print(len(list2))


i=249
while i < 298:
	dict[list2[i]]=0
	i+=1

print(dict)
ifile=open('crash.csv','r')
reader=csv.DictReader(ifile)
total=0
default=0
dicthr={'250':0}
i=0
notmatched=0


print('now going for string matching')

for row in reader:
	
	for country in list2:
		
		if country in row['Location']:
			dict[country]+=1
			total+=1
			break

		
	else:
		notmatched+=1
		
print('now printing dict \n ')
print(dict)
totalpercent=0
for country in list2:
	dictpercent[country]=dict[country]/total
	totalpercent=totalpercent+dictpercent[country]
print('\n')
print(dictpercent)
print('\n')
print('printing totalpercent '+ str(totalpercent))
print('printing total '+ str(total))
print('value of not matched is  \n'+ str(notmatched))
 
for key,value in sorted(dictpercent.items(),key=itemgetter(1),reverse=True)[:50]:
	print('key is '+key+' value is '+str(value*100))

'''while i < 25:
	dicthr[i]=0
	i+=1

for row in reader:
	try:
		print (int((row['Time'])[0:2]))
		i=1
		while i < 25:
			if(int((row['Time'])[0:2])<i):
				dicthr[i]+=1
				total+=1
				i=25
			i+=1

	except Exception as e:
		print(e)
		default+=1
		pass

print(dicthr)
print(default)
print(total)

for key,value in sorted(dicthr.items(),key=itemgetter(1),reverse=True)[:24]:
	print('key is '+str(key)+' value is '+str(value))


'''
ifile.close()			

