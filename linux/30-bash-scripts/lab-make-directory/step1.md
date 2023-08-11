# Make Directory

Create a Bash script named `make_directory.sh` that takes a new directory name from the user. If the directory name does not exist in the current location, the script should create the directory. Otherwise, the script should display an error message.

- The Bash script should be named `make_directory.sh`.
- The script should take a new directory name from the user.
- If the directory name does not exist in the current location, the script should create the directory.
- If the directory name already exists in the current location, the script should display an error message.

```bash
#!/bin/bash
echo "Enter directory name"
read newdir
if [ ! -d "$newdir" ]; then
  mkdir "$newdir"
  echo "Directory created successfully"
else
  echo "Error: Directory already exists"
fi
```

Save the above code in a file named `make_directory.sh`. Run the script with the following command:

```bash
bash make_directory.sh
```
