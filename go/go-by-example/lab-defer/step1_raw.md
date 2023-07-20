# Defer

## Introduction

The `defer` statement is used to delay the execution of a function until the surrounding function returns. It is often used to ensure that some cleanup is performed after a function completes, regardless of the path taken to get there.

In this lab, you need to use `defer` to create a file, write to it, and then close it when you're done.

- The `createFile` function should create a file with the given path and return a pointer to the file.
- The `writeFile` function should write the string "data" to the file.
- The `closeFile` function should close the file and check for errors.

## TODO

```go
func main() {
	f := createFile("/tmp/defer.txt")
	defer closeFile(f)
	writeFile(f)
}

func createFile(p string) *os.File {
	fmt.Println("creating")
	f, err := os.Create(p)
	if err != nil {
		panic(err)
	}
	return f
}

func writeFile(f *os.File) {
	fmt.Println("writing")
	fmt.Fprintln(f, "data")
}

func closeFile(f *os.File) {
	fmt.Println("closing")
	err := f.Close()
	if err != nil {
		fmt.Fprintf(os.Stderr, "error: %v\n", err)
		os.Exit(1)
	}
}
```

```
creating
writing
closing
```

## Summary

In this lab, you learned how to use `defer` to ensure that a function call is performed later in a program's execution, usually for purposes of cleanup. You also learned how to create a file, write to it, and then close it using `defer`.
