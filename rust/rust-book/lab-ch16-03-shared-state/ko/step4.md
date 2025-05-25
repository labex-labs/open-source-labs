# 여러 스레드 간의 Mutex`<T>` 공유

이제 `Mutex<T>`를 사용하여 여러 스레드 간에 값을 공유해 보겠습니다. 10 개의 스레드를 생성하고 각 스레드가 카운터 값을 1 씩 증가시켜 카운터가 0 에서 10 으로 증가하도록 합니다. Listing 16-13 의 예제는 컴파일러 오류가 발생하며, 해당 오류를 사용하여 `Mutex<T>` 사용에 대해 자세히 알아보고 Rust 가 이를 올바르게 사용하는 데 어떻게 도움을 주는지 알아보겠습니다.

파일 이름: `src/main.rs`

```rust
use std::sync::Mutex;
use std::thread;

fn main() {
  1 let counter = Mutex::new(0);
    let mut handles = vec![];

  2 for _ in 0..10 {
      3 let handle = thread::spawn(move || {
          4 let mut num = counter.lock().unwrap();

          5 *num += 1;
        });
      6 handles.push(handle);
    }

    for handle in handles {
      7 handle.join().unwrap();
    }

  8 println!("Result: {}", *counter.lock().unwrap());
}
```

Listing 16-13: `Mutex<T>`로 보호되는 카운터를 각각 증가시키는 10 개의 스레드

Listing 16-12 에서 했던 것처럼, `Mutex<T>` 내부에 `i32`를 저장하기 위해 `counter` 변수를 생성합니다 \[1\]. 다음으로, 숫자 범위를 반복하여 10 개의 스레드를 생성합니다 \[2\]. `thread::spawn`을 사용하고 모든 스레드에 동일한 클로저를 제공합니다. 이 클로저는 카운터를 스레드로 이동시키고 \[3], `lock` 메서드를 호출하여 `Mutex<T>`에 대한 락을 획득한 다음 \[4], 뮤텍스 내의 값에 1 을 더합니다 \[5]. 스레드가 클로저 실행을 마치면 `num`이 스코프를 벗어나 락을 해제하여 다른 스레드가 락을 획득할 수 있습니다.

메인 스레드에서 모든 join handle 을 수집합니다 \[6\]. 그런 다음, Listing 16-2 에서 했던 것처럼, 모든 스레드가 완료되도록 각 handle 에 대해 `join`을 호출합니다 \[7\]. 그 시점에서 메인 스레드는 락을 획득하고 이 프로그램의 결과를 출력합니다 \[8\].

이 예제가 컴파일되지 않을 것이라고 암시했습니다. 이제 그 이유를 알아봅시다!

```bash
error[E0382]: use of moved value: `counter`
  --> src/main.rs:9:36
   |
5  |     let counter = Mutex::new(0);
   |         ------- move occurs because `counter` has type `Mutex<i32>`, which
does not implement the `Copy` trait
...
9  |         let handle = thread::spawn(move || {
   |                                    ^^^^^^^ value moved into closure here,
in previous iteration of loop
10 |             let mut num = counter.lock().unwrap();
   |                           ------- use occurs due to use in closure
```

오류 메시지는 `counter` 값이 루프의 이전 반복에서 이동되었다고 명시합니다. Rust 는 락 `counter`의 소유권을 여러 스레드로 이동할 수 없다고 알려줍니다. 15 장에서 논의한 다중 소유권 방법을 사용하여 컴파일러 오류를 수정해 보겠습니다.
