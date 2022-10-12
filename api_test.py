import requests
import unittest
import json
from bson import json_util
from bson.objectid import ObjectId



class Testing(unittest.TestCase):
    API_URL='http://127.0.0.1:5000/welcome'
    order_URL = " http://127.0.0.1:5000/order"
    item_URL="http://127.0.0.1:5000/getorders"
    order_object = {
        "order":["Large Cake"]
    }
    test = ""
    def test_1_welcome(self):
        r = requests.get(Testing.API_URL)    
        self.assertEqual(r.status_code,200)


    def test_2_order(self):
        r = requests.post(Testing.order_URL,json=Testing.order_object)
        
        self.assertEqual(r.status_code,200)
    
    def test3(self):
        url = f"{Testing.item_URL}/6346c034678b6b22f3bfe577"
        
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)
    
    
