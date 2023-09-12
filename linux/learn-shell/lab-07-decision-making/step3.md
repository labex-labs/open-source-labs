# if-elif-else Statement

You can further expand the if statement to include multiple elif clauses, which allow you to specify additional expressions to evaluate if the previous ones are false.

```bash
#!/bin/bash
NAME="George"
if [ "$NAME" = "John" ]; then
  echo "John Lennon"
elif [ "$NAME" = "George" ]; then
  echo "George Harrison"
else
  echo "This leaves us with Paul and Ringo"
fi
```

The above script will print "George Harrison" because the expression is true.
