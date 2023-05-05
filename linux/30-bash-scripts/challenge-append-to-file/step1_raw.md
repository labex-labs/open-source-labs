### Append to File:

New data can be added into any existing file by using **‘>>’** operator in bash. Create a file named **‘append_file.sh**’ and add the following code to add new content at the end of the file. Here, ‘**Learning Laravel 5**’ will be added at the of ‘**book.txt’** file after executing the script.

#!/bin/bash

echo "Before appending the file"  
cat book.txt

echo "Learning Laravel 5"\>> book.txt  
echo "After appending the file"  
cat book.txt

Run the file with bash command.

$ bash append_file.sh

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20728%20247'%3E%3C/svg%3E)

![](https://linuxhint.com/wp-content/uploads/2018/07/h26.png)
