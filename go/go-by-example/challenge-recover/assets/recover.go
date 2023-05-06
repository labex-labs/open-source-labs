
// This function panics.
func mayPanic() {
	panic("a problem")
}

func main() {
	// `recover` must be called within a deferred function.
	// When the enclosing function panics, the defer will
	// activate and a `recover` call within it will catch
	// the panic.
	defer func() {
		// TODO: Use recover to handle the panic and print the error message.
	}()

	mayPanic()

	// This code will not run, because `mayPanic` panics.
	// The execution of `main` stops at the point of the
	// panic and resumes in the deferred closure.
	fmt.Println("After mayPanic()")
}
