debugActive = True
#possible choise variants
variants={1:'Rock', 2:'Paper', 3:'Scissors'}
#won combinations
wons=((1,3),(2,1),(3,2))
results={}

#debug prints
def debug(prn):
    if debugActive:
        print(prn)

#helper for validating entering values
def appVal(question, valType='str'):
    while True:
        val = input(question)
        if valType == 'int':
            try:
                int(val)
            except ValueError:
                print('Invalid choice')
                continue
        if len(val) > 0:
            return val

#game function
def game():
    #collecting two unique player names
    players=[appVal("Please enter first player's name: "),appVal("Please enter second player's name: ")]
    if players[0] == players[1]:
        print("Please enter two different names")
        return game()

    def startlevel(levelnum, players):
        #helper - returns a player ho won
        def checkValidity(choises):
            #check validity of inputs
            for ch in list(choises):
                if int(choises[ch]) not in variants:
                    print("{}, you wrong. Next time please be careful and choose a proper option".format(ch))
                    choises[ch]='disqualified'
            return{levelnum:choises}
        #starting level execution

        print("-=Level %s=-" %levelnum)
        question="{}, please enter your choice: \n1-Rock,  2-Paper, 3-Scissors:\t"
        #retrieving users choises
        choises = {pl:int(appVal(question.format(pl), 'int')) for pl in players}
        #appending results
        results.update(checkValidity(choises))

    for n in range(1,3):
        startlevel(n,players)

    def resultParse(results):
        levelres={}
        #return who won
        def retrRes(choises):
            debug("starting to verify values {} vs {} ".format(choises[players[0]],choises[players[1]]))
            if choises[players[0]] == choises[players[1]]:
                return("no one wons")
            elif tuple([choises[players[0]],choises[players[1]]]) in wons:
                return(players[0]+ " wons")
            elif tuple([choises[players[1]],choises[players[0]]]) in wons:
                return(players[1]+ " wons")
            return
        for level in results:
            levelres[level]=retrRes(results[level])
        debug(levelres)
    resultParse(results)

game()

