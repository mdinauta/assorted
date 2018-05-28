# This script accesses the schema (the names and data types of every field) of a Salesforce object via the API and writes it to a .csv file. 
# Alternatively, you can print the schema to the terminal.
# There is no way to download or export a schema via the Salesforce UI, so this script can be quite handy.
# It uses the beatbox module to connect to the Salesforce API - see https://code.google.com/p/salesforce-beatbox/.

import beatbox
import csv

sf = beatbox.PythonClient()
sf.login(
	# <username>,
	# <password + security token>
	)

list_of_objects = sf.describeSObjects('account') # Change 'account' to any object
targetObject = list_of_objects[0]
objectFields = targetObject.fields # objectFields will be a dict with the field name strings as keys, and describeSOjectResult objects as values

'''
If you want to print schema to the console:

for k, v in accountFields.iteritems():
	print k + v.type

and comment everything below
'''

# If you want to write schema to a .csv:

out = csv.writer(open('out.csv', 'w'))

schema = {}
for k,v in objectFields.iteritems():
	schema[k] = v.type

for field in schema:
	out.writerow([field, schema[field]])
