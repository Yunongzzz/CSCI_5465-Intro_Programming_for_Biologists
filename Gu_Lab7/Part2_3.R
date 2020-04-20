library(dplyr)
library(sqldf)

# Part II - Loading and manipulating expression data in R

## Load BC MicroArray text files into R

BC_MicroArray <- read.table('BC_MicroArray.txt')
BC_MicroArray_Status <- read.table('BC_MicroArray_Status.txt')

## Create a matrix from the data frame
BC_MicroArray_Matrix <- as.matrix(x = BC_MicroArray, dimnames = list(rownames(BC_MicroArray), colnames(BC_MicroArray)))

## Check the structure of teh data matries

print(is.matrix(BC_MicroArray_Matrix))  # Check if the type if a matrix or not
print(nrow(BC_MicroArray_Matrix))  # Check if the microarray data contain values for 32.864 probes (genes)
print(ncol(BC_MicroArray_Matrix))  # Check if the microarray data contan values for 90 samples


## Print the data for the BRCA1 gene for all samples
BRCA1_data <- filter(BC_MicroArray,rownames(BC_MicroArray) == 'BRCA1')

## Print the values for the first 10 genes for the first ER+ sample (GSM519791) in the microarray dataset
first10_GSM519791 <- as.data.frame(BC_MicroArray$GSM519791)[1:10,]

## Compute the mean and standard deviation of the expression data for the BRCA1 gene across all samples
BRCA1_Mean <- mean(as.numeric(BRCA1_data))
BRCA1_STDV <- sd(as.numeric(BRCA1_data))


## Compute the mean and standard deviation of the expression of all genes in the first ER+ sample (GSM519791)
GSM519791_Mean <- mean(as.numeric(BC_MicroArray$GSM519791))
GSM519791_STDV <- sd(as.numeric(BC_MicroArray$GSM519791))


## Print the list of 10 genes with the highest expression values in order of decreasing expression based on the first ER+ sample (GSM519791)
decreasing_10genes_exp_ERpos <- rownames(sqldf("select * from BC_MicroArray order by GSM519791 DESC LIMIT 10", row.names = TRUE))
print(decreasing_10genes_exp_ERpos)

## Create a vector called ERpos_samples that contains the GSM names of all ER+ samples
ERpos_samples_Prep <- as.data.frame(filter(BC_MicroArray_Status, BC_MicroArray_Status$V3 == '1'))
ERpos_samples <- as.vector(ERpos_samples_Prep$V2)

## Create a vector called ERpos_samples that contains the GSM names of all ER- samples
ERneg_samples_Prep <- as.data.frame(filter(BC_MicroArray_Status, BC_MicroArray_Status$V3 == '0'))
ERneg_samples <- as.vector(ERneg_samples_Prep$V2)


## Compute the difference in the mean expression for each gene between ER+ and ER- sample groups and saved into expr_difference vector
expr_ERpos <- subset(BC_MicroArray_Matrix, select = ERpos_samples)
expr_ERneg <- subset(BC_MicroArray_Matrix, select = ERneg_samples)

ERpos_mean <- as.data.frame(apply(expr_ERpos, 1, mean))
ERneg_mean <- as.data.frame(apply(expr_ERneg, 1, mean))

expr_difference <- ERpos_mean - ERneg_mean
expr_difference <- as.data.frame(expr_difference)


## Compute largest positive and negative difference in mean expression between ER+ and ER- groups
expr_posdiff <- filter(expr_difference, expr_difference$`apply(expr_ERpos, 1, mean)` >= 0)
expr_negdiff <- filter(expr_difference, expr_difference$`apply(expr_ERpos, 1, mean)` <= 0)

expr_posdiff <- as.data.frame(expr_posdiff)
expr_negdiff <- as.data.frame(expr_negdiff)

posdiff_max <- max(expr_posdiff)
negdiff_max <- max(expr_negdiff)


# Part III - Statistical analysis of microarray gene expression data


## Creater a vector of t_statistics measuring the difference in expression for each gene between the ER+ and ER- samples
t_numerator <- expr_difference

ERpos_variance <- as.data.frame(apply(expr_ERpos, 1, var))
ERneg_variance <- as.data.frame(apply(expr_ERneg, 1, var))

num_sample_ERpos <- as.numeric(length(ERpos_samples)) 
num_sample_ERneg <- as.numeric(length(ERneg_samples)) 

t_denominator <- sqrt((ERpos_variance/num_sample_ERpos) + (ERneg_variance/num_sample_ERneg))

t_statistics <- t_numerator/t_denominator
t_statistics <- as.vector(t_statistics)
t_statistics <- as.data.frame(t_statistics)

colnames(t_statistics)[1] <- 'T-Statistic'
## Plot a histogram of t_statistics
hist(t_statistics$`T-Statistic`, breaks = 100,
     main = 'Histogram of t_statistics', xlab = 'breaks', ylab = 'count')


## Compute a vector of p_values, one for each gene
tstat <- as.numeric(t_statistics$`T-Statistic`, 1, mean) 
num_tumor_samples <- num_sample_ERpos + num_sample_ERneg
num_tumor_samples <- as.numeric(num_tumor_samples)
p_val <- 2 * pt(-abs(tstat), (num_tumor_samples - 2))

p_values <- as.vector(p_val)


## Print a list of significantly differentially expressed gene, sorted in order of their 
## significance from smallest to largest
t_statistics <- as.data.frame(t_statistics)
BC_MicroArray_Matrix <- cbind(BC_MicroArray_Matrix, t_statistics)

p_values <- as.data.frame(p_values)
BC_MicroArray_Matrix <- cbind(BC_MicroArray_Matrix, p_values)

sigdiff_expr_genes <- c(rownames(BC_MicroArray_Matrix))

sigdiff_expr_genes <- as.data.frame(sigdiff_expr_genes)
sigdiff_expr_genes <- cbind(sigdiff_expr_genes, BC_MicroArray_Matrix$p_values)
sigdiff_expr_genes <- cbind(sigdiff_expr_genes, BC_MicroArray_Matrix$`T-Statistic`)

colnames(sigdiff_expr_genes)[1] <- 'Gene_Name'
colnames(sigdiff_expr_genes)[2] <- 'P_Values'
colnames(sigdiff_expr_genes)[3] <- 'T-Statistics'

sigdiff_expr_genes <- sigdiff_expr_genes[order(sigdiff_expr_genes$P_Values),]

expr_genes_pval_sig <- filter(sigdiff_expr_genes, sigdiff_expr_genes$P_Values < 0.05)


## Compute number of genes are significantly expressed at p-value and Bonferroni-corrected p-value less than 0.05
num_genes_sigdiff <- as.numeric(nrow(expr_genes_pval_sig)) 

Bonferroni_correct_pval <- p.adjust(p_val, 'bonferroni')
Bonferroni_correct_pval <- as.data.frame(Bonferroni_correct_pval)

colnames(Bonferroni_correct_pval)[1] <- "Adjusted_P_Values"
Sigdiff_Bonferroni_Pval <- filter(Bonferroni_correct_pval, Bonferroni_correct_pval$Adjusted_P_Values < 0.05)

num_genes_bonferroni_sigdiff <- as.numeric(nrow(Sigdiff_Bonferroni_Pval))


## Compute the number of genes are significantly differentially expressed and more highly in ER+ relative to ER- tumors
## and the number of genes are significantly differentially expressed and more lowly in ER+ relative to ER- tumors
ERpos_mean <- as.data.frame(ERpos_mean)
ERneg_mean <- as.data.frame(ERneg_mean)
expr_genes_pval_sig <- as.data.frame(expr_genes_pval_sig)

colnames(ERpos_mean)[1] <- 'Mean_ERPos'
colnames(ERneg_mean)[1] <- 'Mean_ERNeg'

Sigdiff_Expr_Compare <- expr_genes_pval_sig
ER_MeanSig_Compare <- data.frame()
ER_MeanSig_Compare <- rownames(BC_MicroArray_Matrix)
ER_MeanSig_Compare <- as.data.frame(ER_MeanSig_Compare)

ER_MeanSig_Compare <- cbind(ER_MeanSig_Compare, BC_MicroArray_Matrix$p_values)
colnames(ER_MeanSig_Compare)[2] <- "P_Values"

ER_MeanSig_Compare <- cbind(ER_MeanSig_Compare, ERpos_mean$Mean_ERPos)
ER_MeanSig_Compare <- cbind(ER_MeanSig_Compare, ERneg_mean$Mean_ERNeg)

colnames(ER_MeanSig_Compare)[3] <- "ERPos_Mean"
colnames(ER_MeanSig_Compare)[4] <- "ERNeg_Mean"

highlyERPos_Sigdiff <- filter(ER_MeanSig_Compare, P_Values < 0.05 & ERPos_Mean > ERNeg_Mean)
lowlyERPos_Sigdiff <- filter(ER_MeanSig_Compare, P_Values < 0.05 & ERPos_Mean < ERNeg_Mean)

num_highlyERPos_Sigdiff <- as.numeric(nrow(highlyERPos_Sigdiff))
num_lowlyERPos_Sigdiff <- as.numeric(nrow(lowlyERPos_Sigdiff))


## Select top 10 most significantly differentially expressed genes
top10_sigdiff_genes <- sigdiff_expr_genes[1:10,]
top10_sigdiff_genes <- top10_sigdiff_genes[,1]
top10_sigdiff_genes <- as.data.frame(top10_sigdiff_genes)



