
messages := make(chan string)
signals := make(chan bool)

// TODO: Implement a non-blocking receive on the messages channel.
// If a value is available on messages, print "received message <message>".
// If not, print "no message received".

// TODO: Implement a non-blocking send on the messages channel.
// Send the message "hi" to the messages channel.
// If the channel has no buffer and there is no receiver, print "no message sent".

// TODO: Implement a multi-way non-blocking select.
// If a value is available on messages, print "received message <message>".
// If a value is available on signals, print "received signal <signal>".
// If no value is available on either channel, print "no activity".
