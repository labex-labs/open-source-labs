# Maps

## Introduction
In Go, maps are built-in associative data types that allow you to store key/value pairs. This challenge will test your ability to create, manipulate, and delete key/value pairs in a map.

## Problem
In this challenge, you will need to create a map that stores the number of times each word appears in a given string. You will need to split the string into words, and then iterate over each word, adding it to the map if it doesn't already exist, or incrementing its count if it does.

## Requirements
- You must use a map to store the word counts.
- You must split the input string into words.
- You must iterate over each word in the input string.
- You must add each word to the map if it doesn't already exist, or increment its count if it does.

## TODO
```go
func wordCount(s string) map[string]int {
    // TODO: Split the input string into words.
    // TODO: Create a map to store the word counts.
    // TODO: Iterate over each word in the input string.
    // TODO: Add each word to the map if it doesn't already exist, or increment its count if it does.
    // TODO: Return the map.
}
```

## Example
```go
fmt.Println(wordCount("hello world hello")) // Output: map[hello:2 world:1]
fmt.Println(wordCount("the quick brown fox jumps over the lazy dog")) // Output: map[the:2 quick:1 brown:1 fox:1 jumps:1 over:1 lazy:1 dog:1]
```

## Summary
In this challenge, you learned how to use maps in Go to store key/value pairs. You also learned how to split a string into words, iterate over each word, and add it to a map. By completing this challenge, you should have a better understanding of how to use maps in your Go programs.