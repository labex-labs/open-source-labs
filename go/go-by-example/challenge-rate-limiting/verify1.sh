# Running our program we see the first batch of requests
# handled once every ~200 milliseconds as desired.
cd /home/labex/project
go run rate-limiting.go | grep "request 1 2012-10-19 00:38:18.687438 +0000 UTC"