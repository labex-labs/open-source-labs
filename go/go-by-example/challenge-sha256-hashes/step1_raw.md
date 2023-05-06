# SHA256 Hashes

## Introduction
This challenge aims to demonstrate how to compute SHA256 hashes in Go. SHA256 hashes are commonly used to compute short identities for binary or text blobs.

## Problem
Given a string, compute its SHA256 hash.

## Requirements
- The program should import the `crypto/sha256` and `fmt` packages.
- The program should use the `sha256.New()` function to create a new hash.
- The program should use the `Write` function to write the bytes of the string to the hash.
- The program should use the `Sum` function to get the finalized hash result as a byte slice.
- The program should print the original string and the hash result in hexadecimal format.

## TODO
```go
s := "sha256 this string"
h := sha256.New()
h.Write([]byte(s))
bs := h.Sum(nil)
fmt.Println(s)
fmt.Printf("%x\n", bs) // TODO: Print the SHA256 hash of the string
```

## Example
```
sha256 this string
f9d7f926d6a8d5b7b5c5b100f7f85b2b060a290f0d42ccb960a6d6f6d3a7c9f2
```

## Summary
This challenge demonstrated how to compute SHA256 hashes in Go using the `crypto/sha256` package. By following the requirements and completing the TODO section, the program can compute the SHA256 hash of a given string.