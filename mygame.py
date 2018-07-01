debugActive = False


#won combinations
wons=((1,3),(2,1),(3,2))
#defining of signs-identifiers
signs={1:"Rock", 2:"Paper", 3:"Scissors"}
#results of game levels
results={}
#counter for level assignment\execution control
levcountr=1

#helper for debug prints
def debug(prn):
    if debugActive:
        print(prn)
#helper for validating entering values
def appVal(question, valType='str'):
    while True:
        val = input(question)
        if valType == 'int':
            try:
                if int(val) not in range(1, 4):
                    print('Invalid choice')
                    continue
            #in case
            except ValueError:
                print('Invalid choice')
                continue
        if len(val) > 0:
            return val
#game function
def game(levcountr):
    #collecting two unique player names
    players=[appVal("Please enter first player's name: "),appVal("Please enter second player's name: ")]
    if players[0] == players[1]:
        print("Please enter two different names")
        return game(levcountr)


    def resultParse(results):
        levelres={}
        #return who won in one game turn
        def retrRes(choises):
            debug("starting to verify values {} vs {} "
                  .format(choises[players[0]],choises[players[1]]))
            if choises[players[0]] == choises[players[1]]:
                return("no one wons")
            if tuple([choises[players[0]],choises[players[1]]]) in wons:
                return(players[0])
            if tuple([choises[players[1]],choises[players[0]]]) in wons:
                return(players[1])
            #in case of unhandled state
            return None
        #retrieving per level results
        for level in results:
            levelres[level]=retrRes(results[level])

        #res analyzing
        def printRes(levelres,results):
            debug(levelres)
            #calculating results
            summary={}
            for pl in players:
                summary[pl]=list(levelres.values()).count(pl)
            if summary[players[0]] != summary[players[1]]:
                if (summary[players[0]]>summary[players[1]]):
                    print("The winner is %s." % players[0])
                else:
                    print("The winner is %s." % players[1])
            else: print("The winner is: no one.")

            print("Summary {} rounds".format(len(levelres)))
            print("{} won {} rounds, and {} won in {} rounds."
                  .format(players[0],summary[players[0]],players[1],summary[players[1]]))

            #displaying chises
            #preparing structure for weapon statistics
            weapStat = {s: {players[0]: 0, players[1]: 0} for s in signs}
            for res in results:
                print("Round {:<1} choises: {:<3} choosed {:<6} and {:<3} choosed {:<6}  - {} won!"
                      .format(res,players[0],signs[results[res][players[0]]],players[1],signs[results[res][players[1]]],levelres[res]))

                #collecting per player weapon statistics
                for pl in players:
                    plWeap=results[res][pl]
                    weapStat[plWeap][pl] += 1
            debug(weapStat)
            for weap in weapStat:
                for player in weapStat[weap]:
                    if weapStat[weap][player] > 0: #excluding unused weapons
                        print("The weapon {:<5} was used {:<2} times by {}.".format(signs[weap],weapStat[weap][player],player ))
        printRes(levelres, results)

    #level execution - survey and results collection
    def startlevel(levcountr, players):
        #starting level execution
        print("-=Level %s=-" %levcountr)
        question="{}, please enter your choice: \n1-Rock,  2-Paper, 3-Scissors:\t"
        #retrieving users choises
        choises = {pl:int(appVal(question.format(pl), 'int')) for pl in players}
        #appending results
        results.update({levcountr:choises})
       #recursive reexecution

        while True:
            userCont = input("Do you want another round? (y/n)")
            if userCont.lower() not in ("y","n"):
                continue
            if userCont.lower() == "y":
                levcountr += 1
                startlevel(levcountr, players)
                break
            if userCont.lower() == "n":
                break

    #executing first level
    if levcountr == 1:
        startlevel(levcountr, players)

    resultParse(results)

game(levcountr)
