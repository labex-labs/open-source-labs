# 임시 파일 및 디렉토리

이 랩에서는 Go 에서 임시 파일과 디렉토리를 생성해야 합니다.

- `os.CreateTemp`를 사용하여 임시 파일을 생성합니다.
- `os.MkdirTemp`를 사용하여 임시 디렉토리를 생성합니다.
- `os.RemoveAll`을 사용하여 임시 디렉토리를 제거합니다.
- `os.WriteFile`을 사용하여 파일에 데이터를 씁니다.

```sh
$ go run temporary-files-and-directories.go
Temp file name: /tmp/sample610887201
Temp dir name: /tmp/sampledir898854668
```

전체 코드는 다음과 같습니다.

```go
// Throughout program execution, we often want to create
// data that isn't needed after the program exits.
// *Temporary files and directories* are useful for this
// purpose since they don't pollute the file system over
// time.

package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {

	// The easiest way to create a temporary file is by
	// calling `os.CreateTemp`. It creates a file *and*
	// opens it for reading and writing. We provide `""`
	// as the first argument, so `os.CreateTemp` will
	// create the file in the default location for our OS.
	f, err := os.CreateTemp("", "sample")
	check(err)

	// Display the name of the temporary file. On
	// Unix-based OSes the directory will likely be `/tmp`.
	// The file name starts with the prefix given as the
	// second argument to `os.CreateTemp` and the rest
	// is chosen automatically to ensure that concurrent
	// calls will always create different file names.
	fmt.Println("Temp file name:", f.Name())

	// Clean up the file after we're done. The OS is
	// likely to clean up temporary files by itself after
	// some time, but it's good practice to do this
	// explicitly.
	defer os.Remove(f.Name())

	// We can write some data to the file.
	_, err = f.Write([]byte{1, 2, 3, 4})
	check(err)

	// If we intend to write many temporary files, we may
	// prefer to create a temporary *directory*.
	// `os.MkdirTemp`'s arguments are the same as
	// `CreateTemp`'s, but it returns a directory *name*
	// rather than an open file.
	dname, err := os.MkdirTemp("", "sampledir")
	check(err)
	fmt.Println("Temp dir name:", dname)

	defer os.RemoveAll(dname)

	// Now we can synthesize temporary file names by
	// prefixing them with our temporary directory.
	fname := filepath.Join(dname, "file1")
	err = os.WriteFile(fname, []byte{1, 2}, 0666)
	check(err)
}
```
