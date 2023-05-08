// Go offers extensive support for times and durations;
// here are some examples.

package main

import (
	"fmt"
	"time"
)

func main() {
    // TODO
	// We'll start by getting the current time.
	// You can build a `time` struct by providing the
	// year, month, day, etc. Times are always associated
	// with a `Location`, i.e. time zone.
	// You can extract the various components of the time
	// value as expected.
	// The Monday-Sunday `Weekday` is also available.
	// These methods compare two times, testing if the
	// first occurs before, after, or at the same time
	// as the second, respectively.
	// The `Sub` methods returns a `Duration` representing
	// the interval between two times.
	// We can compute the length of the duration in
	// various units.
	// You can use `Add` to advance a time by a given
	// duration, or with a `-` to move backwards by a
	// duration.
}
