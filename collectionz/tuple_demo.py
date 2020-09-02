#!/usr/bin/python
"""
IMMUTABLE
Tuple is very similar to a list with one major difference — it is immutable. We create a tuple using parentheses ‘()’
"""

personal_info = ("Tushar", "Ray", 33, "M")
print("personal_info size = ", len(personal_info))

(firstName, lastName, age, gender) = personal_info  # Unpacking Tuples
print("First name = ", firstName)
print("Last name = ", lastName)
print("Age = ", age)
print("Gender = ", gender)

pair = [
    ('fname', 'Foo'),
    ('lname', 'Bar'),
    ('email', 'foo@bar.com'),
]

for p in pair:
    print('{} : {}'.format(p[0], p[1]))

for p in pair:
    print('{} : {}'.format(*p))

for field, value in pair:
    print('{} : {}'.format(field, value))

# Packing
*a, = "Roshith", "1"
print(type(a))

for first, *rest in [(1, 2, 3), (4, 5, 6, 7)]:
   print("First:", first)
   print("Rest:", rest)
