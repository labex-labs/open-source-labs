// Unit testing is an important part of writing
// principled Go programs. The `testing` package
// provides the tools we need to write unit tests
// and the `go test` command runs tests.

// For the sake of demonstration, this code is in package
// `main`, but it could be any package. Testing code
// typically lives in the same package as the code it tests.
package main

import (
	"fmt"
	"testing"
)