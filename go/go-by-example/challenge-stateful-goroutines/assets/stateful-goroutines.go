
type readOp struct {
	key  int
	resp chan int
}
type writeOp struct {
	key  int
	val  int
	resp chan bool
}

go func() {
	var state = make(map[int]int)
	for {
		select {
		case read := <-reads:
			read.resp <- state[read.key]
		case write := <-writes:
			state[write.key] = write.val
			write.resp <- true
		}
	}
}()

for r := 0; r < 100; r++ {
	go func() {
		for {
			read := readOp{
				key:  rand.Intn(5),
				resp: make(chan int)}
			reads <- read
			<-read.resp
			atomic.AddUint64(&readOps, 1)
			time.Sleep(time.Millisecond)
		}
	}()
}

for w := 0; w < 10; w++ {
	go func() {
		for {
			write := writeOp{
				key:  rand.Intn(5),
				val:  rand.Intn(100),
				resp: make(chan bool)}
			writes <- write
			<-write.resp
			atomic.AddUint64(&writeOps, 1)
			time.Sleep(time.Millisecond)
		}
	}()
}
