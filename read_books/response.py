import re
import unicodedata
import requests
from random import choice
import os

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
        
        self.book = (google_books['items'][0]['volumeInfo']['description'])
        self.book_title = (google_books['items'][0]['volumeInfo']['title'])
        
        return  self.book,self.book_title


class Response:

    def response_front(query):

        analyse = Parser(query)
        userquery = analyse.parse()
        query_book = GoogleApi(userquery)
        book, book_title = query_book.get_books()

        return book,book_title