import re
import unicodedata
import requests
from random import choice
import os
from . import config


class Parser:
    """class contains method to parse the user text input form"""

    def __init__(self, analyse):
        """initialising attribute"""

        self.analyse = analyse

    def parse(self):
        """method analyse the text and transform if necessary"""

        # switch to lower case
        self.analyse = self.analyse.lower()
       
        # remove accent
        self.analyse = ''.join((c for c in unicodedata.normalize
                                ('NFD', self.analyse)
                                if unicodedata.category(c) != 'Mn')
                               )

        # remove punctuation
        self.analyse = re.sub(r"[.!,;?\']", " ", self.analyse).split()

        # to convert the list to string.
        self.analyse = ' '.join(self.analyse)

        return self.analyse


class GoogleApi:
    """classe contains method for geocoding api"""

    def __init__(self,userquery):

        self.query = userquery
        
        
    def get_books(self):

        """method retrieve books"""
        
        payload = {
            'q': self.query,
            'subject:': self.query,
            'inauthor:': self.query,
            'intitle:':self.query,
            'maxResults':2,
            'key': os.environ.get('API_KEY_BACK')}
            
        result = requests.get(
            'https://www.googleapis.com/books/v1/volumes?',
            params=payload)
        google_books = result.json()
        
        books_title = []
        books_desc = []
        books_author = []
        books_date = []
        books_pic = list()
        book_unavalaible = 'non disponible'

        try:
            for book in google_books['items']:

                    if not all(tag in book['volumeInfo']for tag in config.FILTER):
                        continue
                    self.book_title = (book['volumeInfo']['title'])
                    self.book_author = book['volumeInfo']['authors'][0]
                    self.book_pic = (book['volumeInfo']['imageLinks']['thumbnail'])
                    link = '<img class=imessages-picture src='+self.book_pic+'></img>'

                    books_title.append(self.book_title)
                    books_author.append(self.book_author)
                    books_pic.append(link)
                    
                    return books_title,books_author,(str(books_pic).replace("'"," ").replace(","," ").replace('"'," "))
        except KeyError:
            return book_unavalaible
        


class Response:

    def response_front(query):

        analyse = Parser(query)
        userquery = analyse.parse()
        query_book = GoogleApi(userquery)
        books_title,books_author,books_pic = query_book.get_books()

        result = {
            'title': books_title,
            'picture': books_pic,
            'author': books_author
            }

        return result