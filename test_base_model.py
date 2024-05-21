#!/usr/bin/python3
from models.base_model import BaseModel

my_model_json = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                 'created_at': '2017-09-28T21:03:54.052298',
                 '__class__': 'BaseModel',
                 'my_number': 89,
                 'updated_at': '2017-09-28T21:03:54.052302',
                 'name': 'My_First_Model'}
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))


