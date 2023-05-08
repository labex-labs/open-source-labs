# Structs

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

## Example

```sh
$ go run structs.go
{Bob 20}
{Alice 30}
{Fred 0}
&{Ann 40}
&{Jon 42}
Sean
50
51
```
