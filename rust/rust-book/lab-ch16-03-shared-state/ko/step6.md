# Arc`<T>`를 사용한 원자적 참조 카운팅

다행히도, `Arc<T>`는 동시 상황에서 사용하기 안전한 `Rc<T>`와 같은 타입입니다. *a*는 _atomic_(원자적) 을 의미하며, 이는 _atomically reference counted_(원자적으로 참조 카운팅된) 타입임을 의미합니다. 원자성은 여기서 자세히 다루지 않을 추가적인 종류의 동시성 기본 요소입니다. 자세한 내용은 `std::sync::atomic`에 대한 표준 라이브러리 문서를 참조하십시오. 이 시점에서, 원자성이 기본 타입처럼 작동하지만 스레드 간에 공유하는 것이 안전하다는 것만 알면 됩니다.

그렇다면 왜 모든 기본 타입이 원자성이 아니고, 표준 라이브러리 타입이 기본적으로 `Arc<T>`를 사용하도록 구현되지 않는지 궁금할 것입니다. 그 이유는 스레드 안전성이 실제로 필요할 때만 지불하고 싶은 성능 저하를 수반하기 때문입니다. 단일 스레드 내에서 값에 대한 연산만 수행하는 경우, 원자성이 제공하는 보장을 강제할 필요가 없으면 코드가 더 빠르게 실행될 수 있습니다.

예제로 돌아가 보겠습니다: `Arc<T>`와 `Rc<T>`는 동일한 API 를 가지므로, `use` 줄, `new` 호출 및 `clone` 호출을 변경하여 프로그램을 수정합니다. Listing 16-15 의 코드는 마침내 컴파일되고 실행됩니다.

파일 이름: `src/main.rs`

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();

            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Result: {}", *counter.lock().unwrap());
}
```

Listing 16-15: 여러 스레드 간에 소유권을 공유할 수 있도록 `Mutex<T>`를 래핑하기 위해 `Arc<T>` 사용

이 코드는 다음을 출력합니다.

```rust
Result: 10
```

해냈습니다! 0 에서 10 까지 세었습니다. 그다지 인상적이지 않을 수 있지만, `Mutex<T>`와 스레드 안전성에 대해 많은 것을 배웠습니다. 또한 이 프로그램의 구조를 사용하여 카운터를 증가시키는 것보다 더 복잡한 작업을 수행할 수 있습니다. 이 전략을 사용하면 계산을 독립적인 부분으로 나누고, 해당 부분을 스레드로 분할한 다음, `Mutex<T>`를 사용하여 각 스레드가 최종 결과를 해당 부분으로 업데이트할 수 있습니다.

단순한 숫자 연산을 수행하는 경우, 표준 라이브러리의 `std::sync::atomic` 모듈에서 제공하는 `Mutex<T>` 타입보다 간단한 타입이 있습니다. 이러한 타입은 기본 타입에 대한 안전하고 동시적인 원자적 접근을 제공합니다. 이 예제에서는 `Mutex<T>`가 어떻게 작동하는지에 집중할 수 있도록 기본 타입과 함께 `Mutex<T>`를 사용하기로 했습니다.
