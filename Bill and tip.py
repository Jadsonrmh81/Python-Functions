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

        



