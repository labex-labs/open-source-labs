# 여러 오류 유형

이전 예제들은 항상 매우 편리했습니다; `Result`는 다른 `Result`와 상호 작용하고, `Option`은 다른 `Option`과 상호 작용합니다.

때로는 `Option`이 `Result`와 상호 작용해야 하거나, `Result<T, Error1>`이 `Result<T, Error2>`와 상호 작용해야 할 필요가 있습니다. 이러한 경우, 서로 조합 가능하고 상호 작용하기 쉬운 방식으로 다양한 오류 유형을 관리하고자 합니다.

다음 코드에서 `unwrap`의 두 인스턴스는 서로 다른 오류 유형을 생성합니다. `Vec::first`는 `Option`을 반환하고, `parse::<i32>`는 `Result<i32, ParseIntError>`를 반환합니다.

```rust
fn double_first(vec: Vec<&str>) -> i32 {
    let first = vec.first().unwrap(); // Generate error 1
    2 * first.parse::<i32>().unwrap() // Generate error 2
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    println!("The first doubled is {}", double_first(numbers));

    println!("The first doubled is {}", double_first(empty));
    // Error 1: the input vector is empty

    println!("The first doubled is {}", double_first(strings));
    // Error 2: the element doesn't parse to a number
}
```

다음 섹션에서는 이러한 종류의 문제를 처리하기 위한 몇 가지 전략을 살펴보겠습니다.
