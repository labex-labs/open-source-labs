# if-else Statement

You can expand the if statement to include an else clause, which allows you to specify code to execute when the expression is false.

Update the `if.sh` script to include an else clause that prints a message when the `NAME` variable is not equal to "John":

```bash
#!/bin/bash
NAME="Bill"
if [ "$NAME" = "John" ]; then
  echo "True - my name is indeed John"
else
  echo "False"
  echo "You must mistaken me for $NAME"
fi
```

The above script will print "False" and "You must mistaken me for Bill" because the expression is false.
