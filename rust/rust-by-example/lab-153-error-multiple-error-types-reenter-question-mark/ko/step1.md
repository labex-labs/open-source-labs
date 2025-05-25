# `?`의 다른 사용법

이전 예제에서 `parse`를 호출하는 즉시 오류를 라이브러리 오류에서 박스화된 오류로 `map`하는 것을 확인했습니다.

```rust
.and_then(|s| s.parse::<i32>())
    .map_err(|e| e.into())
```

이것은 간단하고 일반적인 연산이므로 생략할 수 있다면 편리할 것입니다. 아쉽게도 `and_then`은 충분히 유연하지 않아서 그렇게 할 수 없습니다. 하지만 대신 `?`를 사용할 수 있습니다.

`?`는 이전에 `unwrap` 또는 `return Err(err)`로 설명되었습니다. 이것은 대부분 사실입니다. 실제로는 `unwrap` 또는 `return Err(From::from(err))`을 의미합니다. `From::from`은 서로 다른 타입 간의 변환 유틸리티이므로, 오류가 반환 타입으로 변환 가능하다면 `?`를 사용하면 자동으로 변환됩니다.

여기서는 `?`를 사용하여 이전 예제를 다시 작성합니다. 결과적으로, 오류 타입에 대해 `From::from`이 구현되면 `map_err`는 사라집니다.

```rust
use std::error;
use std::fmt;

// Change the alias to `Box<dyn error::Error>`.
type Result<T> = std::result::Result<T, Box<dyn error::Error>>;

#[derive(Debug)]
struct EmptyVec;

impl fmt::Display for EmptyVec {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

impl error::Error for EmptyVec {}

// The same structure as before but rather than chain all `Results`
// and `Options` along, we `?` to get the inner value out immediately.
fn double_first(vec: Vec<&str>) -> Result<i32> {
    let first = vec.first().ok_or(EmptyVec)?;
    let parsed = first.parse::<i32>()?;
    Ok(2 * parsed)
}

fn print(result: Result<i32>) {
    match result {
        Ok(n)  => println!("The first doubled is {}", n),
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

이제 실제로 상당히 깔끔해졌습니다. 원래의 `panic`과 비교하면, `unwrap` 호출을 `?`로 대체하는 것과 매우 유사하며, 반환 타입이 `Result`라는 점만 다릅니다. 결과적으로, 최상위 레벨에서 구조 분해 (destructure) 해야 합니다.
