variants=('Rock', 'Paper', 'Scissors')

def checkvars(var1,var2):
    if var1 or var2 not in variants:
        return "Your variants are not allowed by rules, please retry"

    #initial equality check
    if var1 == var2:
        return
    #returns var that won
    if var1 == 'Rock':
        if var2 == 'Scissors':
            return var1
        if var2 == 'Paper':
            return var2
    elif var1 == 'Paper':
        if var2 == 'Rock':
            return var1
        if var2 == 'Scissors':
            return var2
    elif var1 == 'Scissors':
        if var2 == 'Paper':
            return var1
        if var2 == 'Rock':
            return var2
    else:
        return "Something went wrong - combination evaluation error"

#assigning players names
players={input("Please enter first player's name ") : 0,
input("Please enter second player's name "): 0 }

#turn execution
for player in players.keys():
    result ={}
    checkvars(var1, var2)