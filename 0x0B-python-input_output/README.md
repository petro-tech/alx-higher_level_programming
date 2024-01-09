Python - Input/Output

Task 0 - Read file
A function that reads a text file (UTF8) and prints it to stdout

Task 1 - Write to a file
A function that writes a string to a text file (UTF8) and returns the number of characters written

Task 2 - Append to a file
A function that appends a string at the end of a text file (UTF8) and returns the number of characters added

Task 3 - To JSON string
A function that returns the JSON representation of an object (string)

Task 4 - From JSON string to Object
A function that returns an object (Python data structure) represented by a JSON string

Task 5 - Save Object to a f
A function that writes an Object to a text file, using a JSON representation

Task 6 - Create object from a JSON file
A function that creates an Object from a “JSON file”

Task 7 -  Load, add, save
a script that adds all arguments to a Python list, and then save them to a file

Task 8 - Class to JSON
A function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object

Task 9 - Student to JSON
 a class Student that defines a student by:

Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)

Task 10 - Student to JSON with filter
a class Student that defines a student by: (based on 9-student.py)

Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attribute names contained in this list must be retrieved.
Otherwise, all attributes must be retrieved

Task 11 - Student to disk and reload
 a class Student that defines a student by: (based on 10-student.py)

Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attributes name contain in this list must be retrieved.
Otherwise, all attributes must be retrieved
Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
You can assume json will always be a dictionary
A dictionary key will be the public attribute name
A dictionary value will be the value of the public attribute

Task 12 - Pascal's Triangle
 a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
