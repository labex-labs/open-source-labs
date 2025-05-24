# Range (범위)

이 랩에서 해결해야 할 문제는 `range`를 슬라이스 (slice), 배열 (array), 맵 (map), 문자열 (string) 과 함께 사용하는 방법을 시연하는 것입니다.

이 랩을 완료하려면 다음이 필요합니다.

- Golang 구문에 대한 기본적인 지식
- 컴퓨터에 설치된 Golang

```sh
$ go run range.go
sum: 9
index: 1
a - > apple
b - > banana
key: a
key: b
0 103
1 111
```

전체 코드는 다음과 같습니다.

```go
// _range_는 다양한 자료 구조의 요소를 반복합니다.
// 이미 배운 몇 가지 자료 구조와 함께 `range` 를 사용하는 방법을 살펴보겠습니다.

package main

import "fmt"

func main() {

	// 여기서는 `range` 를 사용하여 슬라이스 내 숫자들의 합을 구합니다.
	// 배열도 이와 같이 작동합니다.
	nums := []int{2, 3, 4}
	sum := 0
	for _, num := range nums {
		sum += num
	}
	fmt.Println("sum:", sum)

	// 배열과 슬라이스에 대한 `range` 는 각 항목에 대한
	// 인덱스 (index) 와 값을 모두 제공합니다. 위에서는 인덱스가
	// 필요하지 않아 빈 식별자 `_` 로 무시했습니다. 하지만
	// 때로는 실제로 인덱스가 필요할 때도 있습니다.
	for i, num := range nums {
		if num == 3 {
			fmt.Println("index:", i)
		}
	}

	// 맵에 대한 `range` 는 키/값 쌍을 반복합니다.
	kvs := map[string]string{"a": "apple", "b": "banana"}
	for k, v := range kvs {
		fmt.Printf("%s -> %s\n", k, v)
	}

	// `range` 는 맵의 키만 반복할 수도 있습니다.
	for k := range kvs {
		fmt.Println("key:", k)
	}

	// 문자열에 대한 `range` 는 유니코드 코드
	// 포인트를 반복합니다. 첫 번째 값은 `rune` 의 시작 바이트 인덱스이고
	// 두 번째 값은 `rune` 자체입니다.
	// 자세한 내용은 [Strings and Runes](strings-and-runes) 를 참조하십시오.
	for i, c := range "go" {
		fmt.Println(i, c)
	}
}
```
