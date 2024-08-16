# Test the updated script

Now, let's test our updated script with different numbers of arguments:

```bash
./arguments.sh
./arguments.sh one
./arguments.sh one two
./arguments.sh one two three four
```

You should see different outputs based on the number of arguments provided.

For beginners:

- Running the script without any arguments (`./arguments.sh`) will trigger the first condition in our script.
- Each subsequent command adds more arguments, demonstrating how our script handles different cases.
- Notice how the script's behavior changes based on the number of arguments. This kind of flexibility is very useful in real-world scripts.
