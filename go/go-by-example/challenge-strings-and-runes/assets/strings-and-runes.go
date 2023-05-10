// A Go string is a read-only slice of bytes. The language
// and the standard library treat strings specially - as
// containers of text encoded in [UTF-8](https://en.wikipedia.org/wiki/UTF-8).
// In other languages, strings are made of "characters".
// In Go, the concept of a character is called a `rune` - it's
// an integer that represents a Unicode code point.
// [This Go blog post](https://go.dev/blog/strings) is a good
// introduction to the topic.

package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
    // TODO
	// `s` is a `string` assigned a literal value
	// representing the word "hello" in the Thai
	// language. Go string literals are UTF-8
	// encoded text.
	// Since strings are equivalent to `[]byte`, this
	// will produce the length of the raw bytes stored within.
	// Indexing into a string produces the raw byte values at
	// each index. This loop generates the hex values of all
	// the bytes that constitute the code points in `s`.
	// To count how many _runes_ are in a string, we can use
	// the `utf8` package. Note that the run-time of
	// `RuneCountInString` depends on the size of the string,
	// because it has to decode each UTF-8 rune sequentially.
	// Some Thai characters are represented by multiple UTF-8
	// code points, so the result of this count may be surprising.
	// A `range` loop handles strings specially and decodes
	// each `rune` along with its offset in the string.
	// We can achieve the same iteration by using the
	// `utf8.DecodeRuneInString` function explicitly.
	// This demonstrates passing a `rune` value to a function.
	// Values enclosed in single quotes are _rune literals_. We
	// can compare a `rune` value to a rune literal directly.
}
