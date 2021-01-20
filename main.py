import random
import itertools
import math
import numpy as np


def main(num_of_flips, num_of_trials, fair_coin=True, power_of_two=False, varying_prob=False):
    '''Changes variables here based on each of the questions'''

    # Used for Q: 1, 2, 3, 4, 6, 7, 8 (modded flip_score mod manually to find answer for Q: 8)
    act_score, std_score = flip_coin(num_of_flips, num_of_trials, fair_coin)
    print("\nComputational Expected Score:", act_score, "\nStandard Deviation:", std_score)

    theor_score = mathematical_prob(num_of_flips)
    print("Calculated Expected Probability:", theor_score)

    perc_error = calc_error(act_score, theor_score)
    print("Percent Error: {}%".format(perc_error))

    # Used for Q: 5
    if power_of_two:
        probability = probability_power_of_two(num_of_flips)
        print("\nProbability Answer is a Power of Two:", probability)


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
    E = (q / p) * (((1 + p) ** n) - 1)
    return E


def calc_error(act_score, theor_score):
    err = ((act_score - theor_score) / theor_score) * 100
    return abs(err)


def find_best_heads(num_of_flips, num_of_trials):
    score_data = {}
    max_num = 0
    best = 0
    for i in range(0, 1001):
        for j in range(num_of_trials):
            score = 0
            scores = []
            flips = num_of_flips
            while flips != 0:
                flip = random.randint(0, 1000000)
                if flip <= (1000000 * (.001 * i)):
                    score += 1
                else:
                    score *= 2
                flips -= 1
            scores.append(score)
        average = average_scores(scores)
        if average > 500:
            print('{}%'.format(i * 0.1), average)
            perc = i * 0.1
            score_data[perc] = average

        if average > max_num:
            max_num = average
            best = i

    print('{}%'.format(best * 0.1), max_num)
    print(score_data)


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
    return math.log10(x) / math.log10(2)


def calc_std(data):
    return np.std(data)


if __name__ == "__main__":
    # unfair coin ==> 2/3 probability of heads, and a 1/3probability of tails

    # Q1 and Q2) Expected score after 5 flips, standard deviation
    main(num_of_flips=5, num_of_trials=1000000)

    # Q3 and Q4) Expected score after 15 flips, standard deviation
    #main(num_of_flips=100, num_of_trials=1000000)

    # Q5) Probability that the score is a power of two after 10 flips
    #main(num_of_flips=10, num_of_trials=1000000, power_of_two=True)

    # Q6 and Q7) expected score after 10 flips with unfair coin, standard deviation
    #main(num_of_flips=10, num_of_trials=1000000, fair_coin=False)

    # Q8) What probability of heads gives the highest expected score for 10 flips
    #find_best_heads(num_of_flips=10, num_of_trials=50000)
