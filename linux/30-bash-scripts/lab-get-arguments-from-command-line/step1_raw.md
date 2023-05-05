### Get Arguments from Command Line:

Bash script can read input from command line argument like other programming language. For example, **$1** and **$2** variable are used to read first and second command line arguments. Create a file named “**command\_line.sh**” and add the following script. Two argument values read by the following script and prints the total number of arguments and the argument values as output.

#!/bin/bash  
echo "Total arguments : $#"  
echo "1st Argument = $1"  
echo "2nd argument = $2"

Run the file with bash command.

$ bash command\_line.sh Linux Hint

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20731%2096'%3E%3C/svg%3E)

![](https://linuxhint.com/wp-content/uploads/2018/07/h14.png)

You can check the following link to know more about the use of [bash command line argument](https://linuxhint.com/command_line_arguments_bash_script/).

