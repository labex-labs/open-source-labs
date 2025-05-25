# 채널과 소유권 이전

소유권 규칙은 안전한 동시성 코드를 작성하는 데 도움이 되므로 메시지 전송에서 중요한 역할을 합니다. 동시 프로그래밍에서 오류를 방지하는 것은 Rust 프로그램 전체에서 소유권을 고려하는 것의 장점입니다. 채널과 소유권이 함께 작동하여 문제를 방지하는 방식을 보여주는 실험을 해보겠습니다. 채널을 통해 전송한 _후_ 스폰된 스레드에서 `val` 값을 사용하려고 시도할 것입니다. Listing 16-9 의 코드를 컴파일하여 이 코드가 허용되지 않는 이유를 확인하십시오.

파일 이름: `src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
        println!("val is {val}");
    });

    let received = rx.recv().unwrap();
    println!("Got: {received}");
}
```

Listing 16-9: 채널을 통해 전송한 후 `val`을 사용하려는 시도

여기서는 `tx.send`를 통해 채널을 통해 전송한 후 `val`을 출력하려고 시도합니다. 이것을 허용하는 것은 좋지 않은 생각입니다. 값이 다른 스레드로 전송되면 해당 스레드가 값을 다시 사용하기 전에 값을 수정하거나 삭제할 수 있습니다. 잠재적으로 다른 스레드의 수정으로 인해 일관성이 없거나 존재하지 않는 데이터로 인해 오류 또는 예기치 않은 결과가 발생할 수 있습니다. 그러나 Listing 16-9 의 코드를 컴파일하려고 하면 Rust 에서 오류가 발생합니다.

```bash
error[E0382]: borrow of moved value: `val`
  --> src/main.rs:10:31
   |
8  |         let val = String::from("hi");
   |             --- move occurs because `val` has type `String`, which does
not implement the `Copy` trait
9  |         tx.send(val).unwrap();
   |                 --- value moved here
10 |         println!("val is {val}");
   |                           ^^^ value borrowed here after move
```

우리의 동시성 실수는 컴파일 시간 오류를 발생시켰습니다. `send` 함수는 매개변수의 소유권을 가져가고, 값이 이동하면 수신자가 소유권을 가져갑니다. 이렇게 하면 전송 후 실수로 값을 다시 사용하는 것을 방지할 수 있습니다. 소유권 시스템은 모든 것이 괜찮은지 확인합니다.
