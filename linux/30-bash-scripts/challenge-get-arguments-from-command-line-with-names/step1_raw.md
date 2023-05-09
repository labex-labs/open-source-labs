### Get arguments from command line with names:

How you can read command line arguments with names is shown in the following script. Create a file named, ‘**command_line_names.sh’** and add the following code. Here, two arguments, **X** and **Y** are read by this script and print the sum of X and Y.

#!/bin/bash  
for arg in "$@"  
do  
index\=$(echo $arg | cut \-f1 \-d\=)  
val\=$(echo $arg | cut \-f2 \-d\=)  
case $index in  
X) x\=$val;;

Y) y\=$val;;

\*)  
esac  
done  
((result\=x+y))  
echo "X+Y=$result"

Run the file with bash command and with two command line arguments.

$ bash command_line_names X\=45 Y\=30

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20732%2072'%3E%3C/svg%3E)

![](https://linuxhint.com/wp-content/uploads/2018/07/h15.png)
