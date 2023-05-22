# Summary

This challenge demonstrated how to use channels and goroutines to synchronize access to shared state. By having a single goroutine own the state and using channels to issue read and write requests, we can avoid race conditions and data corruption.
