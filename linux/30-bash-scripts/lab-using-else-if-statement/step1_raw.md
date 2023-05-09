### Using else if statement:

The use of **else if** condition is little different in bash than other programming language. ‘**elif**’ is used to define **else if** condition in bash. Create a file named, ‘**elseif_example.sh**’ and add the following script to check how **else if** is defined in bash script.

#!/bin/bash

echo "Enter your lucky number"  
read n

if \[ $n \-eq 101 \];  
then  
echo "You got 1st prize"  
elif \[ $n \-eq 510 \];  
then  
echo "You got 2nd prize"  
elif \[ $n \-eq 999 \];  
then  
echo "You got 3rd prize"  
else  
echo "Sorry, try for the next time"  
fi

Run the file with bash command.

$ bash elseif_example.sh

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20729%20241'%3E%3C/svg%3E)

![](https://linuxhint.com/wp-content/uploads/2018/07/h12.png)
