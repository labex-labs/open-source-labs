# `dead_code`

컴파일러는 사용되지 않는 함수에 대한 경고를 제공하는 `dead_code` *lint*를 제공합니다. *특성*을 사용하여 lint 를 비활성화할 수 있습니다.

```rust
fn used_function() {}

// `#[allow(dead_code)]` 는 `dead_code` lint 를 비활성화하는 특성입니다.
#[allow(dead_code)]
fn unused_function() {}

fn noisy_unused_function() {}
// FIXME ^ 경고를 억제하기 위한 특성을 추가하세요.

fn main() {
    used_function();
}
```

실제 프로그램에서는 사용되지 않는 코드를 제거해야 합니다. 이 예제에서는 대화형 예제의 특성상 일부 코드를 사용하지 않는 상태로 두었습니다.
