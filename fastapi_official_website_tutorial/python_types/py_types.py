def get_full_name(first: str, last: str) -> str:
    return first.title() + " " + last.title()

print(get_full_name("john", "doe"))

def get_name_and_age(name: str, age: int) -> str:
    return name + age

