
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
