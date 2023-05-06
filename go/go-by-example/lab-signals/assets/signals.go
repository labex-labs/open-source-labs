
// TODO: Create a buffered channel to receive `os.Signal` notifications.
sigs := make(chan os.Signal, 1)

// TODO: Register the channel to receive notifications of specified signals using `signal.Notify`.
signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)

// TODO: Create a goroutine to execute a blocking receive for signals.
go func() {
    // TODO: When it gets one, print it out and then notify the program that it can finish.
    sig := <-sigs
    fmt.Println()
    fmt.Println(sig)
    done <- true
}()

// TODO: Wait for the expected signal and then exit.
<-done
