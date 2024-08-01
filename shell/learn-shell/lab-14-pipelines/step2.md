# Filtering CPU Information

Next, we will filter the CPU information to determine the number of processors in the system. Each processor entry in the `/proc/cpuinfo` file contains a line starting with `processor:` followed by a unique number. We can use the `grep` command to search for this pattern and retrieve the relevant lines.

```bash
cat /proc/cpuinfo | grep processor
```
