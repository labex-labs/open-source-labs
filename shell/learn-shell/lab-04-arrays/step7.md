# Run the script

Now that we've written our script, it's time to run it and see the results.

1. In your terminal, make sure you're in the correct directory:

   ```bash
   cd ~/project
   ```

2. Make the script executable:

   ```bash
   chmod +x arrays.sh
   ```

3. Run the script:

   ```bash
   ./arrays.sh
   ```

You should see output similar to this:

```
NUMBERS array: 1 2 3
STRINGS array: hello world
The number of names listed in the NAMES array: 3
The second name on the NAMES list is: Eric
```

This output shows that our array operations were successful:

- The `NUMBERS` array contains 1, 2, and 3.
- The `STRINGS` array contains "hello" and "world".
- We correctly counted 3 names in the `NAMES` array.
- We successfully retrieved "Eric" as the second name.
