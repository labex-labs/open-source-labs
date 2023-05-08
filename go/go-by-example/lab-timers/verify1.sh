#!/bin/zsh
// The first timer will fire ~2s after we start the
// program, but the second should be stopped before it has
// a chance to fire.
cd /home/labex/project
/usr/local/go/bin/go run timers.go | grep "Timer 1 fired"