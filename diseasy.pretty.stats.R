cap2 = read.csv("H2Zcluster2")
as.data.frame(cap2)
caporg = read.csv("H2ZRanks")
as.data.frame(caporg)

fin = data.frame(caporg$gene, caporg$rankingSem, caporg$rankingSem, cap2$captureSemOpt, caporg$rankingTxt, caporg$captureTxt, cap2$captureTxtOpt)

semorthscores = vector()

for(htarget in hgenes[-1]){
  b = orths[which(orths == htarget,arr.ind = TRUE)[1],-1]
  for(zf in b){
    if(zf != "" && !is.na(zf))
    {semorthscores = append(semorthscores , as.numeric(hzsl[which(zgenes== zf), htarget]))
      print(semorthscores)}
    
  }
}


bs = 0
txtorthscores = vector()

for(htarget in hgenes[-1]){
  b = orths[which(orths == htarget,arr.ind = TRUE)[1],-1]
  for(zf in b){
    
    if(zf != "" && !is.na(zf))
    {txtorthscores = append( txtorthscores , as.numeric(hztl[which(zgenes== zf), htarget]))
    print(txtorthscores)
    bs = bs + 1}
    
  }
}


for (z in zgenes) {
  print(which(orths == z,arr.ind = TRUE)[1]) 
  bs = bs + 1
}

mean(semorthscores)
sd(semorthscores)

mean(txtorthscores)
sd(txtorthscores)

mean(colMeans(as.data.frame(hzsl[,-1])))
sd(colMeans(as.data.frame(hzsl[,-1])))
mean(colMeans(as.data.frame(hztl[,-1])))
sd(colMeans(as.data.frame(hztl[,-1])))


aveScores = matrix(0,nrow = 3, ncol=4, dimnames = list(c("mn","sd","comp"),c("text", "textOrth","semantic","semanticOrth")))
aveScores[3,]=c("text", "textOrth","semantic","semanticOrth")
aveScores[1,1] =as.numeric(mean(colMeans(as.data.frame(hztl[,-1]))))
aveScores[2,1] =as.numeric(sd(colMeans(as.data.frame(hztl[,-1]))))
aveScores[1,2] = as.numeric(mean(txtorthscores))
aveScores[2,2] = as.numeric(sd(txtorthscores))
aveScores[1,3] = as.numeric(mean(colMeans(as.data.frame(hzsl[,-1]))))
aveScores[2,3] = as.numeric(sd(colMeans(as.data.frame(hzsl[,-1]))))
aveScores[1,4] = as.numeric(mean(semorthscores))
aveScores[2,4] = as.numeric(sd(semorthscores))

aveScores2 = as.data.frame(t(aveScores))
aveScores2[,1] = as.numeric(aveScores2[,1])
aveScores2[,2] = as.numeric(aveScores2[,2])

library(ggplot2)
ggplot(aveScores2, aes(x= comp, y=mn, fill=comp))+
  geom_bar(stat = "identity")+
  geom_errorbar(aes(ymin=mn-sd, ymax=mn+sd))+
  scale_fill_brewer(palette="Set3")+
  labs(x="Data", y="Mean", title = "Average Comparison Score vs Average Ortholog Score")


ggplot(fin, aes(x=caporg.rankingSem))+
  geom_histogram(binwidth = 15, fill = "orange", color="black")+
  labs(x="Rank", y="Counts", title = "Distribution of Ortholog Ranking- Semantic Comparison")+
  geom_vline(xintercept=mean(fin$caporg.rankingSem),size=2, show.legend = TRUE)

ggplot(fin, aes(x=caporg.rankingTxt))+
  geom_histogram(binwidth = 15, fill = "cornflowerblue", color="black")+
  labs(x="Rank", y="Counts", title = "Distribution of Ortholog Ranking- Textual Comparison")+
  geom_vline(xintercept=mean(fin$caporg.rankingTxt),size=2, show.legend = TRUE)


ggplot(fin, aes(x=caporg.rankingSem.1))+
  geom_histogram(binwidth = 15, fill = "orange", color="black")+
  labs(x="Rank capturing ortholog in cluster", y="Counts", title = "Distribution of Ortholog Ranking- Semantic Comparison, Cluster distance <0.1")+
  geom_vline(xintercept=mean(fin$caporg.rankingSem.1),size=2, show.legend = TRUE)

ggplot(fin, aes(x=caporg.captureTxt))+
  geom_histogram(binwidth = 15, fill = "cornflowerblue", color="black")+
  labs(x="Rank capturing ortholog in cluster", y="Counts", title = "Distribution of Ortholog Ranking- Textual Comparison, Cluster distance <0.1")+
  geom_vline(xintercept=mean(fin$caporg.captureTxt),size=2, show.legend = TRUE)

ggplot(fin, aes(x=cap2.captureSemOpt))+
  geom_histogram(binwidth = 15, fill = "orange", color="black")+
  labs(x="Rank capturing ortholog in cluster", y="Counts", title = "Distribution of Ortholog Ranking- Semantic Comparison, Optimal clusters")+
  geom_vline(xintercept=mean(fin$cap2.captureSemOpt),size=2, show.legend = TRUE)

ggplot(fin, aes(x=cap2.captureTxtOpt))+
  geom_histogram(binwidth = 15, fill = "cornflowerblue", color="black")+
  labs(x="Rank capturing ortholog in cluster", y="Counts", title = "Distribution of Ortholog Ranking- Textual Comparison, Optimal clusters")+
  geom_vline(xintercept=mean(fin$cap2.captureTxtOpt),size=2, show.legend = TRUE)


averanks = matrix(0, ncol = 4, nrow = 6)
averanks[1,] = c(mean(fin$caporg.rankingSem),sd(fin$caporg.rankingSem),"Rank Only","Semantic")
averanks[2,] = c(mean(fin$caporg.rankingTxt),sd(fin$caporg.rankingTxt),"Rank Only","Text")
averanks[3,] = c(mean(fin$caporg.rankingSem.1),sd(fin$caporg.rankingSem.1),"Cluster < 0.1","Semantic")
averanks[4,] = c(mean(fin$caporg.captureTxt),sd(fin$caporg.captureTxt),"Cluster < 0.1","Text")
averanks[5,] = c(mean(fin$cap2.captureSemOpt),sd(fin$cap2.captureSemOpt),"Optimal Cluster","Semantic")
averanks[6,] = c(mean(fin$cap2.captureTxtOpt),sd(fin$cap2.captureTxtOpt),"Optimal Cluster","Text")
colnames(averanks) = c("Mean","Stand.Deviation","Method","Comparison")

averanks = as.data.frame(averanks)
averanks[,1]=as.numeric(averanks[,1])
averanks[,2]=as.numeric(averanks[,2])

ggplot(averanks, aes(x= reorder(Method, -Mean), y=Mean, fill=Comparison))+
  geom_bar(stat = "identity", position = "dodge")+
  geom_errorbar(aes(ymin=Mean-Stand.Deviation, ymax=Mean+Stand.Deviation), position = "dodge")+
  scale_fill_brewer(palette="Set3")+
  labs(x="Method", y="Average Ranking", title = "Average Rank by Clustering Method")
