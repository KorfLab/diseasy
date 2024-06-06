library(tidyverse)
z2ztxtlines<- read_tsv("z2z-txt-lines.mat")

zztl<-as.dist(z2ztxtlines[,-1])
zztl_avg <- hclust(zztl, method = 'average')
zztl.dend.obj <- as.dendrogram(zztl_avg)
# k= no of clusters, h= height of cut
zztl.dend <- color_branches(zztl.dend.obj, h=0.25)
plot(zztl.dend)

# cut clusters
zztl.cut25 <- cutree(zztl_avg, h=.25)

zztl.cluster.25 <- z2ztxtlines[,-1]
zztl.cluster.25 <- mutate(zztl.cluster.25, cluster = zztl.cut25)
head(zztl.cluster.25)
zztl.count <- count(zztl.cluster.25, cluster)
summary(zztl.count[2])
head(zztl.count)

head(zztl.cut25)

clusters = as.data.frame(as.matrix(zztl.cut550))
filter(clusters, V1 == 1)
clusters


zgenes = z2ztxtlines[1]
cluster = add_column(clusters,zgenes)
rename(cluster, gene = ...1)
cluster

filter(cluster, V1== target)

# heatmap too big
library(pvclust)
set.seed(12456) #This ensure that we will have consistent results with one another
try = as.matrix(z2ztxtlines[,-1])
fit <- pvclust(try, method.hclust = 'average', method.dist = "euclidean", nboot = 10)
plot(fit, print.num=FALSE) # dendogram with p-values

library(gplots)
heatmap.2(try, Rowv=zztl.dend.obj, scale="row", density.info="none", trace="none")


library(cluster)
set.seed(125)

mycluster <- function(x, k) list(cluster=cutree(hclust(zztl, method = "average"),k=k))

myclusGap <- clusGap(z2ztxtlines[,-1],
                     FUN = mycluster, 
                     K.max = 300, 
                     B = 10)

plot(myclusGap, main = "Gap Statistic")

with(myclusGap, maxSE(Tab[,"gap"], Tab[,"SE.sim"], method="globalSEmax")) # 281

# not work
myclusGap2 <- clusGap(z2ztxtlines[,-1],
                     FUN = mycluster, 
                     K.max = 600, 
                     B = 2)

plot(myclusGap2, main = "Gap Statistic")

with(myclusGap2, maxSE(Tab[,"gap"], Tab[,"SE.sim"], method="Tibs2001SEmax"))
