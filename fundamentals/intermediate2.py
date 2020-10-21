# 1. Update Values in Dictionaries and Lists.
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# 1a. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]=15
# print(x)

# 1b. Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name']="bryant"
# print(students)

# 1c. In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0]= "Andres"
# print(sports_directory['soccer'][0])

# 1d. Change the value 20 in z to 30
z[0]['y'] = 30
# print(z[0]['y'])


# 2. Iterate Through a List of Dictionaries.
#   2a. Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. 
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for i in range(len(some_list)):
        # if some_list[i] == some_list(len(some_list)-1-i):
        #     print(some_list)
        print(some_list[i])
        for k , val in some_list[i].items():
            print(f"{k}-{val}")
# iterateDictionary(students) 

# 3. Get Values From a List of Dictionaries
#  3a. Create a function iterateDictionary2(key_name, some_list) that given a list of dictionaries and a key name, the fuction prints the value stored in that key for each dictionary.
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i])
        for k , val in some_list[i].items():
            print(f"the value is {val}, which is stored in {k}")
    
# iterateDictionary2("last_name",students)

# or you can..
def iterateDictionary2(key_name, some_list):
    for student_dictionary in some_list:
        print(student_dictionary[key_name])

# iterateDictionary2("last_name",students)

# 4. Iterate Through a Dictionary with List Values.
#   4a. Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list.
dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    # print(some_dict)
    for key, val in some_dict.items():
        # print(len(val))
        print(f"{len(val)} {key.upper()}")   
        for item in val:
            print(item)
# printInfo(dojo)

