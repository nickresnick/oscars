import numpy as np
import scipy as sp
from sklearn import ensemble
import imdb
import pandas as pd

from bs4 import BeautifulSoup as bsoup
import urllib2

def pull_tables(url):
    header = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(url, headers=header)
    page = urllib2.urlopen(req)
    soup = bsoup(page)
    tables = soup.find_all("table", {"class": "wikitable"})
    film = []
    for table in tables:
        film.append(table.findAll('a')[0].contents[0])
        new = []
        for row in table.findAll('tr'):
            cells = row.findAll('td')
            if len(cells) == 3:
                new.append(cells[0].find(text=True))
        film.append(new)
    return film

def pull_table(url):
    header = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(url, headers=header)
    page = urllib2.urlopen(req)
    soup = bsoup(page)
    table = soup.find_all("table", {"class": "wikitable sortable"})[0]
    film = []
    table = table.findAll('tr')[1:len(table.findAll('tr'))]
    for row in table:
        if len(row.findAll('th')) > 0:
            film.append(row.find('th').findAll('a')[0].contents[0])
            new = []
            for col in row.findAll('a')[2:4]:
                new.append(col.find(text=True))
        else:
            new = []
            for cols in row.findAll('a')[0:2]:
                new.append(cols.find(text=True))
        film.append(new)
    return film

best_picture = pull_tables("https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture")
best_actor = pull_table("https://en.wikipedia.org/wiki/Academy_Award_for_Best_Actor")
best_director = pull_table("https://en.wikipedia.org/wiki/Academy_Award_for_Best_Director")
best_actress = pull_table("https://en.wikipedia.org/wiki/Academy_Award_for_Best_Actress")
