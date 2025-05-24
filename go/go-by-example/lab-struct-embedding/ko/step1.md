# 구조체 임베딩 (Struct Embedding)

`base`라는 구조체를 임베딩하는 `container`라는 구조체를 생성합니다. `base` 구조체는 `int` 타입의 `num` 필드와 문자열을 반환하는 `describe()` 메서드를 가져야 합니다. `container` 구조체는 `string` 타입의 `str` 필드를 가져야 합니다. `container` 구조체는 `base` 구조체의 `num` 필드와 `describe()` 메서드에 접근할 수 있어야 합니다.

- `base` 구조체는 `int` 타입의 `num` 필드를 가져야 합니다.
- `base` 구조체는 문자열을 반환하는 `describe()` 메서드를 가져야 합니다.
- `container` 구조체는 `string` 타입의 `str` 필드를 가져야 합니다.
- `container` 구조체는 `base` 구조체를 임베딩해야 합니다.
- `container` 구조체는 `base` 구조체의 `num` 필드와 `describe()` 메서드에 접근할 수 있어야 합니다.

```sh
$ go run struct-embedding.go
co={num: 1, str: some name}
also num: 1
describe: base with num=1
describer: base with num=1
```

전체 코드는 다음과 같습니다.

```go
// Go 는 구조체와 인터페이스의 _임베딩_을 지원하여
// 더 매끄러운 타입 _구성_을 표현합니다.
// 이는 Go 버전 1.16+ 에서 도입된 go 지시어인 [`//go:embed`](embed-directive) 와 혼동해서는 안 됩니다.
// 이 지시어는 파일과 폴더를 애플리케이션 바이너리에 임베딩합니다.

package main

import "fmt"

type base struct {
	num int
}

func (b base) describe() string {
	return fmt.Sprintf("base with num=%v", b.num)
}

// `container` 는 `base` 를 _임베딩_합니다. 임베딩은
// 이름이 없는 필드처럼 보입니다.
type container struct {
	base
	str string
}

func main() {

	// 리터럴로 구조체를 생성할 때,
	// 임베딩을 명시적으로 초기화해야 합니다. 여기서
	// 임베딩된 타입은 필드 이름 역할을 합니다.
	co := container{
		base: base{
			num: 1,
		},
		str: "some name",
	}

	// `co` 에서 `base` 의 필드에 직접 접근할 수 있습니다.
	// 예를 들어, `co.num`.
	fmt.Printf("co={num: %v, str: %v}\n", co.num, co.str)

	// 또는, 임베딩된 타입 이름을 사용하여
	// 전체 경로를 명시할 수 있습니다.
	fmt.Println("also num:", co.base.num)

	// `container` 가 `base` 를 임베딩하므로, `base` 의 메서드도
	// `container` 의 메서드가 됩니다. 여기서
	// `base` 에서 임베딩된 메서드를
	// `co` 에서 직접 호출합니다.
	fmt.Println("describe:", co.describe())

	type describer interface {
		describe() string
	}

	// 메서드가 있는 구조체를 임베딩하여
	// 다른 구조체에 인터페이스 구현을 부여할 수 있습니다. 여기서
	// `container` 가 `base` 를 임베딩했기 때문에
	// `describer` 인터페이스를 구현하는 것을 볼 수 있습니다.
	var d describer = co
	fmt.Println("describer:", d.describe())
}
```
