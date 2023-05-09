### Read a File:

You can read any file line by line in bash by using loop. Create a file named, ‘**read_file.sh**’ and add the following code to read an existing file named, ‘**book.txt**’.

#!/bin/bash  
file\='book.txt'  
while read line; do  
echo $line  
done < $file

Run the file with bash command.

$ bash read_file.sh

Run the following command to check the original content of ‘**book.txt**’ file.

$ cat book.txt

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20729%20210'%3E%3C/svg%3E)

![](https://linuxhint.com/wp-content/uploads/2018/07/h24.png)

You can check the following link to know the different ways to [read file in bash](https://linuxhint.com/read_file_line_by_line_bash/).
