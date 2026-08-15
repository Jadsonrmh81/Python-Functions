banknote = {
    'dollar': 0.19,
    'euro': 0.17,
    'pound': 0.14,
}

def value(real, convert):
    return real * convert

print('Available banknotes: Dollar, Euro, Pound')
print()

while True:

    user = input('Choose a banknote to convert (or type "exit"): ').lower().strip()
    if user == 'exit':
        print('Program finished.')
        break
    elif user == '':
       print('Please, select a banknote.')
       continue
    elif not user in banknote: # essa linha está registrando que 'exit' não existe no dicionário, logo o looping não encerra, mas se repete através do comando 'continue'
       print('Banknote do not exist.')
       continue
    else:
       choice = banknote[user]
       conv = input(f'Insert the value in BRL to convert to {user}: ').strip() # .strip() funciona apenas com strings
    try:
        money = float(conv)
        print(f'{money:.2f} BRL converted to {user} is: {value(money , choice):.2f}\n') # chamei a funcao novamente
    except:
        print('Invalid value. Try again.')
        
    


    
 
