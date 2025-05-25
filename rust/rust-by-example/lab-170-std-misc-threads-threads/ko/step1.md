# 스레드

Rust 는 `spawn` 함수를 통해 네이티브 OS 스레드를 생성하는 메커니즘을 제공하며, 이 함수의 인수는 이동 가능한 클로저입니다.

```rust
use std::thread;

const NTHREADS: u32 = 10;

// 이것은 `main` 스레드입니다.
fn main() {
    // 생성된 자식 스레드를 저장할 벡터를 만듭니다.
    let mut children = vec![];

    for i in 0..NTHREADS {
        // 다른 스레드를 시작합니다.
        children.push(thread::spawn(move || {
            println!("이것은 스레드 번호 {}입니다", i);
        }));
    }

    for child in children {
        // 스레드가 완료될 때까지 기다립니다. 결과를 반환합니다.
        let _ = child.join();
    }
}
```

이러한 스레드는 OS 에 의해 스케줄링됩니다.
