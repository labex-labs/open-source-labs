
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
