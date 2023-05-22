# Golang JSON Challenge

## Introduction

This challenge aims to test your knowledge of encoding and decoding JSON data in Golang.

## Problem

You are required to complete the code provided to encode and decode JSON data in Golang. The code contains examples of encoding and decoding basic data types, as well as custom data types.

## Requirements

- Basic knowledge of Golang programming language.
- Familiarity with encoding and decoding JSON data in Golang.
- Ability to read and understand existing Golang code.

## TODO

Complete the following code blocks marked with `TODO`:

```go
// TODO: Complete the code to encode the given data to JSON format.
res1B, _ := json.Marshal(res1D)

// TODO: Complete the code to decode the given JSON data to the given struct.
json.Unmarshal([]byte(str), &res)
```

## Example

The expected output of the completed code should be:

```
true
1
2.34
"gopher"
["apple","peach","pear"]
{"apple":5,"lettuce":7}
{"Page":1,"Fruits":["apple","peach","pear"]}
{"page":1,"fruits":["apple","peach","pear"]}
map[num:6.13 strs:[a b]]
6.13
a
{1 [apple peach]}
apple
{"apple":5,"lettuce":7}
```

## Summary

This challenge tests your ability to encode and decode JSON data in Golang. By completing this challenge, you should have a better understanding of how to work with JSON data in Golang.
