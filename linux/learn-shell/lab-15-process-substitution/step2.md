# Input Process Substitution

Process substitution can also be used to process the input to a command from another source. This is useful when you want to store the input in a file and also display it on the console, or when you want to modify the input before passing it to a command.

For example, if you want to store logs of an application into a file and at the same time print them on the console, you can use process substitution with the `tee` command.

```shell
echo "Hello, world!" | tee >(tr '[:upper:]' '[:lower:]' > /tmp/hello.txt)
```

In this example, the output of the `echo` command is passed as input to the `tee` command. The `tee` command writes the input to both the console and a file specified by `/tmp/hello.txt`. The output of the `tee` command is processed by the `tr` command, which converts the uppercase characters to lowercase characters.
