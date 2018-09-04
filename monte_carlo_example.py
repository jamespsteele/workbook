#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 17:43:07 2018

@author: cal
"""

import random
import matplotlib
import matplotlib.pyplot as plt

def rollDice():
    roll = random.randint(1, 100)
    if roll ==100:
        #print(roll, "Try Again")
        return False
    elif roll <= 50: 
        #print(roll, "Try Again")
        return False
    elif 100 > roll >= 50:
        #print(roll, "You Won")
        return True

def simple_gambler(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 0 
    while currentWager < wager:
        if rollDice():
            value += wager
            wX.append(currentWager)
            vY.append(value)
        else:
            value -= wager
            wX.append(currentWager)
            vY.append(value)
        currentWager += 1
        print("Funds: {}".format(value))
        
    plt.plot(wX, vY)
    
def doubler_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager
    global broke_count
    wX = []
    vY = []
    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager
    
    while currentWager <= wager_count:
        if previousWager == 'win':
            #print('last wager was won')
            if rollDice():
                value += wager
                #print(value)
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager
                previousWager = 'loss'
                #print(value)
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0 :
                    #print('we went broke after {} bets'.format(currentWager))
                    broke_count += 1
                    break
        elif previousWager == 'loss':
            #print('we lost - so doubleing down') 
            if rollDice():
                wager = previousWagerAmount * 2
                #print('we one {}'.format(wager))
                value += wager
                #print(value)
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2
                #print('we lost {}'.format(wager))
                value -= wager
                if value < 0: 
                    #print('we went broke after {} bets'.format(currentWager))
                    broke_count += 1
                    break
                #print(value)
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
        currentWager += 1
    #print(value)
    plt.plot(wX, vY)
    
    
xx = 0
broke_count = 0

while xx < 1000:
    doubler_bettor(10000, 100, 1000)
    xx += 1
                

#x = 0
#while x < 100:    
#    simple_gambler(10000, 100, 100)
#    x += 1


print('death rate: {} '.format(broke_count/float(xx) * 100))
print('survival rate: {} '.format(100 - (broke_count/float(xx)*100)))
plt.axhline(0, color = 'r')
plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()

