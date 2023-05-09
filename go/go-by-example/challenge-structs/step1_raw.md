# Structs

## Introduction

This challenge aims to test your knowledge of Go's structs, which are typed collections of fields. Structs are useful for grouping data together to form records.

## Problem

In this challenge, you need to complete the `newPerson` function that constructs a new person struct with the given name. The `person` struct type has `name` and `age` fields.

## Requirements

- The `person` struct type must have `name` and `age` fields.
- The `newPerson` function must construct a new person struct with the given name.
- The `newPerson` function must return a pointer to the newly created person struct.
- The `main` function must print the following:
  - A new struct with name "Bob" and age 20.
  - A new struct with name "Alice" and age 30.
  - A new struct with name "Fred" and age 0.
  - A pointer to a new struct with name "Ann" and age 40.
  - A new struct constructed using the `newPerson` function with name "Jon" and age 42.
  - The name field of a struct with name "Sean" and age 50.
  - The age field of a struct pointer to a struct with name "Sean" and age 50.
  - The age field of a struct pointer to a struct with name "Sean" and age 50 after the age field has been updated to 51.

## TODO

```go
// newPerson constructs a new person struct with the given name.
func newPerson(name string) *person {
	// TODO: Construct a new person struct with the given name.
	// Set the age field to 42.
	// Return a pointer to the newly created person struct.
}

func main() {
	// TODO: Print a new struct with name "Bob" and age 20.
	// TODO: Print a new struct with name "Alice" and age 30.
	// TODO: Print a new struct with name "Fred" and age 0.
	// TODO: Print a pointer to a new struct with name "Ann" and age 40.
	// TODO: Print a new struct constructed using the `newPerson` function with name "Jon".
	// TODO: Print the name field of a struct with name "Sean" and age 50.
	// TODO: Print the age field of a struct pointer to a struct with name "Sean" and age 50.
	// TODO: Update the age field of a struct pointer to a struct with name "Sean" and age 50 to 51.
}
```

## Example

```
{Bob 20}
{Alice 30}
{Fred 0}
&{Ann 40}
&{Jon 42}
Sean
50
51
```

## Summary

In this challenge, you learned how to use Go's structs to group data together to form records. You also learned how to create new structs, access struct fields, and update struct fields.
