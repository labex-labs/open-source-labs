# 송신자를 복제하여 여러 생산자 생성

앞서 `mpsc`가 *multiple producer, single consumer*의 약자라고 언급했습니다. Listing 16-10 의 코드를 확장하여 `mpsc`를 사용하고, 동일한 수신자에게 값을 전송하는 여러 스레드를 생성해 보겠습니다. Listing 16-11 과 같이 송신자를 복제하여 수행할 수 있습니다.

파일 이름: `src/main.rs`

```rust
--snip--

let (tx, rx) = mpsc::channel();

let tx1 = tx.clone();
thread::spawn(move || {
    let vals = vec![
        String::from("hi"),
        String::from("from"),
        String::from("the"),
        String::from("thread"),
    ];

    for val in vals {
        tx1.send(val).unwrap();
        thread::sleep(Duration::from_secs(1));
    }
});

thread::spawn(move || {
    let vals = vec![
        String::from("more"),
        String::from("messages"),
        String::from("for"),
        String::from("you"),
    ];

    for val in vals {
        tx.send(val).unwrap();
        thread::sleep(Duration::from_secs(1));
    }
});

for received in rx {
    println!("Got: {received}");
}

--snip--
```

Listing 16-11: 여러 생산자로부터 여러 메시지 전송

이번에는 첫 번째 스폰된 스레드를 생성하기 전에 송신자에 대해 `clone`을 호출합니다. 이렇게 하면 첫 번째 스폰된 스레드에 전달할 수 있는 새로운 송신자가 생성됩니다. 원래 송신자는 두 번째 스폰된 스레드에 전달합니다. 이렇게 하면 각 스레드가 서로 다른 메시지를 하나의 수신자에게 전송하는 두 개의 스레드가 생성됩니다.

코드를 실행하면 다음과 같은 출력이 표시됩니다.

    Got: hi
    Got: more
    Got: from
    Got: messages
    Got: for
    Got: the
    Got: thread
    Got: you

시스템에 따라 다른 순서로 값이 표시될 수 있습니다. 이것이 동시성을 흥미롭게 만들고 어렵게 만드는 이유입니다. `thread::sleep`을 실험하여 서로 다른 스레드에 다양한 값을 제공하면 각 실행이 더욱 비결정적이며 매번 다른 출력을 생성합니다.

이제 채널이 어떻게 작동하는지 살펴보았으므로 다른 동시성 방법을 살펴보겠습니다.
