import csv
from operator import itemgetter
from geolocation.main import GoogleMaps

ifile=open('crash.csv','r')
reader=csv.DictReader(ifile)
default=0
google_maps = GoogleMaps(api_key='AIzaSyARs71g1TIgn9VYqK4xmdLN64AbwZxBXn0') 

total=0
listLat=[]
listLng=[]

for row in reader:
	
		try:	
			location = google_maps.search(location=row['Location'])
			my_location = location.first()
		
			listLat.insert(total,my_location.lat)
			listLng.insert(total,my_location.lng)
			total+=1
		except Exception as e:
			pass

print('completed')



with open('locationall.csv', 'w') as csvfile:
    fieldnames = ['latitude', 'longitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(total):
    	writer.writerow({'latitude': listLat[i], 'longitude': listLng[i]})
    
print('completed csv')