import re
import os
import sys
import statistics


# Part I

#read in slim_chr_seq.fasta file 

seq_info = []
sequence = []
Current_Sequence = ''

with open("slim_chr2_seq.fasta.txt","r") as f:
	for line in f:
		if line[0] == '>':
			seq_info.append(line[1:].strip())
			if Current_Sequence != '':
				sequence.append(Current_Sequence)

			Current_Sequence = ''
		else:
			Current_Sequence += line.strip()

	sequence.append(Current_Sequence)
	del sequence[0]


#read in vcf file
Chr = []
rsid = []
slim_pos = []
genome_pos = []
ref = []
alt = []
geneinfo = []
Geneinfo = []
with open("slim_chr2_SNPS.vcf","r") as f:
	for line in f:
		parts = line.split()
		Chr.append(parts[0])
		rsid.append(parts[1])
		slim_pos.append(parts[2])
		genome_pos.append(parts[3])
		ref.append(parts[4])
		alt.append(parts[5])
		geneinfo.append(parts[6:])

for i in range(len(geneinfo)):
	GeneInfo = geneinfo[i]
	Gene = ''.join(GeneInfo)
	Geneinfo.append(Gene)


snp_index = []
for i in range(1,len(slim_pos)):
	snp_index.append(int(slim_pos[i]))

SNP = []

for i in range(len(sequence)):
	for j in range(1,len(snp_index)):
		SNP.append(sequence[i][j-1])

def slice_list_per(List, per):
	avg = len(List) / float(per)
	out = []
	last = 0.0

	while last < len(List):
		out.append(List[int(last):int(last + avg)])
		last += avg
	return out

split_SNP = slice_list_per(SNP,155)


Frequency = []

for i in range(1,len(alt)):
	for j in range(len(split_SNP)):
		count = split_SNP[j].count(alt[i])
		frequency = count / 90
	Frequency.append(frequency)

split_Frequency = slice_list_per(Frequency,155)

Freq = []

for i in range(len(split_Frequency)):
	j = 0
	if j <= 155:
		freq = split_Frequency[i][j]
		j += 1
		Freq.append(freq)


def list_str_to_float(List):
	n = 0
	while n < len(List):
		List[n] = float(List[n])
		n += 1
	return List

Freq_int = list_str_to_float(Freq)

highest_frequency = max(Freq_int)
lowest_frequency = min(Freq_int)


Chr = Chr[1:]
rsid = rsid[1:]
slim_pos = slim_pos[1:]
ref = ref[1:]
alt = alt[1:]
Geneinfo = Geneinfo[1:]


def duplicates_index_in_list(List, item):
	return [i for i, x in enumerate(List) if x == item]

highest_freq_index = duplicates_index_in_list(Freq_int, highest_frequency)

id_highest_freq = []

for i in range(len(highest_freq_index)):
	rsid_highest_frequency = rsid[highest_freq_index[i]]
	id_highest_freq.append(rsid_highest_frequency)


lowest_freq_index = duplicates_index_in_list(Freq_int, lowest_frequency)

id_lowest_freq = []

for j in range(len(lowest_freq_index)):
	rsid_lowest_frequency = rsid[lowest_freq_index[j]]
	id_lowest_freq.append(rsid_lowest_frequency)



# Optional Part I

#Self-defined mean SNP frequency calculation function
def mean_frequency(Frequency_List):
	mean_value = statistics.mean(Frequency_List)
	return mean_value

#Get the mean value of all SNP frequencies by calling the function I defined above
mean_value_of_frequency = mean_frequency(Freq)


with open("slim_chr2_SNPs_withfrequencies.vcf","w") as f:
	f.write('Chromosome_Number \t SNP_Name \t SNP_slim_Position \t SNP_Reference_SNP \t SNP_Alternative_SNP \t SNP_Frequency \t Gene_Disease_Information \n')
	for index in range(len(Chr)):
		f.write(str(Chr[index]) + '\t' + str(rsid[index]) + '\t' + str(slim_pos[index]) + '\t' + str(ref[index]) + '\t' + str(alt[index]) + '\t' + str(Freq[index]) + '\t' + str(Geneinfo[index]) + '\n')




#Part II

nh_lymphoma_index = []

for i in range(len(Geneinfo)):
	if(Geneinfo[i].find('Non-Hodgkinlymphoma') >= 0):
		nh_lymphoma_index.append(i)

nh_lymphoma_start = nh_lymphoma_index[0]
nh_lymphoma_end = nh_lymphoma_index[-1] + 1

Seq_info = seq_info[nh_lymphoma_start:nh_lymphoma_end]
Rsid = rsid[nh_lymphoma_start:nh_lymphoma_end]
GeneDiseaseInfo = Geneinfo[nh_lymphoma_start:nh_lymphoma_end]

with open("lymphoma_variants.txt","w") as f:
	f.write('IndividualID \t variantID \t GeneDiseaseInfo \n')
	for i in range(len(Seq_info)):
		f.write(str(Seq_info[i]) + '\t' + str(Rsid[i]) + '\t' + str(GeneDiseaseInfo[i]) + '\n')


synonymous_index = []

for i in range(len(Geneinfo)):
	if(Geneinfo[i].find('synonymous') >= 0):
		synonymous_index.append(i)

synonymous_start = synonymous_index[0]
synonymous_end = synonymous_index[-1] + 1

Synonymous_Frequency = Freq[synonymous_start:synonymous_end]


non_synonymous_index = []

for j in range(len(Geneinfo)):
	if(Geneinfo[j].find('nonsynonymous') >= 0):
		non_synonymous_index.append(j)

non_synonymous_start = non_synonymous_index[0]
non_synonymous_end = non_synonymous_index[-1] + 1

Non_Synonymous_Frequency = Freq[non_synonymous_start:non_synonymous_end]

Average_Synonymous_Frequency = mean_frequency(Synonymous_Frequency)

Average_Non_Synonymous_Frequency = mean_frequency(Non_Synonymous_Frequency)



#Part III

for i in range(len(sequence)):
	snp_check = []
	for j in range(len(slim_pos)):
		snp_check.append(sequence[i][int(slim_pos[j])])
		alt_snp_freq = []
		ref_snp = []
		alt_snp_pos = []
		alt_snp = []
		for k in range(len(snp_check)):
			if snp_check[k] != ref[k]:
				alt_snp_count = 0
				alt_snp.append(snp_check[k])
				ref_snp.append(ref[k])
				alt_snp_pos.append(slim_pos[k])
				alt_snp_count += 1
				alt_snp_frequency = alt_snp_count / 90
				alt_snp_freq.append(alt_snp_frequency)

		
with open("novel_variant.txt","w") as f:
	f.write('SNP_Position \t Reference_SNP \t Alternative_SNP \t Frequency_of_Alternative_SNP \n')
	for i in range(len(alt_snp)):
		f.write(str(alt_snp_pos[i]) + '\t' + str(ref_snp[i]) + '\t' + str(alt_snp[i]) + '\t' + str(alt_snp_freq[i]) + '\n')


#Output file with answers for all the questions in Lab 4

with open("Answers.txt", "w") as f:
	f.write('Answers for Questions in Part I \n \n Q1. Find and print the ids of the SNPs in the population that occur with the highest and lowest frequency. \n \n \n')
	f.write('SNP_ids_Highest_Frequency \t \n \n')
	for index in range(len(id_highest_freq)):
		f.write(str(id_highest_freq[index]) + '\t')
	f.write('\n \n \n')
	f.write('SNP_ids_Lowest_Frequency \t \n \n')
	for index in range(len(id_lowest_freq)):
		f.write(str(id_lowest_freq[index]) + '\t')
	f.write('\n \n \n')
	f.write("Q2. Write your own function that calculates the mean of a list (input: a list, output: that list's mean). Calculate the mean across all SNP frequencies in the population. \n \n \n")
	f.write("My self-Defined function is in the line 142 - 150, it's name is 'mean_frequency', and the mean across all SNP frequencies in the population is in the following: \n \n")
	f.write(str(mean_value_of_frequency))
	f.write('\n \n \n \n \n')
	f.write('Answers for Questions in Part II \n \n Q1. Cross-reference the file you created that contains SNP frequencies (slim_chr2_SNPs_withfrequencies.vcf) and compare frequencies of synonymous versus nonsynonymous SNPs \n \n \n')
	f.write('Average_Frequency_Synonymous_SNPs \t Average_Frequency_Non_Synonymous_SNPs \n \n')
	f.write('\t' + str(Average_Synonymous_Frequency) + '\t \t \t \t \t' + str(Average_Non_Synonymous_Frequency) + '\n \n')
	f.write('And we could obviously concluded that the average of the frequencies of the synonymous SNPs is a little bit greater than the average of the frequencies of the non synonymous SNps. \n')


















		
