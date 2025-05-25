# 여러 스레드를 사용한 다중 소유권

15 장에서, 참조 카운트 값을 생성하기 위해 스마트 포인터 `Rc<T>`를 사용하여 여러 소유자에게 값을 제공했습니다. 여기서도 동일하게 수행하고 어떤 일이 발생하는지 살펴보겠습니다. Listing 16-14 에서 `Mutex<T>`를 `Rc<T>`로 래핑하고 소유권을 스레드로 이동하기 전에 `Rc<T>`를 복제합니다.

파일 이름: `src/main.rs`

```rust
use std::rc::Rc;
use std::sync::Mutex;
use std::thread;

fn main() {
    let counter = Rc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Rc::clone(&counter);
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

Listing 16-14: 여러 스레드가 `Mutex<T>`를 소유하도록 허용하기 위해 `Rc<T>`를 사용하려는 시도

다시 한 번, 컴파일하면... 다른 오류가 발생합니다! 컴파일러는 우리에게 많은 것을 가르쳐주고 있습니다.

```bash
error[E0277]: `Rc<Mutex<i32>>` cannot be sent between threads safely 1
   --> src/main.rs:11:22
    |
11  |           let handle = thread::spawn(move || {
    |  ______________________^^^^^^^^^^^^^_-
    | |                      |
    | |                      `Rc<Mutex<i32>>` cannot be sent between threads
safely
12  | |             let mut num = counter.lock().unwrap();
13  | |
14  | |             *num += 1;
15  | |         });
    | |_________- within this `[closure@src/main.rs:11:36: 15:10]`
    |
= help: within `[closure@src/main.rs:11:36: 15:10]`, the trait `Send` is not
implemented for `Rc<Mutex<i32>>` 2
    = note: required because it appears within the type
`[closure@src/main.rs:11:36: 15:10]`
note: required by a bound in `spawn`
```

와, 오류 메시지가 매우 장황합니다! 여기서 집중해야 할 중요한 부분은 ``Rc<Mutex<i32>>`는 스레드 간에 안전하게 전송될 수 없습니다`\[1]입니다. 컴파일러는 그 이유도 알려줍니다:`트레이트 `Send`가 `Rc<Mutex<i32>>`에 대해 구현되지 않았습니다`\[2]. 다음 섹션에서`Send`에 대해 이야기하겠습니다. 이는 스레드와 함께 사용하는 타입이 동시 상황에서 사용되도록 보장하는 트레이트 중 하나입니다.

불행히도, `Rc<T>`는 스레드 간에 공유하는 것이 안전하지 않습니다. `Rc<T>`가 참조 카운트를 관리할 때, `clone`을 호출할 때마다 카운트에 추가하고 각 복제가 삭제될 때 카운트에서 뺍니다. 그러나 다른 스레드에 의해 카운트 변경이 중단되지 않도록 하기 위해 어떤 동시성 기본 요소를 사용하지 않습니다. 이는 잘못된 카운트, 즉 메모리 누수 또는 완료되기 전에 값이 삭제되는 미묘한 버그로 이어질 수 있습니다. 우리에게 필요한 것은 `Rc<T>`와 정확히 같지만 스레드 안전 방식으로 참조 카운트를 변경하는 타입입니다.
