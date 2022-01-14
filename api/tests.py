import json
from rest_framework.test import APITestCase


from api.models import Car, Rating


class CarTest(APITestCase):
    url = "/api/cars/"

    def setUp(self):
        Car.objects.create(make = 'honda', model = 'civic')
        Car.objects.create(make = 'ford', model = 'focus')
        Rating.objects.create(car_id = Car.objects.get(pk = 1), rating = 5)
        Rating.objects.create(car_id = Car.objects.get(pk = 1), rating = 4)
        Rating.objects.create(car_id = Car.objects.get(pk = 2), rating = 3)



    def test_list_cars(self):
        response = self.client.get(self.url, content_type='application/json' )
        result = response.json()

        expected_response = [
            {
                'id': 1,
                'avg_rating': 4.5,
                'make': 'honda',
                'model': 'civic'},
            {
                'id': 2,
                'avg_rating': 3,
                'make': 'ford',
                'model': 'focus'
            }]

        self.assertEqual(response.status_code, 200)   
        self.assertIsInstance(result, list)
        self.assertEqual(result, expected_response)    

    def test_retrive_cars(self):
        response = self.client.get(f'{self.url}1/', content_type='application/json' )

        result = response.json()
        expected_response = {
            'id': 1,
            'avg_rating': 4.5,
            'make': 'honda',
            'model': 'civic'
        }

        self.assertEqual(response.status_code, 200)   
        self.assertIsInstance(result, dict)
        self.assertEqual(result, expected_response)

    def test_delete_car(self):

        valid_response = self.client.delete(f'{self.url}1/', content_type='application/json')        
        invalid_response = self.client.delete(f'{self.url}100/', content_type='application/json')
        
        get_response = self.client.get(f'{self.url}', content_type='application/json')
        result = get_response.json()
        
        self.assertEqual(valid_response.status_code, 204)   
        self.assertEqual(invalid_response.status_code, 404)   
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)

    def test_list_cars(self):
        response = self.client.get(self.url, content_type='application/json' )
        result = response.json()

        expected_response = [
            {
                'id': 1,
                'avg_rating': 4.5,
                'make': 'honda',
                'model': 'civic'},
            {
                'id': 2,
                'avg_rating': 3,
                'make': 'ford',
                'model': 'focus'
            }]

        self.assertEqual(response.status_code, 200)   
        self.assertIsInstance(result, list)
        self.assertEqual(result, expected_response)

    def test_list_popular(self):
        response = self.client.get('/api/popular/', content_type='application/json' )
        result = response.json()
        print(result)
        expected_response = [
            {
                'id': 1,
                'rates_number': 2,
                'make': 'honda',
                'model': 'civic'},
            {
                'id': 2,
                'rates_number': 1,
                'make': 'ford',
                'model': 'focus'
            }]

        self.assertEqual(response.status_code, 200)   
        self.assertIsInstance(result, list)
        self.assertEqual(result, expected_response)
    
    def test_post_rating(self):
        valid_data = json.dumps({
            "car_id": 2,
            "rating": 5
            })
        invalid_data = json.dumps({
            "car_id": 1,
            "rating": 10
        })

        valid_post_response = self.client.post("/api/rate/", valid_data, content_type='application/json')
        post_result = valid_post_response.json()
        
        invalid_post_response = self.client.post("/api/rate/",data = invalid_data, content_type='application/json' )
        expected_post_response ={
            'car_id': 2,
            'rating': 5
        }

        self.assertEqual(valid_post_response.status_code, 201)   
        self.assertEqual(invalid_post_response.status_code, 400)
        self.assertEqual(invalid_post_response.data['rating'][0], "Ensure this value is less than or equal to 5." )   
        self.assertIsInstance(post_result, dict)
        self.assertEqual(post_result,expected_post_response)


        get_response = self.client.get(f'{self.url}2/', content_type='application/json' )
        get_result = get_response.json()
    
        expected_get_response = {
            'id': 2,
            'avg_rating': 4.0,
            'make': 'ford',
            'model': 'focus'
        }

        self.assertEqual(get_result,expected_get_response)
