import csv
from operator import itemgetter

ifile=open('crash.csv','r')
reader=csv.DictReader(ifile)
default=0
i=0
totalOp=0
totalDoug=0
sum=0
dictModel={}
for row in reader:
	
	try:	
		
		if 'Douglas DC-3'==row['Type']:
			if row['Operator'] in dictModel: 
				dictModel[row['Operator']]+=1
				#dictModelno[row['Type']]+=1
				
			else:
				dictModel[row['Operator']]=1
				#dictModelno[row['Type']]=1
				totalOp=totalOp+1
			totalDoug+=1
	

	except Exception as e:
		print(e)
		default=default+1
		pass

'''for key,value in dictModel.items():
	dictModel[key]=dictModel[key]/dictModelno[key];'''
	
mean=float(totalDoug/totalOp);
for key in dictModel:
	sum=sum+float(((dictModel[key]-mean)**2.0)/totalOp)


print('mean value is '+str(mean))
print('totalOp value is '+str(totalOp))
print('variance is '+str(sum))

print('doug value is '+str(totalDoug))
ifile.close()	
