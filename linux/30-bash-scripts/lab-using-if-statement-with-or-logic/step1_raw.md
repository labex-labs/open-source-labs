### Using if statement with OR logic:

‘**||**’ is used to define **OR** logic in **if** condition. Create a file named **‘if_with_OR.sh’** with the following code to check the use of **OR** logic of **if** statement. Here, the value of **n** will be taken from the user. If the value is equal to **15** or **45** then the output will be “**You won the game**”, otherwise the output will be “**You lost the game**”.

#!/bin/bash

echo "Enter any number"  
read n

if \[\[ ( $n \-eq 15 || $n  \-eq 45 ) \]\]  
then  
echo "You won the game"  
else  
echo "You lost the game"  
fi

Run the file with bash command.

$ bash if_with_OR.sh

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20730%20173'%3E%3C/svg%3E)

![](https://linuxhint.com/wp-content/uploads/2018/07/h11.png)
