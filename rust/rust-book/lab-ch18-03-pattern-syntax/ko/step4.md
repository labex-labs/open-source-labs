# 다중 패턴 (Multiple Patterns)

`match` 표현식에서 패턴 _or_ 연산자인 `|` 구문을 사용하여 여러 패턴을 매칭할 수 있습니다. 예를 들어, 다음 코드에서 `x`의 값을 match arm 과 비교하는데, 첫 번째 arm 은 _or_ 옵션을 가지고 있습니다. 즉, `x`의 값이 해당 arm 의 값 중 하나와 일치하면 해당 arm 의 코드가 실행됩니다.

파일 이름: `src/main.rs`

```rust
let x = 1;

match x {
    1 | 2 => println!("one or two"),
    3 => println!("three"),
    _ => println!("anything"),
}
```

이 코드는 `one or two`를 출력합니다.
