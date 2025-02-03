def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("ashish", "jain"))

# The approach above does not give us the hint of title right away and it is not very useful

# But we can add the types to the parameters so we can get that hinting through our IDE or code editor

def GetFullName(firstname: str, lastname: str):
    fullname = firstname.title() + " " + lastname.title()
    return fullname

# Now this function is not enforcing the type but helping us to know that a string needs to be passes in the function


# Lets try now with some integers
def GetNameWithAge(name: str, age: int):
    nameWithAge = name + " is this old: " + age
    return nameWithAge

# There are the types that we can use in fastapi with python:-
""" 
int
float
bool
bytes
"""
# We can also do the same with our data structures
""" 
tuple
list
dict
set
"""
# ANd we can also define what type of data are we storing in those
""" 
tuple[int, int, str]
set[bytes]
list[str]
dict[float, str]
"""

# We can also do the union type where a variable or an input can be either
def items(item: int | str):
    print(item)

# We can also do something which is like a possibility where one parameter can be either a value or a none, for this we have to import a function from typing library
from typing import Optional
def Hi(name: Optional[str] = None):
    if name is not None:
        print(name)
    else:
        print("Hello")

# For newer version of python we can use something like this as well
def sayHi(name: str | None = None):
    if name is not None:
        print(name)
    else:
        print("Hello")

# It is recommended to use Union instead of optional if using newer versions of python

# We can also use classes as types
class Person:
    def __init__(self, name: str):
        self.name = name

def getPersonName(person: Person):
    return person.name

# Here we are using classes as types to also create instances