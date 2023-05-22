# Spawning Processes

## Problem

The challenge requires the implementation of a Go program that spawns external processes and collects their output.

## Requirements

- The program should be able to spawn external processes.
- The program should be able to collect the output of the external processes.
- The program should handle errors that may arise during the execution of the external processes.

## Example

```sh
# The spawned programs return output that is the same
# as if we had run them directly from the command-line.
$ go run spawning-processes.go
> date
Thu 05 May 2022 10:10:12 PM PDT

# date doesn't have a `-x` flag so it will exit with
# an error message and non-zero return code.
command exited with rc = 1
hello > grep
hello grep

-a > ls -l -h
drwxr-xr-x 4 mark 136B Oct 3 16:29 .
drwxr-xr-x 91 mark 3.0K Oct 3 12:50 ..
-rw-r--r-- 1 mark 1.3K Oct 3 16:28 spawning-processes.go
```
