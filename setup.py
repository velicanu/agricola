import csv
import operator
import sys
import numpy as np

if(len(sys.argv)<6):
    print("usage:")
    print("python3 setup.py <nplayers> <nocc> <nmip> <eik> <e1 e3 ...>")
    exit(1)
players = int(sys.argv[1])
nocc = int(sys.argv[2])
nmip = int(sys.argv[3])
mipdecks = list(sys.argv[4])
decks = sys.argv[5:]
occupations = []
minorimp = []

# randperm occ deck
draw = []
with open('occupation.csv') as csvfile:
    occupations_ = csv.reader(csvfile)
    for row in occupations_:
        if(row and row[0] in decks):
            draw += row[1:]
            occupations.append(row)
draw = np.random.permutation(draw)

# randperm mip deck
mipdraw = []
with open('minor-improvements.csv') as csvfile:
    minorimp_ = csv.reader(csvfile)
    for row in minorimp_:
        if(row and row[0] in mipdecks):
            mipdraw += row[1:]
            minorimp.append(row)
mipdraw = np.random.permutation(mipdraw)

# draw cards for each player
hand = []
miphand = []
for player in range(players):
    print("P",player+1,"  occup  minor imp")
    for card in draw[nocc*player:nocc*(player+1)]:
        which = ""
        for row in occupations:
            if(card in row):
                which = row[0]
        hand.append([which,card])
    shand = sorted(hand, key=operator.itemgetter(0,1))
    # print(np.matrix(shand))
    hand.clear()
    # print("Player",player+1,"draw minor improvement cards:")
    for card in mipdraw[nmip*player:nmip*(player+1)]:
        which = ""
        for row in minorimp:
            if(card in row):
                which = row[0]
        miphand.append([which,card])
    smiphand = sorted(miphand, key=operator.itemgetter(0,1))
    # print(np.matrix(smiphand))
    print(np.concatenate((np.matrix(shand),np.matrix(smiphand)),1))
    hand.clear()
    miphand.clear()
    
