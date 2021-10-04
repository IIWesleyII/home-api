import unittest
import requests

class Test(unittest.TestCase):
    url = "http://127.0.0.1:5000/api/v1/data/housing"
    home = {
            "homes": {
                        
                    "longitude": 12.23,
                    "latitude": 17.88,
                    "housing_median_age": 281,
                    "total_rooms": 1000,
                    "total_bedrooms": 129,
                    "population": 322,
                    "households": 126,
                    "median_income": 8.3252,
                    "median_house_value": 4592600,
                    "ocean_proximity": "A different msg"
                        
                }
            }

    # GET all homes
    def test_get_homes(self):
        res = requests.get(Test.url)
        self.assertEqual(res.status_code, 200)
        self.assertGreater(len(res.json()), 0)
    
    # POST request create new home
    def test_add_homes(self):
        res = requests.post(Test.url, json=Test.home)
        self.assertEqual(res.status_code, 200)



if __name__ == '__main__':
    unittest.main()