# 문자열 인덱싱 (Indexing)

다른 많은 프로그래밍 언어에서는 문자열 내의 개별 문자에 인덱스를 사용하여 참조하여 접근하는 것이 유효하고 일반적인 연산입니다. 그러나 Rust 에서 인덱싱 구문을 사용하여 `String`의 일부에 접근하려고 하면 오류가 발생합니다. Listing 8-19 의 잘못된 코드를 살펴보겠습니다.

```rust
let s1 = String::from("hello");
let h = s1[0];
```

Listing 8-19: `String`에 인덱싱 구문을 사용하려는 시도

이 코드는 다음과 같은 오류를 발생시킵니다.

```bash
error[E0277]: the type `String` cannot be indexed by `{integer}`
 --> src/main.rs:3:13
  |
3 |     let h = s1[0];
  |             ^^^^^ `String` cannot be indexed by `{integer}`
  |
  = help: the trait `Index<{integer}>` is not implemented for
`String`
```

오류와 노트는 그 이유를 설명합니다. Rust 문자열은 인덱싱을 지원하지 않습니다. 하지만 왜 안 될까요? 이 질문에 답하려면 Rust 가 메모리에 문자열을 저장하는 방식을 논의해야 합니다.
