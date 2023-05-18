# Closing Channels

In Golang, closing a channel can be used to communicate completion to the channel's receivers. This challenge will demonstrate how to use a channel to communicate work to be done from the `main()` goroutine to a worker goroutine, and how to close the channel when there are no more jobs for the worker.
