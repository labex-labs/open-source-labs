### Pass Return Value from Function:

Bash function can pass both numeric and string values. How you can pass a string value from the function is shown in the following example. Create a file named, ‘**function_return.sh**’ and add the following code. The function, **greeting()** returns a string value into the variable, **val** which prints later by combining with other string.

#!/bin/bash  
function greeting() {

str\="Hello, $name"  
echo $str

}

echo "Enter your name"  
read name

val\=$(greeting)  
echo "Return value of the function is $val"

Run the file with bash command.

$ bash function_return.sh

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20728%20103'%3E%3C/svg%3E)

![](https://linuxhint.com/wp-content/uploads/2018/07/h21.png)

You can check the following link to know more about the use of [bash functions](https://linuxhint.com/return-string-bash-functions/).
