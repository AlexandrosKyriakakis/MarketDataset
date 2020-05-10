# Super Market Dataset
![](https://www.naftemporiki.gr/fu/p/1493489/638/399/0x000000000167101b/2/2.jpg)
    
    
    This Project selects products from a popular super-market. 
    The scraped data are in [Here].
    

    Contains 6 categories:
        1. Fresh Food
        2. Fridge Items
        3. Drinks
        4. Pet
        5. Personal Care
        6. Home Items

### Dataset Structure
    AB.csv with columns
        1. category
        2. name
        3. producer,
        4. url,price,
        5. barcode
    RandomPeople.csv with columns
        1. id
        2. first_name
        3. last_name
        4. email
        5. gender
        6. SSN

## Installation and Running

    1. $ pip install scrapy
    2. $ git clone https://github.com/AlexandrosKyriakakis/MarketDataset.git
    3. $ cd alex
    4. $ scrapy crawl ab -o ab.csv -t csv
    (if you want no output add "--nolog" at the end of (4.))

## Contributors

    1. Eleni Karanikola
    2. Alexandros Kyriakakis

[Here]: https://github.com/AlexandrosKyriakakis/MarketDataset/tree/master/data