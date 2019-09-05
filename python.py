# =============== imports ==================================
import requests
import csv
import pandas as pd

# ================ Query ======================================

url = "http://inqstatsapi.inqubu.com/?api_key=7d39fbc067d21a0f&cmd=getWorldData&data=population&year=2000"

response = requests.get(url)

json_data = response.json()

# print 'json_data[0].keys()', json_data[0].keys()

df = pd.DataFrame(json_data)


# ================== from json -> csv write ===================

fileToShow = open('country-info.csv', 'w')

output_to_csv = csv.writer(fileToShow)  # create a csv.write

fields = json_data[0].keys()  # fields

output_to_csv.writerow(fields)  # Header row

for row in json_data:

    # print row.values()

    output_to_csv.writerow(row.values())  # Values row
