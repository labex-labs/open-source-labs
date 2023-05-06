
func main() {

	// `os.Args` provides access to raw command-line
	// arguments. Note that the first value in this slice
	// is the path to the program, and `os.Args[1:]`
	// holds the arguments to the program.
	argsWithProg := os.Args
	argsWithoutProg := os.Args[1:]

	// TODO: Print out the first argument passed to the program
	// TODO: Print out the second argument passed to the program
	// TODO: Print out the third argument passed to the program

	fmt.Println(argsWithProg)
	fmt.Println(argsWithoutProg)
}
