# Test if a file exists

To test if a file exists, you can use the `-e` command. This command checks if a file exists as a regular file or a directory.

If the file exists, it will return true; otherwise, it will return false.

```shell
#!/bin/bash
filename="sample.md"
if [ -e "$filename" ]; then
  echo "$filename exists as a file"
fi
```

Cearate a file called `~/project/file.sh`.

```shell
cd ~/project
chmod +x file.sh
./file.sh
```

Then, create a file called `~/project/sample.md`.

```shell
cd ~/project
touch sample.md
```

Re-run the script.

```shell
./file.sh
```

```text
sample.md exists as a file
```
