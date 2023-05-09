### Get substring of String:

Like other programming language, bash has no built-in function to cut value from any string data. But you can do the task of substring in another way in bash that is shown in the following script. To test the script, create a file named ‘**substring_example.sh**’ with the following code. Here, the value, **6** indicates the starting point from where the substring will start and **5** indicates the length of the substring.

#!/bin/bash  
Str\="Learn Linux from LinuxHint"  
subStr\=${Str:6:5}  
echo $subStr

Run the file with bash command.

$ bash substring_example.sh

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20731%2069'%3E%3C/svg%3E)

![](https://linuxhint.com/wp-content/uploads/2018/07/h17.png)
