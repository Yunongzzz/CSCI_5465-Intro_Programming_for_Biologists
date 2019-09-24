#!/usr/bin/python3

#----------------------------------
#
# CSCI 3003/5465 Lab 2
#
#----------------------------------

# play with print statements
print("This seems to be 'ok'\n")
print('''I am trying to write a multiline statement but I am too lazy 
to write multiple lines separately using multiple print statements, and don't feel like using new lines '\\n'.
Something isn't quite right, though! ''' '\n'
'''Can you fix me? .....
"Do. Or do not. There is no try." ''' '\n\n')

# Let's do some arithmetic

#Set initial value of the runSum
runSum = 0
runSum = runSum + 1
runSum = runSum + 1
runSum = runSum + 2
runSum += 2
print(runSum)

# assign strings sequence 1 and 2
sequence1 = 'AAAA'
sequence2 = 'TTTT'

#Correct this to give proper concatenation
sequenceSum = sequence1 + sequence2 
print(sequenceSum)

# Can you explain this?
# String type in python should be inside the quotation mark, the addition between 2 strings are just combine 2 strings together
# What happened to sequence1?
# This is exactly the same thing as sequence1 = sequence1 + sequence2, combine sequence1 and sequence2 together
sequence1 += sequence2
print(sequence1 + sequence2)

email_theU = 'pythonMaster@umn.edu'
print(email_theU)

# Calculate 2^5th power = 32
exp_a = 3
exp_b = 2

# Remember order of operations!
# We could also import math and do the same thing with exp() function
print(2 ** (exp_a + exp_b))

# Subscripting
DNA_bases = 'ACGT'
# print each base out using string subscription:
print("Adenine:", DNA_bases[0])
print("Cytosine:", DNA_bases[1])
print("Guanine:", DNA_bases[2])
print("Thymine:", DNA_bases[3])

# Learn more about the genetic code here: http://en.wikipedia.org/wiki/Genetic_code

# Slicing
DNA_nucleotides = 'AGCTAAATGATCGTCCGAATCGGAATCGATATCGGAATCTAGCGAT'
#Convert the DNA nucleotides to RNA nucleotides using the appropriate string method:
RNA_nucleotides = DNA_nucleotides.replace('T','U')

# Print out the start codon using slices:
print("Start Codon:", RNA_nucleotides[6:9])
# Print out the stop codon using slices:
print("Stop Codon:", RNA_nucleotides[-7:-4])
#Print out the length of the entire coding region:
print("Length of Coding Region:", len(RNA_nucleotides[6:-4]))
# Consider coding region as from the start condon to the stop condon
