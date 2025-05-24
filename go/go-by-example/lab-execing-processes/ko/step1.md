# 프로세스 실행 (Execing Processes)

문제는 현재 Go 프로세스를 다른 프로세스 (예: Go 가 아닌 프로세스) 로 대체하는 것입니다.

- Go 프로그래밍 언어
- Go 의 `exec` 함수에 대한 기본적인 지식
- 환경 변수에 대한 이해

```sh
# 프로그램을 실행하면 `ls` 로 대체됩니다.
$ go run execing-processes.go
total 16
drwxr-xr-x 4 mark 136B Oct 3 16:29 .
drwxr-xr-x 91 mark 3.0K Oct 3 12:50 ..
-rw-r--r-- 1 mark 1.3K Oct 3 16:28 execing-processes.go

# Go 는 고전적인 Unix `fork` 함수를 제공하지 않습니다.
# 일반적으로 goroutine 시작, 프로세스 생성 및 execing
# 프로세스가 `fork` 에 대한 대부분의 사용 사례를 다루기 때문에
# 이것은 문제가 되지 않습니다.
```

전체 코드는 다음과 같습니다.

```go
// 이전 예제에서는
// [외부 프로세스 생성](spawning-processes) 을 살펴보았습니다.
// 실행 중인 Go 프로세스에서 액세스할 수 있는 외부 프로세스가
// 필요할 때 이렇게 합니다. 때로는 현재 Go 프로세스를 다른
// (아마도 Go 가 아닌) 프로세스로 완전히 대체하고 싶을 뿐입니다.
// 이를 위해 Go 의 고전적인
// <a href="https://en.wikipedia.org/wiki/Exec_(operating_system)"><code>exec</code></a>
// 함수 구현을 사용합니다.

package main

import (
	"os"
	"os/exec"
	"syscall"
)

func main() {

	// 예제에서는 `ls` 를 실행합니다. Go 는 실행하려는 바이너리에 대한
	// 절대 경로가 필요하므로 `exec.LookPath` 를 사용하여 찾습니다 (아마도
	// `/bin/ls`).
	binary, lookErr := exec.LookPath("ls")
	if lookErr != nil {
		panic(lookErr)
	}

	// `Exec` 는 인수를 슬라이스 형식으로 필요로 합니다 (하나의 큰 문자열과 반대).
	// `ls` 에 몇 가지 일반적인 인수를 제공합니다. 첫 번째 인수는
	// 프로그램 이름이어야 합니다.
	args := []string{"ls", "-a", "-l", "-h"}

	// `Exec` 는 사용할 [환경 변수](environment-variables) 세트도 필요합니다.
	// 여기서는 현재 환경만 제공합니다.
	env := os.Environ()

	// 다음은 실제 `syscall.Exec` 호출입니다. 이 호출이
	// 성공하면 프로세스 실행이 여기서 종료되고 `/bin/ls -a -l -h`
	// 프로세스로 대체됩니다. 오류가 발생하면 반환 값을 얻게 됩니다.
	execErr := syscall.Exec(binary, args, env)
	if execErr != nil {
		panic(execErr)
	}
}
```
