# My API

## Installed libraries
'''
Flask==1.0.2
Flask-JWT==0.3.2
Flask-RESTful==0.3.6
Flask-SQLAlchemy==2.3.2
'''
## Run
Run app.py file
## Description
In this app You can:
- create user (stores in database)
- authenticate user (JWT method)
- create stores
- delete single store by name
- create items with price, name, and store_id
- get list of stores and items added to this stores
- get by name - store and items added to this store
- get list of all items in all stores
- get single item by name
- replace by name (update price or change store) - single item
- remove single item by name

Application sends/gets data in JSON format