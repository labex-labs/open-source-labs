## Solution

Create a new file named `echo_example.sh` and add the following script:

```bash
#!/bin/bash  
echo "Printing text with newline"  
echo -n "Printing text without newline"  
echo -e "\nRemoving \t backslash \t characters\n"
```

Save the file and make it executable using the following command:

```bash
chmod +x echo_example.sh
```

Run the script using the following command:

```bash
./echo_example.sh
```

The output should be:

```bash
Printing text with newline
Printing text without newlineRemoving      backslash        characters
```

