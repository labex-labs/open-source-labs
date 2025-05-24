# 디렉토리

현재 작업 디렉토리에서 새로운 하위 디렉토리를 생성하고, 부모 디렉토리를 포함한 디렉토리 계층을 생성하며, 디렉토리 내용을 나열하고, 현재 작업 디렉토리를 변경하고, 디렉토리를 재귀적으로 방문하는 Go 프로그램을 만듭니다.

- 현재 작업 디렉토리에 새로운 하위 디렉토리를 생성합니다.
- 임시 디렉토리를 생성할 때는 삭제를 `defer`하는 것이 좋습니다. `os.RemoveAll`은 전체 디렉토리 트리 ( `rm -rf`와 유사) 를 삭제합니다.
- `MkdirAll`을 사용하여 부모 디렉토리를 포함한 디렉토리 계층을 생성합니다. 이는 명령줄의 `mkdir -p`와 유사합니다.
- `ReadDir`은 디렉토리 내용을 나열하고 `os.DirEntry` 객체의 슬라이스를 반환합니다.
- `Chdir`을 사용하면 `cd`와 유사하게 현재 작업 디렉토리를 변경할 수 있습니다.
- 모든 하위 디렉토리를 포함하여 디렉토리를 재귀적으로 방문합니다. `Walk`는 방문한 모든 파일 또는 디렉토리를 처리하기 위해 콜백 함수를 허용합니다.

```sh
$ go run directories.go
Listing subdir/parent
child true
file2 false
file3 false
Listing subdir/parent/child
file4 false
Visiting subdir
subdir true
subdir/file1 false
subdir/parent true
subdir/parent/child true
subdir/parent/child/file4 false
subdir/parent/file2 false
subdir/parent/file3 false
```

전체 코드는 다음과 같습니다.

```go
// Go 는 파일 시스템에서 *디렉토리*를 다루기 위한 몇 가지 유용한 함수를 가지고 있습니다.

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

	// 현재 작업 디렉토리에 새로운 하위 디렉토리를 생성합니다.
	err := os.Mkdir("subdir", 0755)
	check(err)

	// 임시 디렉토리를 생성할 때는 삭제를 `defer` 하는 것이 좋습니다. `os.RemoveAll`
	// 은 전체 디렉토리 트리 ( `rm -rf`와 유사) 를 삭제합니다.
	defer os.RemoveAll("subdir")

	// 새로운 빈 파일을 생성하는 도우미 함수입니다.
	createEmptyFile := func(name string) {
		d := []byte("")
		check(os.WriteFile(name, d, 0644))
	}

	createEmptyFile("subdir/file1")

	// `MkdirAll` 을 사용하여 부모 디렉토리를 포함한 디렉토리 계층을 생성할 수 있습니다.
	// 이는 명령줄의 `mkdir -p`와 유사합니다.
	err = os.MkdirAll("subdir/parent/child", 0755)
	check(err)

	createEmptyFile("subdir/parent/file2")
	createEmptyFile("subdir/parent/file3")
	createEmptyFile("subdir/parent/child/file4")

	// `ReadDir` 은 디렉토리 내용을 나열하고 `os.DirEntry` 객체의 슬라이스를 반환합니다.
	c, err := os.ReadDir("subdir/parent")
	check(err)

	fmt.Println("Listing subdir/parent")
	for _, entry := range c {
		fmt.Println(" ", entry.Name(), entry.IsDir())
	}

	// `Chdir` 을 사용하면 `cd` 와 유사하게 현재 작업 디렉토리를 변경할 수 있습니다.
	err = os.Chdir("subdir/parent/child")
	check(err)

	// 이제 *현재* 디렉토리를 나열할 때 `subdir/parent/child` 의 내용을 볼 수 있습니다.
	c, err = os.ReadDir(".")
	check(err)

	fmt.Println("Listing subdir/parent/child")
	for _, entry := range c {
		fmt.Println(" ", entry.Name(), entry.IsDir())
	}

	// 시작했던 곳으로 다시 `cd` 합니다.
	err = os.Chdir("../../..")
	check(err)

	// 또한 모든 하위 디렉토리를 포함하여 디렉토리를 *재귀적으로* 방문할 수 있습니다. `Walk` 는
	// 방문한 모든 파일 또는 디렉토리를 처리하기 위해 콜백 함수를 허용합니다.
	fmt.Println("Visiting subdir")
	err = filepath.Walk("subdir", visit)
}

// `visit` 은 `filepath.Walk` 에 의해 재귀적으로 발견된 모든 파일 또는 디렉토리에 대해 호출됩니다.
func visit(p string, info os.FileInfo, err error) error {
	if err != nil {
		return err
	}
	fmt.Println(" ", p, info.IsDir())
	return nil
}
```
