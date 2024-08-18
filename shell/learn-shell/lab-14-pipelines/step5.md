# Finding Unique CPU Models

If your system has multiple CPUs, they might be of different models. Let's find out how many unique CPU models are present:

```bash
cat /proc/cpuinfo | grep "model name" | sort | uniq | wc -l
```

This pipeline:

1. Reads the CPU info
2. Filters for "model name" lines
3. Sorts the output (which is necessary for the next step)
4. Removes duplicate lines with `uniq`
5. Counts the remaining lines

The `sort` command is necessary because `uniq` only removes adjacent duplicate lines. By sorting first, we ensure all duplicates are adjacent.

The result is the number of unique CPU models in your system. If you see `1`, it means all your CPU cores are the same model.
