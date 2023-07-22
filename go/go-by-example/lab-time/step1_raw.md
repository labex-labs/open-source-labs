# Time

## Introduction

This lab aims to test your understanding of Go's time and duration support.

The code below contains examples of how to work with time and duration in Go. However, some parts of the code are missing. Your task is to complete the code to make it work as expected.

- Basic knowledge of Go programming language.
- Familiarity with Go's time and duration support.

## TODO

```go
// We'll start by getting the current time.
now := time.Now()
fmt.Println(now)

// You can build a `time` struct by providing the
// year, month, day, etc. Times are always associated
// with a `Location`, i.e. time zone.
then := time.Date(
    2009, 11, 17, 20, 34, 58, 651387237, time.UTC)
fmt.Println(then)

// You can extract the various components of the time
// value as expected.
fmt.Println(then.Year())
fmt.Println(then.Month())
fmt.Println(then.Day())
fmt.Println(then.Hour())
fmt.Println(then.Minute())
fmt.Println(then.Second())
fmt.Println(then.Nanosecond())
fmt.Println(then.Location())

// The Monday-Sunday `Weekday` is also available.
fmt.Println(then.Weekday())

// These methods compare two times, testing if the
// first occurs before, after, or at the same time
// as the second, respectively.
fmt.Println(then.Before(now))
fmt.Println(then.After(now))
fmt.Println(then.Equal(now))

// The `Sub` methods returns a `Duration` representing
// the interval between two times.
diff := now.Sub(then)
fmt.Println(diff)

// We can compute the length of the duration in
// various units.
fmt.Println(diff.Hours())
fmt.Println(diff.Minutes())
fmt.Println(diff.Seconds())
fmt.Println(diff.Nanoseconds())

// You can use `Add` to advance a time by a given
// duration, or with a `-` to move backwards by a
// duration.
fmt.Println(then.Add(diff))
fmt.Println(then.Add(-diff))
```

```
2022-01-01 12:00:00.000000001 +0000 UTC m=+0.000000002
2009-11-17 20:34:58.651387237 +0000 UTC
2009
November
17
20
34
58
651387237
UTC
Tuesday
true
false
false
131615h25m1.348612764s
131615.41704183556
7896925.022510134
473815501.3506081
473815501350608100
2050-06-01 08:59:59.651387237 +0000 UTC
1969-05-14 12:10:57.651387237 +0000 UTC
```

## Summary

This lab tested your ability to work with Go's time and duration support. You learned how to extract various components of a time value, compare two times, compute the length of a duration, and advance a time by a given duration.
