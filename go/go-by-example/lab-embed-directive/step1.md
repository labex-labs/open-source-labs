# Embed Directive

Your task is to modify the given code to embed files and folders into the Go binary and print their contents.

- You must use the `embed` package to embed files and folders.
- You must use the `string` and `[]byte` types to store the contents of the embedded files.
- You must use the `embed.FS` type to embed multiple files or folders with wildcards.
- You must print the contents of the embedded files.

```sh
# Use these commands to run the example.
# (Note: due to limitation on go playground,
# this example can only be run on your local machine.)
$ mkdir -p folder
$ echo "hello go" > folder/single_file.txt
$ echo "123" > folder/file1.hash
$ echo "456" > folder/file2.hash

$ go run embed-directive.go
hello go
hello go
123
456
```

There is the full code below:

```go
// `//go:embed` is a [compiler
// directive](https://pkg.go.dev/cmd/compile#hdr-Compiler_Directives) that
// allows programs to include arbitrary files and folders in the Go binary at
// build time. Read more about the embed directive
// [here](https://pkg.go.dev/embed).
package main

// Import the `embed` package; if you don't use any exported
// identifiers from this package, you can do a blank import with `_ "embed"`.
import (
	"embed"
)

// `embed` directives accept paths relative to the directory containing the
// Go source file. This directive embeds the contents of the file into the
// `string` variable immediately following it.
//
//go:embed folder/single_file.txt
var fileString string

// Or embed the contents of the file into a `[]byte`.
//
//go:embed folder/single_file.txt
var fileByte []byte

// We can also embed multiple files or even folders with wildcards. This uses
// a variable of the [embed.FS type](https://pkg.go.dev/embed#FS), which
// implements a simple virtual file system.
//
//go:embed folder/single_file.txt
//go:embed folder/*.hash
var folder embed.FS

func main() {

	// Print out the contents of `single_file.txt`.
	print(fileString)
	print(string(fileByte))

	// Retrieve some files from the embedded folder.
	content1, _ := folder.ReadFile("folder/file1.hash")
	print(string(content1))

	content2, _ := folder.ReadFile("folder/file2.hash")
	print(string(content2))
}

```
