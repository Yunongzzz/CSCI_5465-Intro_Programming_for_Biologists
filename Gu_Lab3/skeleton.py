#!/usr/bin/python

# Lab 3
# Script: charged_sequence.py
# Problem Description: 
#    Read in amino acid sequences from an input file and
#    calculate statistics on the 'disordered' region.

import re

with open('Hsp90_conserved.txt','r') as fin:

	with open('aaoutput.txt','w') as fout:

		# Write aaoutput.txt title

		fout.write('Amino_Acid_Names \t Positive_AA_Disordered_% \t Negative_AA_Disordered_% \t Length_Disordered \t Positive_AA_Seq_% \t Negative_AA_Seq_% \n')

		for line in fin:
			split_line = line.split('\t')
			name = split_line[0]
			aaname = name[1:]
			seq = split_line[1]

			# 1 Extra Credit Point Part - make sure conserved domain exist then excute the following calculations

			if ('EYLEE' in seq) and ('LNKTKP' in seq):

				EYLEE_start_index = seq.index('EYLEE')
				EYLEE_end_index = EYLEE_start_index + len('EYLEE')

				LNKTKP_start_index = seq.index('LNKTKP')
				LNKTKP_end_index = LNKTKP_start_index + len('LNKTKP')


				if EYLEE_end_index < LNKTKP_start_index:

					disordered_linker_sequence = seq[(EYLEE_end_index+1):LNKTKP_start_index]


				if LNKTKP_end_index <EYLEE_start_index:

					disordered_linker_sequence = seq[(LNKTKP_end_index+1):EYLEE_start_index]


				length_disordered_region = len(disordered_linker_sequence)


				r_count = disordered_linker_sequence.count('R')
				h_count = disordered_linker_sequence.count('H')
				k_count = disordered_linker_sequence.count('K')


				sum_positive_aa = r_count + h_count + k_count


				d_count = disordered_linker_sequence.count('D')
				e_count = disordered_linker_sequence.count('E')


				sum_negative_aa = d_count + e_count


				percent_positive_aa_disordered = sum_positive_aa / length_disordered_region * 100

				percent_negative_aa_disordered = sum_negative_aa / length_disordered_region * 100

				percent_positive_aa_whole_seq = sum_positive_aa / len(seq) * 100

				percent_negative_aa_whole_seq = sum_negative_aa / len(seq) * 100


				fout.write(aaname)
				fout.write('\t')
				fout.write(str(percent_positive_aa_disordered))
				fout.write('\t')
				fout.write(str(percent_negative_aa_disordered))
				fout.write('\t')
				fout.write(str(length_disordered_region))
				fout.write('\t')
				fout.write(str(percent_positive_aa_whole_seq))
				fout.write('\t')
				fout.write(str(percent_negative_aa_whole_seq))
				fout.write('\n')





















