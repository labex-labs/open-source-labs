# The spawned programs return output that is the same
# as if we had run them directly from the command-line.
cd /home/labex/project
go run spawning-processes.go | grep "> date"