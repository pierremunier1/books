import re
import unicodedata
import requests
from random import choice
import os
from . import config

class GoogleApi:
    """classe contains method for geocoding api"""

    def __init__(self,query):

        self.query = query
        
    def get_books(self):

        """method retrieve books"""
       
        payload = {
            'q': self.query,
            'subject:': self.query,
            'inauthor:': self.query,
            'intitle:':self.query,
            'maxResults':1,
            'key': os.environ.get('API_KEY_BACK')}
            
        result = requests.get(
            'https://www.googleapis.com/books/v1/volumes?',
            params=payload)
        google_books = result.json()
        books_title = []
        books_desc = []
        books_author = []
        books_date = []
        books_pic = []
        books_cat = []
        books_pic_detail = []
        try:
    
            for book in google_books['items']:

                    if not all(tag in book['volumeInfo']for tag in config.FILTER):
                        continue
                    self.book_title = (book['volumeInfo']['title'])
                    self.book_author = book['volumeInfo']['authors'][0]
                    self.book_pic = (book['volumeInfo']['imageLinks']['thumbnail'])
                    self.book_desc = (book['volumeInfo']['description'])
                    self.book_id = (book['volumeInfo']['industryIdentifiers'][0]['identifier'])
                    self.categorie = (book['volumeInfo']['categories'][0])
                    link = f"<div><a href={self.book_id}><img class=imessages-picture src={self.book_pic}></img></a></div>"
                    books_title.append(self.book_title)
                    books_author.append(self.book_author)
                    books_pic.append(link)
                    books_pic_detail.append(self.book_pic)
                    books_desc.append(self.book_desc)
                    books_cat.append(self.categorie)

            return books_title,books_author,books_pic,books_desc,books_cat,books_pic_detail
        except:
            return '','','','','',''

        
class Response:
    """return response to the front"""
    def response_front(query):

        """send data to the front"""

        query_book = GoogleApi(query)
        books_title,books_author,books_pic,books_desc,books_cat,books_pic_detail = query_book.get_books()

        result = {
            'title': books_title,
            'picture': books_pic,
            'author': books_author,
            'description': books_desc,
            'categorie':books_cat,
            'picture_detail': books_pic_detail
            }

        return result

    def build(result):

        """modify structure of list"""
        
        result = (str(
            result)
            .replace("'",'')
            .replace('[','')
            .replace(']','')
            .replace("'"," ")
            .replace(","," ")
            .replace('"'," "))

        return result





        