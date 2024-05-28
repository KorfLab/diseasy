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
