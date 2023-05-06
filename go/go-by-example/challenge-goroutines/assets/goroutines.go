
func f(from string) {
	for i := 0; i < 3; i++ {
		fmt.Println(from, ":", i)
	}
}

func main() {

	// Call f function synchronously
	f("direct")

	// Call f function asynchronously using a goroutine
	go f("goroutine")

	// Start a goroutine to execute an anonymous function
	go func(msg string) {
		fmt.Println(msg)
	}("going")

	// Wait for goroutines to finish executing
	time.Sleep(time.Second)
	fmt.Println("done")
}
