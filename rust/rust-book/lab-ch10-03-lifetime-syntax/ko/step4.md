# 함수에서 제네릭 생명주기

두 문자열 슬라이스 중 더 긴 슬라이스를 반환하는 함수를 작성해 보겠습니다. 이 함수는 두 개의 문자열 슬라이스를 받아 단일 문자열 슬라이스를 반환합니다. `longest` 함수를 구현한 후, Listing 10-19 의 코드는 `The longest string is abcd`를 출력해야 합니다.

Filename: `src/main.rs`

```rust
fn main() {
    let string1 = String::from("abcd");
    let string2 = "xyz";

    let result = longest(string1.as_str(), string2);
    println!("The longest string is {result}");
}
```

Listing 10-19: 두 문자열 슬라이스 중 더 긴 슬라이스를 찾기 위해 `longest` 함수를 호출하는 `main` 함수

`longest` 함수가 매개변수의 소유권을 가져가지 않도록 하기 위해 문자열 대신 참조인 문자열 슬라이스를 함수가 사용하도록 하려고 합니다. Listing 10-19 에서 사용하는 매개변수가 원하는 매개변수인 이유에 대한 자세한 내용은 "매개변수로서의 문자열 슬라이스"를 참조하십시오.

Listing 10-20 과 같이 `longest` 함수를 구현하려고 하면 컴파일되지 않습니다.

Filename: `src/main.rs`

```rust
fn longest(x: &str, y: &str) -> &str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

Listing 10-20: 두 문자열 슬라이스 중 더 긴 슬라이스를 반환하지만 아직 컴파일되지 않는 `longest` 함수의 구현

대신, 생명주기에 대해 이야기하는 다음 오류가 발생합니다.

```bash
error[E0106]: missing lifetime specifier
 --> src/main.rs:9:33
  |
9 | fn longest(x: &str, y: &str) -> &str {
  |               ----     ----     ^ expected named lifetime parameter
  |
  = help: this function's return type contains a borrowed value,
but the signature does not say whether it is borrowed from `x` or `y`
help: consider introducing a named lifetime parameter
  |
9 | fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
  |           ++++     ++          ++          ++
```

도움말 텍스트는 반환되는 참조가 `x` 또는 `y`를 참조하는지 Rust 가 알 수 없기 때문에 반환 유형에 제네릭 생명주기 매개변수가 필요함을 나타냅니다. 실제로, 이 함수의 본문에서 `if` 블록은 `x`에 대한 참조를 반환하고 `else` 블록은 `y`에 대한 참조를 반환하므로 우리도 알 수 없습니다!

이 함수를 정의할 때, 이 함수에 전달될 구체적인 값을 알 수 없으므로 `if` 케이스 또는 `else` 케이스가 실행될지 알 수 없습니다. 또한 전달될 참조의 구체적인 생명주기를 알 수 없으므로 Listing 10-17 및 10-18 에서 했던 것처럼 범위를 살펴보고 반환하는 참조가 항상 유효한지 확인할 수 없습니다. 차용 검사기 역시 이를 결정할 수 없습니다. 왜냐하면 `x`와 `y`의 생명주기가 반환 값의 생명주기와 어떻게 관련되는지 알 수 없기 때문입니다. 이 오류를 수정하려면, 차용 검사기가 분석을 수행할 수 있도록 참조 간의 관계를 정의하는 제네릭 생명주기 매개변수를 추가합니다.
