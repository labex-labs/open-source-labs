### Create and Execute First BASH Program:

You can run bash script from the terminal or by executing any bash file. Run the following command from the terminal to execute a very simple bash statement. The output of the command will be ‘**Hello World**’.

$ echo "Hello World"

![](https://linuxhint.com/wp-content/uploads/2018/07/h.png)

![](https://linuxhint.com/wp-content/uploads/2018/07/h.png)

Open any editor to create a bash file. Here, **nano** editor is used to create the file and filename is set as ‘**First.sh’**

$ nano First.sh

Add the following bash script to the file and save the file.

#!/bin/bash  
echo "Hello World"

![](https://linuxhint.com/wp-content/uploads/2018/07/h1.png)

![](https://linuxhint.com/wp-content/uploads/2018/07/h1.png)

You can run bash file by two ways. One way is by using bash command and another is by setting execute permission to bash file and run the file. Both ways are shown here.

$ bash First.sh

**Or,**

$ chmod a+x First.sh  
$ ./First.sh

![](https://linuxhint.com/wp-content/uploads/2018/07/h2.png)

![](https://linuxhint.com/wp-content/uploads/2018/07/h2.png)
