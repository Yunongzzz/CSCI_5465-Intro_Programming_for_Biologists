# Install bioconductor
source('http://www.bioconductor.org/biocLite.R')

# OR, once bioconductor is installed:
library(BiocInstaller)

# Get topGO and yeast annotations
biocLite('topGO')
# biocLite("AnnotationDbi")
biocLite('org.Sc.sgd.db')
library(topGO)
library(org.Sc.sgd.db)


# Get all ids that map to a GO term
all_ids = mappedkeys(org.Sc.sgdGO)

# Set the "gene_universe" as only those ORF IDs that were
# present in the high-variance version of the expression data.
# Here, you need to replace the vector "ORFs" with the
# vector of orfs from the high-variance expression matrix, 
# and comment out or delete the statment, "ORFs = all_ids".
ORFs = interesting_gene_info$ORF
gene_universe = all_ids[all_ids %in% ORFs]

# Using your cluster of interest, set the vector "interesting_genes"
# to contain the names (ORF names) of the genes in that cluster.
# The two lines of code below ("set.seed(789)" and "interesting_genes = ...")
# are just placeholders so you can see how the later steps are supposed to work. 
# Randomly select 250 genes to test for enrichment
set.seed(789)
interesting_genes = sample(gene_universe, 232, replace = FALSE)

### Format our input data appropriately for topGO
# First, we combine our gene universe and list of interesting genes into one vector...
# It is a named factor: the names correspond to all genes in the gene universe,
# and the value for each gene is either '0' (not interesting) or '1' (interesting)

gene_list = factor(as.integer(gene_universe %in% interesting_genes))
names(gene_list) = gene_universe

# Because topGO does not support yeast GO annotations in the easiest way possible,
# We have to build our annotations into a list that it can use

orf_2_go_list = as.list(org.Sc.sgdGO[intersect(gene_universe,mappedkeys(org.Sc.sgdGO))])
orf_2_go_final = lapply(orf_2_go_list, function(x) {
                      unique(unlist(lapply(x, `[[`, 'GOID')))
})

# Build the topGOdata object
GO_bp_tester = new('topGOdata',
                    description = 'csci_3003 rocks',
                    ontology = 'BP',    # Use either BP, CC, or MF
                    allGenes = gene_list,
                    annotationFun = annFUN.gene2GO,
                    gene2GO = orf_2_go_final
                    )

# Perform the test and get results
result_fisher = runTest(GO_bp_tester, algorithm = 'classic', statistic = 'fisher')

# See general Fisher test results
result_fisher

# Generate a table containing the most enriched GO terms
results = GenTable(GO_bp_tester, fisher_p = result_fisher, orderBy = 'fisher_p', topNodes = 10)

# View results!
results

# For this visualization
biocLite("Rgraphviz")
library(Rgraphviz)

showSigOfNodes(GO_bp_tester, score(result_fisher))

