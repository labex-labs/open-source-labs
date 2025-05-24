# 텍스트 템플릿

이 랩에서는 동적 콘텐츠를 생성하기 위해 `text/template` 패키지를 사용하는 방법을 시연해야 합니다.

- `text/template` 패키지를 사용하여 동적 콘텐츠를 생성합니다.
- `template.Must` 함수를 사용하여 `Parse`가 오류를 반환하는 경우 패닉을 발생시킵니다.
- `{{.FieldName}}` 액션을 사용하여 구조체 필드에 접근합니다.
- `{{if . -}} yes {{else -}} no {{end}}\n` 액션을 사용하여 템플릿에 대한 조건부 실행을 제공합니다.
- `{{range .}}{{.}} {{end}}\n` 액션을 사용하여 슬라이스, 배열, 맵 또는 채널을 반복합니다.

```sh
$ go run templates.go
Value: some text
Value: 5
Value: [Go Rust C++ C#]
Name: Jane Doe
Name: Mickey Mouse
yes
no
Range: Go Rust C++ C#
```

전체 코드는 다음과 같습니다.

```go
// Go 는 `text/template` 패키지를 사용하여 동적 콘텐츠를 생성하거나 사용자에게 맞춤형 출력을 표시하는 기능을 기본적으로 제공합니다. `html/template` 이라는 형제 패키지는 동일한 API 를 제공하지만 추가적인 보안 기능을 갖추고 있으며 HTML 을 생성하는 데 사용해야 합니다.

package main

import (
	"os"
	"text/template"
)

func main() {

	// 우리는 새로운 템플릿을 생성하고 문자열에서 본문을 파싱할 수 있습니다.
	// 템플릿은 정적 텍스트와 `{{...}}` 로 묶인 "액션"의 혼합으로, 동적으로 콘텐츠를 삽입하는 데 사용됩니다.
	t1 := template.New("t1")
	t1, err := t1.Parse("Value is {{.}}\n")
	if err != nil {
		panic(err)
	}

	// 또는, `template.Must` 함수를 사용하여 `Parse` 가 오류를 반환하는 경우 패닉을 발생시킬 수 있습니다. 이는 특히 전역 범위에서 초기화된 템플릿에 유용합니다.
	t1 = template.Must(t1.Parse("Value: {{.}}\n"))

	// 템플릿을 "실행"함으로써 액션에 대한 특정 값으로 텍스트를 생성합니다. `{{.}}` 액션은 `Execute` 에 매개변수로 전달된 값으로 대체됩니다.
	t1.Execute(os.Stdout, "some text")
	t1.Execute(os.Stdout, 5)
	t1.Execute(os.Stdout, []string{
		"Go",
		"Rust",
		"C++",
		"C#",
	})

	// 아래에서 사용할 헬퍼 함수입니다.
	Create := func(name, t string) *template.Template {
		return template.Must(template.New(name).Parse(t))
	}

	// 데이터가 구조체인 경우 `{{.FieldName}}` 액션을 사용하여
	// 해당 필드에 접근할 수 있습니다. 템플릿이 실행될 때 접근 가능하려면 필드를 export 해야 합니다.
	t2 := Create("t2", "Name: {{.Name}}\n")

	t2.Execute(os.Stdout, struct {
		Name string
	}{"Jane Doe"})

	// 맵에도 동일하게 적용됩니다. 맵의 경우 키 이름에 대한 제한이 없습니다.
	t2.Execute(os.Stdout, map[string]string{
		"Name": "Mickey Mouse",
	})

	// if/else는 템플릿에 대한 조건부 실행을 제공합니다. 값은 0, 빈 문자열,
	// nil 포인터 등과 같이 해당 유형의 기본값인 경우 false 로 간주됩니다.
	// 이 샘플은 템플릿의 또 다른 기능을 보여줍니다. 액션에서 `-` 를 사용하여 공백을 제거합니다.
	t3 := Create("t3",
		"{{if . -}} yes {{else -}} no {{end}}\n")
	t3.Execute(os.Stdout, "not empty")
	t3.Execute(os.Stdout, "")

	// range 블록을 사용하면 슬라이스, 배열, 맵 또는 채널을 반복할 수 있습니다. range 블록 내부에서 `{{.}}` 는 반복의 현재 항목으로 설정됩니다.
	t4 := Create("t4",
		"Range: {{range .}}{{.}} {{end}}\n")
	t4.Execute(os.Stdout,
		[]string{
			"Go",
			"Rust",
			"C++",
			"C#",
		})
}
```
