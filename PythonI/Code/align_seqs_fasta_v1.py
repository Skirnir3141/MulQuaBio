#!/usr/bin/env python3

"""Module that takes in any two given fasta files, aligns them, and outputs the
best alignment as a third file."""
__author__ = 'Michael Jordan (mgj23@imperial.ac.uk)'
__version__ = '0.0.1'

import sys
import random
import os
import doctest

# Import a fasta and output full sequence as one variable.
def import_dna(x):
    """
    >>> import_dna("test1.fasta")
    'ATCGCCGGATTACGGG'
    """
    with open(x, "r") as f:
        seq = ""
        f2 = f.readlines()[1:]
        for line in f2:
            seq = seq + line.strip()
    return seq

# Function to pick which line of DNA is shorter and which is longer. Returns
# sequences plus length of each.
def assign_lines(x, y):
    """
    >>> assign_lines("ATCGCCGGATTACGGG", "CAATTCGGAT")
    (16, 10, 'ATCGCCGGATTACGGG', 'CAATTCGGAT')
    """
    seq1 = x
    seq2 = y
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
def find_best_alignment(x="test1.fasta", y="test2.fasta"):
    # Pull in sequences and determine which is longer.
    vars = assign_lines(import_dna(x), import_dna(y))
    l1 = vars[0]
    l2 = vars[1]
    s1 = vars[2]
    s2 = vars[3]
    collect_results = []

    # Create a list of all alignments.
    for i in range(l1):
        collect_results.append(create_alignment(s1, s2, l1, l2, i))
    
    # Determine max score across alignments.
    max_score = 0
    for i in range(len(collect_results)):
        if collect_results[i][3] > max_score:
            max_score = collect_results[i][3]

    # Collect all alignments that have a score equal to the max score.
    collect_results_two = []    
    for i in range(len(collect_results)):
        if collect_results[i][3] == max_score:
            collect_results_two.append(collect_results[i])

    # Pick an alignment at random among best alignments.
    final_alignment = random.choice(collect_results_two)

    # Save best alignment in a new file.
    with open(
        os.path.splitext(x)[0] + "_" + os.path.splitext(y)[0] + "_" +
            "alignment.txt",
        "a") as f:
        for i in final_alignment:
            f.write(str(i) + "\n")

def main(argv):
    if len(sys.argv) > 1:
        find_best_alignment(sys.argv[1], sys.argv[2])
    else:
        find_best_alignment()

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)