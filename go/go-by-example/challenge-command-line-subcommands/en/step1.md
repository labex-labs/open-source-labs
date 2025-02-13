# Command Line Subcommands

You are required to create a program that supports two subcommands, `foo` and `bar`, each with its own set of flags. The `foo` subcommand should have two flags, `enable` and `name`, while the `bar` subcommand should have one flag, `level`.

## Requirements

- The program should use the `flag` package to define and parse flags.
- The `foo` subcommand should have two flags, `enable` and `name`, both of type string.
- The `bar` subcommand should have one flag, `level`, of type int.
- The program should print an error message if an invalid subcommand is provided.
- The program should print the values of the flags for the subcommand that is invoked.

## Example

```sh
$ go build command-line-subcommands.go

# First invoke the foo subcommand.
$ ./command-line-subcommands foo -enable -name=joe a1 a2
subcommand 'foo'
enable: true
name: joe
tail: [a1 a2]

# Now try bar.
$ ./command-line-subcommands bar -level 8 a1
subcommand 'bar'
level: 8
tail: [a1]

# But bar won't accept foo's flags.
$ ./command-line-subcommands bar -enable a1
flag provided but not defined: -enable
Usage of bar:
-level int
level

# Next we'll look at environment variables, another common
# way to parameterize programs.
```
