
debugActive = False
#won combinations
wons=((1,3),(2,1),(3,2))
signs={1:"Rock", 2:"Paper", 3:"Scissors"}
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
def game():
    #collecting two unique player names
    players=[appVal("Please enter first player's name: "),appVal("Please enter second player's name: ")]
    if players[0] == players[1]:
        print("Please enter two different names")
        return game()

    def startlevel(levelnum, players):
        #starting level execution
        print("-=Level %s=-" %levelnum)
        question="{}, please enter your choice: \n1-Rock,  2-Paper, 3-Scissors:\t"
        #retrieving users choises
        choises = {pl:int(appVal(question.format(pl), 'int')) for pl in players}
        #appending results
        results.update({levelnum:choises})

    for n in range(1,5):
        startlevel(n,players)


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
            else: print("no one")

            print("Summary {} rounds".format(len(levelres)))
            print("{} won {} rounds, and {} won in {} rounds"
                  .format(players[0],count[players[0]],players[1],count[players[1]]))
            weapStat={s:{players[0]:0,players[1]:0} for s in signs}
            for res in results:
                print("Round {} choises: {} choosed {} and {} choosed {}, {} won"
                      .format(res,players[0],signs[results[res][players[0]]],players[1],signs[results[res][players[1]]],levelres[res]))
                #retrieving weapon statistics
                #{1: {'gopp': 1, 'fopp': 2}, 2: {'gopp': 3, 'fopp': 2}, 3: {'gopp': 3, 'fopp': 2},
                # 4: {'gopp': 1, 'fopp': 2}}

                for pl in results.values():
                    print(pl) #Player #weapon
                    for weap in pl.values():
                        print("its",pl)
                        for p in pl:
                            weapStat[weap][p]+=1
                        #weapStat[weap][pl]+=1


            print(weapStat)
                    #weapStat[val][players.index(val)] +=1

            #for we in weapStat:
            #    print("{} was used {} times".format(signs[we], weapStat[we]))
            #print(results)
        printRes(levelres, results)

    resultParse(results)
game()
