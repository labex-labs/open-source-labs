### Using Case Statement:

**Case** statement is used as the alternative of **if-elseif-else** statement. The starting and ending block of this statement is defined by ‘**case**’ and ‘**esac**’. Create a new file named, ‘**case\_example.sh**’ and add the following script. The output of the following script will be same to the previous **else if** example.

#!/bin/bash  
  
echo "Enter your lucky number"  
read n  
case $n in  
101)  
echo echo "You got 1st prize" ;;  
510)  
echo "You got 2nd prize" ;;  
999)  
echo "You got 3rd prize" ;;  
\*)  
echo "Sorry, try for the next time" ;;  
esac

Run the file with bash command.

$ bash case\_example.sh

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20725%20318'%3E%3C/svg%3E)

![](https://linuxhint.com/wp-content/uploads/2018/07/h13.png)

