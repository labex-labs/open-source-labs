# Add the shebang and initialize the arrays

Now, let's start writing our script by adding the shebang and initializing our arrays.

1. Add the following content to `array-comparison.sh`:

```bash
#!/bin/bash

# Initialize the arrays
a=(3 5 8 10 6)
b=(6 5 4 12)
c=(14 7 5 7)
```

Let's break this down:

- The first line `#!/bin/bash` is called a shebang. It tells the system to use the Bash interpreter to run this script. This line is crucial for any shell script.
- We then initialize three arrays: `a`, `b`, and `c`. In Bash, arrays are defined by enclosing the elements in parentheses `()` and separating them with spaces.
- Each array contains different integer values. We'll use these arrays to find common elements.
