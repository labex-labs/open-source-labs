# Pass Return Value from Function

In this lab, we will focus on passing a string value from a Bash function. We will create a function that returns a string value and then use that value in our script.

- A Bash script editor
- Basic knowledge of Bash scripting
- Access to a Linux or Unix operating system

To pass a string value from a Bash function, we can create a function that returns a string value and then use that value in our script. Here is an example:

```bash
#!/bin/bash
function greeting() {

  str="Hello, $name"
  echo $str

}

echo "Enter your name"
read name

val=$(greeting)
echo "Return value of the function is $val"
```

In this example, we create a function called **greeting()** that takes no arguments. Inside the function, we create a string variable called **str** that contains a greeting message with the user's name. We then use the **echo** command to print the value of **str**.

In the main part of the script, we prompt the user to enter their name using the **read** command. We then call the **greeting()** function and store the return value in a variable called **val**. Finally, we print the value of **val** using the **echo** command.

When we run this script, we should see the greeting message with the user's name printed to the console.
