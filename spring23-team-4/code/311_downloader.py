from bs4 import BeautifulSoup
import requests
import json
import re
import os


def get_ld_json(url: str) -> dict:
    parser = "html.parser"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, parser)
    return json.loads("".join(soup.find("script", {"type":"application/ld+json"}).contents))


def download_datasets():
    for x in get_ld_json('https://data.boston.gov/dataset/311-service-requests')['@graph']:
        if not 'schema:url' in x:
            continue
        url = x['schema:url']
        if not url[-3:] == 'csv':
            continue

        m = re.search('20\d\d', url.split('/')[-1])

        if not m:
            m = re.search('20\d\d', x['schema:name'])

            if not m:
                print(x)
                return False

        year = m.group()
        print(year)

        filename = f'../data/311 Service Request - {year}.csv'

        if os.path.exists(filename):
            print('Existing, skipped\n')
            continue

        data = requests.get(url, allow_redirects=True)

        print('Data retrieved')

        with open(filename, 'w') as file:
            file.write(data.text)

        print('Data written\n')


download_datasets()
