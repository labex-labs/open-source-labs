# 형식화된 출력

출력은 `std::fmt`에 정의된 일련의 `매크로(macros)`에 의해 처리되며, 그 중 일부는 다음과 같습니다.

- `format!`: 형식화된 텍스트를 `String`에 씁니다.
- `print!`: `format!`과 동일하지만 텍스트가 콘솔 (io::stdout) 에 출력됩니다.
- `println!`: `print!`와 동일하지만 줄 바꿈이 추가됩니다.
- `eprint!`: `print!`와 동일하지만 텍스트가 표준 오류 (io::stderr) 에 출력됩니다.
- `eprintln!`: `eprint!`와 동일하지만 줄 바꿈이 추가됩니다.

모두 동일한 방식으로 텍스트를 구문 분석합니다. 게다가 Rust 는 컴파일 시간에 형식 지정의 정확성을 검사합니다.

```rust
fn main() {
    // 일반적으로 `{}` 는 모든 인수로 자동 대체됩니다. 이들은 문자열화됩니다.
    println!("{} days", 31);

    // 위치 인수를 사용할 수 있습니다. `{}` 안에 정수를 지정하면
    // 어떤 추가 인수가 대체될지 결정됩니다. 인수는 형식 문자열 바로 뒤 0 부터 시작합니다.
    println!("{0}, this is {1}. {1}, this is {0}", "Alice", "Bob");

    // 명명된 인수도 마찬가지입니다.
    println!("{subject} {verb} {object}",
             object="the lazy dog",
             subject="the quick brown fox",
             verb="jumps over");

    // `:` 뒤에 형식 지정 문자를 지정하여 다른 형식을 호출할 수 있습니다.
    println!("Base 10:               {}",   69420); // 69420
    println!("Base 2 (binary):       {:b}", 69420); // 10000111100101100
    println!("Base 8 (octal):        {:o}", 69420); // 207454
    println!("Base 16 (hexadecimal): {:x}", 69420); // 10f2c
    println!("Base 16 (hexadecimal): {:X}", 69420); // 10F2C

    // 지정된 너비로 텍스트를 오른쪽 정렬할 수 있습니다. 이렇게 하면 "    1"이 출력됩니다.
    // (총 너비가 5 가 되도록 공백 4 개와 "1" 하나).
    println!("{number:>5}", number=1);

    // 숫자를 추가 0 으로 채울 수 있습니다.
    println!("{number:0>5}", number=1); // 00001
    // 그리고 부호를 뒤집어 왼쪽 정렬할 수 있습니다. 이렇게 하면 "10000"이 출력됩니다.
    println!("{number:0<5}", number=1); // 10000

    // `$` 를 추가하여 형식 지정자에서 명명된 인수를 사용할 수 있습니다.
    println!("{number:0>width$}", number=1, width=5);

    // Rust 는 올바른 수의 인수가 사용되었는지도 확인합니다.
    println!("My name is {0}, {1} {0}", "Bond");
    // FIXME ^ 누락된 인수 추가: "James"

    // `fmt::Display` 를 구현하는 타입만 `{}` 로 형식화할 수 있습니다. 사용자 정의
    // 타입은 기본적으로 `fmt::Display` 를 구현하지 않습니다.

    #[allow(dead_code)] // 사용하지 않는 모듈에 대해 경고하는 `dead_code` 비활성화
    struct Structure(i32);

    // `Structure` 가 `fmt::Display` 를 구현하지 않기 때문에
    // 이 코드는 컴파일되지 않습니다.
    // println!("This struct `{}` won't print...", Structure(3));
    // TODO ^ 이 줄의 주석을 해제해 보세요

    // Rust 1.58 이상에서는 주변 변수에서 인수를 직접 캡처할 수 있습니다.
    // 위와 마찬가지로 "    1", 공백 4 개와 "1"이 출력됩니다.
    let number: f64 = 1.0;
    let width: usize = 5;
    println!("{number:>width$}");
}
```

`std::fmt`에는 텍스트 표시를 제어하는 많은 `트레이트(traits)`가 포함되어 있습니다. 두 가지 중요한 트레이트의 기본 형태는 다음과 같습니다.

- `fmt::Debug`: `{?:}` 마커를 사용합니다. 디버깅 목적으로 텍스트를 형식화합니다.
- `fmt::Display`: `{}` 마커를 사용합니다. 보다 우아하고 사용자 친화적인 방식으로 텍스트를 형식화합니다.

여기서는 std 라이브러리가 이러한 타입에 대한 구현을 제공하기 때문에 `fmt::Display`를 사용했습니다. 사용자 정의 타입에 대한 텍스트를 출력하려면 더 많은 단계가 필요합니다.

`fmt::Display` 트레이트를 구현하면 자동으로 `ToString` 트레이트가 구현되어 타입을 `String`으로 변환할 수 있습니다.

*43 번째 줄*에서 `#[allow(dead_code)]`는 그 뒤의 모듈에만 적용되는 \[속성 (attribute)]입니다.

## 활동

- 위의 코드에서 오류가 발생하지 않도록 문제를 수정하세요 (FIXME 참조).
- `Structure` 구조체를 형식화하려는 줄의 주석을 해제해 보세요 (TODO 참조).
- `Pi is roughly 3.142`를 출력하는 `println!` 매크로 호출을 추가하여 표시되는 소수점 자릿수를 제어하세요. 이 연습을 위해 `let pi = 3.141592`를 pi 의 추정치로 사용하세요. (힌트: 표시할 소수점 자릿수를 설정하려면 `std::fmt` 문서를 확인해야 할 수 있습니다.)
