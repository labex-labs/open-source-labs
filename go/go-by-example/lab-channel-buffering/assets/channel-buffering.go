
messages := make(chan string, 2)

// TODO: Send "buffered" and "channel" into the channel without a corresponding concurrent receive.

fmt.Println(<-messages)
fmt.Println(<-messages)
