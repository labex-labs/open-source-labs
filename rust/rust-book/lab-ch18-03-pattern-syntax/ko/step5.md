# `..=`를 사용한 값 범위 매칭 (Matching Ranges of Values with ..=)

`..=` 구문을 사용하면 포함 범위 (inclusive range) 의 값과 매칭할 수 있습니다. 다음 코드에서 패턴이 주어진 범위 내의 값 중 하나와 일치하면 해당 arm 이 실행됩니다.

파일 이름: `src/main.rs`

```rust
let x = 5;

match x {
    1..=5 => println!("one through five"),
    _ => println!("something else"),
}
```

`x`가 `1`, `2`, `3`, `4`, 또는 `5`이면 첫 번째 arm 이 일치합니다. 이 구문은 동일한 아이디어를 표현하기 위해 `|` 연산자를 사용하는 것보다 여러 매칭 값에 더 편리합니다. `|`를 사용하려면 `1 | 2 | 3 | 4 | 5`를 지정해야 합니다. 범위를 지정하는 것은 특히 1 에서 1,000 사이의 모든 숫자를 매칭하려는 경우 훨씬 더 짧습니다!

컴파일러는 컴파일 시간에 범위가 비어 있지 않은지 확인하며, Rust 가 범위가 비어 있는지 여부를 알 수 있는 유일한 유형은 `char` 및 숫자 값이므로 범위는 숫자 또는 `char` 값에만 허용됩니다.

다음은 `char` 값의 범위를 사용하는 예입니다.

파일 이름: `src/main.rs`

```rust
let x = 'c';

match x {
    'a'..='j' => println!("early ASCII letter"),
    'k'..='z' => println!("late ASCII letter"),
    _ => println!("something else"),
}
```

Rust 는 `'c'`가 첫 번째 패턴의 범위 내에 있음을 알고 `early ASCII letter`를 출력합니다.
