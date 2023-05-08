# Golang Challenge: Select

## Problem

In this challenge, you are given two channels, `c1` and `c2`, which will receive a value after some amount of time. Your task is to use `select` to await both of these values simultaneously, printing each one as it arrives.

## Requirements

- You should use the `select` statement to wait on both channels.
- You should print the value received from each channel as it arrives.

## Example

```sh
# We receive the values `"one"` and then `"two"` as
# expected.
$ time go run select.go 
received one
received two

# Note that the total execution time is only ~2 seconds
# since both the 1 and 2 second `Sleeps` execute
# concurrently.
real	0m2.245s

```