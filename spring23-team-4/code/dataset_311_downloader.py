from bs4 import BeautifulSoup
import requests
import json
import re
import os
import pandas as pd

__311_dataset_URL = 'https://data.boston.gov/dataset/311-service-requests'


def download_datasets(verbose=False):

    parser = "html.parser"
    req = requests.get(__311_dataset_URL)
    contents = BeautifulSoup(req.text, parser).find("script", {"type": "application/ld+json"}).contents
    graph = json.loads("".join([str(x) for x in contents]))['@graph']

    sources = []

    for x in graph:
        if 'schema:url' not in x:
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
        if verbose:
            print(year)

        filename = f'../data/311 Service Request - {year}.csv'

        sources.append((year, filename))

        if os.path.exists(filename):
            if verbose:
                print('Existing, skipped\n')
            continue

        data = requests.get(url, allow_redirects=True)

        if verbose:
            print('Data retrieved')

        with open(filename, 'w') as file:
            file.write(data.text)

        if verbose:
            print('Data written\n')

    return [s for _, s in sorted(sources, key=lambda c: c[0])]


def download_and_load_datasets():
    sources = download_datasets()
    dataframes = [pd.read_csv(source) for source in sources]
    return pd.concat(dataframes)


if __name__ == '__main__':
    download_datasets(verbose=True)
