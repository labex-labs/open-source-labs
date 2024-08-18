# Adding an Else Clause

Now, let's expand our if statement to include an else clause. This allows us to specify what should happen when the condition is false.

Open the `if.sh` file in the WebIDE again and modify it as follows:

```bash
#!/bin/bash

NAME="Alice"
if [ "$NAME" = "John" ]; then
  echo "The name is John"
else
  echo "The name is not John"
fi
```

Let's go through the changes:

1. We've changed the `NAME` variable to "Alice". This is to demonstrate what happens when the condition is false.

2. We've added an `else` clause. This clause specifies what should happen if the condition in the if statement is false.

3. After the `else`, we've added another `echo` command that will run if `NAME` is not "John".

The `else` clause is optional in if statements, but it's very useful when you want to do something specific when the condition is false, rather than just doing nothing.

Save the file with these changes.

Now, run the script again:

```bash
./if.sh
```

This time, you should see the output: `The name is not John`

This is because `NAME` is now "Alice", so the condition `[ "$NAME" = "John" ]` is false, and the code in the `else` block is executed.

Try changing the `NAME` variable back to "John" and run the script again. What output do you get? This is a good way to test that your if-else statement is working correctly for both cases.
