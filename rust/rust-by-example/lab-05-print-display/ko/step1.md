# Display (표시)

`fmt::Debug`는 그다지 간결하고 깔끔해 보이지 않으므로, 출력 형식을 사용자 정의하는 것이 종종 유리합니다. 이는 `{}` 인쇄 마커를 사용하는 `fmt::Display`를 수동으로 구현하여 수행됩니다. 구현은 다음과 같습니다.

```rust
// Import (via `use`) the `fmt` module to make it available.
use std::fmt;

// Define a structure for which `fmt::Display` will be implemented. This is
// a tuple struct named `Structure` that contains an `i32`.
struct Structure(i32);

// To use the `{}` marker, the trait `fmt::Display` must be implemented
// manually for the type.
impl fmt::Display for Structure {
    // This trait requires `fmt` with this exact signature.
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Write strictly the first element into the supplied output
        // stream: `f`. Returns `fmt::Result` which indicates whether the
        // operation succeeded or failed. Note that `write!` uses syntax which
        // is very similar to `println!`.
        write!(f, "{}", self.0)
    }
}
```

`fmt::Display`는 `fmt::Debug`보다 깔끔할 수 있지만, 이는 `std` 라이브러리에게 문제를 제시합니다. 모호한 타입은 어떻게 표시해야 할까요? 예를 들어, `std` 라이브러리가 모든 `Vec<T>`에 대해 단일 스타일을 구현한다면, 어떤 스타일이어야 할까요? 다음 두 가지 중 하나일까요?

- `Vec<path>`: `/:/etc:/home/username:/bin` (`:`로 분할)
- `Vec<number>`: `1,2,3` (`,`로 분할)

아니요, 모든 타입에 대한 이상적인 스타일이 없으며, `std` 라이브러리는 이를 규정하지 않습니다. `fmt::Display`는 `Vec<T>` 또는 다른 제네릭 컨테이너에 대해 구현되지 않습니다. 이러한 제네릭 경우에는 `fmt::Debug`를 사용해야 합니다.

하지만 이는 문제가 되지 않습니다. 제네릭하지 않은 새로운 _컨테이너_ 타입의 경우 `fmt::Display`를 구현할 수 있기 때문입니다.

```rust
use std::fmt; // Import `fmt`

// A structure holding two numbers. `Debug` will be derived so the results can
// be contrasted with `Display`.
#[derive(Debug)]
struct MinMax(i64, i64);

// Implement `Display` for `MinMax`.
impl fmt::Display for MinMax {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Use `self.number` to refer to each positional data point.
        write!(f, "({}, {})", self.0, self.1)
    }
}

// Define a structure where the fields are nameable for comparison.
#[derive(Debug)]
struct Point2D {
    x: f64,
    y: f64,
}

// Similarly, implement `Display` for `Point2D`.
impl fmt::Display for Point2D {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Customize so only `x` and `y` are denoted.
        write!(f, "x: {}, y: {}", self.x, self.y)
    }
}

fn main() {
    let minmax = MinMax(0, 14);

    println!("Compare structures:");
    println!("Display: {}", minmax);
    println!("Debug: {:?}", minmax);

    let big_range =   MinMax(-300, 300);
    let small_range = MinMax(-3, 3);

    println!("The big range is {big} and the small is {small}",
             small = small_range,
             big = big_range);

    let point = Point2D { x: 3.3, y: 7.2 };

    println!("Compare points:");
    println!("Display: {}", point);
    println!("Debug: {:?}", point);

    // Error. Both `Debug` and `Display` were implemented, but `{:b}`
    // requires `fmt::Binary` to be implemented. This will not work.
    // println!("What does Point2D look like in binary: {:b}?", point);
}
```

따라서 `fmt::Display`는 구현되었지만 `fmt::Binary`는 구현되지 않았으므로 사용할 수 없습니다. `std::fmt`에는 이러한 `trait`가 많이 있으며, 각각 자체 구현이 필요합니다. 이는 `std::fmt`에서 자세히 설명합니다.

## 활동

위 예제의 출력을 확인한 후, `Point2D` 구조체를 가이드로 사용하여 예제에 `Complex` 구조체를 추가하십시오. 동일한 방식으로 인쇄하면 출력은 다음과 같아야 합니다.

```txt
Display: 3.3 + 7.2i
Debug: Complex { real: 3.3, imag: 7.2 }
```
