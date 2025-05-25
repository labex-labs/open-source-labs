# 에러 타입 정의하기

때로는 모든 다른 에러를 단일 에러 타입으로 마스킹하는 것이 코드를 단순화합니다. 사용자 정의 에러를 통해 이를 보여드리겠습니다.

Rust 는 자체 에러 타입을 정의할 수 있도록 합니다. 일반적으로 "좋은" 에러 타입은 다음과 같습니다.

- 동일한 타입으로 다양한 에러를 표현합니다.
- 사용자에게 훌륭한 에러 메시지를 제공합니다.
- 다른 타입과 쉽게 비교할 수 있습니다.
  - 좋음: `Err(EmptyVec)`
  - 나쁨: `Err("Please use a vector with at least one element".to_owned())`
- 에러에 대한 정보를 담을 수 있습니다.
  - 좋음: `Err(BadChar(c, position))`
  - 나쁨: `Err("+ cannot be used here".to_owned())`
- 다른 에러와 잘 조합됩니다.

```rust
use std::fmt;

type Result<T> = std::result::Result<T, DoubleError>;

// Define our error types. These may be customized for our error handling cases.
// Now we will be able to write our own errors, defer to an underlying error
// implementation, or do something in between.
#[derive(Debug, Clone)]
struct DoubleError;

// Generation of an error is completely separate from how it is displayed.
// There's no need to be concerned about cluttering complex logic with the display style.
//
// Note that we don't store any extra info about the errors. This means we can't state
// which string failed to parse without modifying our types to carry that information.
impl fmt::Display for DoubleError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    vec.first()
        // Change the error to our new type.
        .ok_or(DoubleError)
        .and_then(|s| {
            s.parse::<i32>()
                // Update to the new error type here also.
                .map_err(|_| DoubleError)
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
