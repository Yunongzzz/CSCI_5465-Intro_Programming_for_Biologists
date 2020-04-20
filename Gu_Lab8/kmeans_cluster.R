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