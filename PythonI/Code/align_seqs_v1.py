#!/usr/bin/env python3

"""Module that takes in a TXT containing two DNA sequences and outputs a TXT
file containing the best alignment along with its score. Input TXT must be in
the current working directory. Output TXT will be saved in current working
directory."""
__author__ = 'Michael Jordan (mgj23@imperial.ac.uk)'
__version__ = '0.0.1'

import random

def import_dna(x):
    # Open a file and create a list with one item for each line.
    with open(x, "r") as f:
        lines = [line.rstrip() for line in f]
    return lines

# Function to pick which line of DNA is shorter and which is longer. Returns
# sequences plus length of each.
def assign_lines(x):
    seq1 = x[0]
    seq2 = x[1]
    # Assign the longer sequence s1, and the shorter to s2
    # l1 is length of the longest, l2 that of the shortest
    l1 = len(seq1)
    l2 = len(seq2)
    if l1 >= l2:
        s1 = seq1
        s2 = seq2
    else:
        s1 = seq2
        s2 = seq1
        l1, l2 = l2, l1 # swap the two lengths
    return l1, l2, s1, s2

# A function that computes a score by returning the number of matches starting
# from arbitrary startpoint (chosen by user)
def create_alignment(s1, s2, l1, l2, startpoint):
    matched = "" # to hold string displaying alignements
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]: # if the bases match
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"

    return ["." * startpoint + matched, "." * startpoint + s2, s1, score]

# Creates all alignments for two DNA sequences and returns the best. If there
# is a tie, best alignment is picked at random among highest scoring
# alignments.
def find_best_alignment(x, y):
    vars = assign_lines(import_dna(x))
    l1 = vars[0]
    l2 = vars[1]
    s1 = vars[2]
    s2 = vars[3]
    collect_results = []

    for i in range(l1): # Note that you just take the last alignment with the highest score
        collect_results.append(create_alignment(s1, s2, l1, l2, i))
    
    max_score = 0

    for i in range(len(collect_results)):
        if collect_results[i][3] > max_score:
            max_score = collect_results[i][3]

    collect_results_two = []    

    for i in range(len(collect_results)):
        if collect_results[i][3] == max_score:
            collect_results_two.append(collect_results[i])

    final_alignment = random.choice(collect_results_two)
    with open(y, "a") as f:
        for i in final_alignment:
            f.write(str(i) + "\n")

find_best_alignment("test_dna.txt", "test_dna_results.txt")