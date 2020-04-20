# Lab 6 Script
# Comments in R are the same as in python!

# change this to work with the input file we provided
filename = "breast_cancer_expression_data.txt"

# If you look at R scripts from other sources, you may see the `<-` operator used.
# 1) From the following example, what does `<-` do?
a = 5
b <- 5
print(a == b)

# 2) What does the following do?
substr(filename,1,1)
# 3) What about this?
substr(filename,1,nchar(filename)-4)
# Hint: the help menu in RStudio can be accessed by typing a functions name prefixed with a '?'

# import the data file into an R 'data.frame' using the built-in read table function
data = read.table(filename,sep="\t",header=TRUE,quote="")
# 4) What does the names function do?
names(data)

# 5) What does the head function do?
head(data)

# Let's extract data from the data.frame and store them in variables
# Data in a data.frame can be accessed by index
genes = data[,2]
# Data in a data frame can also be accessed by name
gene_descriptions = data[,"Gene_desc"]
# 6) What does the "c" function do?
Tumor_cols = c("Tumor_1_ERPos_expr","Tumor_2_ERNeg_expr")
expr_data = data[,Tumor_cols]

# After you've run the above code, explore the variables in the workspace panel

# 7) Explain what each of the following does:
expr_data[1,2]
expr_data[2,1]

expr_data[,1]
expr_data[2,]

# Lets plot a histogram of the data:
# First sample 1 (ER+ tumor)
hist(expr_data[,1],
     breaks=100,
     main="ER - Gene Expression",
     xlab="Expression",
     ylab="Frequency"
)
# Now sample 2 (ER- Tumor)
hist(expr_data[,2],
     breaks=100,
     main="ER - Gene Expression",
     xlab="Expression",
     ylab="Frequency"
)

# 8) describe what the following statement does:
diffs = expr_data[,1] - expr_data[,2]

# 9) What is the max function and what does it do?
max_diff = max(diffs)              

# 10) What does this statement do?
max_index = which(diffs == max_diff) 
print(as.character(genes[max_index]))
print(as.character(gene_descriptions[max_index]))



