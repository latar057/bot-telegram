import requests
import bs4
import random
import constants

def pars():
    '''Список с анекдотами'''
    url_joke = constants.url_joke
    res = requests.get(url_joke)
    pars_web = bs4.BeautifulSoup(res.text, features='html.parser')
    list_jokes = [c.text for c in pars_web.select('p')]
    random.shuffle(list_jokes)
    return list_jokes

if __name__ == '__main__':
    pars()
