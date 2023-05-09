# Solution

```bash
#!/bin/bash
read -p "Enter a number: " n
if [ $n -lt 10 ]; then
  echo "It is a one digit number"
else
  echo "It is a two digit number"
fi
```

Save the above script in a file named `simple_if.sh`. Run the script with the following command:

```bash
bash simple_if.sh
```
