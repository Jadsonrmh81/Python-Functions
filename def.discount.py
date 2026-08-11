
def discount(value , dis):
    return value - dis

user = input('Insert the value: ').strip()

try:
    money = float(user)
    if money > 100.0:
        nv = money * 0.15
        print(f'Your current value: {discount(money , nv)}')
    else:
        print(f'You typed the value of ${money:.2f} dollars.')
except:
    print('Invalid value.')

# 

# correção:

# na saída de dados dava erro pois 'user' é uma string, e eu defini para o programa rejeitar strings. Como :.2f só funciona para números. dá erro.
# Logo, o correto é usar 'money' para imprimir o valor, pois ele converteu 'user' para um valor float, sendo possível usar :.2f.