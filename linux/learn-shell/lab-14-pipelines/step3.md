# Counting the Processors

Now that we have the processor entries, we can use the `wc` command with the `-l` option to count the number of lines in the output. Each line represents a processor, so the line count will give us the total number of processors.

```bash
cat /proc/cpuinfo | grep processor | wc -l
```
