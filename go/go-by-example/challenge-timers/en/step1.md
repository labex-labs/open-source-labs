# Timers

The challenge requires the implementation of a timer that waits for a specified duration and then fires. Additionally, the timer should be cancellable before it fires.

## Requirements

- The `time` package should be imported.
- Two timers should be created, one that waits for 2 seconds and another that waits for 1 second.
- The first timer should print "Timer 1 fired" when it fires.
- The second timer should print "Timer 2 fired" when it fires.
- The second timer should be cancelled before it fires.
- The program should wait for 2 seconds to show that the second timer did not fire.

## Example

```sh
// The first timer will fire ~2s after we start the
// program, but the second should be stopped before it has
// a chance to fire.
$ go run timers.go
Timer 1 fired
Timer 2 stopped
```
