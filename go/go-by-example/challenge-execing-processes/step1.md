# Execing Processes

The problem is to replace the current Go process with another process, such as a non-Go process.

## Requirements

- Go programming language
- Basic knowledge of Go's `exec` function
- Familiarity with environment variables

## Example

```sh
# When we run our program it is replaced by `ls`.
$ go run execing-processes.go
total 16
drwxr-xr-x 4 mark 136B Oct 3 16:29 .
drwxr-xr-x 91 mark 3.0K Oct 3 12:50 ..
-rw-r--r-- 1 mark 1.3K Oct 3 16:28 execing-processes.go

# Note that Go does not offer a classic Unix `fork`
# function. Usually this isn't an issue though, since
# starting goroutines, spawning processes, and exec'ing
# processes covers most use cases for `fork`.
```
