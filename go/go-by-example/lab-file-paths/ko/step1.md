# 파일 경로

이 랩에서는 `filepath` 패키지를 사용하여 파일 경로에 대한 다양한 작업을 수행해야 합니다. 예를 들어, 이식 가능한 방식으로 경로를 구성하고, 경로를 디렉토리와 파일 구성 요소로 분할하고, 경로가 절대 경로인지 확인하고, 파일의 확장자를 찾고, 두 경로 사이의 상대 경로를 찾는 등의 작업을 수행합니다.

- `Join`을 사용하여 이식 가능한 방식으로 경로를 구성합니다.
- `Dir` 및 `Base`를 사용하여 경로를 디렉토리와 파일 구성 요소로 분할합니다.
- `IsAbs`를 사용하여 경로가 절대 경로인지 확인합니다.
- `Ext`를 사용하여 파일의 확장자를 찾습니다.
- `TrimSuffix`를 사용하여 파일 이름에서 확장자를 제거합니다.
- `Rel`을 사용하여 두 경로 사이의 상대 경로를 찾습니다.

```sh
$ go run file-paths.go
p: dir1/dir2/filename
dir1/filename
dir1/filename
Dir(p): dir1/dir2
Base(p): filename
false
true
.json
config
t/file
../c/t/file

```

전체 코드는 다음과 같습니다.

```go
// `filepath` 패키지는 운영 체제 간에 이식 가능한 방식으로
// *파일 경로*를 파싱하고 구성하는 기능을 제공합니다. 예를 들어, Linux 에서는 `dir/file` 이고
// Windows 에서는 `dir\file` 입니다.
package main

import (
	"fmt"
	"path/filepath"
	"strings"
)

func main() {

	// `Join` 은 이식 가능한 방식으로 경로를 구성하는 데 사용해야 합니다.
	// 임의의 수의 인수를 받아 계층적 경로를 구성합니다.
	p := filepath.Join("dir1", "dir2", "filename")
	fmt.Println("p:", p)

	// `/` 또는 `\` 를 수동으로 연결하는 대신 항상 `Join` 을 사용해야 합니다.
	// 이식성을 제공하는 것 외에도 `Join` 은 불필요한 구분 기호와
	// 디렉토리 변경을 제거하여 경로를 정규화합니다.
	fmt.Println(filepath.Join("dir1//", "filename"))
	fmt.Println(filepath.Join("dir1/../dir1", "filename"))

	// `Dir` 및 `Base` 를 사용하여 경로를 디렉토리와 파일로 분할할 수 있습니다.
	// 또는 `Split` 을 사용하면 동일한 호출에서 둘 다 반환됩니다.
	fmt.Println("Dir(p):", filepath.Dir(p))
	fmt.Println("Base(p):", filepath.Base(p))

	// 경로가 절대 경로인지 확인할 수 있습니다.
	fmt.Println(filepath.IsAbs("dir/file"))
	fmt.Println(filepath.IsAbs("/dir/file"))

	filename := "config.json"

	// 일부 파일 이름에는 점 뒤에 확장자가 있습니다.
	// `Ext` 를 사용하여 이러한 이름에서 확장자를 분리할 수 있습니다.
	ext := filepath.Ext(filename)
	fmt.Println(ext)

	// 확장자가 제거된 파일 이름을 찾으려면
	// `strings.TrimSuffix` 를 사용합니다.
	fmt.Println(strings.TrimSuffix(filename, ext))

	// `Rel` 은 *base*와 *target* 사이의 상대 경로를 찾습니다.
	// target 을 base 에 상대적으로 만들 수 없는 경우 오류를 반환합니다.
	rel, err := filepath.Rel("a/b", "a/b/t/file")
	if err != nil {
		panic(err)
	}
	fmt.Println(rel)

	rel, err = filepath.Rel("a/b", "a/c/t/file")
	if err != nil {
		panic(err)
	}
	fmt.Println(rel)
}
```
