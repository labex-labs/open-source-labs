# Hello World

Write a program that prints the message "hello world" to the console.

- The program should use the `fmt` package to print the message.
- The program should be written in Golang.

```sh
# To run the program, put the code in `hello-world.go` and
# use `go run`.
$ go run hello-world.go
hello world

# Sometimes we'll want to build our programs into
# binaries. We can do this using `go build`.
$ go build hello-world.go
$ ls
hello-world hello-world.go

# We can then execute the built binary directly.
$ ./hello-world
hello world

# Now that we can run and build basic Go programs, let's
# learn more about the language.
```

There is the full code below:

```go
// Our first program will print the classic "hello world"
// message. Here's the full source code.
package main

import "fmt"

func main() {
	fmt.Println("hello world")
}
```
