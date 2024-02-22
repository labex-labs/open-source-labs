# Base64 Encoding

You are required to write a Golang program that encodes and decodes a given string using both standard and URL-compatible base64 encoding.

## Requirements

- The program should import the `encoding/base64` package with the `b64` name instead of the default `base64`.
- The program should encode the given string using both standard and URL-compatible base64 encoding.
- The program should decode the encoded string using both standard and URL-compatible base64 decoding.
- The program should print the encoded and decoded strings to the console.

## Example

```sh
# The string encodes to slightly different values with the
# standard and URL base64 encoders (trailing `+` vs `-`)
# but they both decode to the original string as desired.
$ go run base64-encoding.go
YWJjMTIzIT8kKiYoKSctPUB+
abc123!?$*&()'-=@~

YWJjMTIzIT8kKiYoKSctPUB-
abc123!?$*&()'-=@~

```
