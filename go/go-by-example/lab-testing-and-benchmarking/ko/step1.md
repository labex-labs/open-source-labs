# 테스트 및 벤치마킹

이 랩에서 해결해야 할 문제는 `IntMin`이라는 정수 최소값 함수의 간단한 구현을 테스트하고 벤치마킹하는 것입니다.

- `testing` 패키지를 임포트해야 합니다.
- `IntMin` 함수는 두 개의 정수 매개변수를 받아 정수를 반환해야 합니다.
- `TestIntMinBasic` 함수는 기본 입력 값에 대해 `IntMin` 함수를 테스트해야 합니다.
- `TestIntMinTableDriven` 함수는 테이블 기반 스타일을 사용하여 `IntMin` 함수를 테스트해야 합니다.
- `BenchmarkIntMin` 함수는 `IntMin` 함수를 벤치마킹해야 합니다.

```sh
# 현재 프로젝트의 모든 테스트를 상세 모드로 실행합니다.

# 현재 프로젝트의 모든 벤치마크를 실행합니다. 모든 테스트는
# 벤치마크 전에 실행됩니다. `bench` 플래그는
# 정규 표현식으로 벤치마크 함수 이름을 필터링합니다.
```

전체 코드는 다음과 같습니다.

```go
// 유닛 테스트는 원칙적인 Go 프로그램을 작성하는 데 중요한 부분입니다.
// `testing` 패키지는 유닛 테스트를 작성하는 데 필요한 도구를 제공하며
// `go test` 명령은 테스트를 실행합니다.

// 설명을 위해 이 코드는 `main` 패키지에 있지만,
// 어떤 패키지든 될 수 있습니다. 테스트 코드는 일반적으로
// 테스트하는 코드와 동일한 패키지에 있습니다.
package main

import (
	"fmt"
	"testing"
)

// 우리는 정수 최소값의 이 간단한 구현을 테스트할 것입니다. 일반적으로, 우리가 테스트하는 코드는
// `intutils.go` 와 같은 이름의 소스 파일에 있을 것이고,
// 이에 대한 테스트 파일은 `intutils_test.go` 라는 이름을 갖게 됩니다.
func IntMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// 테스트는 `Test` 로 시작하는 이름의 함수를 작성하여 생성됩니다.
func TestIntMinBasic(t *testing.T) {
	ans := IntMin(2, -2)
	if ans != -2 {
		// `t.Error*` 는 테스트 실패를 보고하지만
		// 테스트 실행을 계속합니다. `t.Fatal*` 은 테스트
		// 실패를 보고하고 즉시 테스트를 중단합니다.
		t.Errorf("IntMin(2, -2) = %d; want -2", ans)
	}
}

// 테스트 작성이 반복적일 수 있으므로,
// 테스트 입력 및 예상 출력을 테이블에 나열하고
// 단일 루프가 이를 반복하며 테스트 로직을 수행하는 *테이블 기반 스타일*을 사용하는 것이 관용적입니다.
func TestIntMinTableDriven(t *testing.T) {
	var tests = []struct {
		a, b int
		want int
	}{
		{0, 1, 0},
		{1, 0, 0},
		{2, -2, -2},
		{0, -1, -1},
		{-1, 0, -1},
	}

	for _, tt := range tests {
		// t.Run 은 각
		// 테이블 항목에 대해 하나씩 "서브테스트"를 실행할 수 있게 합니다.
		// `go test -v`를 실행할 때 별도로 표시됩니다.
		testname := fmt.Sprintf("%d,%d", tt.a, tt.b)
		t.Run(testname, func(t *testing.T) {
			ans := IntMin(tt.a, tt.b)
			if ans != tt.want {
				t.Errorf("got %d, want %d", ans, tt.want)
			}
		})
	}
}

// 벤치마크 테스트는 일반적으로 `_test.go` 파일에 있으며
// `Benchmark` 로 시작하는 이름을 갖습니다. `testing` 러너는
// 각 벤치마크 함수를 여러 번 실행하여
// 각 실행에서 `b.N` 을 증가시켜 정밀한 측정을 수집합니다.
func BenchmarkIntMin(b *testing.B) {
	// 일반적으로 벤치마크는 우리가
	// 벤치마킹하는 함수를 루프 `b.N` 번 실행합니다.
	for i := 0; i < b.N; i++ {
		IntMin(1, 2)
	}
}
```
