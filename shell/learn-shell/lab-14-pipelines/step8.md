# Calculating Total RAM in Gigabytes

Finally, let's calculate the total RAM in gigabytes:

```bash
cat /proc/meminfo | grep "MemTotal" | awk '{print $2/1024/1024 " GB"}'
```

This pipeline:

1. Reads memory info
2. Filters for the "MemTotal" line
3. Uses `awk` to convert kilobytes to gigabytes

`awk` is a powerful text-processing tool. Here, it's doing a calculation: it takes the second field (`$2`, which is the memory in kilobytes), divides it by 1024 twice (to convert KB to MB to GB), and adds "GB" at the end.

The result is your total RAM in gigabytes. For example, if you see `7.79025 GB`, that means your system has approximately 8 GB of RAM.
