# When we run the program the `"ping"` message is
# successfully passed from one goroutine to another via
# our channel.
cd /home/labex/project
go run channels.go | grep "ping"