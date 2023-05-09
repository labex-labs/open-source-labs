### Using For Loop:

The basic **for** loop declaration is shown in the following example. Create a file named ‘**for_example.sh**’ and add the following script using **for** loop. Here, **for** loop will iterate for **10** times and print all values of the variable, **counter** in single line.

#!/bin/bash  
for (( counter\=10; counter\>0; counter-- ))  
do  
echo \-n "$counter "  
done  
printf "\\n"

Run the file with bash command.

$ bash for_example.sh

![](https://linuxhint.com/wp-content/uploads/2018/07/h7.png)

![](https://linuxhint.com/wp-content/uploads/2018/07/h7.png)

You can use for loop for different purposes and ways in your bash script. You can check the following link to know more about the use of [bash for loop](https://linuxhint.com/bash-for-loop-examples/).
