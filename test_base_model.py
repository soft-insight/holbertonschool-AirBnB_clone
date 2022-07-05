#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
print('--'*50)
my_model.save()


print(my_model.__class__)
print(type(my_model.__dict__))
print(type(my_model.__dict__['created_at']))
print('Hola')

my_model_json = my_model.to_dict()
print(my_model_json)
print()
print(type(my_model_json))
print(type(my_model_json['created_at']))

print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
