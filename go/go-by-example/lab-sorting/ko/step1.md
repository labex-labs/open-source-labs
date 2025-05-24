# 정렬 (Sorting)

이 랩에서 해결해야 할 문제는 `sort` 패키지를 사용하여 문자열 슬라이스와 정수 슬라이스를 정렬하는 것입니다.

- `sort` 패키지를 임포트해야 합니다.
- 문자열 슬라이스를 정렬하려면 `sort.Strings()` 함수를 사용해야 합니다.
- 정수 슬라이스를 정렬하려면 `sort.Ints()` 함수를 사용해야 합니다.
- 정수 슬라이스가 이미 정렬되었는지 확인하려면 `sort.IntsAreSorted()` 함수를 사용해야 합니다.

```sh
# 프로그램을 실행하면 정렬된 문자열과 정수 슬라이스, 그리고 `AreSorted` 테스트의 결과로 `true` 가 출력됩니다.
$ go run sorting.go
Strings: [a b c]
Ints: [2 4 7]
Sorted: true
```

전체 코드는 다음과 같습니다.

```go
// Go 의 `sort` 패키지는 내장 타입 및 사용자 정의 타입에 대한 정렬을 구현합니다.
// 먼저 내장 타입에 대한 정렬을 살펴보겠습니다.

package main

import (
	"fmt"
	"sort"
)

func main() {

	// 정렬 메서드는 내장 타입에 특화되어 있습니다.
	// 다음은 문자열의 예입니다. 정렬은 제자리에서 이루어지므로
	// 주어진 슬라이스를 변경하며, 새로운 슬라이스를 반환하지 않습니다.
	strs := []string{"c", "a", "b"}
	sort.Strings(strs)
	fmt.Println("Strings:", strs)

	// `int` 정렬의 예입니다.
	ints := []int{7, 2, 4}
	sort.Ints(ints)
	fmt.Println("Ints:   ", ints)

	// 슬라이스가 이미 정렬되었는지 확인하기 위해 `sort` 를 사용할 수도 있습니다.
	s := sort.IntsAreSorted(ints)
	fmt.Println("Sorted: ", s)
}
```
