# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as BS


def get_soup(fl):
    with open(fl, 'r') as f:
        soup = BS(f, 'lxml')
    return soup

def get_description(soup):
    raw_head = soup.find('h1').text
    head = " ".join([raw_head[:22], raw_head[22:]])
    return head


if __name__=="__main__":
    soup = get_soup('raw.txt')
    desc = get_description(soup)
    print(desc)    



