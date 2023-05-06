
// Create a ticker that ticks every 500ms until we stop it.
// Use a channel to await the values as they arrive.
// Use the `select` statement to receive values from the channel.
// Stop the ticker after 1600ms.

func tickerFunc() {
    ticker := // TODO: Create a ticker that ticks every 500ms
    done := make(chan bool)

    go func() {
        for {
            select {
            case <-done:
                return
            case t := <-ticker.C:
                fmt.Println("Tick at", t)
            }
        }
    }()

    // TODO: Stop the ticker after 1600ms
    fmt.Println("Ticker stopped")
}
