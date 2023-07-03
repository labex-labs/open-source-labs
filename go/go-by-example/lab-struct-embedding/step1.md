# Struct Embedding

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

## Solution

```go
// Go supports _embedding_ of structs and interfaces
// to express a more seamless _composition_ of types.
// This is not to be confused with [`//go:embed`](embed-directive) which is
// a go directive introduced in Go version 1.16+ to embed
// files and folders into the application binary.

package main

import "fmt"

type base struct {
	num int
}

func (b base) describe() string {
	return fmt.Sprintf("base with num=%v", b.num)
}

// A `container` _embeds_ a `base`. An embedding looks
// like a field without a name.
type container struct {
	base
	str string
}

func main() {

	// When creating structs with literals, we have to
	// initialize the embedding explicitly; here the
	// embedded type serves as the field name.
	co := container{
		base: base{
			num: 1,
		},
		str: "some name",
	}

	// We can access the base's fields directly on `co`,
	// e.g. `co.num`.
	fmt.Printf("co={num: %v, str: %v}\n", co.num, co.str)

	// Alternatively, we can spell out the full path using
	// the embedded type name.
	fmt.Println("also num:", co.base.num)

	// Since `container` embeds `base`, the methods of
	// `base` also become methods of a `container`. Here
	// we invoke a method that was embedded from `base`
	// directly on `co`.
	fmt.Println("describe:", co.describe())

	type describer interface {
		describe() string
	}

	// Embedding structs with methods may be used to bestow
	// interface implementations onto other structs. Here
	// we see that a `container` now implements the
	// `describer` interface because it embeds `base`.
	var d describer = co
	fmt.Println("describer:", d.describe())
}

```
