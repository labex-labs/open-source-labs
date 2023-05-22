// Some command-line tools, like the `go` tool or `git`
// have many *subcommands*, each with its own set of
// flags. For example, `go build` and `go get` are two
// different subcommands of the `go` tool.
// The `flag` package lets us easily define simple
// subcommands that have their own flags.

package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {
    // TODO
	// We declare a subcommand using the `NewFlagSet`
	// function, and proceed to define new flags specific
	// for this subcommand.
	// For a different subcommand we can define different
	// supported flags.
	// The subcommand is expected as the first argument
	// to the program.
	// Check which subcommand is invoked.
	// For every subcommand, we parse its own flags and
	// have access to trailing positional arguments.
}
