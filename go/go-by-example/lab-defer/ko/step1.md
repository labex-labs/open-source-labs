# Defer (지연)

이 랩에서는 `defer`를 사용하여 파일을 생성하고, 파일에 쓰고, 완료되면 파일을 닫아야 합니다.

- `createFile` 함수는 주어진 경로로 파일을 생성하고 파일에 대한 포인터를 반환해야 합니다.
- `writeFile` 함수는 문자열 "data"를 파일에 써야 합니다.
- `closeFile` 함수는 파일을 닫고 오류를 확인해야 합니다.

```sh
# 프로그램을 실행하면 파일이 쓰여진 후 닫히는 것을 확인할 수 있습니다.
$ go run defer.go
creating
writing
closing
```

전체 코드는 다음과 같습니다.

```go
// _Defer_는 일반적으로 정리 (cleanup) 목적으로, 프로그램 실행의 나중에 함수 호출이
// 수행되도록 보장하는 데 사용됩니다. `defer` 는 예를 들어
// 다른 언어에서 `ensure` 및 `finally` 가 사용되는 곳에서 자주 사용됩니다.

package main

import (
	"fmt"
	"os"
)

// 파일을 생성하고, 파일에 쓰고, 완료되면 닫고 싶다고 가정해 봅시다.
// `defer` 를 사용하여 이를 수행하는 방법은 다음과 같습니다.
func main() {

	// `createFile` 로 파일 객체를 얻은 직후,
	// `closeFile` 로 해당 파일의 닫기를 지연시킵니다. 이것은
	// `writeFile` 이 완료된 후,
	// 둘러싸는 함수 (`main`) 의 끝에서 실행됩니다.
	f := createFile("/tmp/defer.txt")
	defer closeFile(f)
	writeFile(f)
}

func createFile(p string) *os.File {
	fmt.Println("creating")
	f, err := os.Create(p)
	if err != nil {
		panic(err)
	}
	return f
}

func writeFile(f *os.File) {
	fmt.Println("writing")
	fmt.Fprintln(f, "data")

}

func closeFile(f *os.File) {
	fmt.Println("closing")
	err := f.Close()
	// 지연된 함수에서도 파일을 닫을 때 오류를 확인하는 것이 중요합니다.
	if err != nil {
		fmt.Fprintf(os.Stderr, "error: %v\n", err)
		os.Exit(1)
	}
}
```
