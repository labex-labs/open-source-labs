
// TODO: Spawn an external process that takes no arguments or input and prints something to stdout.
// Use the `exec.Command` helper to create an object to represent this external process.
// Use the `Output` method to run the command, wait for it to finish, and collect its standard output.
dateCmd := exec.Command("date")
dateOut, err := dateCmd.Output()

// TODO: Spawn an external process that takes arguments and prints something to stdout.
// Use the `exec.Command` helper to create an object to represent this external process.
// Use the `Output` method to run the command, wait for it to finish, and collect its standard output.
// Handle errors that may arise during the execution of the command.
_, err = exec.Command("date", "-x").Output()

// TODO: Spawn an external process that takes input from stdin and prints something to stdout.
// Use the `exec.Command` helper to create an object to represent this external process.
// Use `StdinPipe` and `StdoutPipe` to grab input/output pipes.
// Write some input to the process, read the resulting output, and wait for the process to exit.
grepCmd := exec.Command("grep", "hello")
grepIn, _ := grepCmd.StdinPipe()
grepOut, _ := grepCmd.StdoutPipe()
grepCmd.Start()
grepIn.Write([]byte("hello grep\ngoodbye grep"))
grepIn.Close()
grepBytes, _ := io.ReadAll(grepOut)
grepCmd.Wait()

// TODO: Spawn an external process that takes a full command with a string.
// Use the `exec.Command` helper to create an object to represent this external process.
// Use the `Output` method to run the command, wait for it to finish, and collect its standard output.
// Handle errors that may arise during the execution of the command.
lsCmd := exec.Command("bash", "-c", "ls -a -l -h")
lsOut, err := lsCmd.Output()
