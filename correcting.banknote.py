banknote = {
    'dollar': 0.19,
    'euro': 0.17,
    'pound': 0.14,
}

def value(real, convert):
    return real * convert

print('Available banknotes: Dollar, Euro, Pound\n') # \n serve para pular linha. Você também pode pular várias outras linhas dentro do mesmo print.

while True:

    user = input('Choose a banknote to convert (or type "exit"): ').lower().strip()
    
    if user == 'exit':
        print('Program finished.')
        break
    elif user == '':
        print('Please, select a banknote.')
        continue
    elif user not in banknote:
        print('Banknote does not exist.')
        continue # como as possibilidades de erro já foram abordadas, a única opção que resta é da cédula existir no dicionário. Else aqui é redundante.
    
    # O bloco try/except deve abraçar a pergunta do valor e o cálculo
    try:
        choice = banknote[user]
        conv = input(f'Insert the value in BRL to convert to {user}: ').strip()
        money = float(conv)
        print(f'{money:.2f} BRL converted to {user} is: {value(money, choice):.2f}\n')
    except ValueError:
        print('Invalid value. Please enter a number.\n')

# except: capturar todas as exceções
# except ValueError: capturar apenas o erro de valor inválido