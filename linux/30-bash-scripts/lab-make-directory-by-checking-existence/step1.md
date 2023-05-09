# Make Directory by Checking Existence

## Problem

Create a Bash script named `directory_exist.sh` that prompts the user to enter a directory name. The script should then check if the directory already exists in the current location. If the directory exists, the script should print "Directory exist". If the directory does not exist, the script should create the directory and print "Directory created".

## Requirements

- The script should be named `directory_exist.sh`.
- The script should prompt the user to enter a directory name.
- The script should check if the directory already exists in the current location using the `-d` option.
- If the directory exists, the script should print "Directory exist".
- If the directory does not exist, the script should create the directory using the `mkdir` command.
- The script should print "Directory created" after creating the directory.

## Solution

```bash
#!/bin/bash
echo "Enter directory name"
read ndir
if [ -d "$ndir" ]; then
  echo "Directory exist"
else
  $(mkdir $ndir)
  echo "Directory created"
fi
```

To run the script, use the following command:

```
bash directory_exist.sh
```
