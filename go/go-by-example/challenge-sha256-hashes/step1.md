# SHA256 Hashes

## Problem

Given a string, compute its SHA256 hash.

## Requirements

- The program should import the `crypto/sha256` and `fmt` packages.
- The program should use the `sha256.New()` function to create a new hash.
- The program should use the `Write` function to write the bytes of the string to the hash.
- The program should use the `Sum` function to get the finalized hash result as a byte slice.
- The program should print the original string and the hash result in hexadecimal format.

## Example

```sh
# Running the program computes the hash and prints it in
# a human-readable hex format.
$ go run sha256-hashes.go
sha256 this string
1af1dfa857bf1d8814fe1af8983c18080019922e557f15a8a...

# You can compute other hashes using a similar pattern to
# the one shown above. For example, to compute
# SHA512 hashes import `crypto/sha512` and use
# `sha512.New()`.

# Note that if you need cryptographically secure hashes,
# you should carefully research
# [hash strength](https://en.wikipedia.org/wiki/Cryptographic_hash_function)!
```
