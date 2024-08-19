# Introducing Elif

Sometimes, we want to check multiple conditions. This is where the `elif` (else if) clause comes in handy. Let's modify our script to handle multiple names.

Update the `if.sh` file with the following content:

```bash
#!/bin/bash

NAME="George"
if [ "$NAME" = "John" ]; then
  echo "John Lennon"
elif [ "$NAME" = "Paul" ]; then
  echo "Paul McCartney"
elif [ "$NAME" = "George" ]; then
  echo "George Harrison"
elif [ "$NAME" = "Ringo" ]; then
  echo "Ringo Starr"
else
  echo "Unknown member"
fi
```

Let's break down this script:

1. We start with `NAME="George"`. This will be the name we're checking.
2. The first `if` statement checks if the name is "John".
3. If it's not "John", we move to the first `elif` (else if) statement, which checks if the name is "Paul".
4. If it's not "Paul", we move to the next `elif`, checking for "George".
5. If it's not "George", we check for "Ringo".
6. If none of these conditions are true, we fall through to the `else` clause, which will echo "Unknown member".

The `elif` clause allows you to check multiple conditions in sequence. You can have as many `elif` clauses as you need. The conditions are checked in order, and the first one that's true will have its corresponding code block executed.

Save the file with these changes.

Now, run the script:

```bash
./if.sh
```

You should see the output: `George Harrison`

Try changing the `NAME` variable to different values ("John", "Paul", "Ringo", or something else entirely) and run the script each time. Observe how the output changes based on the value of `NAME`.
