from flask import Flask, request, jsonify ,Response
from flask_pymongo import PyMongo
from flask_cors import CORS
import bson
import pandas as pd
import gridfs
from bson.json_util import dumps

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
mongo_connection = PyMongo(
    app, uri='mongodb+srv://keval:123@cluster0.cnz42.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    
@app.route('/add', methods=['POST'])
def add_items():
    if "image" in request.files:
        product_image = request.files['image']
        mongo_connection.save_file(product_image.foldername,product_image.filename, product_image)
        mongo_connection.db.product.insert_one({'title': request.form['title'],
                                    'description':request.form['description'],
                                            'price':request.form['price'],
                                            'product_image_name':product_image.foldername,
                                            'currency':request.form['currency']})
    else:
        mongo_connection.db.product.insert_one({'title': request.form['title'],
                                    'description':request.form['description'],
                                            'price':request.form['price'],
                                            'currency':request.form['currency']})
        
        return jsonify({"message":"Please enter all the fields"})
    return jsonify({"message":"Product added successfully"}),201


@app.route('/retrive', methods=['GET'])
def get_items():
    return_list=[]
    products = mongo_connection.db.product.find()
    json_data = dumps(products)
    return json_data


@app.route('/get/<project_id>', methods=['GET'])
def get_specific_items(project_id):
    return_list = []
    print(project_id)
    products = mongo_connection.db.product.find_one({"_id": project_id})
    for i in products:
        print(i)
    return str(products)



@app.route('/download/project_csv', methods=['GET'])
def get_items_csv():
    return_list = []
    products = mongo_connection.db.product.find()
    for prod in products:
        return_list.append(prod)
    df = pd.DataFrame(return_list)
    return Response(
        df.to_csv("shopify_project.csv", sep='\t', encoding='utf-8'),
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=shopify_project.csv"})

@app.route('/remove', methods=['DELETE'])
def remove_item():
    content = request.get_json() 
    obj_id = bson.ObjectId(content["id"])
    if content['id']:
        mongo_connection.db.product.delete_one({"_id":obj_id})
        return jsonify(True)
    else: 
        return jsonify(False)


@app.route('/update', methods=['PUT'])
def update_item():
   obj_id = bson.ObjectId(request.form["id"])
   data_id = mongo_connection.db.product.find_one({"_id":obj_id})
   if "image" in request.files:
        product_image = request.files['image']
        mongo_connection.save_file(product_image.filename, product_image)
        mongo_connection.db.product.update_one(data_id,{"$set":{"product_image_name":product_image.filename}})
   for k,v in request.form.items():
       mongo_connection.db.product.update_one(data_id,{"$set":{k:v}})
   return jsonify({"message":True})
   
    

    
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8087)
