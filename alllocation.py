import csv
from operator import itemgetter
from geolocation.main import GoogleMaps

ifile=open('crash.csv','r')
reader=csv.DictReader(ifile)
default=0
google_maps = GoogleMaps(api_key='AIzaSyARs71g1TIgn9VYqK4xmdLN64AbwZxBXn0') 
error=0
breakvar=0
total=0
listLat=[]
listLng=[]
csvfile=open('sandend.csv', 'w')
fieldnames = ['slatitude', 'slongitude','elatitude','elongitude']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

writer.writeheader()

for row in reader:
	
		try:	
			location1 = google_maps.search(location=((row['Route']).split('-'))[0])
			my_location1 = location1.first()
			location2 = google_maps.search(location=((row['Route']).split('-'))[1])
			my_location2 = location2.first()


			writer.writerow({'slatitude': my_location1.lat, 'slongitude': my_location1.lng,'elatitude':my_location2.lat,'elongitude':my_location2.lng})

			total+=1
			if breakvar>20:
				break
			breakvar+=1
			print(total)

		except Exception as e:
			error+=1
			pass

print('completed')
print('error is '+str(error))
print('total is '+str(total))