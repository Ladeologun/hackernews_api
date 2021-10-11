from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Story


class TestAPI(APITestCase):
    BASE_URL = 'http://localhost:8000/api'
    client = APIClient()

    def test_get_all_news_stories(self):
        '''
        Test that clients can retrieve all news_items in database
        '''
        news = self.client.get(f'{self.BASE_URL}/stories/')
        self.assertEqual(news.status_code, status.HTTP_200_OK)

    def test_filter(self):
        '''
        Test that news item can be filtered by type
        '''
        news_item = Story(title='JavaScript and React', author='omolade ologun', type='job', url='',  time=34195892, score='3' )
        news_item_2 = Story(title='JavaScript and React', author='omolade ologun', type='story', url='', time=34195892, score='3' )
        news_item.save()
        news_item_2.save()

        query = 'Job'
        query_2 = 'story'
        filter = self.client.get(f'{self.BASE_URL}?type={query}')
        filter_2 = self.client.get(f'{self.BASE_URL}?type={query_2}')
        
        self.assertEqual(query.lower(), news_item.type)
        self.assertEqual((filter.request['QUERY_STRING']), 'type=Job')
        self.assertEqual(query_2, news_item_2.type)
        self.assertEqual((filter_2.request['QUERY_STRING']), 'type=story')
    

    def test_search(self):
        '''
        Test that news title can be searched by text
        '''
        news_item = Story(title='JavaScript and React', author='ologun omolade', type='story', url='', time=34195892, score='3' )
        news_item.save()
        query = 'React'
        search = self.client.get(f'{self.BASE_URL}?q={query}')

        self.assertTrue(query in news_item.title.split(' '))
        self.assertEqual((search.request['QUERY_STRING']), 'q=React')

    def test_create_news_item(self):
        '''
        Test that a news item is created
        '''
        payload = {
            "title": "How to walk across a parking lot (2011)",
            "descendants":22,
            "author": "baobaba",
            "type": "story",
            "url": "https://www.raptitude.com/2011/09/how-to-walk-across-a-parking-lot",
            "score": 2
        }

        news = self.client.post(f"{self.BASE_URL}/addstory/", payload)
        self.assertEqual(news.status_code, status.HTTP_201_CREATED)