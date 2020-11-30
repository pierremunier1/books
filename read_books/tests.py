from django.test import TestCase
from unittest import mock
from .response import GoogleApi
import os


class TestGoogleApi(TestCase):
    @mock.patch('requests.get')
    def test_get_book(self, mock_get):

        self.query = "Alice's Adventures in Wonderland"

        mock_response = mock.Mock()

        result = {
            'items': [
                {
                    'volumeInfo':  {
                        'title': "Alice's Adventures in Wonderland",
                        'authors': [
                            'Lewis Carroll'
                        ],
                        'imageLinks':{
                            'thumbnail': "http://books.google.com/books/content?id=Y7sOAAAAIAAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
                        },
                        'description':{ 'test'
                        },
                        'industryIdentifiers': [{'identifier': 'Y7sOAAAAIAAJ'}]

                    }
                }
                    ]
            }
            
        # Define response data for my Mock object
        mock_response.json.return_value = result
        mock_response.status_code = 200

        # Define response for the fake API
        mock_get.return_value = mock_response

        # Call the function
        query_book = GoogleApi("Alice's Adventures in Wonderland")
        query = query_book.get_books()
   
        self.assertEqual(query, 
            (["Alice's Adventures in Wonderland"],['Lewis Carroll'],'[ <div><a href=book_id=Y7sOAAAAIAAJ><img class=imessages-picture src=http://books.google.com/books/content?id=Y7sOAAAAIAAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api></img></a></div> ]',[{'test'}])
            
        )
        mock_get.assert_called_once_with('https://www.googleapis.com/books/v1/volumes?', params={
            'key': os.environ.get('API_KEY_BACK'),
            'q': self.query,
            'subject:': self.query,
            'inauthor:': self.query,
            'intitle:':self.query,
            'maxResults':5,
        })
      
