
# coding: utf-8

# In[1]:


import requests as r
import matplotlib.pyplot as mp


# In[3]:


def crypto_differences(primary='BTC', secondary='USD'):
    url = 'https://api.cryptonator.com/api/full/btc-usd/'.format(primary.lower(), secondary.lower()) # url of crypto
    # currency rate change and convert int into a format
    json = r.get(url).json()['ticker']['markets']
    market = []
    volume = []
    price = []

    for ab in range(len(json)):
        market.append(json[ab]['market'])
        volume.append(json[ab]['volume'])
        price.append(float(json[ab]['price']))
    mp.figure(figsize=(18, 8)),
    mp.scatter(price, volume, s=150)

    mp.title('Crypto Currency Rate Graph', size=26)
    mp.xlabel('Rates in' + str(secondary).upper(), size=18)
    mp.ylabel('Currencies Volumes', size=30)

    print('Minimum price at:\t', market[(price.index(min(price)))], min(price), '\nMaximum price at:\t',
          market[(price.index(max(price)))], min(price), '\nDifference :\t\t', int((max(price) - min(price))),
          secondary,
          '\nProfit ratio: \t\t', round((max(price) - min(price)) / min(price), 4))


    for i in range(len(market)): # for annotating
        mp.annotate(market[i], (price[i], volume[i]))

    for i, v in enumerate(market): # use 'enumerate' for annotating and and accessing value in 'CLI'
        print(i, v)
    print(len(market)) # shows length of  elements
    mp.show()


crypto_differences()

