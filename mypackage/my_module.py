from math import sqrt
import numpy as np


def standard_mean_error(y):

    '''
    returns the standard mean error of an experiment
    Args:
        y: A list of all the values of an experiment
    return:
        A floating point number of the standard mean error
    for example:

        mean_standard error([31.7, 29.6, 28.8, 30.6, 29.5, 28.9, 30.4, 29.2, 30.8, 29.9]) == 0.29645621965288455

    '''

    N = len(y) #A constant representing the number of experiments
    standard_deviation = np.std(y)


    error = sqrt(standard_deviation)/sqrt(N)


    return error

print(f'the mean standard error is {standard_mean_error([31.7, 29.6, 28.8, 30.6, 29.5, 28.9, 30.4, 29.2, 30.8, 29.9])}')


