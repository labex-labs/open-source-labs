# Line Filters

## Problem

The problem to be solved in this challenge is to write a Go program that reads input text from stdin, capitalizes all the letters in the text, and then prints the modified text to stdout.

## Requirements

- The program must read input text from stdin.
- The program must capitalize all the letters in the input text.
- The program must print the modified text to stdout.

## Example

```sh
# To try out our line filter, first make a file with a few
# lowercase lines.
$ echo 'hello'   > /tmp/lines
$ echo 'filter' >> /tmp/lines

# Then use the line filter to get uppercase lines.
$ cat /tmp/lines | go run line-filters.go
HELLO
FILTER

```