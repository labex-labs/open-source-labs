// Go offers built-in support for JSON encoding and
// decoding, including to and from built-in and custom
// data types.

package main

import (
	"encoding/json"
	"fmt"
	"os"
)

// We'll use these two structs to demonstrate encoding and
// decoding of custom types below.
type response1 struct {
	Page   int
	Fruits []string
}

// Only exported fields will be encoded/decoded in JSON.
// Fields must start with capital letters to be exported.
type response2 struct {
	Page   int      `json:"page"`
	Fruits []string `json:"fruits"`
}

func main() {
    // TODO
	// First we'll look at encoding basic data types to
	// JSON strings. Here are some examples for atomic
	// values.
	// And here are some for slices and maps, which encode
	// to JSON arrays and objects as you'd expect.
	// The JSON package can automatically encode your
	// custom data types. It will only include exported
	// fields in the encoded output and will by default
	// use those names as the JSON keys.
	// You can use tags on struct field declarations
	// to customize the encoded JSON key names. Check the
	// definition of `response2` above to see an example
	// of such tags.
	// Now let's look at decoding JSON data into Go
	// values. Here's an example for a generic data
	// structure.
	// We need to provide a variable where the JSON
	// package can put the decoded data. This
	// `map[string]interface{}` will hold a map of strings
	// to arbitrary data types.
	// Here's the actual decoding, and a check for
	// associated errors.
	// In order to use the values in the decoded map,
	// we'll need to convert them to their appropriate type.
	// For example here we convert the value in `num` to
	// the expected `float64` type.
	// Accessing nested data requires a series of
	// conversions.
	// We can also decode JSON into custom data types.
	// This has the advantages of adding additional
	// type-safety to our programs and eliminating the
	// need for type assertions when accessing the decoded
	// data.
	// In the examples above we always used bytes and
	// strings as intermediates between the data and
	// JSON representation on standard out. We can also
	// stream JSON encodings directly to `os.Writer`s like
	// `os.Stdout` or even HTTP response bodies.
}
