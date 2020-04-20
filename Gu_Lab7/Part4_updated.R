# A. install DEseq 
# -- Warning, this will take ~5 mins to install
if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("DESeq2")

library("DESeq2")
# B. Add Code to read in RNA-Seq data
BCRS <- read.table("",header=T,row.names=1,sep="\t",quote="")
BCRS_stat <- read.table("",header=T,sep="\t",quote="")
rownames(BCRS_stat) <- BCRS_stat$
# C. Convert Status table into a factor
BCRS_stat$ <- factor(BCRS_stat$)
cds <- DESeqDataSetFromMatrix(countData = ,
                              colData = ,
                              design = ~ )
# D. Normalize for Size Effects:
cds <- DESeq(cds)

# E. Calculate Differential Expression
res <- results(cds,contrast = c('','',''))

# F. Extract top 100 genes by their adusted p-value using FDR
res <- res[order(res$padj),]



