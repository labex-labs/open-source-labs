# Extracting CPU Clock Speed

Let's extract the CPU clock speeds:

```bash
cat /proc/cpuinfo | grep "cpu MHz" | cut -d ':' -f 2
```

This pipeline:

1. Reads the CPU info
2. Filters for "cpu MHz" lines
3. Uses `cut` to extract the part after the colon

The `cut` command is used to extract sections from each line of input. Here, `-d ':'` sets the delimiter to a colon, and `-f 2` selects the second field (everything after the colon).

The result is a list of CPU clock speeds in MHz. You might see different values if your CPU supports dynamic frequency scaling.
