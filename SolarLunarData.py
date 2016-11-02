import datetime
import urllib2

bodies = {
	"Sun": 10,
	"Moon": 11
}

location = raw_input("Please enter your desired location: ").split(',')
place = location[0].strip()
state = location[1].strip()
time_interval = raw_input("Please enter desired time interval: (minutes) ").split(' ')
interval = time_interval[0]
body = raw_input("Please enter desired celestial body: (Sun/Moon) ")

date = str(datetime.date.today()).split('-')

URL = "http://aa.usno.navy.mil"
endpoint = "/cgi-bin/aa_altazw.pl?form=1&body=%s&year=%s&month=%s&day=%s&intv_mag=%s&state=%s&place=%s" % \
			(bodies[body], date[0], date[1], date[2], interval, state, place)

print ""
print "RETRIEVING FROM..."
print URL+endpoint

content = urllib2.urlopen(URL+endpoint)

data = []
record = False
for line in content:
	if "</pre>" in line: #end of data
		record = False
	if record:
		data.append(line.strip())
	if "h  m         o           o" in line: #start of data
		record = True
content.close()

print "DONE!"

data = filter(None, data)

for i in range(len(data)):
	datum_lst = data[i].split(' ')
	datum_lst = filter(None, datum_lst)
	data[i] = datum_lst

print ""
print "DATA FORMAT:"
print ["Central Daylight Time (hrs:mins)", "Altitude (degrees), Azimuth  (degrees)"] 

raw_input("")
for line in data:
	print line

#print data

#print content.read()