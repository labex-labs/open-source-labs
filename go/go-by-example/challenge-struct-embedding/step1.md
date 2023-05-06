# Golang Challenge: Struct Embedding

## Problem

Create a struct named `container` that embeds a struct named `base`. The `base` struct should have a field named `num` of type `int` and a method named `describe()` that returns a string. The `container` struct should have a field named `str` of type `string`. The `container` struct should be able to access the `num` field and `describe()` method of the `base` struct.

## Requirements

- The `base` struct should have a field named `num` of type `int`.
- The `base` struct should have a method named `describe()` that returns a string.
- The `container` struct should have a field named `str` of type `string`.
- The `container` struct should embed the `base` struct.
- The `container` struct should be able to access the `num` field and `describe()` method of the `base` struct.

## Example

```sh
$ go run struct-embedding.go
co={num: 1, str: some name}
also num: 1
describe: base with num=1
describer: base with num=1

```