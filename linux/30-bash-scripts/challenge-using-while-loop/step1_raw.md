### Using While Loop:

Create a bash file with the name, **‘while_example.sh’,** to know the use of **while** loop. In the example, **while** loop will iterate for **5** times. The value of **count** variable will increment by **1** in each step. When the value of **count** variable will 5 then the **while** loop will terminate.

#!/bin/bash  
valid\=true  
count\=1  
while \[ $valid \]  
do  
echo $count  
if \[ $count \-eq 5 \];  
then  
break  
fi  
((count++))  
done

Run the file with bash command.

$ bash while_example.sh

![](https://linuxhint.com/wp-content/uploads/2018/07/h6.png)

![](https://linuxhint.com/wp-content/uploads/2018/07/h6.png)

You can check the following link to know more about the use of [bash while loop](https://linuxhint.com/bash-while-loop-examples/).
