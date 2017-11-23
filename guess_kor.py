import random as rand
print('created for shajid (not shazid)')
print('1 theke 9 er moddhe ekta number lekh !')
bad_exp = ['dhur bolod !','haire abailla !','tore dia hoibo na !','tui moira ja !']
good_exp = ['shabash beta !','tui to legend !','hmm hoise !']
running = True
while running:
    value = int(rand.randrange(1, 9))
    print(value)
    user_guess = int(input('>'))
    if user_guess == value:
        print(rand.choice(good_exp))
    elif user_guess <= value:
        if user_guess > 0:
            print(rand.choice(bad_exp))
        else:
            print('ki ulta palta lekhos !')
    elif user_guess >= value:
        if user_guess < 10:
            print(rand.choice(bad_exp))
        else:
            print('ki ulta palta lekhos !')
