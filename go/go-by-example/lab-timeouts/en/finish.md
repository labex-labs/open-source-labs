# Summary

In this lab, we learned how to implement timeouts in Go using channels and `select`. We used a buffered channel to prevent goroutine leaks in case the channel is never read, and `time.After` to await a value to be sent after the timeout. We also used `select` to proceed with the first receive that's ready.
