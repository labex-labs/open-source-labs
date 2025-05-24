# 파일 쓰기

문자열과 바이트를 파일에 쓰고 버퍼된 라이터 (buffered writers) 를 사용하는 Go 프로그램을 작성해야 합니다.

- 프로그램은 문자열과 바이트를 파일에 써야 합니다.
- 프로그램은 버퍼된 라이터 (buffered writers) 를 사용해야 합니다.

```sh
# 파일 쓰기 코드를 실행해 보세요.
$ go run writing-files.go
wrote 5 bytes
wrote 7 bytes
wrote 9 bytes

# 그런 다음 작성된 파일의 내용을 확인합니다.
$ cat /tmp/dat1
hello
go
$ cat /tmp/dat2
some
writes
buffered

# 다음으로 방금 본 파일 I/O 아이디어 중 일부를
# `stdin` 및 `stdout` 스트림에 적용하는 방법을 살펴보겠습니다.
```

전체 코드는 다음과 같습니다.

```go
// Go 에서 파일 쓰기는 앞서 읽기에서 보았던 패턴과 유사합니다.

package main

import (
	"bufio"
	"fmt"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {

	// 먼저, 문자열 (또는 바이트) 을 파일에 덤프하는 방법입니다.
	d1 := []byte("hello\ngo\n")
	err := os.WriteFile("/tmp/dat1", d1, 0644)
	check(err)

	// 더 세분화된 쓰기를 위해 파일을 쓰기 모드로 엽니다.
	f, err := os.Create("/tmp/dat2")
	check(err)

	// 파일을 연 직후 `Close` 를 defer 하는 것이 관용적입니다.
	defer f.Close()

	// 예상대로 바이트 슬라이스를 `Write` 할 수 있습니다.
	d2 := []byte{115, 111, 109, 101, 10}
	n2, err := f.Write(d2)
	check(err)
	fmt.Printf("wrote %d bytes\n", n2)

	// `WriteString` 도 사용할 수 있습니다.
	n3, err := f.WriteString("writes\n")
	check(err)
	fmt.Printf("wrote %d bytes\n", n3)

	// 안정적인 저장소에 쓰기를 플러시하려면 `Sync` 를 실행합니다.
	f.Sync()

	// `bufio` 는 앞서 보았던 버퍼된 리더 (buffered readers) 외에도
	// 버퍼된 라이터 (buffered writers) 를 제공합니다.
	w := bufio.NewWriter(f)
	n4, err := w.WriteString("buffered\n")
	check(err)
	fmt.Printf("wrote %d bytes\n", n4)

	// 모든 버퍼된 작업이 기본 라이터 (underlying writer) 에 적용되었는지 확인하려면 `Flush` 를 사용합니다.
	w.Flush()

}
```
