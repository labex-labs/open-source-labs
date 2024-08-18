# Make the script executable and run it

Now that we have completed our script, let's make it executable and run it.

1. In the terminal, make the script executable:

```bash
chmod +x ~/project/array-comparison.sh
```

The `chmod` command changes the permissions of a file. The `+x` option adds executable permissions, allowing you to run the script.

2. Run the script:

```bash
~/project/array-comparison.sh
```

This command executes your script. The `~/project/` part specifies the path to the script.

You should see output similar to this:

```
Common elements between a and b: 5 6
Common elements among a, b, and c: 5
```

This output shows that:

- The common elements between arrays `a` and `b` are 5 and 6.
- The common element among all three arrays (`a`, `b`, and `c`) is 5.

If you don't see this output or encounter an error, double-check your script for any typos or missing parts.
