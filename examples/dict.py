from collections import defaultdict

cities = {'San Francisco': 'US', 'London':'UK',
        'Manchester':'UK', 'Paris':'France',
        'Los Angeles':'US', 'Seoul':'Korea'}

print(cities)
d=defaultdict(list)
for city, country in cities.items():
    d[country].append(city)

print(d)