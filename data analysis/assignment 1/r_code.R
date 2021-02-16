# take input from the user
probability <- function (nguests){
numerator = 1
  x <- rep(1, length(nguests))
  y <- rep(1, length(nguests))
  print(x)
# check is the input is negative, positive or zero
if(nguests <= 0) {
  TotalValue <- 0
  print("Sorry, negative nguests and zeros are not allowed")
} else {
  for(i in 1:nguests) {
    numerator = numerator * ((365 -i + 1)/365)
    x[i] <- i
    y[i] <- 1-numerator
  }
  TotalValue <- 1-(numerator) 
  plot(x, y, type = "l", pch = 19,col = "red", xlab = "no of guests", ylab = "probability")
  
}
  return(TotalValue)
}
nguests = as.integer(readline(prompt="Enter no of guests: "))
total = probability(nguests)
print(paste("The Probability of", nguests ,"is", total))









