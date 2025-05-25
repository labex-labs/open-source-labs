# 여러 값 전송 및 수신 대기 확인

Listing 16-8 의 코드는 컴파일되고 실행되었지만 두 개의 별도 스레드가 채널을 통해 서로 통신하고 있다는 것을 명확하게 보여주지 않았습니다. Listing 16-10 에서는 Listing 16-8 의 코드가 동시적으로 실행되고 있음을 증명할 수 있도록 몇 가지 수정을 했습니다. 이제 스폰된 스레드는 여러 메시지를 전송하고 각 메시지 사이에 1 초 동안 일시 중지됩니다.

파일 이름: `src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("thread"),
        ];

        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

    for received in rx {
        println!("Got: {received}");
    }
}
```

Listing 16-10: 여러 메시지를 전송하고 각 메시지 사이에 일시 중지

이번에는 스폰된 스레드에 메인 스레드로 전송하려는 문자열 벡터가 있습니다. 각 문자열을 개별적으로 전송하면서 반복하고, `Duration` 값이 1 초인 `thread::sleep` 함수를 호출하여 각 문자열 사이에 일시 중지합니다.

메인 스레드에서는 더 이상 `recv` 함수를 명시적으로 호출하지 않습니다. 대신 `rx`를 반복자 (iterator) 로 취급하고 있습니다. 수신된 각 값에 대해 출력하고 있습니다. 채널이 닫히면 반복이 종료됩니다.

Listing 16-10 의 코드를 실행하면 각 줄 사이에 1 초의 일시 중지가 있는 다음 출력을 볼 수 있습니다.

    Got: hi
    Got: from
    Got: the
    Got: thread

메인 스레드의 `for` 루프에 일시 중지하거나 지연하는 코드가 없으므로 메인 스레드가 스폰된 스레드에서 값을 수신하기를 기다리고 있음을 알 수 있습니다.
