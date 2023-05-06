# Golang Challenge: Struct Embedding

## Introduction
This challenge aims to test your understanding of struct embedding in Golang. You will be required to create a struct that embeds another struct and access its fields and methods.

## Problem
Create a struct named `container` that embeds a struct named `base`. The `base` struct should have a field named `num` of type `int` and a method named `describe()` that returns a string. The `container` struct should have a field named `str` of type `string`. The `container` struct should be able to access the `num` field and `describe()` method of the `base` struct.

## Requirements
- The `base` struct should have a field named `num` of type `int`.
- The `base` struct should have a method named `describe()` that returns a string.
- The `container` struct should have a field named `str` of type `string`.
- The `container` struct should embed the `base` struct.
- The `container` struct should be able to access the `num` field and `describe()` method of the `base` struct.

## TODO
Complete the `container` struct by embedding the `base` struct and adding a `str` field. Access the `num` field and `describe()` method of the `base` struct using the `container` struct.

```go
type base struct {
	num int
}

func (b base) describe() string {
	// TODO: return a string that describes the base struct
}

type container struct {
	// TODO: embed the base struct and add a str field
}

func main() {
	// TODO: create a container struct and access the num field and describe() method of the base struct
}
```

## Example
```
co={num: 1, str: some name}
also num: 1
describe: base with num=1
describer: base with num=1
```

## Summary
In this challenge, you learned how to embed a struct in another struct and access its fields and methods. You also learned how to bestow interface implementations onto other structs using struct embedding.