install.packages("dplyr")
library("dplyr")

getwd()
setwd("/Users/CheHoon/cheprojects/class101")

df <- read.csv("class101_20210611.csv")
df_original <- df


#function that strips 월,원, and commas from price string and converts to type int 
cleanPrice <- function(df, priceCol){
  
  df[[priceCol]] <- gsub("[월원,]","",df[[priceCol]])
  df[[priceCol]] <- as.integer(df[[priceCol]])
  return(df)
}

#clean monthlyPayment column
df <- cleanPrice(df,'monthlyPayment')

#move values from monthlyPayment to finalPrice for rows where installmentPeriod is 최종금액 
index <- which(df$installmentPeriod == "최종 금액")
df[index,'finalPrice'] <- df[index,'monthlyPayment']
df[index,'monthlyPayment'] <- NA

#clean remaining price columns
df <- cleanPrice(df,'finalPrice')
df <- cleanPrice(df,'discountAmount')
df <- cleanPrice(df,'couponDiscount')
df <- cleanPrice(df,'originalPrice')



