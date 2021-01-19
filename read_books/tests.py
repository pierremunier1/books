from django.test import TestCase,Client
from unittest import mock
from .response import GoogleApi, Response
import os
from django.urls import reverse
from users.models import CustomUser
from .models import Category, Book


###################################################################################
#   Tests response.py
#
# #################################################################################

class TestGoogleApi(TestCase):
    """test google api function"""


    @mock.patch('requests.get')
    def test_get_book(self, mock_get):
        """test main function to obtain book via goolge api"""

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
                        'industryIdentifiers': [{'identifier': 'Y7sOAAAAIAAJ'}
                        ],
                        'categories': [
                            'Alice (Fictitious character : Carroll)'
                        ]

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
            (["Alice's Adventures in Wonderland"],['Lewis Carroll'],[ '<div><a href=Y7sOAAAAIAAJ><img class=imessages-picture src=http://books.google.com/books/content?id=Y7sOAAAAIAAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api></img></a></div>'],[{'test'}],['Alice (Fictitious character : Carroll)'],['http://books.google.com/books/content?id=Y7sOAAAAIAAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api'])
            
        )
        mock_get.assert_called_once_with('https://www.googleapis.com/books/v1/volumes?', params={
            'key': os.environ.get('API_KEY_BACK'),
            'q': self.query,
            'subject:': self.query,
            'inauthor:': self.query,
            'intitle:':self.query,
            'maxResults':12,
        })
      

class TestResponse(TestCase):
    """initializing tests variables"""

    books_title = "Alice's Adventures in Wonderland"
    books_author = 'Lewis Carroll'
    books_pic =  '<div><a href=Y7sOAAAAIAAJ><img class=imessages-picture src=http://books.google.com/books/content?id=Y7sOAAAAIAAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api></img></a></div>'
    books_desc = 'test'
    books_cat = 'Alice (Fictitious character : Carroll)'
    books_pic_detail = 'http://books.google.com/books/content?id=Y7sOAAAAIAAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api'

    result = {
        'title': books_title,
        'picture': books_pic,
        'author': books_author,
        'description': books_desc,
        'categorie':books_cat,
        'picture_detail': books_pic_detail

        }
    @mock.patch('read_books.response.Response.response_front',mock.MagicMock(return_value=result))  
    def test_response_front(self):
        """test return of response_front function"""

        query = Response.response_front()
        self.assertEqual(query, 
            {'title': "Alice's Adventures in Wonderland", 'picture': '<div><a href=Y7sOAAAAIAAJ><img class=imessages-picture src=http://books.google.com/books/content?id=Y7sOAAAAIAAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api></img></a></div>', 'author': 'Lewis Carroll', 'description': 'test', 'categorie': 'Alice (Fictitious character : Carroll)', 'picture_detail': 'http://books.google.com/books/content?id=Y7sOAAAAIAAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api'}
        )


    def test_build(self):
        """create clean link"""

        category = ['Musique']
        self.analyse = Response.build(category)
        assert self.analyse == "Musique"


###################################################################################
#   Tests views.py
#
# #################################################################################


class TestViews(TestCase):
    """test all views functions"""

    def setUp(self):
        """initializing test variables"""

        self.username = "admin"
        self.password = "admin"
        self.email = "admin@cg.com"
        self.client = Client()
        self.customuser = CustomUser.objects.create_user(
            self.username,self.email, self.password)
        self.customuser.save()

        category = Category.objects.create(category_name='fiction')
        book_alice = {
            'google_id':'Y7sOAAAAIAAJ',
            'slug': "alice",
            'book_name': "Alice's Adventures in Wonderland",
            'author':'Lewis Carroll',
            'description': 'test',
            'picture': 'https://test',
            'picture_detail': 'https://test',
            'category': Category.objects.get(category_name=category),
            'customuser': CustomUser.objects.get(username=self.customuser),
        
        }
        self.book_alice_obj = Book.objects.create(**book_alice)
       

    result = {
            'picture': "<div><a href=Y7sOAAAAIAAJ><img class=imessages-picture src=http://books.google.com/books/content?id=Y7sOAAAAIAAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api></img></a></div>",'title':"Alice's Adventures in Wonderland"
            }

    @mock.patch('read_books.response.Response.response_front',mock.MagicMock(return_value=result))
    def test_search(self):
        """test search of book"""

        response = self.client.get(reverse('result'), {'query': "Alice's Adventures in Wonderland"})
        query = Response.response_front()
        self.assertJSONEqual(response.content,query)

    result_1 = {
        'picture': "<div><a href=Y7sOAAAAIAAJ><img class=imessages-picture src=http://books.google.com/books/content?id=Y7sOAAAAIAAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api></img></a></div>",
        'title':"Alice's Adventures in Wonderland",
        'description': "test",
        'picture_detail':'http://books.google.com/books/content?id=Y7sOAAAAIAAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api',
        'categorie':'Alice (Fictitious character : Carroll)',
        'author':'Lewis Carroll'
    }
   
    @mock.patch('read_books.response.Response.response_front',mock.MagicMock(return_value=result_1))
    def test_detail(self):
        """obtain detail of book"""

        book_id='Y7sOAAAAIAAJ'
        response = self.client.get(reverse('book',args=[book_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book.html')
        
    def test_save(self):
        """save book into the database"""

        book_id = 'Y7sOAAAAIAAJ'
        login = self.client.login(
            username=self.username, password=self.password)
        self.assertTrue(login)
        response = self.client.get(reverse('save_book',args=[book_id]),follow=True)
        self.assertEquals(response.status_code, 200)
        response_1 = self.client.post(f'/book/{book_id}')
        self.assertEquals(response_1.status_code, 302)
        self.assertRedirects(response,'/')


    def test_favorite(self):
        """access to the library"""

        login=self.client.login(username=self.username, password=self.password)
        response = self.client.post(('/users/login/?next=/favorite'), {
            'username': self.username,
            'password': self.password
        })
        self.assertTrue(login)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,'/favorite')
    
    def test_favorite_detail(self):
        """obtain detail from favorite book"""

        
        response = self.client.get(reverse('favorite',args=[self.book_alice_obj.slug]),follow=True)
        book = Book.objects.filter(slug=self.book_alice_obj.slug).first()
        self.assertEqual(book.slug,"alice")
        self.assertTemplateUsed(response,'detail.html')
        

    def test_best_books(self):
        """show favorite books"""

        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_favorite_remove_book(self):
        """test access to remove book"""

        book_id = 'Y7sOAAAAIAAJ'
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('save_book',args=[book_id]),follow=True)
        response_1 = self.client.get(reverse('remove_book',args=[self.book_alice_obj.slug]),follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_1.status_code, 200)
    