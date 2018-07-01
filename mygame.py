run = True
debugActive = False
levcountr=0
#won combinations
wons=((1,3),(2,1),(3,2))
#defining of signs-identifiers
signs={1:"Rock", 2:"Paper", 3:"Scissors"}

results={}
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
            count={}
            for pl in players:
                count[pl]=list(levelres.values()).count(pl)
            if count[players[0]] != count[players[1]]:
                if (count[players[0]]>count[players[1]]):
                    print("The winner is %s" % players[0])
                else:
                    print("The winner is %s" % players[1])
            else: print("The winner is: no one")

            print("Summary {} rounds".format(len(levelres)))
            print("{} won {} rounds, and {} won in {} rounds"
                  .format(players[0],count[players[0]],players[1],count[players[1]]))

            #displaying chises
            #preparing structure for weapon statistics
            weapStat = {s: {players[0]: 0, players[1]: 0} for s in signs}
            for res in results:
                print("Round {:<1} choises: {:<3} choosed {:<9} and {:<3} choosed {:<9}  {} won"
                      .format(res,players[0],signs[results[res][players[0]]],players[1],signs[results[res][players[1]]],levelres[res]))

                #collecting per player weapon statistics
                for pl in players:
                    plWeap=results[res][pl]
                    weapStat[plWeap][pl] += 1
            debug(weapStat)
            for weap in weapStat:
                for player in weapStat[weap]:
                    print("The weapon {:<9} was used {:<2} times by {:^5}".format(signs[weap],weapStat[weap][player],player ))
        printRes(levelres, results)

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
            print(userCont.lower()== "y")
            if userCont.lower() != "y" or userCont.lower() != "n":
                print("user answer",userCont.lower())
                break
            if userCont.lower() == "y":
                levcountr += 1
                startlevel(levcountr, players)
            if userCont.lower() == "n":
                return

    #executing level
    print(levcountr)
    if levcountr == 0:
        startlevel(levcountr, players)

    resultParse(results)

game(levcountr)
