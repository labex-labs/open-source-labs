# Numeric Comparisons

Shell scripts can also compare numbers. Let's create a new script to demonstrate numeric comparisons.

Create a new file called `numeric.sh`:

```bash
touch numeric.sh
```

Open `numeric.sh` in the WebIDE and add the following content:

```bash
#!/bin/bash

NUMBER=10

if [ $NUMBER -lt 5 ]; then
  echo "The number is less than 5"
elif [ $NUMBER -eq 10 ]; then
  echo "The number is exactly 10"
elif [ $NUMBER -gt 15 ]; then
  echo "The number is greater than 15"
else
  echo "The number is between 5 and 15, but not 10"
fi
```

This script introduces numeric comparison operators:

- `-lt`: less than
- `-eq`: equal to
- `-gt`: greater than

There are also others you can use:

- `-le`: less than or equal to
- `-ge`: greater than or equal to
- `-ne`: not equal to

Notice that we use these special operators instead of symbols like `<` or `>`. This is because in Bash, `<` and `>` are used for input/output redirection, not for numeric comparison.

Now, let's make the script executable and run it:

```bash
chmod +x numeric.sh
./numeric.sh
```

You should see the output: `The number is exactly 10`

Try changing the `NUMBER` variable to different values and run the script again. See how the output changes based on the value you set.

For example, if you change `NUMBER` to 20, you should get "The number is greater than 15". If you change it to 7, you should get "The number is between 5 and 15, but not 10".
