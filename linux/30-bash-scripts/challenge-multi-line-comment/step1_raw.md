### Use of Multi-line comment:

You can use multi line comment in bash in various ways. A simple way is shown in the following example. Create a new bash named, **‘multiline-comment.sh’** and add the following script. Here, **‘:’** and **“** **’** **”** symbols are used to add multiline comment in bash script. This following script will calculate the square of 5.

#!/bin/bash  
: '  
The following script calculates  
the square value of the number, 5.  
'  
((area\=5\*5))  
echo $area

Run the file with bash command.

$ bash multiline-comment.sh

![](https://linuxhint.com/wp-content/uploads/2018/07/h5.png)

![](https://linuxhint.com/wp-content/uploads/2018/07/h5.png)

You can check the following link to know more about the use of [bash comment](https://linuxhint.com/bash_comments/).

