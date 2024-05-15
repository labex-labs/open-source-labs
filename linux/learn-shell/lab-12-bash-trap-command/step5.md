# Refactor the Trap Action

Instead of using an inline message in the `trap` command, let's refactor it to use a function. Add a function definition to the script:

```bash
function booh {
  echo "Booh!"
}
```

Now, modify the `trap` command to use the `booh` function as the action:

```bash
trap booh SIGINT SIGTERM
```
