# 중첩 및 레이블

중첩된 루프를 다룰 때 외부 루프를 `break` 또는 `continue`하는 것이 가능합니다. 이러한 경우 루프는 특정 `'레이블`로 주석 처리되어야 하며, `break`/`continue` 문에 레이블이 전달되어야 합니다.

```rust
#![allow(unreachable_code)]

fn main() {
    'outer: loop {
        println!("외부 루프 진입");

        'inner: loop {
            println!("내부 루프 진입");

            // 이것은 내부 루프만 중단합니다.
            //break;

            // 이것은 외부 루프를 중단합니다.
            break 'outer;
        }

        println!("이 지점은 절대 도달하지 않습니다.");
    }

    println!("외부 루프 종료");
}
```
