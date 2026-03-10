def get_full_name(first: str, last: str) -> str:
    return first.title() + " " + last.title()

print(get_full_name("john", "doe"))

def get_name_and_age(name: str, age: int) -> str:
    return name + age


# generic types

list_of_ints: list[int] = [1, 2, 3]
list_of_strs: list[str] = ["a", "b", "c"]


'''
    The variable items_t is a tuple with 3 items, an int, another int, and a str.
    The variable items_s is a set, and each of its items is of type bytes.
'''
def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s


'''
    For dictionaries, you pass two types: 1) type for the keys, and 2) type for the values
'''
def process_items(prices: dict[str, float]):
    return prices

'''
    Class as a type
'''
class Person:
    def __init__(self, name: str):
        self.name = name

def print_person_name(person: Person):
    print(person.name)

####################
# Pydantic models ##
#################### 

'''
    Pydantic is a python model used for data validation.
'''           

from datetime import datetime

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)  # dictionary unpacking
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123