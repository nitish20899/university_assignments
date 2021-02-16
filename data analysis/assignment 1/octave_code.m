# Implementing the equation of probability
n= input("choose the number of guests:" );
numerator=1;
if(n<=0)
  disp("sorry negative or zero numbers are not allowed");
else
  for i = [1:n]
    numerator=numerator*((365-i+1)/365);
    x(i)=i;
    y(i)=1-numerator;
    fprintf(["The probability of having " ,num2str(i), "  guest is:",num2str(1-numerator),'\n']);
  endfor
  plot(x,y,"or-")
  title("Equation of probability")
  xlabel('nguests')
  ylabel('probability')
endif