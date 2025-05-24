# 구조체 (Structs)

이 랩에서는 주어진 이름으로 새로운 person 구조체를 생성하는 `newPerson` 함수를 완성해야 합니다. `person` 구조체 타입은 `name`과 `age` 필드를 가지고 있습니다.

- `person` 구조체 타입은 `name`과 `age` 필드를 가져야 합니다.
- `newPerson` 함수는 주어진 이름으로 새로운 person 구조체를 생성해야 합니다.
- `newPerson` 함수는 새로 생성된 person 구조체에 대한 포인터를 반환해야 합니다.
- `main` 함수는 다음을 출력해야 합니다:
  - 이름이 "Bob"이고 나이가 20 인 새로운 구조체.
  - 이름이 "Alice"이고 나이가 30 인 새로운 구조체.
  - 이름이 "Fred"이고 나이가 0 인 새로운 구조체.
  - 이름이 "Ann"이고 나이가 40 인 새로운 구조체에 대한 포인터.
  - `newPerson` 함수를 사용하여 생성된 이름이 "Jon"이고 나이가 42 인 새로운 구조체.
  - 이름이 "Sean"이고 나이가 50 인 구조체의 name 필드.
  - 이름이 "Sean"이고 나이가 50 인 구조체에 대한 구조체 포인터의 age 필드.
  - age 필드가 51 로 업데이트된 후 이름이 "Sean"이고 나이가 50 인 구조체에 대한 구조체 포인터의 age 필드.

```sh
$ go run structs.go
{Bob 20}
{Alice 30}
{Fred 0}
&{Ann 40}
&{Jon 42}
Sean
50
51
```

전체 코드는 다음과 같습니다:

```go
// Go 의 _structs_는 필드의 유형화된 컬렉션입니다.
// 레코드를 형성하기 위해 데이터를 함께 그룹화하는 데 유용합니다.

package main

import "fmt"

// 이 `person` 구조체 타입은 `name` 과 `age` 필드를 가지고 있습니다.
type person struct {
	name string
	age  int
}

// `newPerson` 은 주어진 이름으로 새로운 person 구조체를 생성합니다.
func newPerson(name string) *person {
	// 로컬 변수에 대한 포인터를 안전하게 반환할 수 있습니다.
	// 로컬 변수는 함수의 범위를 벗어나도 유지됩니다.
	p := person{name: name}
	p.age = 42
	return &p
}

func main() {

	// 이 구문은 새로운 구조체를 생성합니다.
	fmt.Println(person{"Bob", 20})

	// 구조체를 초기화할 때 필드의 이름을 지정할 수 있습니다.
	fmt.Println(person{name: "Alice", age: 30})

	// 생략된 필드는 0 으로 채워집니다.
	fmt.Println(person{name: "Fred"})

	// `&` 접두사는 구조체에 대한 포인터를 생성합니다.
	fmt.Println(&person{name: "Ann", age: 40})

	// 새로운 구조체 생성을 생성자 함수에 캡슐화하는 것이 관용적입니다.
	fmt.Println(newPerson("Jon"))

	// 점을 사용하여 구조체 필드에 접근합니다.
	s := person{name: "Sean", age: 50}
	fmt.Println(s.name)

	// 구조체 포인터와 함께 점을 사용할 수도 있습니다.
	// 포인터는 자동으로 역참조됩니다.
	sp := &s
	fmt.Println(sp.age)

	// 구조체는 변경 가능합니다.
	sp.age = 51
	fmt.Println(sp.age)
}
```
