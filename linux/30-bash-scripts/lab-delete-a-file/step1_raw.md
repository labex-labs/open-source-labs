### Delete a File:

‘**rm**’ command is used in bash to remove any file. Create a file named ‘**delete_file.sh**’ with the following code to take the filename from the user and remove. Here, **‘-i’** option is used to get permission from the user before removing the file.

#!/bin/bash  
echo "Enter filename to remove"  
read fn  
rm \-i $fn

Run the file with bash command.

$ ls  
$ bash delete_file.sh  
$ ls

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20732%20185'%3E%3C/svg%3E)

![](https://linuxhint.com/wp-content/uploads/2018/07/h25.png)
