def person(age):
    return age

user = input('Insert your age: ').strip()

try:
    a = int(user)
    if a < 0:
        raise ValueError('Invalid age.')
except:
    print(f'Your age: {person(a)}') 