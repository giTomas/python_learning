# !/usr/bin/python

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'Californa': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print "-" * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

print "-" * 10
for state, abbrev in states.items():
    print "%s has the city %s" % (state, abbrev)

print "-" * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

print "-" * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

city = cities.get('TX', 'Does Not Exist')
print city
