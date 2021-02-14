try:
    n = int(input("Enter the number of guests: "))
    if n<=0:
        print('Please enter the positive integer which is greater than >=1')
except:
    print('Error : The number you entered is not an integer')

numerator = 1
x = [i for i in range(1,n+1)]
y = []
for i in range(1,n+1):
    numerator = numerator*((365-i+1)/365)
    print('If the no of guests={} then the probability is {}'.format(i,1-numerator))
    y.append(1-numerator)

    # Plotting Graph

import matplotlib.pyplot as plt
plt.plot(x,y)
plt.xlabel('No of guests')
plt.ylabel('Probability')
plt.title('For n={}'.format(n))
