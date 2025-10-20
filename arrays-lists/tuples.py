import collections
#Tuples are an inmmutable list that hold records
lax_coordinates = (33.9425,-118.408056)
city,year,pop,chg,area = ('Toyko', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA','CE342567'), ('ESP','XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)


#Tuple unpacking
lat,long = lax_coordinates
print(lat)
print(long)

#Use * to grab excess items as a list
a,b, *body, c = range(48)
print(a)
print(b)
print(body)
print(c)

#Named Tuples produce subclasses of tuples enhanced with field names and a class name
City = collections.namedtuple('City', 'name country population coordinates')
toyko = City('Toyko','JP', 36.933, (35.689722, 139.691667))
print(toyko)
print(toyko.population)

