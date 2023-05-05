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
