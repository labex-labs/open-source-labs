# Perform Cleanup with Trap

One common usage of the `trap` command is to perform cleanup activities, such as deleting temporary files. Add a command to delete a folder and exit the script when a specific signal is received:

```bash
trap "rm -f folder; exit" 2
```

In this example, when the `SIGINT` signal is received (Ctrl+C), the script will delete the folder named `folder` and then exit gracefully.
