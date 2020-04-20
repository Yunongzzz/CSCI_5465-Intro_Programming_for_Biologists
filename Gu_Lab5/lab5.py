# CSCI 5465 Lab 5 Assignment
# Quincy Gu

# Part I: Practice with Functions
# (a) - (1), (2), (3)

# Self defined function "is_valid_humanlocus()"

def is_valid_humanlocus(humanlocus):
    if '.' in humanlocus:
        humanlocus_period_split = humanlocus.split('.')
        first_int_check = humanlocus_period_split[1]
        left_period_side = humanlocus_period_split[0]
        if first_int_check.isdigit() == True:
            if ('p' in left_period_side or 'q' in left_period_side):
                left_period_side_unifypq = left_period_side.replace('q', 'p')
                humanlocus_split = left_period_side_unifypq.split('p')
                second_int_check = humanlocus_split[1]
                chr_check = humanlocus_split[0]
                if second_int_check.isdigit() == True:
                    if chr_check.isdigit() == False:
                        if len(chr_check) == 1:
                            if ('X' in chr_check or 'Y' in chr_check):
                                return True
                    else:
                        if (int(chr_check) <= 22 and int(chr_check) >= 1):
                            return True


assert is_valid_humanlocus('6p21.3'), "Incorrect output!"
assert not is_valid_humanlocus('nonsense'), "Incorrect output!"

# (b)

# Additional assert checking statements

assert not is_valid_humanlocus('6p21,3'), "Incorrect output!"   # Reason is humanlocus only could be period there
assert not is_valid_humanlocus('48q21.3'), "Incorrect output!"   # Reason is chromosome number should be from 1 to 22

# Self define function "is_locus_onshortarm"

def is_locus_onshortarm(validlocus):
    if is_valid_humanlocus(validlocus) == True:
        if 'p' in validlocus:
            return(print('good'))
        else:
            return(print('not short arm'))
    else:
        return(print('Invalid Human Locus'))


# Part II: Analyzing SNP Data


# (a) been skipped and everything from part (a) all get done in part (b)

# (b)
def read_SNP_file(SNP_data):
    id = []
    Chr = []
    Position = []
    SNP1 = []
    SNP2 = []
    with open(SNP_data) as f:
        lines = f.read().splitlines()
        for i in range(len(lines)):
            lp_split = lines[i].split('(')
            left_lp = lp_split[0]
            right_lp = lp_split[1]
            comma_split = right_lp.split(',')
            snp1 = comma_split[0]
            rp_split = comma_split[1].split(')')
            snp2 = rp_split[0]
            dash_split = left_lp.split('-')
            pos = dash_split[1]
            left_dash = dash_split[0]
            chr_split = left_dash.split('chr')
            ID = chr_split[0]
            CHR = chr_split[1]

            id.append(ID)
            Chr.append(CHR)
            Position.append(pos)
            SNP1.append(snp1)
            SNP2.append(snp2)

        Organized_SNP_Data = {'id':id,'Chr':Chr,'Position':Position,'SNP1':SNP1,'SNP2':SNP2}

        assert not CHR == '23','Incorrect Chr'   # Assert statement here to guarantee the chromosome number is valid
        return Organized_SNP_Data

# (c)
Greg_Chr = read_SNP_file('GregMendel_SNPs.txt')['Chr']
Lilly_Chr = read_SNP_file('LillyMendel_SNPs.txt')['Chr']
Greg_SNP1 = read_SNP_file('GregMendel_SNPs.txt')['SNP1']
Lilly_SNP1 = read_SNP_file('LillyMendel_SNPs.txt')['SNP1']
Greg_SNP2 = read_SNP_file('GregMendel_SNPs.txt')['SNP2']
Lilly_SNP2 = read_SNP_file('LillyMendel_SNPs.txt')['SNP2']

POS = read_SNP_file('GregMendel_SNPs.txt')['Position']

Bold_Position = []
for i in range(len(Greg_Chr)):
    if Greg_Chr[i] == '10':
        if Lilly_Chr[i] == '10':
            if Greg_SNP1[i] == Lilly_SNP1[i]:
                if Greg_SNP2[i] == Lilly_SNP2[i]:
                    Bold_Position.append(POS[i])

Bold_Pos = []
for i in range(len(Bold_Position)):
    Bold_POS = int(Bold_Position[i])
    Bold_Pos.append(Bold_POS)

MIN_POS = min(Bold_Pos)
MAX_POS = max(Bold_Pos)

shared_region = (MIN_POS,MAX_POS)

print(shared_region)  # Report the shared region

# (d)
snp_def = {}
with open('SNP_definitions.txt') as f:
    lines = f.read().splitlines()[1:]
    for i in range(len(lines)):
        line = lines[i].strip().split('\t')
        key = line[0]
        values = line[1:]
        snp_def.setdefault(key,[]).extend(values)

# (e)
Num_POS = []
Greg_id = read_SNP_file('GregMendel_SNPs.txt')['id']
Greg_ID = []
for i in range(len(Greg_Chr)):
    Num_POS.append(int(POS[i]))
    if Greg_Chr[i] == '9':
        if (Num_POS[i] <= 22106000 and Num_POS[i] >= 22070000):
            Greg_ID.append(Greg_id[i])

Greg_Disease_Index = []
for i in range(len(Greg_ID)):
    snp_def_keys = list(snp_def.keys())
    if Greg_ID[i] in snp_def_keys:
        Greg_Disease_Index.append(Greg_ID[i])

Greg_disease = []
for i in range(len(Greg_Disease_Index)):
    Greg_Disease = snp_def.get(str(Greg_Disease_Index[i]))
    Greg_disease.append(','.join(Greg_Disease))

heart_disease = []
for i in range(len(Greg_disease)):
    if 'myocardial infarction' in Greg_disease[i]:
        heart_disease.append(Greg_disease[i])

print(heart_disease)  # Answers for Part II (e)


# (f)

# The 'rs333' is the SNP locus that interests me at SNPedia.com
# It is well-known that rs333 resistance to HIV

Lilly_id = read_SNP_file('LillyMendel_SNPs.txt')['id']

if 'rs333' in Greg_id:
    print("rs333 is in Greg's SNPs locus")
    print(snp_def['rs333'])
else:
    print("rs333 is not in Greg's SNPs locus, and therefore we could not find any info about the association between rs333 SNP and Greg's Possible Health Issue")

if 'rs333' in Lilly_id:
    print("rs333 is in Lilly's SNPs locus")
    print(snp_def['rs333'])
else:
    print("rs333 is not in Lilly's SNPs locus, and therefore we could not find any info about the association between rs333 SNP and Lilly's Possible Health Issue")