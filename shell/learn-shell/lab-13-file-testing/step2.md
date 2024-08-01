# Test if a directory exists

To test if a directory exists, you can use the `-d` command. This command checks if a directory exists. If the directory exists, it will return true; otherwise, it will return false.

```shell
#!/bin/bash
directory_name="test_directory"
if [ -d "$directory_name" ]; then
  echo "$directory_name exists as a directory"
fi
```

Cearate a file called `~/project/directory.sh`.

```shell
cd ~/project
chmod +x directory.sh
./directory.sh
```

Then, create a directory called `~/project/test_directory`.

```shell
cd ~/project
mkdir test_directory
```

Re-run the script.

```shell
./directory.sh
```

```text
test_directory exists as a directory
```
