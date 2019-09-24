#!/usr/bin/python3

# The line above tells the computer which interpreter the script was written for

# This program demonstrates how to read a FASTA file and do some
# simple processing of the sequence
#
# A FASTA file in a plain text file containing sequences
# A line begining with a ">" indicates a label
# all other lines below a label (they do not start with ">") contain the
# sequence for that label

# Change this to use your own file.
file_name = "BRCA1_variant1_FASTA.txt" 

# open takes in a file name and 'opens' it for reading (r) or writing (w)
input_file = open(file_name, 'r')

# The first line of a fasta file contains information about the sequence
# that follows
# readline is a method that acts on a file and returns a string
# strip is a method that acts on a string and returns a string
seq_info = input_file.readline().strip()
sequence = ''

for line in input_file:
    # Strip is a method that will remove trailing whitespace from a string
    sequence += line.strip()

# **Always** close files you have opened
input_file.close()

# Converts all Nucleotides to upper-case using built in string methods

# With the above code, we should include the header of the sequence FASTA file, otherwise we will lose the seq_info
sequence = sequence.upper()
print("------------------------------------------")
print("Loaded Sequence Info: ", seq_info)
print("------------------------------------------")
print("Sequence: ", sequence)

# translate is a method that takes in a translation table
comp_sequence = sequence.translate(str.maketrans("ACGT","TGCA"))
# Use slicing to reverse the sequence
rev_comp_seq   = comp_sequence[::-1]

print("------------------------------------------")
print("Reverse Complement sequence:", rev_comp_seq)

# Functions are designated by the 'def' keyword and a series of statements
# that are indented by white space. Functions are convenient for performing
# long tasks more than once.
def sequence_stats(input_sequence, sequence_title):
    ''' This function returns sequence statistics on an input sequence '''
    # Caluculate occurances of bases
    a_count = input_sequence.count('A')
    c_count = input_sequence.count('C')
    g_count = input_sequence.count('G')
    t_count = input_sequence.count('T')
    sequence_length = len(input_sequence)
    print("------------------------------------------")
    print("Sequence Statistics for",sequence_title)
    print(" Fraction of A's: ", a_count/sequence_length)
    print(" Fraction of C's: ", c_count/sequence_length)
    print(" Fraction of G's: ", g_count/sequence_length)
    print(" Fraction of T's: ", t_count/sequence_length)
    print("Total Length: ", sequence_length)


# Compute the statisitcs on various sequences 
sequence_stats(sequence,"My Favorite Gene")
sequence_stats(rev_comp_seq,"Reverse Complement")
