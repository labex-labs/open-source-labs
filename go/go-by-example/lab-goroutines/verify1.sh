# When we run this program, we see the output of the
# blocking call first, then the output of the two
# goroutines. The goroutines' output may be interleaved,
# because goroutines are being run concurrently by the
# Go runtime.
cd /home/labex/project
go run goroutines.go | grep "direct : 0"