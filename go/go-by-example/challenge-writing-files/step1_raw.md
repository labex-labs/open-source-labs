# Writing Files

## Introduction

This challenge aims to test your ability to write files in Go. You will learn how to write a string or bytes into a file and how to use buffered writers.

## Problem

You need to write a Go program that writes a string and bytes into a file and uses buffered writers.

## Requirements

- The program should write a string and bytes into a file.
- The program should use buffered writers.

## TODO

Complete the following code to meet the requirements of the challenge. Use the TODO keyword to mark the code that needs to be completed.

```
package main

import (
	"bufio"
	"fmt"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {

	// To start, here's how to dump a string (or just
	// bytes) into a file.
	d1 := []byte("hello\ngo\n")
	err := os.WriteFile("/tmp/dat1", d1, 0644)
	check(err)

	// For more granular writes, open a file for writing.
	f, err := os.Create("/tmp/dat2")
	check(err)

	// It's idiomatic to defer a `Close` immediately
	// after opening a file.
	defer f.Close()

	// You can `Write` byte slices as you'd expect.
	d2 := []byte{115, 111, 109, 101, 10}
	n2, err := f.Write(d2)
	check(err)
	fmt.Printf("wrote %d bytes\n", n2)

	// A `WriteString` is also available.
	n3, err := f.WriteString("writes\n")
	check(err)
	fmt.Printf("wrote %d bytes\n", n3)

	// Issue a `Sync` to flush writes to stable storage.
	f.Sync()

	// `bufio` provides buffered writers in addition
	// to the buffered readers we saw earlier.
	w := bufio.NewWriter(f)
	n4, err := w.WriteString("buffered\n")
	check(err)
	fmt.Printf("wrote %d bytes\n", n4)

	// Use `Flush` to ensure all buffered operations have
	// been applied to the underlying writer.
	w.Flush()

	// TODO: Write a string "Hello World" to the file using the buffered writer.
	// TODO: Write a byte slice {72, 101, 108, 108, 111} to the file using the buffered writer.

}
```

## Example

The output of the program should be:

```
wrote 5 bytes
wrote 7 bytes
wrote 9 bytes
```

The content of the file should be:

```
some
writes
buffered
Hello World
Hello
```

## Summary

In this challenge, you learned how to write a string or bytes into a file and how to use buffered writers in Go.
