def old(age):
    return age

user = input('Insert your current age: ').strip()

try:
    if (old(user)) < 0:
        raise ValueError ('Invalid age.')
except:
    print(f'The age of {old(user)} is valid.')


# try não toma decisões. Ele apenas diz:

# "Execute este bloco. Se alguma exceção acontecer aqui, vá para o except.

# Quem decide se uma exceção deve acontecer é o if

# raise não substitui if; ele é acionado por ele.