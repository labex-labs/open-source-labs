### Using if statement:

You can use if condition with single or multiple conditions. Starting and ending block of this statement is define by **‘if’** and **‘fi’**. Create a file named ‘**simple_if.sh**’ with the following script to know the use **if** statement in bash. Here, **10** is assigned to the variable, **n**. if the value of **$n** is less than 10 then the output will be “**It is a one digit number**”, otherwise the output will be “**It is a two digit number**”. For comparison, **‘-lt’** is used here. For comparison, you can also use **‘-eq’** for **equality**, **‘-ne’** for **not equality** and **‘-gt’** for **greater than** in bash script.

#!/bin/bash  
n\=10  
if \[ $n \-lt 10 \];  
then  
echo "It is a one digit number"  
else  
echo "It is a two digit number"  
fi

Run the file with bash command.

$ bash simple_if.sh

![](https://linuxhint.com/wp-content/uploads/2018/07/h9.png)

![](https://linuxhint.com/wp-content/uploads/2018/07/h9.png)
