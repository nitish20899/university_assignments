println("Enter the number of guests: ")
num = readline()
num = parse(Int64, num)
if (num<=0)
    println("Please enter the positive integer which is greater than >=1")
end
numerator = 1
x = []
for i = 1:num
    append!( x,i)
end
y = []
for i= 1:num
    global numerator = numerator*((365-i+1)/365)
    println("If the no of guests=$i then the probability is $(1-numerator)")
    append!(y,1-numerator)
end

# visualizing

using Plots
plot(x, y,label = "Probability", lw = 3)
xlabel!("No of guests")
ylabel!("Probability")
