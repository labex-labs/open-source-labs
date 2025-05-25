# 설명 문서 테스트

Rust 프로젝트를 문서화하는 주요 방법은 소스 코드에 주석을 추가하는 것입니다. 설명 문서 주석은 CommonMark Markdown 사양으로 작성되며 코드 블록을 포함할 수 있습니다. Rust 는 정확성을 관리하므로 이러한 코드 블록은 컴파일되어 설명 문서 테스트로 사용됩니다.

````rust
/// 함수를 설명하는 간략한 요약입니다.
///
/// 다음 줄은 자세한 설명입니다. 코드 블록은
/// 3 개의 백틱으로 시작하며 내부에 암시적인 `fn main()`과 `extern crate <cratename>`이 있습니다.
/// `doccomments` 크레이트를 테스트한다고 가정합니다.
///
/// ```
/// let result = doccomments::add(2, 3);
/// assert_eq!(result, 5);
/// ```
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

/// 일반적으로 설명 문서 주석에는 "예제", "예외 발생", "실패" 섹션이 포함될 수 있습니다.
///
/// 다음 함수는 두 수를 나눕니다.
///
/// # 예제
///
/// ```
/// let result = doccomments::div(10, 2);
/// assert_eq!(result, 5);
/// ```
///
/// # 예외 발생
///
/// 두 번째 인수가 0 이면 함수가 예외를 발생시킵니다.
///
/// ```rust
/// // 0 으로 나눌 경우 예외 발생
/// doccomments::div(10, 0);
/// ```
pub fn div(a: i32, b: i32) -> i32 {
    if b == 0 {
        panic!("Divide-by-zero error");
    }

    a / b
}
````

설명 문서의 코드 블록은 정기적인 `cargo test` 명령을 실행할 때 자동으로 테스트됩니다.

```shell
[object Object]
```

## 설명 문서 테스트의 동기

설명 문서 테스트의 주요 목적은 기능을 연습하는 예제 역할을 하는 것입니다. 이는 중요한 지침 중 하나입니다. 문서에서 예제를 완전한 코드 스니펫으로 사용할 수 있도록 합니다. 하지만 `?`를 사용하면 `main`이 `unit`을 반환하기 때문에 컴파일이 실패합니다. 설명 문서에서 일부 소스 줄을 숨길 수 있는 기능이 도움이 됩니다. `fn try_main() -> Result<(), ErrorType>`을 작성하고 숨기고 숨겨진 `main`에서 `unwrap`할 수 있습니다. 복잡해 보이나요? 예제를 보겠습니다.

````rust
/// doc 테스트에서 숨겨진 `try_main` 사용.
///
/// ```
/// # // 숨겨진 줄은 `#` 기호로 시작하지만 여전히 컴파일 가능합니다!
/// # fn try_main() -> Result<(), String> { // doc 에 표시된 본문을 감싸는 줄
/// let res = doccomments::try_div(10, 2)?;
/// # Ok(()) // try_main 에서 반환
/// # }
/// # fn main() { // main 시작
/// #    try_main().unwrap(); // try_main 호출 및 unwrap
/// #                         // 따라서 오류 발생 시 테스트가 예외를 발생시킵니다.
/// # }
/// ```
pub fn try_div(a: i32, b: i32) -> Result<i32, String> {
    if b == 0 {
        Err(String::from("Divide-by-zero"))
    } else {
        Ok(a / b)
    }
}
````
