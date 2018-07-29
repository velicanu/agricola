import csv
import operator
import sys
import numpy as np
# import pandas as pd

decks = sys.argv[2:]
players = int(sys.argv[1])
occupations = []
# both = [x in a for x in b]

# print(sys.argv)
draw = []
with open('occupation.csv') as csvfile:
    occupations_ = csv.reader(csvfile)
    for row in occupations_:
        if(row and row[0] in decks):
            draw += row[1:]
            occupations.append(row)
        # print(row)
        # print(np.random.permutation(row[1:]))
        # if("216" in row):
            # print(row[0],"contains",216)
draw = np.random.permutation(draw)
hand = []

for player in range(players):
    print("Player",player+1,"draw occupation cards:")
    for card in draw[7*player:7*(player+1)]:
        which = ""
        for row in occupations:
            if(card in row):
                which = row[0]
        hand.append([which,card])
    shand = sorted(hand, key=operator.itemgetter(0,1))
    print(np.matrix(shand))
    hand.clear()
# print(hand)
# print(shand)
# print(draw)
# print(draw[0:7])
# print(draw[7:14])
