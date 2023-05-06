
// TODO: Use a mutex to synchronize access to the counters map.
type Container struct {
	counters map[string]int
}

// TODO: Implement the inc method to increment the named counter.
func (c *Container) inc(name string) {
	c.counters[name]++
}

func main() {
	c := Container{
		counters: map[string]int{"a": 0, "b": 0},
	}

	var wg sync.WaitGroup

	doIncrement := func(name string, n int) {
		for i := 0; i < n; i++ {
			// TODO: Call the inc method to increment the named counter.
		}
		wg.Done()
	}

	wg.Add(3)
	go doIncrement("a", 10000)
	go doIncrement("a", 10000)
	go doIncrement("b", 10000)

	wg.Wait()
	// TODO: Use fmt.Println to print the counters map.
}
