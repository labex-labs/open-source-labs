# Structs

In this lab, you need to complete the `newPerson` function that constructs a new person struct with the given name. The `person` struct type has `name` and `age` fields.

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

There is the full code below:

```go
// Go's _structs_ are typed collections of fields.
// They're useful for grouping data together to form
// records.

package main

import "fmt"

// This `person` struct type has `name` and `age` fields.
type person struct {
	name string
	age  int
}

// `newPerson` constructs a new person struct with the given name.
func newPerson(name string) *person {
	// You can safely return a pointer to local variable
	// as a local variable will survive the scope of the function.
	p := person{name: name}
	p.age = 42
	return &p
}

func main() {

	// This syntax creates a new struct.
	fmt.Println(person{"Bob", 20})

	// You can name the fields when initializing a struct.
	fmt.Println(person{name: "Alice", age: 30})

	// Omitted fields will be zero-valued.
	fmt.Println(person{name: "Fred"})

	// An `&` prefix yields a pointer to the struct.
	fmt.Println(&person{name: "Ann", age: 40})

	// It's idiomatic to encapsulate new struct creation in constructor functions
	fmt.Println(newPerson("Jon"))

	// Access struct fields with a dot.
	s := person{name: "Sean", age: 50}
	fmt.Println(s.name)

	// You can also use dots with struct pointers - the
	// pointers are automatically dereferenced.
	sp := &s
	fmt.Println(sp.age)

	// Structs are mutable.
	sp.age = 51
	fmt.Println(sp.age)
}

```
