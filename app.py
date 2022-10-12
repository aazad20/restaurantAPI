from flask import Flask
from flask import jsonify
from flask import request
from json import dumps
from pymongo import MongoClient
import json
from bson import json_util
from bson.objectid import ObjectId
# import pika 
# from flask_rabbitmq import Queue
# from flask_rabbitmq import RabbitMQ


app = Flask(__name__)


client = MongoClient('localhost', 27017)
pizza_house = client.pizza_house
orders = pizza_house.orders

# queue = Queue()


@app.route('/welcome')
def hello_world():
   
    status = 200
    message = 'Welcome to Pizza House'
    
    return jsonify({
        "status": status,
        "message": message
    })



@app.route('/order', methods=['POST'])
def order():
    js = request.get_json()

    result = orders.insert_one(js).inserted_id 
    data ={
        "id":json.loads(json_util.dumps(result))["$oid"],
        "status":200
        }
    return jsonify(data)




@app.route('/getorders')
def get_all_orders():
    response = orders.find()
    ord=[]
    for r in response:
        
        temp = {
            "id": json.loads(json_util.dumps(r["_id"])),
            "items":r['order']
        }
        ord.append(temp)
    return jsonify(ord)


@app.route('/getorders/<string:order_id>',methods=["GET"])
def get_order(order_id):
    try:
        response = orders.find_one({"_id": ObjectId(order_id)})
        
        data =response['order']
        
    except:
        data={
            'message':'No such order exists'
        }
    return jsonify(data) 





@app.errorhandler(404)
def page_not_found(error):
    success = False
    message = str(error)

    return jsonify({
        "success": success,
        "message": message
    }), 404


@app.errorhandler(500)
def server_error(error):
    success = False
    message = str(error)

    return jsonify({
        "success": success,
        "message": message
    }), 500


if __name__ == '__main__':
    app.run(debug=True)