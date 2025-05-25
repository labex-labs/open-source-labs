# spawn 을 사용하여 새로운 스레드 생성

새로운 스레드를 생성하려면 `thread::spawn` 함수를 호출하고, 새로운 스레드에서 실행하려는 코드를 포함하는 클로저 (closure, 13 장에서 클로저에 대해 이야기했습니다) 를 전달합니다. Listing 16-1 의 예제는 메인 스레드 (main thread) 에서 텍스트를 출력하고, 새로운 스레드에서 다른 텍스트를 출력합니다.

파일 이름: `src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }
}
```

Listing 16-1: 메인 스레드가 다른 것을 출력하는 동안 새로운 스레드를 생성하여 한 가지를 출력

Rust 프로그램의 메인 스레드가 완료되면, 생성된 모든 스레드는 실행이 완료되었는지 여부에 관계없이 종료됩니다. 이 프로그램의 출력은 매번 약간 다를 수 있지만, 다음과 유사하게 보일 것입니다.

    hi number 1 from the main thread!
    hi number 1 from the spawned thread!
    hi number 2 from the main thread!
    hi number 2 from the spawned thread!
    hi number 3 from the main thread!
    hi number 3 from the spawned thread!
    hi number 4 from the main thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!

`thread::sleep`에 대한 호출은 스레드가 짧은 시간 동안 실행을 중지하도록 하여 다른 스레드가 실행되도록 합니다. 스레드는 아마도 번갈아 가며 실행될 것이지만, 이는 보장되지 않습니다. 이는 운영 체제가 스레드를 어떻게 스케줄링하는지에 달려 있습니다. 이 실행에서 메인 스레드가 먼저 출력되었는데, 이는 생성된 스레드의 print 문이 코드에서 먼저 나타났음에도 불구하고 그렇습니다. 그리고 생성된 스레드에 `i`가 9 가 될 때까지 출력하도록 지시했지만, 메인 스레드가 종료되기 전에 5 까지만 출력되었습니다.

이 코드를 실행하고 메인 스레드의 출력만 보거나, 겹치는 부분이 전혀 보이지 않는다면, 운영 체제가 스레드 간에 전환할 수 있는 더 많은 기회를 만들기 위해 범위의 숫자를 늘려보세요.
