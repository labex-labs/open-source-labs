### Create function with Parameters:

Bash can’t declare function parameter or arguments at the time of function declaration. But you can use parameters in function by using other variable. If two values are passed at the time of function calling then $1 and $2 variable are used for reading the values. Create a file named ‘**function|\_parameter.sh**’ and add the following code. Here, the function, ‘**Rectangle\_Area’** will calculate the area of a rectangle based on the parameter values.

#!/bin/bash  
  
Rectangle\_Area() {  
area\=$(($1 \* $2))  
echo "Area is : $area"  
}  
  
Rectangle\_Area 10 20

Run the file with bash command.

$ bash function\_parameter.sh

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20735%2072'%3E%3C/svg%3E)

![](https://linuxhint.com/wp-content/uploads/2018/07/h20.png)

