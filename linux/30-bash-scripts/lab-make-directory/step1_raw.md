### Make Directory:

Bash uses ‘**mkdir**’ command to create a new directory. Create a file named ‘**make_directory.sh**’ and add the following code to take a new directory name from the user. If the directory name is not exist in the current location then it will create the directory, otherwise the program will display error.

#!/bin/bash  
echo "Enter directory name"  
read newdir  
\`mkdir $newdir\`

Run the file with bash command.

$ bash make_directory.sh

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20734%20120'%3E%3C/svg%3E)

![](https://linuxhint.com/wp-content/uploads/2018/07/h22.png)
