# Random Numbers

You are required to write a program that generates random integers and floats within a specified range. The program should also be able to produce varying sequences of numbers by changing the seed.

## Requirements

- The program should use the `math/rand` package to generate random numbers.
- The program should generate random integers within a specified range.
- The program should generate random floats within a specified range.
- The program should be able to produce varying sequences of numbers by changing the seed.

## Example

```sh
# Depending on where you run this sample, some of the
# generated numbers may be different. Note that on
# the Go playground seeding with `time.Now()` still
# produces deterministic results due to the way the
# playground is implemented.
$ go run random-numbers.go
81,87
0.6645600532184904
7.123187485356329,8.434115364335547
0,28
5,87
5,87

# See the [`math/rand`](https://pkg.go.dev/math/rand)
# package docs for references on other random quantities
# that Go can provide.
```
