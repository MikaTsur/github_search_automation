import pytest
import json
import logging
import test_files

# some_json = {
#   "name": "John Doe",
#   "age": 30,
#   "city": "New York"
# }

# some_name_age = {
# "mika": 39,
# "yonathan": 33
# }


# def test_iteration():
#     json_file_path = r'C:\Users\morellyo\Desktop\python\automation_tests\test_files\ice_cream.json'

#     with open(json_file_path, 'r') as file:
#         data = json.load(file)

#     keys=[]
#     key_count={}

#     for key in data:
#         keys.append(key)
#         key_count[key] = key_count.get(key, 0)+1 

#     logging.info(json.dumps(keys))
#     logging.info(json.dumps(key_count))

#     #############################################

#     jhon = []

#     for key in some_json:
#         jhon.append(key)

#     logging.info(jhon)

#     #############################################

#     new_some_name_age = []

#     for key in some_name_age:
#         new_some_name_age.append(key)

#     logging.info(new_some_name_age)

#     #############################################

#     my_child = {
#         "Hodaya": 7,
#         "Iscah": 4,
#         "Hanoch": 1
#     }

#     children = []

#     for key in my_child:
#         children.append(key)

#     logging.info(children)

#     #############################################

#     colors = {
#         "blue": 1 ,
#         "red": 2,
#         "pink": 3
#     }

#     new_colors = []

#     for key in colors:
#         new_colors.append(key)

#     logging.info(new_colors)
        

#     #############################################

#     abc = { "a" : 'aaa', 'b':'bbb', 'c':'ccc'}
#     new_abc = []

#     for key in abc:
#         new_abc.append(key)

#     logging.info(new_abc)
#     #############################################

#     nums = {"1" : 111, "2": 222, "3":333}
#     new_nums = []

#     for key in nums:
#         new_nums.append(key)

#     logging.info(new_nums)

#     #############################################

#     a123 = {"aa":"aaa", "bb":"bbb", "cc":"ccc"}
#     new_a123 = []

#     for key in a123:
#         new_a123.append(key)

#     logging.info(new_a123)
        

#     #############################################

#     bbb = {"asas":2,"sasa":3}
#     new_bbb = []

#     for key in bbb:
#         new_bbb.append(key)

#     logging.info(new_bbb)

    ###########################################
  # Four-level dictionary

my_key = []
my_value = []
sec_key=[]
sec_value=[]
my_levels = {
    "key1": "value1",
    "key2": {
        "2_key_2": "2_value_2"},
    "key3": {
        "2_key_3":"2_value_3"}
                }


# for key, value in my_levels.items():
#     my_key.append(key)
#     my_value.append(value)
#     if isinstance(value, dict):  
#         for key2, value2 in value.items():  
#             sec_key.append(key2)
#             sec_value.append(value2)

# logging.info(my_key)
# logging.info(my_value)
# logging.info(sec_key)
# logging.info(sec_value)
# ##########################################

aaa1 = []
aaa2 = []

bbb = []
ccc = []

some_json = {
    "a1":"a2",
    "b1": {"c1": "c2"
    }}

for key, value in some_json.items():
    if isinstance(value, dict):
        for key2, value2 in value.items():
            bbb.append(key2)
            ccc.append(value2)

logging.info(f'that is key{bbb}')
logging.info(f'that is value{ccc}')


import logging

child1 = []
child2 = []

morell = {
    'yonatan': 'father',
    'mika': 'mother',
    'children': {
        'hodaya': '7',
        'Iscah': '5',
        'Hanoch': '1'
    }
}

for key, value in morell.items():  #
    if isinstance(value, dict):
        for key1, value1 in value.items(): 
            child1.append(key1) 
            child2.append(value1)  
            
logging.info(f'xxxxxxxxxxxxxxxx{child1}')
logging.info(f'xxxxxxxxxxxxxxxx{child2}')

abc1 = []
abc2 = []

tsur = {
    'Liat':'grenpa',
    'child':{
        'mika':'girl',
        'matan': 'boy'
    }}

for key, value in tsur.items():
    if isinstance(value, dict):
        for key1_0, value1_0 in value.items():
            abc1.append(key1_0)
            abc2.append(value1_0)

logging.info(f'ttttttttttttttttttttt{abc1}')
logging.info(f'ttttttttttttttttttttt{abc2}')

ice_cream1 = []
ice_cream2= []

ice_cream = {
    'dairy':'milk',
    'fruits':{
        'coconuts':'white'
    }
}
for key, value in ice_cream.items():
    if isinstance(value, dict):
        for key1, value2 in value.items():
            ice_cream1.append(key1)
            ice_cream2.append(value2)

logging.info(f'ttttttttttttttttttttt{ice_cream1}')
logging.info(f'ttttttttttttttttttttt{ice_cream2}')

jjj1 = ""
jjj2 = ""

json_1 = {

    "1","1",
    "2",{
        "3":3
    }}
for key, value in json_1.items():
    if isinstance(value, dict):
        for key1, value1 in value.items():
            jjj1.append(key1)
            jjj2.append(key1)
logging.info(jjj1)
logging.info(jjj2)


