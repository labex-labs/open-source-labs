# Time Formatting and Parsing

## Introduction
This challenge focuses on time formatting and parsing in Golang. Golang provides pattern-based layouts for time formatting and parsing.

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

## TODO
Complete the following code blocks:
```
t1, e := time.Parse(
    time.RFC3339,
    "2012-11-01T22:08:41+00:00")
p(t1)

p(t.Format("3:04PM"))
p(t.Format("Mon Jan _2 15:04:05 2006"))
p(t.Format("2006-01-02T15:04:05.999999-07:00"))
form := "3 04 PM"
t2, e := time.Parse(form, "8 41 PM")
p(t2)

fmt.Printf("%d-%02d-%02dT%02d:%02d:%02d-00:00\n",
    t.Year(), t.Month(), t.Day(),
    t.Hour(), t.Minute(), t.Second())

_, e = time.Parse(ansic, "8:41PM")
p(e)
```

## Example
```
2006-01-02T15:04:05Z
2012-11-01 22:08:41 +0000 +0000
3:52PM
Sun Mar  7 15:52:57 2021
2021-03-07T15:52:57.999999-08:00
0000-01-01 20:41:00 +0000 UTC
2021-03-07T15:52:57-00:00
parsing time "8:41PM" as "Mon Jan _2 15:04:05 2006": cannot parse "8:41PM" as "Mon"
```

## Summary
In this challenge, we learned how to format and parse time in Golang using the `time` package. We used the `time.RFC3339` layout to format and parse time and the `Mon Jan 2 15:04:05 MST 2006` reference time to show the pattern with which to format/parse a given time/string. We also used the `Parse` and `Format` functions to parse and format time, respectively.