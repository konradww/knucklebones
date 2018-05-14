#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
#  draw lots (random.sample(xrange(1,7), 6)
class Games(object):
    playerPoints = int(0)
    historyRandom = []
    resultThrow = []
    resultThrowOne = []
    itemRepeatThrow = str("start")
    itemOne = -1
    resultItemOne = -1
    itemTwo = -1
    resultItemTwo = -1
    itemThree = -1
    resultItemThree = -1
    itemFour = -1
    resultItemFour = -1
    itemFive = -1
    resultItemFive = -1
    itemSix = -1
    resultItemSix = -1
    # poker
    StraightFlush = -1
    resultStraightFlush = -1
    # four same cards
    Four_of_a_kind = -1
    resultFour_of_a_kind = -1
    full = -1
    # full
    resultFull = -1
    # 2,3,4,5,6
    Big_straight = -1
    resultBig_straight = -1
    # 1,2,3,4,5
    Little_straight = -1
    resultLittle_straight = -1
    # 3 same cards
    Three_of_a_kind = -1
    resultThree_of_a_kind = -1
    help = -1
    # all points
    resultHelp = -1

    def throw(self):
        # python xrange
        for x in range(1, 6):
            self.resultThrow.append(random.randint(1, 6))
        x = []
        x = sorted(self.resultThrow)
        self.resultThrow = x
        print("One Random: {}".format(self.resultThrow))

    def repeatThrow(self):
        userCheckItem = []
        # Enter numbers from 1 to 6, exit q, you can enter the loop again after the draw.
        self.itemRepeatThrow = "start"
        while self.itemRepeatThrow != "q":
            # while len(userCheckItem) < 5:
            try:
                # raw_input python2
                self.itemRepeatThrow = (input('Wprowadz numer kostki, jesli chcesz zakonczyc wybierasz(q)'))
                if int(self.itemRepeatThrow) > 0 and int(self.itemRepeatThrow) < 6 and (int(self.itemRepeatThrow) not in userCheckItem) == True:
                    self.resultThrow[int(self.itemRepeatThrow)-1] = random.randint(1, 6)
                    userCheckItem.append(int(self.itemRepeatThrow))
                    # print(self.itemRepeatThrow, userCheckItem)
                elif int(self.itemRepeatThrow) <= 0 or int(self.itemRepeatThrow) >= 6:
                    print("You choice bad number")

                elif int(self.itemRepeatThrow) in userCheckItem == True:
                    print("You have already thrown this dice.")

                else:
                    print("You choice bad number")
            except ValueError:
                if self.itemRepeatThrow == "q":
                    print("Random closed.")
                else:
                    print("error")
            # print("Cube changed>> %n" % userCheckItem)
            # if you have already selected all 5 cubes, finish the loop.
            if len(userCheckItem) == 5: 
                self.itemRepeatThrow = "q"
        print("Result: %i")
        # print (self.historyRandom[len(self.historyRandom)-1])
        # print("3+2x(F)") !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.historyRandom.append(sorted(self.resultThrow))
        self.resultThrow  =[]
        userCheckItem = []
        itemRepeatThrow = "start"
    
    def checkRandom(self):
        print(self.historyRandom[len(self.historyRandom)-1])
        if self.help < 0:
            self.help = 0
            for i in range(5):
                self.help = + self.historyRandom[-1][i]
            if  self.resultHelp == -1:
                print("Help(R): %i" % self.help)
        if self.itemOne < 0:
            self.itemOne = 0
            for i in range(5):
                if self.historyRandom[-1][i] == 1:
                    self.itemOne = + 1
            if self.resultItemOne == -1 and self.itemOne>0:
                print("itemOne %i" % self.itemOne)
        if self.itemTwo < 0:
            self.itemTwo = 0
            for i in range(5):
                if self.historyRandom[-1][i] == 2:
                    self.itemTwo = + 2
            if  self.resultItemTwo == -1 and self.itemTwo>0:
                print("itemTwo %i" % self.itemTwo)
        if self.itemThree < 0:
            self.itemThree = 0
            for i in range(5):
                if self.historyRandom[-1][i] == 3:
                    self.itemThree = + 3
            if self.resultItemThree == -1 and self.itemThree > 0:
                print("itemThree %i" % self.itemThree)

        if self.itemFour < 0:
            self.itemFour = 0
            for i in range(5):
                if self.historyRandom[-1][i] == 4:
                    self.itemFour = + 4
            if  self.resultItemFour == -1 and self.itemFour>0:
                print("itemFour %i" % self.itemFour)

        if self.itemFive < 0:
            self.itemFive = 0
            for i in range(5):
                if self.historyRandom[-1][i] == 5:
                    self.itemFive = + 5
            if  self.resultItemFive == -1 and self.itemFive>0:
                print("itemFive %i" % self.itemFive)

        if self.itemSix < 0:
            self.itemSix = 0
            for i in range(5):
                if self.historyRandom[-1][i] == 6:
                    self.itemSix = + 6
            if  self.resultItemSix == -1 and self.itemSix>0:
                print("itemSix %i" % self.itemSix)

        if self.Four_of_a_kind < 0:
            if self.itemSix == 24 or self.itemFive == 20 or self.itemFour == 16 or self.itemThree == 12 or self.itemTwo == 8 or self.itemOne == 4:
                print("Four_of_a_kind(K)")
                self.Four_of_a_kind = 40

        if self.Little_straight < 0:
            if self.itemSix == 6 and self.itemFive == 5 and self.itemFour == 4 and self.itemThree == 3 and self.itemTwo == 2:
                print("Little_straight(L)")
                self.Little_straight = 30
        if self.Big_straight < 0:
            if self.itemFive == 5 and self.itemFour == 4 and self.itemThree == 3 and self.itemTwo == 2 and self.itemOne == 1:
                print("Big_straight(B)")
                self.Big_straight = 40
        if self.StraightFlush < 0:
            if self.itemSix == 30 and self.itemFive == 25 and self.itemFour == 20 and self.itemThree == 15 and self.itemTwo == 10 and self.itemOne == 5:
                self.StraightFlush = 50

        if self.Three_of_a_kind < 0:
            # xrange python 2
            for x in range(1, 6):
                if self.historyRandom[-1].count(x) >= 3:
                    print("Three_of_a_kind(P)")
                    self.resultThree_of_a_kind = 15
                    # I have to check how many points the player will get for 3 same cards.
        if self.full < 0:
            for x in range(1, 6):
                # print(self.historyRandom[-1]
                if self.historyRandom[-1].count(x) == 3:
                    for x in range(1, 6):
                        if self.historyRandom[-1].count(x) == 2:
                            self.full = 25


    def ChoiceItem(self):
        resultX = ""
        while resultX == "":
            resultX = (input('Zapisz wynik do tabeli:'))
            if resultX == "1" and self.resultItemOne < 0:
                self.resultItemOne = self.itemOne
                self.playerPoints = + self.resultItemOne
                self.itemSix = -1
                self.itemFive = -1
                self.itemFour = -1
                self.itemThree = -1
                self.itemTwo = -1
                self.itemOne = -1
                self.help = -1
                self.Three_of_a_kind = -1
                self.Four_of_a_kind = -1
                self.full = -1
                self.Little_straight = -1
                self.Big_straight = -1
                self.StraightFlush = -1
            if resultX == "2" and self.resultItemTwo < 0:
                self.resultItemTwo = self.itemTwo
                self.playerPoints = + self.resultItemTwo
                self.itemSix = -1
                self.itemFive = -1
                self.itemFour = -1
                self.itemThree = -1
                self.itemTwo = -1
                self.itemOne = -1
                self.help = -1
                self.Three_of_a_kind = -1
                self.Four_of_a_kind = -1
                self.full = -1
                self.Little_straight = -1
                self.Big_straight = -1
                self.StraightFlush = -1
            if resultX == "3" and self.resultItemThree < 0:
                self.resultItemThree = self.itemThree
                self.playerPoints = + self.resultItemThree
                self.itemSix = -1
                self.itemFive = -1
                self.itemFour = -1
                self.itemThree = -1
                self.itemTwo = -1
                self.itemOne = -1
                self.help = -1
                self.Three_of_a_kind = -1
                self.Four_of_a_kind = -1
                self.full = -1
                self.Little_straight = -1
                self.Big_straight = -1
                self.StraightFlush = -1
            if resultX == "4" and self.resultItemFour < 0:
                self.resultItemFour = self.itemFour
                self.playerPoints = + self.resultItemFour
                self.itemSix = -1
                self.itemFive = -1
                self.itemFour = -1
                self.itemThree = -1
                self.itemTwo = -1
                self.itemOne = -1
                self.help = -1
                self.Three_of_a_kind = -1
                self.Four_of_a_kind = -1
                self.full = -1
                self.Little_straight = -1
                self.Big_straight = -1
                self.StraightFlush = -1
            if resultX == "5" and self.resultItemFive < 0:
                self.resultItemFive = self.itemFive
                self.playerPoints = + self.resultItemFive
                self.itemSix = -1
                self.itemFive = -1
                self.itemFour = -1
                self.itemThree = -1
                self.itemTwo = -1
                self.itemOne = -1
                self.help = -1
                self.Three_of_a_kind = -1
                self.Four_of_a_kind = -1
                self.full = -1
                self.Little_straight = -1
                self.Big_straight = -1
                self.StraightFlush = -1
            if resultX == "6" and self.resultItemSix < 0:
                self.resultItemSix = self.itemSix
                self.playerPoints = + self.resultItemSix
                self.itemSix = -1
                self.itemFive = -1
                self.itemFour = -1
                self.itemThree = -1
                self.itemTwo = -1
                self.itemOne = -1
                self.help = -1
                self.Three_of_a_kind = -1
                self.Four_of_a_kind = -1
                self.full = -1
                self.Little_straight = -1
                self.Big_straight = -1
                self.StraightFlush = -1

            if resultX == "R" and self.resultHelp < 0:
                self.resultHelp = self.help
                self.playerPoints = + self.resultHelp
                self.itemSix = -1
                self.itemFive = -1
                self.itemFour = -1
                self.itemThree = -1
                self.itemTwo = -1
                self.itemOne = -1
                self.help = -1
                self.Three_of_a_kind = -1
                self.Four_of_a_kind = -1
                self.full = -1
                self.Little_straight = -1
                self.Big_straight = -1
                self.StraightFlush = -1
            else:
                print("To pole zostało już wypełnione")
                # flaga, nie bedzie mozna zakonczyc petli wyboru
                flaga = 1 
            if resultX == "K":
                self.resultFour_of_a_kind = self.Four_of_a_kind
                self.playerPoints = + 30
                self.itemSix = -1
                self.itemFive = -1
                self.itemFour = -1
                self.itemThree = -1
                self.itemTwo = -1
                self.itemOne = -1
                self.help = -1
                self.Three_of_a_kind = -1
                self.Four_of_a_kind = -1
                self.full = -1
                self.Little_straight = -1
                self.Big_straight = -1
                self.StraightFlush = -1

            if resultX == "T":
                self.resultThree_of_a_kind = self.Three_of_a_kind
                self.playerPoints = + 15
                self.itemSix = -1
                self.itemFive = -1
                self.itemFour = -1
                self.itemThree = -1
                self.itemTwo = -1
                self.itemOne = -1
                self.help = -1
                self.Three_of_a_kind = -1
                self.Four_of_a_kind = -1
                self.full = -1
                self.Little_straight = -1
                self.Big_straight = -1
                self.StraightFlush = -1

            if resultX == "F" and self.resultFull < 0:
                self.resultFull = self.full
                self.playerPoints = + 25
                self.Pair = -1
                self.Three = -1
                self.Big_straight = -1
                self.Little_straight = -1
                self.Four_of_a_kind = -1
                self.help = -1
                self.itemSix = -1
                self.itemFive = -1
                self.itemFour = -1
                self.itemThree = -1
                self.itemTwo = -1
                self.itemOne = -1
                self.StraightFlush = -1
                self.full = -1

            if resultX == "L" and self.resultLittle_straight < 0:
                self.resultLittle_straight = self.full
                self.playerPoints = + 25
                self.Pair = -1
                self.Three = -1
                self.Big_straight = -1
                self.Little_straight = -1
                self.Four_of_a_kind = -1
                self.help = -1
                self.itemSix = -1
                self.itemFive = -1
                self.itemFour = -1
                self.itemThree = -1
                self.itemTwo = -1
                self.itemOne = -1
                self.StraightFlush = -1
                self.full = -1

            if resultX == "L" and self.resultBig_straight < 0:
                self.resultBig_straight = self.full
                self.playerPoints = + self.playerPoints
                self.Pair = -1
                self.Three = -1
                self.Big_straight = -1
                self.Little_straight = -1
                self.Four_of_a_kind = -1
                self.help = -1
                self.itemSix = -1
                self.itemFive = -1
                self.itemFour = -1
                self.itemThree = -1
                self.itemTwo = -1
                self.itemOne = -1
                self.StraightFlush = -1
                self.full = -1

            if resultX == "P" and self.resultStraightFlush < 0:
                self.resultStraightFlush = self.StraightFlush
                self.playerPoints = + 50
                self.help = -1
                self.itemSix = -1
                self.itemFive = -1
                self.itemFour = -1
                self.itemThree = -1
                self.itemTwo = -1
                self.itemOne = -1
                self.StraightFlush = -1
                self.full = -1

    def CurrentResult(self):
        print("one:", self.resultItemOne,
              "two:", self.resultItemTwo,
              "three:",self.resultItemThree,
              "four:", self.resultItemFour,
              "five:", self.resultItemFive,
              "six:", self.resultItemSix)
        print("Help:", self.resultHelp,
              "\nresultFull:", self.resultFull,
              "\nThree of a kind", self.resultThree_of_a_kind,
              "\nFour of a kind:", self.resultFour_of_a_kind,
              "\nPoker:", self.resultStraightFlush)

        print('*' * self.playerPoints)
        print("result: %i" % self.playerPoints)
        print('*' * self.playerPoints)


object1 = Games()

for x in range(0, 4):
    object1.throw()
    object1.repeatThrow()
    object1.checkRandom()
    object1.ChoiceItem()
    object1.CurrentResult()


