# Base64 Encoding

## Introduction

This challenge aims to test your knowledge of base64 encoding in Golang.

## Problem

You are required to write a Golang program that encodes and decodes a given string using both standard and URL-compatible base64 encoding.

## Requirements

- The program should import the `encoding/base64` package with the `b64` name instead of the default `base64`.
- The program should encode the given string using both standard and URL-compatible base64 encoding.
- The program should decode the encoded string using both standard and URL-compatible base64 decoding.
- The program should print the encoded and decoded strings to the console.

## TODO

```go
// TODO: Encode the given string using standard base64 encoding
sEnc := b64.StdEncoding.EncodeToString([]byte(data))

// TODO: Decode the standard encoded string
sDec, _ := b64.StdEncoding.DecodeString(sEnc)

// TODO: Encode the given string using URL-compatible base64 encoding
uEnc := b64.URLEncoding.EncodeToString([]byte(data))

// TODO: Decode the URL-compatible encoded string
uDec, _ := b64.URLEncoding.DecodeString(uEnc)
```

## Example

```
Encoded using standard base64 encoding: YWJjMTIzIT8kKiYoKSctPUB+
Decoded using standard base64 decoding: abc123!?$*&()'-=@~

Encoded using URL-compatible base64 encoding: YWJjMTIzIT8kKiYoKSctPUB-
Decoded using URL-compatible base64 decoding: abc123!?$*&()'-=@~
```

## Summary

In this challenge, you learned how to encode and decode a given string using both standard and URL-compatible base64 encoding in Golang.
