# Time Formatting and Parsing

## Problem

The problem is to format and parse time in Golang using the provided layouts.

## Requirements

- Use the `time` package to format and parse time.
- Use the `time.RFC3339` layout to format and parse time.
- Use the `Mon Jan 2 15:04:05 MST 2006` reference time to show the pattern with which to format/parse a given time/string.
- Use the `Parse` function to parse time.
- Use the `Format` function to format time.
- Use the `fmt.Println` function to print the formatted time.
- Use the `fmt.Printf` function to print the formatted time with extracted components.

## Example

```sh
$ go run time-formatting-parsing.go
2014-04-15T18:00:15-07:00
2012-11-01 22:08:41 +0000 +0000
6:00PM
Tue Apr 15 18:00:15 2014
2014-04-15T18:00:15.161182-07:00
0000-01-01 20:41:00 +0000 UTC
2014-04-15T18:00:15-00:00
parsing time "8:41PM" as "Mon Jan _2 15:04:05 2006": ...
```
