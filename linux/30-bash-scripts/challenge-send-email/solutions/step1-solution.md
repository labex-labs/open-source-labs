## Solution

The following code can be used to create the `mail_example.sh` script.

```bash
#!/bin/bash
Recipient="admin@example.com"
Subject="Greeting"
Message="Welcome to our site"
`mail -s $Subject $Recipient <<< $Message`
```

To run the script, execute the following command in the terminal:
```bash
$ bash mail_example.sh
```

This will send an email to the recipient with the subject "Greeting" and the message "Welcome to our site".
