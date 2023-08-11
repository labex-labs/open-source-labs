# Get User Input

Create a Bash script named 'user_input.sh' that takes input from the user and displays it on the screen. The script should prompt the user to enter their name and then display a welcome message that includes their name.

- The script should use the 'read' command to take input from the user.
- The script should prompt the user to enter their name.
- The script should display a welcome message that includes the user's name.
- The script should be named 'user_input.sh'.

Here is an example script that meets the requirements:

```bash
#!/bin/bash
echo "Enter Your Name"
read name
echo "Welcome $name to LinuxHint"
```

Save this script as 'user_input.sh' and run it with the following command:

```bash
bash user_input.sh
```

When you run the script, it will prompt you to enter your name. After you enter your name, it will display a welcome message that includes your name.
