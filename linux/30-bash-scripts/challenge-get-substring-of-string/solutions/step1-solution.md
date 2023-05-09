# Solution

Here is an example Bash script that demonstrates how to get a substring of a string:

```bash
#!/bin/bash
string="Learn Bash scripting from BashChallenge"
substring=${string:6:4}
echo $substring
```

In this script, we define a string variable `string` with the value "Learn Bash scripting from BashChallenge". We then use the Bash built-in syntax `${string:6:4}` to extract a substring starting from the 6th position and having a length of 4 characters. Finally, we print the extracted substring using the `echo` command.
