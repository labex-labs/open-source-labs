# Analyzing Memory Information

Let's switch gears and look at memory information. The file `/proc/meminfo` contains details about system memory. We'll use the `head` command to view just the first few lines:

```bash
cat /proc/meminfo | head -n 5
```

This command displays the first 5 lines of memory information. The `head` command is used to output the first part of files. The `-n 5` option tells it to show the first 5 lines.

You should see information about total memory, free memory, and other memory stats.
