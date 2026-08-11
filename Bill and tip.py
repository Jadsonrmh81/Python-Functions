def tip(bill):
    return bill

customer = input('Insert the value of the bill: ').strip()

try:
    value = float(customer)
    if value >= 100:
       print(f'Bill: ${value:.2f}')
       print(f'Tip: ${tip(value * 0.10):.2f}')
    else:
       print(f"Bill: ${value:.2f}")
       print(f'Tip: ${tip(value * 0.5):.2f}')
except:
      print('Something wrong. Try again.')

        
# E sim: você conseguiu. Desta vez, o mais importante nem é o programa estar perfeito; 
# é você ter olhado para ele e pensado "espera, isso aqui está errado" e conseguido ajustar 
# sem depender da resposta.

# Esse programa é a prova viva do seu aprendizado.


