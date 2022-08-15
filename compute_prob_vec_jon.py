import numpy as np

def vectorized_stuff(i):
    N = 10**i
    r = np.random.random(N)
    r1 = r[r>=0.5]
    r1 = r1[r1<=0.6]
    return len(r1)/float(N)*100


if __name__=="__main__":

    print "%g percent probability of falling in the interval."\
    % vectorized_stuff(1),"\n"

    print "%g percent probability of falling in the interval."\
    % vectorized_stuff(2),"\n"

    print "%g percent probability of falling in the interval."\
    % vectorized_stuff(3),"\n"

    print "%g percent probability of falling in the interval."\
    % vectorized_stuff(6),"\n"

"""
1x-193-157-194-32:uke12 Jon$ python compute_prob_vec.py
"""
