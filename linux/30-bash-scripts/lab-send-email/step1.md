# Send Email

## Problem

Create a Bash script named `mail_example.sh` that sends an email to a designated recipient, using the 'mail' command. The email should have a specified subject and message.

## Requirements

To successfully complete this challenge, the script should:

* Declare a 'Recipient' variable with the email address of the recipient
* Declare a 'Subject' variable with the subject of the email
* Declare a 'Message' variable with the content of the email
* Use the 'mail' command to send the email with the specified subject, message, and recipient

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
