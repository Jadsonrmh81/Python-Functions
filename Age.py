def old(age):
    return age

user = input('Insert your current age: ').strip()

try:
    if (old(user)) < 0:
        raise ValueError ('Invalid age.')
except:
    print(f'The age of {old(user)} is valid.')
