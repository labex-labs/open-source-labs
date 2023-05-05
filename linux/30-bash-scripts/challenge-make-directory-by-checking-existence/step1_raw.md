### Make directory by checking existence:

If you want to check the existence of directory in the current location before executing the ‘**mkdir**’ command then you can use the following code. **‘-d**’ option is used to test a particular directory is exist or not. Create a file named, ‘**directory_exist.sh’** and add the following code to create a directory by checking existence.

#!/bin/bash  
echo "Enter directory name"  
read ndir  
if \[ \-d "$ndir" \]  
then  
echo "Directory exist"  
else  
\`mkdir $ndir\`  
echo "Directory created"  
fi

Run the file with bash command.

$ bash directory_exist.sh

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20729%20130'%3E%3C/svg%3E)

![](https://linuxhint.com/wp-content/uploads/2018/07/h23.png)

You can check the following link to know more about [bash directory creation](https://linuxhint.com/bash_mkdir_not_existent_path/).
