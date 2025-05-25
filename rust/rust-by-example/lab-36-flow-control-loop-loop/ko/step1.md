# loop

Rust 는 무한 루프를 나타내기 위해 `loop` 키워드를 제공합니다.

`break` 문은 언제든지 루프를 종료하는 데 사용할 수 있으며, `continue` 문은 반복의 나머지 부분을 건너뛰고 새로운 반복을 시작하는 데 사용할 수 있습니다.

```rust
fn main() {
    let mut count = 0u32;

    println!("무한까지 세봅시다!");

    // 무한 루프
    loop {
        count += 1;

        if count == 3 {
            println!("세");

            // 이 반복의 나머지 부분 건너뛰기
            continue;
        }

        println!("{}", count);

        if count == 5 {
            println!("됐습니다.");

            // 이 루프 종료
            break;
        }
    }
}
```
