# Maps

## Problem

In this challenge, you will need to create a map that stores the number of times each word appears in a given string. You will need to split the string into words, and then iterate over each word, adding it to the map if it doesn't already exist, or incrementing its count if it does.

## Requirements

- You must use a map to store the word counts.
- You must split the input string into words.
- You must iterate over each word in the input string.
- You must add each word to the map if it doesn't already exist, or increment its count if it does.

## Example

```sh
# Note that maps appear in the form `map[k:v k:v]` when
# printed with `fmt.Println`.
$ go run maps.go
map: map[k1:7 k2:13]
v1: 7
v3: 0
len: 2
map: map[k1:7]
prs: false
map: map[bar:2 foo:1]
```
