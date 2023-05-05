## Solution

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
