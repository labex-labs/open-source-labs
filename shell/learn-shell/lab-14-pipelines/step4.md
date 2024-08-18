# Counting CPU Cores

To count the number of CPU cores, we can count the number of "processor" lines in the output. We'll use the `wc` (word count) command with the `-l` option to count lines:

```bash
cat /proc/cpuinfo | grep "processor" | wc -l
```

This pipeline does three things:

1. `cat /proc/cpuinfo` reads the CPU info
2. `grep "processor"` filters for lines containing "processor"
3. `wc -l` counts the number of lines in the output

The result is the number of CPU cores in your system. For example, if you see `4`, that means your system has 4 CPU cores.
