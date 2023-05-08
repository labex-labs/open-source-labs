# We receive the values `"one"` and then `"two"` as
# expected.
cd /home/labex/project
time go run select.go | grep "received one"