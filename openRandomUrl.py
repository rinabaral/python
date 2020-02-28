import webbrowser
from random import choice

My_urls = ['https://www.nytimes.com',
           'https://www.youtube.com',
           'https://www.bbc.com',
           'https://ekantipur.com',
           'https://twitter.com',
           'https://www.onlinekhabar.com',
           'https://medium.com',
           'https://thehimalayantimes.com',
           'https://www.instagram.com/',
           'https://www.facebook.com',
           'https://edition.cnn.com/']
length = len(My_urls)
for My_url in range(length):
    webbrowser.open(choice(My_urls))
    

