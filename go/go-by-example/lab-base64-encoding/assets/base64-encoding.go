// Go provides built-in support for [base64
// encoding/decoding](https://en.wikipedia.org/wiki/Base64).

package main

// This syntax imports the `encoding/base64` package with
// the `b64` name instead of the default `base64`. It'll
// save us some space below.
import (
	b64 "encoding/base64"
	"fmt"
)

func main() {
    // TODO
	// Here's the `string` we'll encode/decode.
	// Go supports both standard and URL-compatible
	// base64. Here's how to encode using the standard
	// encoder. The encoder requires a `[]byte` so we
	// convert our `string` to that type.
	// Decoding may return an error, which you can check
	// if you don't already know the input to be
	// well-formed.
	// This encodes/decodes using a URL-compatible base64
	// format.
}
