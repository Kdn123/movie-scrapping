import requests
from lxml import html
from threading import Thread
import csv
url = "https://m.imdb.com/name/nm0000375/filmotype/actor"

data = requests.get(url).text

tree = html.fromstring(data)

# name = tree.xpath('//span[@class="h3"]/text()')
url1 = tree.xpath('//div[@class="col-xs-12 col-md-6"]//a/@href')

# print(name)
# print(url1)

n, rating, l1=[], [], []
def imdb(a):
    try:
        url2 = "https://m.imdb.com/"
        ur = url2+a
        d = requests.get(ur).text
        x = html.fromstring(d)
        name = x.xpath('//h1/text()')
        rate = x.xpath('//span[@class="AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV"]/text()')
        # current_data=list(zip(name,rate))
        if rate != [] :
            n.append(name[0])
            rating.append(rate[0])
    # print(current_data)
    except Exception as e:
        print(e) 
print("started")
# class abc(Thread):
#     def run(self):
for i in url1:
    thrd = Thread(target=imdb, args=(i,))
    thrd.start()
    l1.append(thrd)
for j in l1:
    j.join()


# a1=abc()
# a1.start()
zipping = list(zip(n, rating))

movcsv= "mnames.csv"
with open(movcsv, 'w', newline='')as file:
    writer = csv.writer(file)
    writer.writerows(zipping)




