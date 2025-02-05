# Summary

This lab demonstrated how to implement a worker pool using goroutines and channels. The worker pool receives work on the `jobs` channel and sends the corresponding results on the `results` channel. Each worker sleeps for a second per job to simulate an expensive task.
