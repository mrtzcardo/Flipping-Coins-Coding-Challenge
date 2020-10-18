'''We are going to play a simple game. We start with 0 points. 
We will flip a coin. If it comes up heads, we get a point. 
If comes up tails, we double our current score.'''
import random
import itertools
import math
import numpy as np

def main():
    '''Changes variables here based on each of the questions'''
    num_of_flips = 100
    num_of_trials = 1000000
    fair_coin = True

    # Used for Q: 1, 2, 3, 4, 6, 7, 8 (modded flip_score mod manually to find answer for Q: 8)
    act_score, std_score = flip_coin(num_of_flips, num_of_trials, fair_coin)
    print("\nComputational Expected Score:", act_score, "\nStandard Deviation:", std_score)

    # Used for Q: 5
    #probability = probability_power_of_two(num_of_flips)
    #print("Probability:", probability)

    # Attempted to use for Q: 8
    #max, count = find_best_heads(num_of_flips)
    #print(max, count)

    theor_score = mathematical_prob(num_of_flips)
    print("Calculated Expected Probability:", theor_score)

    perc_error = calc_error(act_score, theor_score)
    print("Percent Error: {}%\n".format(perc_error))

def flip_coin(num_of_flips, num_of_trials, fair_coin, find_best_head=False):
    scores = []

    while num_of_trials != 0:
        scores.append(flip_score(num_of_flips, fair_coin))
        num_of_trials -= 1
    
    average = average_scores(scores)
    std = calc_std(scores)

    return average, std


def flip_score(num_of_flips, fair_coin):
    score = 0
    if fair_coin:
        while num_of_flips != 0:
            flip = (random.randint(0, 1000000)) % 2
            if flip == 0:
                score += 1
            elif flip == 1:
                score = score * 2
            num_of_flips -= 1
        return score

    else:
        while num_of_flips != 0:
            flip = (random.randint(0, 1000000)) % 3
            if flip == 0:
                score += 1
            else:
                score = score * 2
            num_of_flips -= 1
        return score

def mathematical_prob(num_of_flips):
    n = num_of_flips
    q = .5
    p = .5
    E = (q/p) * (((1+p)**n) - 1)
    return E

def calc_error(act_score, theor_score):
    err = ((act_score - theor_score) / theor_score) * 100
    return abs(err)

'''
wasn't working correctly
def find_best_heads(num_of_flips):
    flips = num_of_flips
    max = 0
    count = 3
    while True:
        trial = 1000000
        scores = []
        score = 0
        average = 0
        num_of_flips = flips
        while trial != 0:
            while num_of_flips != 0:
                flip = (random.randint(0, 1000000)) % count
                if flip == 0:
                    score += 1
                else:
                    score = score * 2
                num_of_flips -= 1
            scores.append(score)
            trial -= 1
        average = average_scores(scores)
        #print(average, count)
        if average > max:
            max = average
            count += 1
            print(max, average, count)
        '''
        

def average_scores(scores):
    total_score = 0
    for score in scores:
        total_score += score

    average_score = total_score / len(scores)

    return average_score

def probability_power_of_two(num_of_flips):
    combinations = all_combinations(num_of_flips)
    scored_combinations = score_combinations(combinations)
    count = count_power_of_two(scored_combinations)
    return count / (2 ** num_of_flips)

def all_combinations(num_of_flips):
    # returns a list of lists containing every possible combination
    return list(map(list, itertools.product([0, 1], repeat=num_of_flips)))


def score_combinations(list_of_combinations):
    # returns a list of scores for each combination in list
    possible_scores = []
    for combination in list_of_combinations:
        score = 0
        for flip in combination:
            if flip == 1:
                score += 1
            elif flip == 0:
                score = score * 2 
        possible_scores.append(score)
    return possible_scores


def count_power_of_two(list_of_scores): 
    power_of_two_scores = 0
    for score in list_of_scores:
        if score == 0:
            pass
        elif math.ceil(log_2(score)) == math.floor(log_2(score)):
                power_of_two_scores += 1
    return power_of_two_scores


def log_2(x): 
    return (math.log10(x) / math.log10(2))


def calc_std(data):
    return np.std(data)

if __name__ == "__main__":
    main()
    