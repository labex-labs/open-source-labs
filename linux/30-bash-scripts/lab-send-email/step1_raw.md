### Send Email:

You can send email by using ‘**mail**’ or ‘**sendmail**’ command. Before using these commands, you have to install all necessary packages. Create a file named, ‘**mail\_example.sh**’ and add the following code to send the email.

#!/bin/bash  
Recipient\=”admin@example.com”  
Subject\=”Greeting”  
Message\=”Welcome to our site”  
\`mail \-s $Subject $Recipient <<< $Message\`

Run the file with bash command.

$ bash mail\_example.sh

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20733%2069'%3E%3C/svg%3E)

![](https://linuxhint.com/wp-content/uploads/2018/07/h28.png)

