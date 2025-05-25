# 함수 유사 (Function-like) 매크로

함수 유사 매크로는 함수 호출처럼 보이는 매크로를 정의합니다. `macro_rules!` 매크로와 마찬가지로 함수보다 더 유연합니다. 예를 들어 알 수 없는 수의 인수를 사용할 수 있습니다. 그러나 `macro_rules!` 매크로는 "일반 메타 프로그래밍을 위한 macro_rules! 를 사용한 선언적 매크로"에서 논의한 일치하는 구문으로만 정의할 수 있습니다. 함수 유사 매크로는 `TokenStream` 매개변수를 사용하며, 정의는 다른 두 유형의 절차적 매크로와 마찬가지로 Rust 코드를 사용하여 해당 `TokenStream`을 조작합니다. 함수 유사 매크로의 예는 다음과 같이 호출될 수 있는 `sql!` 매크로입니다.

```rust
let sql = sql!(SELECT * FROM posts WHERE id=1);
```

이 매크로는 내부의 SQL 문을 구문 분석하고 구문적으로 올바른지 확인합니다. 이는 `macro_rules!` 매크로가 수행할 수 있는 것보다 훨씬 더 복잡한 처리입니다. `sql!` 매크로는 다음과 같이 정의됩니다.

```rust
#[proc_macro]
pub fn sql(input: TokenStream) -> TokenStream {
```

이 정의는 사용자 정의 `derive` 매크로의 시그니처와 유사합니다. 괄호 안에 있는 토큰을 수신하고 생성하려는 코드를 반환합니다.
