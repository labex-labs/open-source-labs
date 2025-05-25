# ..를 사용하여 값의 나머지 부분 (Remaining Parts of a Value with ..)

여러 부분으로 구성된 값을 사용할 때, `..` 구문을 사용하여 특정 부분을 사용하고 나머지를 무시하여, 무시된 각 값에 대해 밑줄을 나열할 필요가 없도록 할 수 있습니다. `..` 패턴은 패턴의 나머지 부분에서 명시적으로 일치시키지 않은 값의 모든 부분을 무시합니다. Listing 18-23 에서 3 차원 공간의 좌표를 저장하는 `Point` 구조체가 있습니다. `match` 표현식에서 `x` 좌표만 사용하고 `y` 및 `z` 필드의 값은 무시하려고 합니다.

파일 이름: `src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
    z: i32,
}

let origin = Point { x: 0, y: 0, z: 0 };

match origin {
    Point { x, .. } => println!("x is {x}"),
}
```

Listing 18-23: `..`를 사용하여 `x`를 제외한 `Point`의 모든 필드 무시하기

`x` 값을 나열한 다음 `..` 패턴을 포함합니다. 이는 특히 하나 또는 두 개의 필드만 관련이 있는 많은 필드가 있는 구조체로 작업할 때 `y: _` 및 `z: _`를 나열하는 것보다 빠릅니다.

구문 `..`는 필요한 만큼 많은 값으로 확장됩니다. Listing 18-24 는 튜플과 함께 `..`를 사용하는 방법을 보여줍니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let numbers = (2, 4, 8, 16, 32);

    match numbers {
        (first, .., last) => {
            println!("Some numbers: {first}, {last}");
        }
    }
}
```

Listing 18-24: 튜플에서 첫 번째 및 마지막 값만 일치시키고 다른 모든 값 무시하기

이 코드에서 첫 번째 및 마지막 값은 `first` 및 `last`와 일치합니다. `..`는 중간의 모든 것을 일치시키고 무시합니다.

그러나 `..`를 사용하는 것은 모호하지 않아야 합니다. 어떤 값을 일치시키고 어떤 값을 무시해야 하는지 명확하지 않은 경우 Rust 는 오류를 발생시킵니다. Listing 18-25 는 `..`를 모호하게 사용하는 예제를 보여주므로 컴파일되지 않습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let numbers = (2, 4, 8, 16, 32);

    match numbers {
        (.., second, ..) => {
            println!("Some numbers: {second}");
        },
    }
}
```

Listing 18-25: 모호한 방식으로 `..`를 사용하려는 시도

이 예제를 컴파일하면 다음과 같은 오류가 발생합니다.

```bash
error: `..` can only be used once per tuple pattern
 --> src/main.rs:5:22
  |
5 |         (.., second, ..) => {
  |          --          ^^ can only be used once per tuple pattern
  |          |
  |          previously used here
```

Rust 가 `second`와 값을 일치시키기 전에 튜플에서 얼마나 많은 값을 무시해야 하는지, 그리고 그 후에 얼마나 많은 값을 더 무시해야 하는지 결정하는 것은 불가능합니다. 이 코드는 `2`를 무시하고, `second`를 `4`에 바인딩한 다음 `8`, `16`, `32`를 무시하려는 것을 의미할 수 있습니다. 또는 `2`와 `4`를 무시하고, `second`를 `8`에 바인딩한 다음 `16`과 `32`를 무시하려는 것을 의미할 수 있습니다. 등등. 변수 이름 `second`는 Rust 에 특별한 의미가 없으므로, 이처럼 두 곳에서 `..`를 사용하는 것은 모호하기 때문에 컴파일러 오류가 발생합니다.
