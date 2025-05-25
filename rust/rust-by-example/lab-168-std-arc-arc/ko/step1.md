# Arc

스레드 간 공유 소유가 필요한 경우 `Arc`(Atomically Reference Counted) 를 사용할 수 있습니다. 이 구조체는 `Clone` 구현을 통해 메모리 힙에 있는 값의 위치에 대한 참조 포인터를 생성하고 참조 카운터를 증가시킵니다. 스레드 간에 소유권을 공유하기 때문에 값에 대한 마지막 참조 포인터가 범위를 벗어나면 변수가 삭제됩니다.

```rust
use std::time::Duration;
use std::sync::Arc;
use std::thread;

fn main() {
    // 이 변수 선언 부분에서 값이 지정됩니다.
    let apple = Arc::new("the same apple");

    for _ in 0..10 {
        // 여기서는 메모리 힙의 참조를 가리키는 포인터이므로 값이 지정되지 않습니다.
        let apple = Arc::clone(&apple);

        thread::spawn(move || {
            // Arc 가 사용되었으므로 Arc 변수 포인터의 위치에 할당된 값을 사용하여 스레드를 생성할 수 있습니다.
            println!("{:?}", apple);
        });
    }

    // 생성된 모든 스레드에서 Arc 인스턴스가 출력되도록 합니다.
    thread::sleep(Duration::from_secs(1));
}
```
