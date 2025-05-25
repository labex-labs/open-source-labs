# 리터럴 매칭 (Matching Literals)

6 장에서 보았듯이, 리터럴에 대해 패턴을 직접 매칭할 수 있습니다. 다음 코드는 몇 가지 예시를 제공합니다.

파일 이름: `src/main.rs`

```rust
let x = 1;

match x {
    1 => println!("one"),
    2 => println!("two"),
    3 => println!("three"),
    _ => println!("anything"),
}
```

이 코드는 `one`을 출력합니다. 왜냐하면 `x`의 값이 `1`이기 때문입니다. 이 구문은 특정 구체적인 값을 얻을 경우 코드가 작업을 수행하도록 하려는 경우에 유용합니다.
