# `zeroval` doesn't change the `i` in `main`, but
# `zeroptr` does because it has a reference to
# the memory address for that variable.
cd /home/labex/project
go run pointers.go | grep "initial: 1"