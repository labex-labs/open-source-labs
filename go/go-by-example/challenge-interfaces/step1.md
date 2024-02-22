# Interfaces

The problem is to implement an interface in Go, we just need to implement all the methods in the interface. Here we implement `geometry` on `rect`s and `circle`s.

## Requirements

- Implement an interface in Go.
- Implement all the methods in the interface.
- Use a generic `measure` function to work on any `geometry`.
- Use instances of `circle` and `rect` structs as arguments to `measure`.

## Example

```sh
$ go run interfaces.go
{3 4}
12
14
{5}
78.53981633974483
31.41592653589793

# To learn more about Go's interfaces, check out this
# [great blog post](https://jordanorelli.tumblr.com/post/32665860244/how-to-use-interfaces-in-go).
```
