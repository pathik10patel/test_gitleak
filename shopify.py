from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import bson
import gridfs

app = Flask(__name__)
app.config["DEBUG"] = True
mongo_connection= PyMongo(app, uri ='mongodb://root:password@mongo:27017/local?authSource=admin' )


    
@app.route('/add', methods=['POST'])
def add_items():
    if "image" in request.files:
        product_image = request.files['image']
        mongo_connection.save_file(product_image.filename, product_image)
        mongo_connection.db.product.insert_one({'title': request.form['title'],
                                    'description':request.form['description'],
                                            'price':request.form['price'],
                                            'product_image_name':product_image.filename,
                                            'currency':request.form['currency']})
    else:
        mongo_connection.db.product.insert_one({'title': request.form['title'],
                                    'description':request.form['description'],
                                            'price':request.form['price'],
                                            'currency':request.form['currency']})
        
        return jsonify({"message":"Please enter all the fields"})
    return jsonify({"message":"Product added successfully"})


@app.route('/retrive', methods=['GET'])
def get_items():
    return_list=[]
    products = mongo_connection.db.product.find()
    for prod in products: 
        return_list.append(prod)
    return str(return_list)


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
