# 채널

Rust 는 스레드 간 통신을 위한 비동기 `채널`을 제공합니다. 채널은 두 개의 엔드포인트, `Sender`와 `Receiver` 사이에 정보의 단방향 흐름을 허용합니다.

```rust
use std::sync::mpsc::{Sender, Receiver};
use std::sync::mpsc;
use std::thread;

static NTHREADS: i32 = 3;

fn main() {
    // 채널은 두 개의 엔드포인트 `Sender<T>` 와 `Receiver<T>` 를 가지며,
    // 여기서 `T` 는 전송될 메시지의 타입입니다.
    // (타입 주석은 불필요합니다)
    let (tx, rx): (Sender<i32>, Receiver<i32>) = mpsc::channel();
    let mut children = Vec::new();

    for id in 0..NTHREADS {
        // sender 엔드포인트는 복사될 수 있습니다.
        let thread_tx = tx.clone();

        // 각 스레드는 채널을 통해 자신의 id 를 전송합니다.
        let child = thread::spawn(move || {
            // 스레드는 `thread_tx` 의 소유권을 갖습니다.
            // 각 스레드는 채널에 메시지를 큐에 넣습니다.
            thread_tx.send(id).unwrap();

            // 전송은 블록킹되지 않는 작업이므로, 스레드는 메시지를 전송한 직후 즉시 계속됩니다.
            println!("스레드 {} 완료", id);
        });

        children.push(child);
    }

    // 여기서 모든 메시지가 수집됩니다.
    let mut ids = Vec::with_capacity(NTHREADS as usize);
    for _ in 0..NTHREADS {
        // `recv` 메서드는 채널에서 메시지를 가져옵니다.
        // `recv` 는 사용 가능한 메시지가 없으면 현재 스레드를 블록합니다.
        ids.push(rx.recv());
    }

    // 스레드가 남은 작업을 완료할 때까지 기다립니다.
    for child in children {
        child.join().expect("oops! 자식 스레드가 패닉했습니다.");
    }

    // 메시지가 전송된 순서를 보여줍니다.
    println!("{:?}", ids);
}
```
