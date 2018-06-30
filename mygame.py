



variants={1:'Rock', 2:'Paper', 3:'Scissors'}

wons=[[1,3],[2,1],[3,2]]

results={}
def startgame():
    curlevel=0
    players = (input("Please enter first player's name "),
               input("Please enter second player's name "))

    def startlevel(levelnum, players):
        #helper - returns a player ho won
        def checkValidity(choises):
            #check validity of inputs
            for ch in list(choises):
                if int(choises[ch]) not in variants:
                    print("{},you wrong. Next time please be careful and choose a proper option".format(ch))
                    choises[ch]='disqualified'
            #updating results
            return{levelnum:choises}


            #for won, loose in wons:

            #return

        #starting level execution
        print("-=Level %s=-" %levelnum)
        question="{}, please enter your choice \n1-Rock,  2-Paper, 3-Scissors\t"
        #retrieving users choises
        choises = {pl:input(question.format(pl)) for pl in players}
        #appending results in table
        results.update(checkValidity(choises))

        print(results)
        #return(checkWhoWon(choises))


    for n in range(1,3):
        startlevel(n,players)



startgame()






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

