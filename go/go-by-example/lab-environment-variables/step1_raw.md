# Environment Variables

## Introduction

This lab will cover the basics of environment variables in Unix programs. Environment variables are used to convey configuration information to programs.

In this lab, you will need to set, get, and list environment variables.

- Use `os.Setenv` to set a key/value pair.
- Use `os.Getenv` to get a value for a key.
- Use `os.Environ` to list all key/value pairs in the environment.
- Use `strings.SplitN` to split the key and value.

## TODO

Complete the following code to set, get, and list environment variables:

```
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {

	// TODO: Set the environment variable FOO to "1"

	// TODO: Print the value of FOO using os.Getenv

	// TODO: Print the value of BAR using os.Getenv. This should return an empty string.

	// TODO: Use os.Environ to list all key/value pairs in the environment. Print only the keys.
	for _, e := range os.Environ() {
		pair := strings.SplitN(e, "=", 2)
		fmt.Println(pair[0])
	}
}
```

```
FOO: 1
BAR:

PATH
PWD
...
```

## Summary

In this lab, you learned how to set, get, and list environment variables in Unix programs. This is a fundamental concept that is used in many programs to convey configuration information.
