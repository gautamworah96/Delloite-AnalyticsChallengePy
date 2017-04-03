import csv
from operator import itemgetter

ifile=open('crash.csv','r')
reader=csv.DictReader(ifile)
default=0
i=0
total=0
dictModel={}
for row in reader:
	
	try:	
		
		if row['Operator'] in dictModel:
			dictModel[row['Operator']]+=int(row['Fatalities'])
			#dictModelno[row['Type']]+=1
		else:
			dictModel[row['Operator']]=int(row['Fatalities'])
			#dictModelno[row['Type']]=1
	
		total=total+1
	

	except Exception as e:
		print(e)
		default+=1
		pass

'''for key,value in dictModel.items():
	dictModel[key]=dictModel[key]/dictModelno[key];'''
	

for key in sorted(dictModel.items(),key=itemgetter(1),reverse=True)[:20]:
	try:
		print('key is '+str(key)+' value is '+str(dictModel[key]))
	except Exception as e:
		print(e)
		pass


print('default value is '+str(default))
print('total value is '+str(total))
ifile.close()	
