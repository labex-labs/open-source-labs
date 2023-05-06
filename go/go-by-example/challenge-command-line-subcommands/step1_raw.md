# Golang Challenge: Command Line Subcommands

## Introduction
This challenge aims to test your ability to define and use subcommands with their own set of flags in Golang.

## Problem
You are required to create a program that supports two subcommands, `foo` and `bar`, each with its own set of flags. The `foo` subcommand should have two flags, `enable` and `name`, while the `bar` subcommand should have one flag, `level`.

## Requirements
- The program should use the `flag` package to define and parse flags.
- The `foo` subcommand should have two flags, `enable` and `name`, both of type string.
- The `bar` subcommand should have one flag, `level`, of type int.
- The program should print an error message if an invalid subcommand is provided.
- The program should print the values of the flags for the subcommand that is invoked.

## TODO
```go
// We declare a subcommand using the `NewFlagSet`
// function, and proceed to define new flags specific
// for this subcommand.
fooCmd := flag.NewFlagSet("foo", flag.ExitOnError)
fooEnable := fooCmd.Bool("enable", false, "enable")
fooName := fooCmd.String("name", "", "name")

// For a different subcommand we can define different
// supported flags.
barCmd := flag.NewFlagSet("bar", flag.ExitOnError)
barLevel := barCmd.Int("level", 0, "level")

// The subcommand is expected as the first argument
// to the program.
if len(os.Args) < 2 {
    fmt.Println("expected 'foo' or 'bar' subcommands")
    os.Exit(1)
}

// Check which subcommand is invoked.
switch os.Args[1] {

// For every subcommand, we parse its own flags and
// have access to trailing positional arguments.
case "foo":
    fooCmd.Parse(os.Args[2:])
    fmt.Println("subcommand 'foo'")
    fmt.Println("  enable:", *fooEnable)
    fmt.Println("  name:", *fooName)
    fmt.Println("  tail:", fooCmd.Args())
case "bar":
    barCmd.Parse(os.Args[2:])
    fmt.Println("subcommand 'bar'")
    fmt.Println("  level:", *barLevel)
    fmt.Println("  tail:", barCmd.Args())
default:
    fmt.Println("expected 'foo' or 'bar' subcommands")
    os.Exit(1)
}
```

## Example
```
$ go run main.go foo -enable -name John Doe
subcommand 'foo'
  enable: true
  name: John Doe
  tail: []

$ go run main.go bar -level 5 arg1 arg2
subcommand 'bar'
  level: 5
  tail: [arg1 arg2]

$ go run main.go baz
expected 'foo' or 'bar' subcommands
```

## Summary
In this challenge, you learned how to define and use subcommands with their own set of flags in Golang using the `flag` package. You also learned how to parse the flags for each subcommand and access the trailing positional arguments.