### Combine String variables:

You can easily combine string variables in bash. Create a file named “**string\_combine.sh**” and add the following script to check how you can combine string variables in bash by placing variables together or using **‘+’** operator.

#!/bin/bash  
  
string1\="Linux"  
string2\="Hint"  
echo "$string1$string2"  
string3\=$string1+$string2  
string3+=" is a good tutorial blog site"  
echo $string3

Run the file with bash command.

$ bash string\_combine.sh

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20731%2087'%3E%3C/svg%3E)

![](https://linuxhint.com/wp-content/uploads/2018/07/h16.png)

