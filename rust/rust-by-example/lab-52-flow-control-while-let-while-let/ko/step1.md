# while let

`if let`과 유사하게 `while let`은 번거로운 `match` 문열을 더 쉽게 처리할 수 있도록 합니다. 다음은 `i`를 증가시키는 예시입니다.

```rust
// `optional` 을 `Option<i32>` 타입으로 만듭니다.
let mut optional = Some(0);

// 반복적으로 테스트합니다.
loop {
    match optional {
        // 만약 `optional` 이 분해되면, 블록을 평가합니다.
        Some(i) => {
            if i > 9 {
                println!("9 보다 크므로 종료!");
                optional = None;
            } else {
                println!("`i` 는 `{:?}` 입니다. 다시 시도합니다.", i);
                optional = Some(i + 1);
            }
            // ^ 3 개의 들여쓰기가 필요합니다!
        },
        // 분해에 실패하면 루프를 종료합니다.
        _ => { break; }
        // ^ 왜 이렇게 해야 할까요? 더 나은 방법이 있어야 합니다!
    }
}
```

`while let`을 사용하면 이 코드를 훨씬 더 간결하게 작성할 수 있습니다.

```rust
fn main() {
    // `optional` 을 `Option<i32>` 타입으로 만듭니다.
    let mut optional = Some(0);

    // 이 코드는 " `optional` 을 `Some(i)` 로 분해할 때까지 블록 (`{}`) 을 평가하고, 그렇지 않으면 `break` 합니다."를 의미합니다.
    while let Some(i) = optional {
        if i > 9 {
            println!("9 보다 크므로 종료!");
            optional = None;
        } else {
            println!("`i` 는 `{:?}` 입니다. 다시 시도합니다.", i);
            optional = Some(i + 1);
        }
        // ^ 오른쪽으로의 들여쓰기가 줄어들고, 실패하는 경우를 명시적으로 처리할 필요가 없습니다.
    }
    // ^ `if let`에는 추가적인 `else`/`else if` 절이 있었습니다. `while let`에는 이러한 절이 없습니다.
}
```
