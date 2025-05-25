# 오류 `Box` 처리

원래의 오류를 보존하면서 간단한 코드를 작성하는 한 가지 방법은 오류를 `Box` 처리하는 것입니다. 단점은 기본 오류 타입이 런타임에만 알려지고 정적으로 결정되지 않는다는 것입니다.

`From`을 통해 `Error` 트레이트를 구현하는 모든 타입을 트레이트 객체 `Box<Error>`로 변환하는 `Box` 구현을 stdlib 가 제공하여 오류를 boxing 하는 데 도움을 줍니다.

```rust
use std::error;
use std::fmt;

// Change the alias to `Box<error::Error>`.
type Result<T> = std::result::Result<T, Box<dyn error::Error>>;

#[derive(Debug, Clone)]
struct EmptyVec;

impl fmt::Display for EmptyVec {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

impl error::Error for EmptyVec {}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    vec.first()
        .ok_or_else(|| EmptyVec.into()) // Converts to Box
        .and_then(|s| {
            s.parse::<i32>()
                .map_err(|e| e.into()) // Converts to Box
                .map(|i| 2 * i)
        })
}

fn print(result: Result<i32>) {
    match result {
        Ok(n) => println!("The first doubled is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    print(double_first(numbers));
    print(double_first(empty));
    print(double_first(strings));
}
```
