# Embed 지시어 (Directive)

주어진 코드를 수정하여 파일과 폴더를 Go 바이너리에 임베드하고 내용을 출력하는 것이 과제입니다.

- `embed` 패키지를 사용하여 파일과 폴더를 임베드해야 합니다.
- `string` 및 `[]byte` 타입을 사용하여 임베드된 파일의 내용을 저장해야 합니다.
- 와일드카드 (wildcard) 를 사용하여 여러 파일 또는 폴더를 임베드하려면 `embed.FS` 타입을 사용해야 합니다.
- 임베드된 파일의 내용을 출력해야 합니다.

```sh
# 예제를 실행하려면 다음 명령을 사용하십시오.
# (참고: go playground 의 제한으로 인해,
# 이 예제는 로컬 머신에서만 실행할 수 있습니다.)
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

전체 코드는 다음과 같습니다.

```go
// `//go:embed` 는 [컴파일러
// 지시어](https://pkg.go.dev/cmd/compile#hdr-Compiler_Directives) 로,
// 빌드 시점에 임의의 파일과 폴더를 Go 바이너리에 포함할 수 있도록 합니다. embed 지시어에 대해 자세히 알아보려면
// [여기](https://pkg.go.dev/embed) 를 참조하십시오.
package main

// `embed` 패키지를 임포트합니다. 이 패키지에서 내보낸 식별자를 사용하지 않는 경우, `_ "embed"`를 사용하여 빈 임포트를 수행할 수 있습니다.
import (
	"embed"
)

// `embed` 지시어는 Go 소스 파일을 포함하는 디렉토리를 기준으로 상대 경로를 허용합니다. 이 지시어는 파일의 내용을 바로 뒤에 오는 `string` 변수에 임베드합니다.
//
//go:embed folder/single_file.txt
var fileString string

// 또는 파일의 내용을 `[]byte` 에 임베드합니다.
//
//go:embed folder/single_file.txt
var fileByte []byte

// 또한 와일드카드를 사용하여 여러 파일 또는 폴더를 임베드할 수도 있습니다. 이는 간단한 가상 파일 시스템을 구현하는 [embed.FS 타입](https://pkg.go.dev/embed#FS) 의 변수를 사용합니다.
//
//go:embed folder/single_file.txt
//go:embed folder/*.hash
var folder embed.FS

func main() {

	// `single_file.txt` 의 내용을 출력합니다.
	print(fileString)
	print(string(fileByte))

	// 임베드된 폴더에서 일부 파일을 검색합니다.
	content1, _ := folder.ReadFile("folder/file1.hash")
	print(string(content1))

	content2, _ := folder.ReadFile("folder/file2.hash")
	print(string(content2))
}
```
