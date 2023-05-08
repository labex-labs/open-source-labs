# Number Parsing

## Problem

Parsing numbers from strings is a common task in many programs. This challenge requires you to use the built-in `strconv` package to parse different types of numbers from strings.

## Requirements

- Use the `strconv` package to parse numbers from strings.
- Parse a float with `ParseFloat`.
- Parse an int with `ParseInt`.
- Parse a hex-formatted number with `ParseInt`.
- Parse an unsigned int with `ParseUint`.
- Parse a base-10 int with `Atoi`.
- Handle errors returned by the parse functions.

## Example

```sh
$ go run number-parsing.go
1.234
123
456
789
135
strconv.ParseInt: parsing "wat": invalid syntax

# Next we'll look at another common parsing task: URLs.
```
