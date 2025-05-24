# 프로세스 생성 (Spawning Processes)

이 랩은 외부 프로세스를 생성하고 출력을 수집하는 Go 프로그램의 구현을 요구합니다.

- 프로그램은 외부 프로세스를 생성할 수 있어야 합니다.
- 프로그램은 외부 프로세스의 출력을 수집할 수 있어야 합니다.
- 프로그램은 외부 프로세스 실행 중에 발생할 수 있는 오류를 처리해야 합니다.

```sh
# 생성된 프로그램은 명령줄에서 직접 실행한 것과
# 동일한 출력을 반환합니다.
$ go run spawning-processes.go
> date
Thu 05 May 2022 10:10:12 PM PDT

# date 는 `-x` 플래그가 없으므로
# 오류 메시지와 0 이 아닌 반환 코드로 종료됩니다.
command exited with rc = 1
hello > grep
hello grep

-a > ls -l -h
drwxr-xr-x 4 mark 136B Oct 3 16:29 .
drwxr-xr-x 91 mark 3.0K Oct 3 12:50 ..
-rw-r--r-- 1 mark 1.3K Oct 3 16:28 spawning-processes.go
```

전체 코드는 다음과 같습니다.

```go
// 때때로 Go 프로그램은 다른, Go 가 아닌
// 프로세스를 생성해야 합니다.

package main

import (
	"fmt"
	"io"
	"os/exec"
)

func main() {

	// 먼저 인수가 없거나 입력이 없고
	// stdout 에 무언가를 출력하는 간단한 명령으로 시작합니다. `exec.Command` 헬퍼는 이 외부 프로세스를 나타내는
	// 객체를 생성합니다.
	dateCmd := exec.Command("date")

	// `Output` 메서드는 명령을 실행하고,
	// 완료될 때까지 기다린 다음 표준 출력을 수집합니다.
	// 오류가 없으면 `dateOut` 은 날짜 정보가 있는 바이트를
	// 저장합니다.
	dateOut, err := dateCmd.Output()
	if err != nil {
		panic(err)
	}
	fmt.Println("> date")
	fmt.Println(string(dateOut))

	// `Output` 및 `Command` 의 다른 메서드는
	// 명령을 실행하는 데 문제가 있는 경우 (예: 잘못된 경로)
	// `*exec.Error` 를 반환하고, 명령이 실행되었지만 0 이 아닌 반환
	// 코드로 종료된 경우 `*exec.ExitError` 를 반환합니다.
	_, err = exec.Command("date", "-x").Output()
	if err != nil {
		switch e := err.(type) {
		case *exec.Error:
			fmt.Println("failed executing:", err)
		case *exec.ExitError:
			fmt.Println("command exit rc =", e.ExitCode())
		default:
			panic(err)
		}
	}

	// 다음으로, `stdin` 에서 외부 프로세스로 데이터를 파이프하고
	// `stdout` 에서 결과를 수집하는 약간 더 복잡한 경우를 살펴보겠습니다.
	grepCmd := exec.Command("grep", "hello")

	// 여기서는 명시적으로 입력/출력 파이프를 가져오고,
	// 프로세스를 시작하고, 일부 입력을 쓰고,
	// 결과 출력을 읽고, 마지막으로 프로세스가
	// 종료될 때까지 기다립니다.
	grepIn, _ := grepCmd.StdinPipe()
	grepOut, _ := grepCmd.StdoutPipe()
	grepCmd.Start()
	grepIn.Write([]byte("hello grep\ngoodbye grep"))
	grepIn.Close()
	grepBytes, _ := io.ReadAll(grepOut)
	grepCmd.Wait()

	// 위의 예제에서는 오류 검사를 생략했지만,
	// 모든 오류에 대해 일반적인 `if err != nil` 패턴을 사용할 수 있습니다.
	// 또한 `StdoutPipe` 결과만 수집하지만,
	// `StderrPipe` 를 정확히 같은 방식으로 수집할 수 있습니다.
	fmt.Println("> grep hello")
	fmt.Println(string(grepBytes))

	// 명령을 생성할 때는
	// 명시적으로 구분된 명령과
	// 인수 배열을 제공해야 합니다.
	// 단일 명령줄 문자열을 전달할 수 있는 것과는 대조적입니다. 전체
	// 문자열로 명령을 생성하려면 `bash` 의 `-c`
	// 옵션을 사용할 수 있습니다.
	lsCmd := exec.Command("bash", "-c", "ls -a -l -h")
	lsOut, err := lsCmd.Output()
	if err != nil {
		panic(err)
	}
	fmt.Println("> ls -a -l -h")
	fmt.Println(string(lsOut))
}
```
