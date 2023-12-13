# Solution

```bash
#!/bin/bash
filename=$1
if [ -f "$filename" ]; then
  echo "File exists"
else
  echo "File does not exist"
fi
```

Save the above code in a file named 'file_exist.sh'. Run the following commands to check the existence of the file. Here, **book.txt** file exists and  **book2.txt** is not exist in the current location.

```bash
ls
bash file_exist.sh book.txt
bash file_exist.sh book2.txt
```
