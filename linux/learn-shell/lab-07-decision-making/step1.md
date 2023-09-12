# Basic if Statement

The basic syntax of an if statement in shell programming is as follows:

```bash
if [ expression ]; then
    # code to execute if the expression is true
fi
```

Let's start by creating a simple if statement that checks if a variable called `NAME` is equal to "John".

```bash
#!/bin/bash
NAME="John"
if [ "$NAME" = "John" ]; then
  echo "True - my name is indeed John"
fi
```
