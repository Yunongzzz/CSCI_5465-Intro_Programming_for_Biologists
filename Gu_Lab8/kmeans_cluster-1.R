library(dplyr)




## Loading the data

precluster_data <- load('gasch_expression_data.RData')

## Calculate variance of each gene across the set of 173 conditions

var_gene_conditions <- apply(expr_data, 1, var)
var_gene_conditions <- as.data.frame(var_gene_conditions)
colnames(var_gene_conditions) <- 'Variance'

## Select top 2000 highest values in the variance column 

var_gene_2000_index <- order(var_gene_conditions$Variance, decreasing = TRUE) [1:2000]
var_gene_2000_index <- as.data.frame(var_gene_2000_index)
colnames(var_gene_2000_index) <- 'Index'


## Create the cluster data applied to the following kmean-clustering function

cluster_data <- expr_data[var_gene_2000_index$Index[1:2000],]
cluster_data <- as.data.frame(cluster_data)

kmeans_cluster <- function(data, k){
  # We want the gene expression values to be the columns, conditions to be rows
  data <- t(data)

  # Randomize the initial gene cluster assignments
  cluster_labels <- sample(1:k, size=ncol(data), replace=TRUE)
  # initialize the center at 0
  center <- matrix(rep(0,nrow(data)*k), ncol=k)
  # initialize the distance vector to 0
  dis <- rep(0, times=k)
  cost <- 0
  for(i in 1:ncol(data)){
    cost <- cost + sqrt(sum((data[,i]-center[,cluster_labels[i]])^2,na.rm=T))
  }
  print(paste('Initial Cost ',cost,sep=''))
  count <- 0
  while(TRUE){
    cost_old <- cost
    
    for(i in 1:k){

      if(sum(cluster_labels == i) == 0){
        center[,i] <- center[,i]
      }
      else if(sum(cluster_labels == i) == 1){
        center[,i] <- data[,cluster_labels == i]
      }
      else{
        center[,i] <- rowMeans(data[,cluster_labels == i])
      }
    }
    # for every gene
    for(i in 1:ncol(data)){
      # for every centroid
      for(j in 1:ncol(center)){
        dis[j] <- sqrt(sum((data[,i]-center[,j])^2,na.rm=T))
      }
      # assign into closest cluster
      cluster_labels[i] <- which.min(dis)
    }
    
    cost <- 0
    for(i in 1:ncol(data)){
      cost <- cost + sqrt(sum((data[,i]-center[,cluster_labels[i]])^2,na.rm=T))
    }
    print(paste('Iteration: ',count,' -- cost:',cost,sep=''))
    if(abs(cost - cost_old) < 0.0001){
      break
    }
    count <- count + 1
  }
  return(cluster_labels)
}

results <- kmeans_cluster(cluster_data,50)
results <- as.data.frame(results)




count_kmeans_results <- table(unlist(results))
count_kmeans_results <- as.data.frame(count_kmeans_results)
colnames(count_kmeans_results) <- c('cluster_results','counts')


most_cluster_count <- count_kmeans_results[which.max(count_kmeans_results$counts),1]
most_cluster_count <- as.numeric(most_cluster_count)


Results <- cbind(results, 1:2000)
Results <- subset(Results, Results$results <= 10)
colnames(Results) <- c('Cluster_Index','Gene_Index')
Results <- Results[order(Results$Cluster_Index),]


for(i in Results$Cluster_Index == 1) {
  cluster_data_1 <- cluster_data[Results$Gene_Index,]
  cluster1_average <- apply(cluster_data_1, 2, ave)
  png(filename = 'Plot for Cluster 1.png')
  matplot(t(cluster_data_1), type = 'l', xlab = 'Conditions', ylab = 'Gene Expression Level')
  lines(t(cluster1_average),lwd = 5)
  dev.off()
}


for(i in Results$Cluster_Index == 2) {
  cluster_data_2 <- cluster_data[Results$Gene_Index,]
  cluster2_average <- apply(cluster_data_2, 2, ave)
  matplot(t(cluster_data_2), type = 'l', xlab = 'Conditions', ylab = 'Gene Expression Level')
  lines(t(cluster2_average),lwd = 5)
}

for(i in Results$Cluster_Index == 3) {
  cluster_data_3 <- cluster_data[Results$Gene_Index,]
  cluster3_average <- apply(cluster_data_3, 2, ave)
  matplot(t(cluster_data_3), type = 'l', xlab = 'Conditions', ylab = 'Gene Expression Level')
  lines(t(cluster3_average),lwd = 5)
}

for(i in Results$Cluster_Index == 4) {
  cluster_data_4 <- cluster_data[Results$Gene_Index,]
  cluster4_average <- apply(cluster_data_4, 2, ave)
  matplot(t(cluster_data_4), type = 'l', xlab = 'Conditions', ylab = 'Gene Expression Level')
  lines(t(cluster4_average),lwd = 5)
}

for(i in Results$Cluster_Index == 5) {
  cluster_data_5 <- cluster_data[Results$Gene_Index,]
  cluster5_average <- apply(cluster_data_5, 2, ave)
  matplot(t(cluster_data_5), type = 'l', xlab = 'Conditions', ylab = 'Gene Expression Level')
  lines(t(cluster5_average),lwd = 5)
}

for(i in Results$Cluster_Index == 6) {
  cluster_data_6 <- cluster_data[Results$Gene_Index,]
  cluster6_average <- apply(cluster_data_6, 2, ave)
  matplot(t(cluster_data_6), type = 'l', xlab = 'Conditions', ylab = 'Gene Expression Level')
  lines(t(cluster6_average),lwd = 5)
}


for(i in Results$Cluster_Index == 7) {
  cluster_data_7 <- cluster_data[Results$Gene_Index,]
  cluster7_average <- apply(cluster_data_7, 2, ave)
  matplot(t(cluster_data_7), type = 'l', xlab = 'Conditions', ylab = 'Gene Expression Level')
  lines(t(cluster7_average),lwd = 5)
}



for(i in Results$Cluster_Index == 8) {
  cluster_data_8 <- cluster_data[Results$Gene_Index,]
  cluster8_average <- apply(cluster_data_8, 2, ave)
  matplot(t(cluster_data_8), type = 'l', xlab = 'Conditions', ylab = 'Gene Expression Level')
  lines(t(cluster8_average),lwd = 5)
}


for(i in Results$Cluster_Index == 9) {
  cluster_data_9 <- cluster_data[Results$Gene_Index,]
  cluster9_average <- apply(cluster_data_9, 2, ave)
  matplot(t(cluster_data_9), type = 'l', xlab = 'Conditions', ylab = 'Gene Expression Level')
  lines(t(cluster9_average),lwd = 5)
}

for(i in Results$Cluster_Index == 10) {
  cluster_data_10 <- cluster_data[Results$Gene_Index,]
  cluster10_average <- apply(cluster_data_10, 2, ave)
  matplot(t(cluster_data_10), type = 'l', xlab = 'Conditions', ylab = 'Gene Expression Level')
  lines(t(cluster10_average),lwd = 5)
}



### Interesting Profile is for Cluster 1


cluster1_mean <- as.data.frame(apply(cluster_data_1, 2, mean))
colnames(cluster1_mean) <- 'Mean'
cluster1_mean <- t(cluster1_mean)

cluster_data1 <- rbind(cluster_data_1,cluster1_mean)

overexpress_cluster1 <- subset(cluster_data1, cluster_data1[271,] > 0)



underexpress_cluster1 <- subset(cluster_data1, cluster_data1[271,] < 0)

interesting_gene_names <- as.data.frame(rownames(cluster_data_1))
colnames(interesting_gene_names) <- "Interesting Gene Names"

GENE_INFO <- cbind(gene_info, rownames(gene_info))
colnames(GENE_INFO) [ncol(GENE_INFO)] <- 'Gene_Names'

interesting_gene_info <- subset(GENE_INFO, Gene_Names %in% interesting_gene_names$`Interesting Gene Names`)
interesting_gene_info <- subset(interesting_gene_info, select = - Gene_Names)

























