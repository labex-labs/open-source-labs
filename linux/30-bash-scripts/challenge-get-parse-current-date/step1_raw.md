### Get Parse Current Date:

You can get the current system date and time value using \`**date**\` command. Every part of date and time value can be parsed using ‘**Y’, ‘m’, ‘d’, ‘H’, ‘M’** and ‘**S’**. Create a new file named ‘**date\_parse.sh’** and add the following code to separate day, month, year, hour, minute and second values.

#!/bin/bash  
Year\=\`date +%Y\`  
Month\=\`date +%m\`  
Day\=\`date +%d\`  
Hour\=\`date +%H\`  
Minute\=\`date +%M\`  
Second\=\`date +%S\`  
echo \`date\`  
echo "Current Date is: $Day\-$Month\-$Year"  
echo "Current Time is: $Hour:$Minute:$Second"

Run the file with bash command.

$ bash date\_parse.sh

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20736%20106'%3E%3C/svg%3E)

![](https://linuxhint.com/wp-content/uploads/2018/07/h29.png)

