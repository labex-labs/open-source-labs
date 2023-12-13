# Test if File Exist

## Problem

Create a Bash script named 'file_exist.sh' that takes a filename as an argument and checks if the file exists in the current location. If the file exists, the script should print "File exists" and if the file does not exist, the script should print "File does not exist".

## Requirements

- The script should be named 'file_exist.sh'.
- The script should take a filename as an argument.
- The script should use the '-f' option to check the file existence.
- If the file exists, the script should print "File exists".
- If the file does not exist, the script should print "File does not exist".

## Example

To run the script, use the following command:

```bash
bash file_exist.sh filename.txt
```

Output:

```bash
File exists
```

```bash
bash file_exist.sh non_existent_file.txt
```

Output:

```bash
File does not exist
```
