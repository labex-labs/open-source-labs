# Use Signal Numbers in the Trap Command

Instead of using signal names in the `trap` command, you can also use their corresponding numbers. We can use the earlier command `kill -l` to determine the numbers. Modify the `trap` command to use signal numbers:

```bash
trap booh 2 15
```

In this example, `2` corresponds to `SIGINT` and `15` corresponds to `SIGTERM`.
