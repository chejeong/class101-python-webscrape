install.packages("writexl")
library("writexl")


getwd()
setwd("/Users/CheHoon/cheprojects/class101")

df <- read.csv("Data/class101_20210611.csv")
df_original <- df

#drop false index columns
df <- df[-c(1,2)]

#function that strips 월,원, and commas from price string and converts to type int 
cleanPrice <- function(df, priceCol){
  
  df[[priceCol]] <- gsub("[월원,-]","",df[[priceCol]])
  df[[priceCol]] <- as.integer(df[[priceCol]])
  return(df)
}

#clean monthlyPayment column
df <- cleanPrice(df,'monthlyPayment')

#move values from monthlyPayment to finalPrice for rows where installmentPeriod is 최종금액 
index <- which(df$installmentPeriod == "최종 금액")
df[index,'finalPrice'] <- df[index,'monthlyPayment']
df[index,'monthlyPayment'] <- NA
df[index,'installmentPeriod'] <- ""


#clean remaining price columns
df <- cleanPrice(df,'finalPrice')
df <- cleanPrice(df,'discountAmount')
df <- cleanPrice(df,'couponDiscount')
df <- cleanPrice(df,'originalPrice')

#converting to correct data types
df$reviewNum <- as.numeric(df$reviewNum)
df$likes <- as.numeric(df$likes)
df$installmentPeriod <- as.character(df$installmentPeriod)

#clean satisfaction column
colnames(df)[13] <- "satisfactionPct"
df$satisfactionPct <- gsub("%","",df$satisfactionPct)
df$satisfactionPct <- as.numeric(df$satisfactionPct)

#clean discountPct column
df$discountPct <- gsub("%","",df$discountPct)
df$discountPct <- as.numeric(df$discountPct)

#clean communityPosts column
df$communityPosts <- gsub("개의 글|,","",df$communityPosts)
df$communityPosts <- as.numeric(df$communityPosts)

#clean feedbackNum column
df$feedbackNum <- gsub("개의 피드백 더보기|,","",df$feedbackNum)
df$feedbackNum <- as.numeric(df$feedbackNum)

#clean installmentPeriod
colnames(df)[23] <- "installmentPeriodInMonths"
df$installmentPeriodInMonths <- gsub("개월 할부","",df$installmentPeriodInMonths)
df$installmentPeriodInMonths <- as.numeric(df$installmentPeriodInMonths)

#clean social media
df2 <- df %>% select(creatorName, creatorSocialMedia)
index <- which(df2$creatorSocialMedia=="")
df2 <- df2[-c(index),]


df3 <- data.frame(creatorSocialMedia = character())

for (i in 1:nrow(df2)) {
  
  creatorName <- df2[i,"creatorName"]
  classURL <- df2[i,"classURL"]
  snslinks <- unlist(strsplit(df2[i,"creatorSocialMedia"],', ')[[1]])
  
  for (j in 1:length(snslinks)) {
    
    creatorSocialMedia = snslinks[j]
    df_row <- data.frame("creatorName" = creatorName, "creatorSocialMedia" = creatorSocialMedia)
    df3 <- rbind(df3, df_row)
    
  }
  
}

#sort by creatorName
df3 <- df3[order(df3['creatorName']),]
#drop duplicates
df3 <- unique(df3)

df <- df[-c(11,29)]


#export as excel files
write_xlsx(df, "/Users/CheHoon/Desktop/Class101Data.xlsx")
write_xlsx(df3, "/Users/CheHoon/Desktop/Class101CreatorSocialMedia.xlsx")







