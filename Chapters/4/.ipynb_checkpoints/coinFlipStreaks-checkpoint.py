#!/usr/bin/python3

'''
Coin Flip Streaks
For this exercise, we’ll try doing an experiment. If you flip a coin 100 times and write down an “H” for each heads and “T” for each tails, you’ll create a list that looks like “T T T T H H H H T T.” If you ask a human to make up 100 random coin flips, you’ll probably end up with alternating head-tail results like “H T H T H H T H T T,” which looks random (to humans), but isn’t mathematically random. A human will almost never write down a streak of six heads or six tails in a row, even though it is highly likely to happen in truly random coin flips. Humans are predictably bad at being random.

Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails. Your program breaks up the experiment into two parts: the first part generates a list of randomly selected 'heads' and 'tails' values, and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row. As a hint, the function call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.

You can start with the following template:

import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.

    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))

Of course, this is only an estimate, but 10,000 is a decent sample size. Some knowledge of mathematics could give you the exact answer and save you the trouble of writing a program, but programmers are notoriously bad at math.

'''
EXPERIMENTNUMBERMAX=10000 # originally 10000
COINFLIPMAX=100
TARGETSTREAKLENGTH=6

import random
numberOfStreaks = 0
for experimentNumber in range(EXPERIMENTNUMBERMAX):
    coin_flip_list = [] # create a new list to store coin flips        
    # Code that creates a list of 100 'heads' or 'tails' values.
    for _ in range(COINFLIPMAX):
        if random.randint(0,1)%2 == 0: # If even assign heads.
            coin_flip_list.append("H")
        else: # else odd, assign tails.
            coin_flip_list.append("T")
    # Code that checks if there is a streak of 6 heads or tails in a row.
    streaks = {}
    for flip in enumerate(coin_flip_list):
        # returns form (0, 'H')
        if streaks: # if dict not empty
            # compare values
            if flip[1] == starting_HorT: # current flip matches prvious flip, extend the streak
                streak_length += 1
                streaks.update({(starting_index,starting_HorT): streak_length})
            else: #current flip does not match previous flip, start new streak and new starting point.
                streak_length = 1
                starting_index = flip[0]
                starting_HorT = flip[1]
                streaks.setdefault(flip, streak_length)            
        else: #dict is empty and just starting
            streak_length = 1
            start = flip #unneccesssary?
            current_index = flip[0] #unneccesssary?
            current_HorT = flip[1] #unneccesssary?
            starting_index = flip[0]
            starting_HorT = flip[1]
            streaks.setdefault(flip, streak_length)
        #do something at the end????
    numberOfStreaks += sum(1 for v in streaks.values() if v == TARGETSTREAKLENGTH)    
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
