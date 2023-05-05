# Send Email

## Introduction

In Bash, you can send emails using the `mail` or `sendmail` command. However, before using these commands, you need to install the necessary packages.

## Problem

Create a Bash script named `mail_example.sh` that sends an email to a recipient with a subject and message. The script should contain the following code:

```bash
#!/bin/bash  
Recipient="admin@example.com"  
Subject="Greeting"  
Message="Welcome to our site"  
`mail -s $Subject $Recipient <<< $Message`
```

To run the script, use the following command:

```bash
bash mail_example.sh
```

## Requirements

- The Bash script should be named `mail_example.sh`.
- The recipient's email address should be stored in a variable named `Recipient`.
- The email subject should be stored in a variable named `Subject`.
- The email message should be stored in a variable named `Message`.
- The `mail` command should be used to send the email.
- The script should be executable using the `bash` command.

## Solution

To send an email using Bash, you need to use the `mail` command. The `mail` command takes the recipient's email address, subject, and message as arguments. In the Bash script, you can store these values in variables and pass them to the `mail` command using command substitution.

## Summary

In this Bash challenge, you learned how to send an email using the `mail` command in Bash. You created a Bash script that sends an email to a recipient with a subject and message. You also learned how to store values in variables and pass them to commands using command substitution.