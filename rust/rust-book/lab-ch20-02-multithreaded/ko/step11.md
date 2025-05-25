# execute 메서드 구현하기

마침내 `ThreadPool`에서 `execute` 메서드를 구현해 보겠습니다. 또한 `Job`을 구조체에서 `execute`가 받는 클로저의 타입을 보유하는 트레이트 객체에 대한 타입 별칭으로 변경합니다. "타입 별칭으로 타입 동의어 만들기"에서 설명했듯이, 타입 별칭을 사용하면 긴 타입을 사용 편의성을 위해 더 짧게 만들 수 있습니다. Listing 20-19 를 살펴보세요.

파일 이름: `src/lib.rs`

```rust
--snip--

type Job = Box<dyn FnOnce() + Send + 'static>;

impl ThreadPool {
    --snip--

    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
      1 let job = Box::new(f);

      2 self.sender.send(job).unwrap();
    }
}

--snip--
```

Listing 20-19: 각 클로저를 보유하는 `Box`에 대한 `Job` 타입 별칭을 생성한 다음 채널을 통해 작업을 전송하기

`execute`에서 얻는 클로저를 사용하여 새 `Job` 인스턴스를 생성한 후 \[1], 해당 작업을 채널의 전송 끝으로 보냅니다 \[2]. 전송에 실패하는 경우를 대비하여 `send`에 대해 `unwrap`을 호출하고 있습니다. 예를 들어, 모든 스레드의 실행을 중지하면 수신 끝이 새 메시지 수신을 중지하는 경우에 발생할 수 있습니다. 현재, 스레드의 실행을 중지할 수 없습니다. 풀이 존재하는 한 스레드는 계속 실행됩니다. `unwrap`을 사용하는 이유는 실패 사례가 발생하지 않는다는 것을 알고 있지만 컴파일러는 이를 알지 못하기 때문입니다.

하지만 아직 다 끝나지 않았습니다! `Worker`에서 `thread::spawn`에 전달되는 클로저는 여전히 채널의 수신 끝을 *참조*할 뿐입니다. 대신, 클로저가 영원히 루프를 돌면서 채널의 수신 끝에 작업을 요청하고 작업을 받으면 실행해야 합니다. Listing 20-20 에 표시된 변경 사항을 `Worker::new`에 적용해 보겠습니다.

파일 이름: `src/lib.rs`

```rust
--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || loop {
            let job = receiver
              1 .lock()
              2 .unwrap()
              3 .recv()
              4 .unwrap();

            println!("Worker {id} got a job; executing.");

            job();
        });

        Worker { id, thread }
    }
}
```

Listing 20-20: `Worker` 인스턴스의 스레드에서 작업 수신 및 실행

여기서는 먼저 `receiver`에서 `lock`을 호출하여 뮤텍스를 획득하고 \[1], 오류가 발생하면 `unwrap`을 호출하여 패닉합니다 \[2]. 뮤텍스를 획득하는 데 실패할 수 있습니다. 뮤텍스가 _poisoned_ 상태인 경우, 즉 다른 스레드가 잠금을 해제하는 대신 잠금을 유지한 채 패닉한 경우에 발생할 수 있습니다. 이 상황에서는 `unwrap`을 호출하여 이 스레드가 패닉하도록 하는 것이 올바른 조치입니다. 이 `unwrap`을 원하는 의미의 오류 메시지가 있는 `expect`로 자유롭게 변경할 수 있습니다.

뮤텍스에 대한 잠금을 얻으면 `recv`를 호출하여 채널에서 `Job`을 수신합니다 \[3]. 마지막 `unwrap`은 여기에서도 모든 오류를 지나갑니다 \[4]. 이는 발신자를 보유한 스레드가 종료된 경우 발생할 수 있으며, 수신자가 종료되면 `send` 메서드가 `Err`를 반환하는 방식과 유사합니다.

`recv` 호출은 차단되므로, 아직 작업이 없으면 현재 스레드는 작업이 사용 가능해질 때까지 대기합니다. `Mutex<T>`는 한 번에 하나의 `Worker` 스레드만 작업을 요청하도록 보장합니다.

이제 스레드 풀이 작동 상태입니다! `cargo run`을 실행하고 몇 가지 요청을 해보세요.

```bash
[object Object]
```

성공! 이제 연결을 비동기적으로 실행하는 스레드 풀이 있습니다. 4 개 이상의 스레드가 생성되지 않으므로 서버가 많은 요청을 받더라도 시스템이 과부하되지 않습니다. */sleep*에 대한 요청을 하면 서버는 다른 스레드가 실행하도록 하여 다른 요청을 처리할 수 있습니다.

> 참고: 여러 브라우저 창에서 동시에 */sleep*을 열면 5 초 간격으로 한 번에 하나씩 로드될 수 있습니다. 일부 웹 브라우저는 캐싱을 위해 동일한 요청의 여러 인스턴스를 순차적으로 실행합니다. 이 제한은 웹 서버로 인해 발생하는 것이 아닙니다.

18 장에서 `while let` 루프에 대해 배우고 나면 Listing 20-21 과 같이 `Worker` 스레드 코드를 작성하지 않은 이유가 궁금할 수 있습니다.

파일 이름: `src/lib.rs`

```rust
--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || {
            while let Ok(job) = receiver.lock().unwrap().recv() {
                println!("Worker {id} got a job; executing.");

                job();
            }
        });

        Worker { id, thread }
    }
}
```

Listing 20-21: `while let`을 사용하는 `Worker::new`의 대체 구현

이 코드는 컴파일되고 실행되지만 원하는 스레딩 동작이 발생하지 않습니다. 느린 요청은 다른 요청이 처리될 때까지 대기하게 합니다. 그 이유는 다소 미묘합니다. `Mutex` 구조체에는 공개된 `unlock` 메서드가 없습니다. 잠금의 소유권은 `lock` 메서드가 반환하는 `LockResult<MutexGuard<T>>` 내의 `MutexGuard<T>`의 수명에 기반하기 때문입니다. 컴파일 시, borrow checker 는 `Mutex`로 보호되는 리소스는 잠금을 보유하지 않는 한 액세스할 수 없다는 규칙을 적용할 수 있습니다. 그러나 이 구현은 `MutexGuard<T>`의 수명을 염두에 두지 않으면 의도보다 더 오래 잠금이 유지될 수도 있습니다.

`let job = receiver.lock().unwrap().recv().unwrap();`를 사용하는 Listing 20-20 의 코드는 `let`을 사용하면 등호 오른쪽에 있는 표현식에서 사용된 모든 임시 값이 `let` 문이 종료될 때 즉시 삭제되기 때문에 작동합니다. 그러나 `while let`(및 `if let` 및 `match`) 은 연결된 블록이 끝날 때까지 임시 값을 삭제하지 않습니다. Listing 20-21 에서 잠금은 `job()` 호출 기간 동안 유지되므로 다른 `Worker` 인스턴스는 작업을 수신할 수 없습니다.
