// URLs provide a [uniform way to locate resources](https://adam.herokuapp.com/past/2010/3/30/urls_are_the_uniform_way_to_locate_resources/).
// Here's how to parse URLs in Go.

package main

import (
	"fmt"
	"net"
	"net/url"
)

func main() {
    // TODO
	// We'll parse this example URL, which includes a
	// scheme, authentication info, host, port, path,
	// query params, and query fragment.
	// Parse the URL and ensure there are no errors.
	// Accessing the scheme is straightforward.
	// `User` contains all authentication info; call
	// `Username` and `Password` on this for individual
	// values.
	// The `Host` contains both the hostname and the port,
	// if present. Use `SplitHostPort` to extract them.
	// Here we extract the `path` and the fragment after
	// the `#`.
	// To get query params in a string of `k=v` format,
	// use `RawQuery`. You can also parse query params
	// into a map. The parsed query param maps are from
	// strings to slices of strings, so index into `[0]`
	// if you only want the first value.
}
