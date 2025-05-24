# 함수를 이용한 정렬

이 랩에서 해결해야 할 문제는 문자열 슬라이스를 길이별로 정렬하는 사용자 정의 정렬 함수를 Go 에서 구현하는 것입니다.

- `byLength` 타입은 `[]string` 타입의 별칭으로 생성되어야 합니다.
- `sort.Interface`는 `byLength` 타입에 구현되어야 합니다.
- `Len` 및 `Swap` 함수는 `byLength` 타입에 구현되어야 합니다.
- `Less` 함수는 실제 사용자 정의 정렬 로직을 포함하도록 `byLength` 타입에 구현되어야 합니다.
- `main` 함수는 원래의 `fruits` 슬라이스를 `byLength`로 변환한 다음, 해당 타입의 슬라이스에 대해 `sort.Sort`를 사용해야 합니다.

```sh
# 프로그램을 실행하면 원하는 대로 문자열
# 길이별로 정렬된 목록이 표시됩니다.
$ go run sorting-by-functions.go
[kiwi peach banana]

# 이와 동일한 패턴 (사용자 정의
# 타입 생성, 해당 타입에 세 가지 `Interface` 메서드 구현,
# 그리고 해당 사용자 정의 타입의 컬렉션에 대해 sort.Sort 호출) 을 따르면,
# 임의의 함수를 사용하여 Go 슬라이스를 정렬할 수 있습니다.
```

전체 코드는 다음과 같습니다.

```go
// 때로는 자연적인 순서가 아닌 다른 기준으로
// 컬렉션을 정렬해야 할 수 있습니다. 예를 들어,
// 알파벳순이 아닌 문자열 길이를 기준으로 정렬하려는 경우를 가정해 보겠습니다.
// 다음은 Go 에서 사용자 정의 정렬의 예입니다.

package main

import (
	"fmt"
	"sort"
)

// Go 에서 사용자 정의 함수로 정렬하려면
// 해당 타입이 필요합니다. 여기서는 기본 제공 `[]string`
// 타입의 별칭인 `byLength` 타입을 만들었습니다.
type byLength []string

// `sort.Interface` - `Len`, `Less`, 및
// `Swap` - 을 우리 타입에 구현하여 `sort` 패키지의
// 제네릭 `Sort` 함수를 사용할 수 있습니다. `Len` 및 `Swap` 은
// 일반적으로 타입 간에 유사하며 `Less` 는
// 실제 사용자 정의 정렬 로직을 포함합니다. 이 경우 문자열 길이가 증가하는 순서로
// 정렬하므로 여기서는 `len(s[i])` 및 `len(s[j])` 를 사용합니다.
func (s byLength) Len() int {
	return len(s)
}
func (s byLength) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}
func (s byLength) Less(i, j int) bool {
	return len(s[i]) < len(s[j])
}

// 이 모든 것이 준비되면 이제 원래의 `fruits` 슬라이스를
// `byLength` 로 변환한 다음, 해당 타입의
// 슬라이스에 대해 `sort.Sort` 를 사용하여 사용자 정의 정렬을 구현할 수 있습니다.
func main() {
	fruits := []string{"peach", "banana", "kiwi"}
	sort.Sort(byLength(fruits))
	fmt.Println(fruits)
}
```
