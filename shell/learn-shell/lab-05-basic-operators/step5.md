# Make the script executable and run it

Now that our script is complete, we need to make it executable and then run it.

1. In the terminal, make the script executable with the `chmod` command:

   ```bash
   chmod +x ~/project/fruit_basket.sh
   ```

   This command changes the mode of the file, adding execute (`x`) permission for the user.

2. Now, let's run the script:

   ```bash
   ~/project/fruit_basket.sh
   ```

   This command tells Bash to execute our script. The `~/project/` part specifies the path to our script.

You should see output similar to:

```
Total Cost is 128 cents
```

This output shows that the total cost of our fruit basket (1 pineapple, 2 bananas, 3 watermelons, and the basket itself) is 128 cents.
