# macro_rules!

Rust 는 메타 프로그래밍을 가능하게 하는 강력한 매크로 시스템을 제공합니다. 이전 챕터에서 보았듯이, 매크로는 함수처럼 보이지만, 이름이 느낌표 `!`로 끝난다는 점이 다릅니다. 하지만 함수 호출을 생성하는 대신, 매크로는 소스 코드로 확장되어 프로그램의 나머지 부분과 함께 컴파일됩니다. 그러나 C 및 기타 언어의 매크로와 달리, Rust 매크로는 문자열 전처리가 아닌 추상 구문 트리 (Abstract Syntax Trees, AST) 로 확장되므로 예상치 못한 우선 순위 버그가 발생하지 않습니다.

매크로는 `macro_rules!` 매크로를 사용하여 생성됩니다.

```rust
// This is a simple macro named `say_hello`.
macro_rules! say_hello {
    // `()` indicates that the macro takes no argument.
    () => {
        // The macro will expand into the contents of this block.
        println!("Hello!")
    };
}

fn main() {
    // This call will expand into `println!("Hello")`
    say_hello!()
}
```

그렇다면 매크로가 유용한 이유는 무엇일까요?

1.  DRY (Don't Repeat Yourself, 중복 금지). 여러 위치에서 서로 다른 타입으로 유사한 기능이 필요한 경우가 많습니다. 종종 매크로를 작성하는 것은 코드 중복을 피하는 유용한 방법입니다. (자세한 내용은 나중에)

2.  도메인 특화 언어 (Domain-Specific Languages, DSL). 매크로를 사용하면 특정 목적을 위한 특별한 구문을 정의할 수 있습니다. (자세한 내용은 나중에)

3.  가변 인터페이스 (Variadic interfaces). 때로는 가변 개수의 인수를 받는 인터페이스를 정의하고 싶을 수 있습니다. 예시는 형식 문자열에 따라 임의의 수의 인수를 받을 수 있는 `println!`입니다. (자세한 내용은 나중에)
