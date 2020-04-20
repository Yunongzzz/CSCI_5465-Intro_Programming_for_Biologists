library(mcp.project)
# A. install DEseq 
# -- Warning, this will take ~5 mins to install
if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("DESeq2")

library("DESeq2")
# B. Add Code to read in RNA-Seq data


###################
#these lines need to be updated with the appropriate filenames!!
###################
BCRS <- read.table("BC_RNAseq.txt",header=T,row.names=1,sep="\t",quote="")
BCRS_stat <- read.table("BC_RNAseq_Status.txt",header=T,sep="\t",quote="")
###################


rownames(BCRS_stat) <- BCRS_stat$BCID
# C. Convert Status table into a factor
BCRS_stat$ERStat <- factor(BCRS_stat$ERStat)
cds <- DESeqDataSetFromMatrix(countData = BCRS,
                              colData = BCRS_stat,
                              design = ~ ERStat)
# D. Normalize for Size Effects:
cds <- DESeq(cds)

# E. Calculate Differential Expression
res <- results(cds,contrast = c('ERStat','0','1'))

# F. Extract top 100 genes by their adusted p-value using FDR
res <- res[order(res$padj),]
adjp_fdr <- p.adjust(res$pvalue,method = 'fdr',n=length(res$pvalue))
adjp_fdr <- as.data.frame(adjp_fdr)

res <- cbind(res,adjp_fdr)
colnames(res)[7] <- "FDR"

res <- res[order(res$FDR),]

mostsig_100_genes <- rownames(res[1:100,])
