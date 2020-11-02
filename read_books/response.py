import re
import unicodedata
import requests
from random import choice
import os


class GoogleApi:
    """classe contains method for geocoding api"""

    def __init__(self, userQuery):
        """initializing instance attributes"""

        self.user_query = userQuery
        self.book = str

    def get_books(self):
        """method retrieve books"""

        payload = {
            'intitle': self.user_query,
            'key': os.environ.get('API_KEY_BACK')}
        result = requests.get(
            'https://www.googleapis.com/books/v1/volumes?q=',
            params=payload)
        google_books = result.json()
        status = google_books['status']
        print(google_books)

        if status == 'OK':
            self.book = (
                google_books
                )
    
            return self.book
        return '','',''
