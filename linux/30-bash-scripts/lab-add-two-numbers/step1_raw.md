### Add Two Numbers:

You can do the arithmetical operations in bash in different ways. How you can add two integer numbers in bash using double brackets is shown in the following script. Create a file named ‘**add_numbers.sh**’ with the following code. Two integer values will be taken from the user and printed the result of addition.

#!/bin/bash  
echo "Enter first number"  
read x  
echo "Enter second number"  
read y  
(( sum\=x+y ))  
echo "The result of addition=$sum"

Run the file with bash command.

$ bash add_numbers.sh

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20733%20137'%3E%3C/svg%3E)

![](https://linuxhint.com/wp-content/uploads/2018/07/h18.png)

You can check the following link to know more about [bash arithmetic](https://linuxhint.com/bash_arithmetic_operations/).
