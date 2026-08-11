while True:
    def greetings(name):
        greetings()
        
    print('hello human')
    user = input('').lower().strip()
    if user == 'exit':
        print('program finished')
        break
    
    # função def SEMPRE fora do loop
    # o loop repete a função várias vezes, por isso dá erro