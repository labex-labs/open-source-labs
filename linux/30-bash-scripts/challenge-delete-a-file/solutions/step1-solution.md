## Solution

Create a file named `delete_file.sh` with the following code:

```bash
#!/bin/bash  
echo "Enter filename to remove"  
read fn  
rm -i $fn
```

Save the file and run it using the following commands:

```bash
ls  
bash delete_file.sh  
ls
```

The script will prompt you to enter the filename you want to delete. Once you enter the filename, it will ask for confirmation before deleting the file.

