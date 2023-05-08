# Strings and Runes

## Problem

The problem to be solved in this challenge is to understand how to work with strings and runes in Go. Specifically, the challenge will cover how to get the length of a string, how to index into a string, how to count the number of runes in a string, and how to iterate over the runes in a string.

## Requirements

To complete this challenge, you will need:
- A basic understanding of Go syntax
- Knowledge of Go strings and runes
- The Go standard library

## Example

```sh
$ go run strings-and-runes.go
Len: 18
e0 b8 aa e0 b8 a7 e0 b8 b1 e0 b8 aa e0 b8 94 e0 b8 b5 
Rune count: 6
U+0E2A 'ส' starts at 0
U+0E27 'ว' starts at 3
U+0E31 'ั' starts at 6
U+0E2A 'ส' starts at 9
U+0E14 'ด' starts at 12
U+0E35 'ี' starts at 15

Using DecodeRuneInString
U+0E2A 'ส' starts at 0
found so sua
U+0E27 'ว' starts at 3
U+0E31 'ั' starts at 6
U+0E2A 'ส' starts at 9
found so sua
U+0E14 'ด' starts at 12
U+0E35 'ี' starts at 15

```