import csv
from operator import itemgetter



ifile=open('crash.csv','r')
reader=csv.DictReader(ifile)
default=0
i=0
total=0
dictModel={}
dictModelno={}
for row in reader:
	
	try:	
		
		if row['Type'] =='Douglas DC-3':
			
		
		
	

	except Exception as e:
		print(e)
		default+=1
		pass

	

for key,value in sorted(dictModel.items(),key=itemgetter(1),reverse=False)[:50]:
	print('key is '+str(key)+' value is '+str(value)+'no of timmes crashed is '+str(dictModelno[key]))


print('default value is '+str(default))
print('total value is '+str(total))
ifile.close()	
