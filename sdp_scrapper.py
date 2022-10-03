from bs4 import BeautifulSoup
import datetime
from tinydb import TinyDB, Query
import urllib3
import xlsxwriter

def make_soup(url):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    return BeautifulSoup(r.data,'lxml')

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://shop.sdp-si.com/catalog'
total_added = 0

res = make_soup(url)
print(res)