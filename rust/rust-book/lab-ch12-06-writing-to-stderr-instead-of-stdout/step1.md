# Writing Error Messages to Standard Error Instead of Standard Output

At the moment, we’re writing all of our output to the terminal using the
`println!` macro. In most terminals, there are two kinds of output: _standard
output_ (`stdout`) for general information and _standard error_ (`stderr`) for
error messages. This distinction enables users to choose to direct the
successful output of a program to a file but still print error messages to the
screen.

The `println!` macro is only capable of printing to standard output, so we have
to use something else to print to standard error.
