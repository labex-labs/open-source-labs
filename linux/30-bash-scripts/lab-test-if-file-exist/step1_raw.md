### Test if File Exist:

You can check the existence of file in bash by using **‘-e’** or **‘-f’** option. **‘-f’** option is used in the following script to test the file existence. Create a file named, ‘**file_exist.sh**’ and add the following code. Here, the filename will pass from the command line.

#!/bin/bash  
filename\=$1  
if \[ \-f "$filename" \]; then  
echo "File exists"  
else  
echo "File does not exist"  
fi

Run the following commands to check the existence of the file. Here, **book.txt** file exists and  **book2.txt** is not exist in the current location.

$ ls  
$ bash file_exist.sh book.txt  
$ bash file_exist.sh book2.txt

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20725%20148'%3E%3C/svg%3E)

![](https://linuxhint.com/wp-content/uploads/2018/07/h27.png)
