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
        self.book  = str
  
    
    def get_books(self):
    
        """method retrieve books"""
        
        payload = {
            'q': self.query,
            'key': os.environ.get('API_KEY_BACK')}
            
        result = requests.get(
            'https://www.googleapis.com/books/v1/volumes?',
            params=payload)
        google_books = result.json()

        books_title = []
        books_desc = []
        books_author = []
        books_date = []

        for book in google_books['items']:
                   
                    if not all(tag in book['volumeInfo']for tag in config.FILTER):
                        continue
                    self.book = (book['volumeInfo']['description'])
                    self.book_title = (book['volumeInfo']['title'])
                    self.book_author = book['volumeInfo']['authors'][0]
                    self.book_date = (book['volumeInfo']['publishedDate'])
                
                    result = self.book_author,self.book_date

                    books_title.append(self.book_title)
                    books_desc.append(self.book)
                    books_author.append(self.book_author)
                    books_date.append(self.book_date)
        
        return books_title,books_desc,books_author,books_date
        
                   
class Response:

    def response_front(query):

        analyse = Parser(query)
        userquery = analyse.parse()
        query_book = GoogleApi(userquery)
        books_title,books_desc,books_author,books_date = query_book.get_books()

        result = {
            'title': books_title,
            'response': books_desc
            }


        return result