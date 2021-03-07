probability_DensityFn <- function (){
# Choose the mean as 0 and standard deviation as 1.
x <- seq(-5, 5,0.01)
y <- c(-0.4, 0.4)
#y <- 1/sqrt(2*pi)*exp(-x^2/2)

first_derivative <- function(x) {}
second_derivative <- function(x) {}
normalDensity <- function(x)  dnorm(x,0,1)
body(first_derivative) <- D(body(normalDensity), 'x')
body(second_derivative) <- D(body(first_derivative), 'x')
firstderivative= D(dnorm(x),'x')


plot(x,normalDensity(x), type="l",col="blue",ylim=c(-0.4,0.4),xlab="x",ylab="y")
lines(x,first_derivative(x),type="l",col="red")
lines(x,second_derivative(x),type="l",col="green")
abline(v=0, h=0)
}

probability_DensityFn()