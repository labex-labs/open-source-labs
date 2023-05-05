### Wait Command:

**wait**  is a built-in command of Linux that waits for completing any running process. **wait** command is used with a particular process id or job id. If no process id or job id is given with wait command then it will wait for all current child processes to complete and returns exit status. Create a file named ‘**wait_example.sh’** and add the following script.

#!/bin/bash  
echo "Wait command" &  
process_id\=$!  
wait $process_id  
echo "Exited with status $?"

Run the file with bash command.

$ bash wait_example.sh

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20727%2061'%3E%3C/svg%3E)

![](https://linuxhint.com/wp-content/uploads/2018/07/h30.png)

You can check the following link to know more about [bash linux wait command](https://linuxhint.com/wait_command_linux/).
