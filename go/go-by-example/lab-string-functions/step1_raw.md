# String Functions

## Introduction

The `strings` package in Golang provides many useful string-related functions. This challenge aims to test your understanding of some of these functions.

## Problem

Complete the code below to print the output of various string functions provided by the `strings` package.

## Requirements

- Use the `strings` package to complete the challenge.
- Use the `fmt.Println` function to print the output.
- Do not modify the function name or parameters.

## TODO

```go
package main

import (
	"fmt"
	s "strings"
)

var p = fmt.Println

func main() {

	p("Contains:  ", s.Contains("test", "es"))
	p("Count:     ", s.Count("test", "t"))
	p("HasPrefix: ", s.HasPrefix("test", "te"))
	p("HasSuffix: ", s.HasSuffix("test", "st"))
	p("Index:     ", s.Index("test", "e"))
	p("Join:      ", s.Join([]string{"a", "b"}, "-"))
	p("Repeat:    ", s.Repeat("a", 5))
	p("Replace:   ", s.Replace("foo", "o", "0", -1))
	p("Replace:   ", s.Replace("foo", "o", "0", 1))
	p("Split:     ", s.Split("a-b-c-d-e", "-"))
	p("ToLower:   ", s.ToLower("TEST"))
	p("ToUpper:   ", s.ToUpper("test"))
}
```

## Example

```
Contains:   true
Count:      2
HasPrefix:  true
HasSuffix:  true
Index:      1
Join:       a-b
Repeat:     aaaaa
Replace:    f00
Replace:    f0o
Split:      [a b c d e]
ToLower:    test
ToUpper:    TEST
```

## Summary

This challenge tests your understanding of the `strings` package in Golang. You should be able to use the various functions provided by the package to manipulate strings.
