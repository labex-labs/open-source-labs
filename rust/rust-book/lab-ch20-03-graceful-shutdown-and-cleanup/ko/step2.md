# ThreadPool 에 Drop 트레이트 구현하기

ThreadPool 에 `Drop`을 구현하는 것부터 시작해 봅시다. 풀이 drop 될 때, 스레드는 모두 join 하여 작업을 완료해야 합니다. Listing 20-22 는 `Drop` 구현의 첫 번째 시도를 보여줍니다; 이 코드는 아직 제대로 작동하지 않습니다.

파일 이름: `src/lib.rs`

```rust
impl Drop for ThreadPool {
    fn drop(&mut self) {
      1 for worker in &mut self.workers {
          2 println!("Shutting down worker {}", worker.id);

          3 worker.thread.join().unwrap();
        }
    }
}
```

Listing 20-22: 스레드 풀이 범위를 벗어날 때 각 스레드를 join

먼저 스레드 풀의 각 `workers`를 반복합니다 \[1]. `self`가 가변 참조이므로 `&mut`를 사용하며, `worker`도 변경할 수 있어야 합니다. 각 `worker`에 대해, 이 특정 `Worker` 인스턴스가 종료되고 있음을 알리는 메시지를 출력합니다 \[2], 그런 다음 해당 `Worker` 인스턴스의 스레드에서 `join`을 호출합니다 \[3]. `join` 호출이 실패하면, `unwrap`을 사용하여 Rust 가 패닉 상태로 들어가 graceful shutdown 을 하지 않도록 합니다.

이 코드를 컴파일할 때 발생하는 오류는 다음과 같습니다:

```bash
error[E0507]: cannot move out of `worker.thread` which is behind a mutable
reference
    --> src/lib.rs:52:13
     |
52   |             worker.thread.join().unwrap();
     |             ^^^^^^^^^^^^^ ------ `worker.thread` moved due to this
method call
     |             |
     |             move occurs because `worker.thread` has type
`JoinHandle<()>`, which does not implement the `Copy` trait
     |
note: this function takes ownership of the receiver `self`, which moves
`worker.thread`
```

오류는 각 `worker`에 대한 가변 빌림만 있고 `join`이 인수의 소유권을 가져가기 때문에 `join`을 호출할 수 없다고 알려줍니다. 이 문제를 해결하려면, `join`이 스레드를 소비할 수 있도록 `thread`를 소유하는 `Worker` 인스턴스에서 스레드를 이동해야 합니다. Listing 17-15 에서 이 작업을 수행했습니다: `Worker`가 `Option<thread::JoinHandle<()>>`을 대신 가지고 있다면, `Option`에서 `take` 메서드를 호출하여 값을 `Some` 변형에서 이동시키고 그 자리에 `None` 변형을 남길 수 있습니다. 즉, 실행 중인 `Worker`는 `thread`에 `Some` 변형을 갖게 되며, `Worker`를 정리하려는 경우 `Some`을 `None`으로 대체하여 `Worker`가 실행할 스레드가 없도록 합니다.

따라서 `Worker`의 정의를 다음과 같이 업데이트하려고 합니다:

파일 이름: `src/lib.rs`

```rust
struct Worker {
    id: usize,
    thread: Option<thread::JoinHandle<()>>,
}
```

이제 컴파일러에 의존하여 변경해야 할 다른 위치를 찾아봅시다. 이 코드를 확인하면 두 개의 오류가 발생합니다:

```bash
error[E0599]: no method named `join` found for enum `Option` in the current
scope
  --> src/lib.rs:52:27
   |
52 |             worker.thread.join().unwrap();
   |                           ^^^^ method not found in
`Option<JoinHandle<()>>`

error[E0308]: mismatched types
  --> src/lib.rs:72:22
   |
72 |         Worker { id, thread }
   |                      ^^^^^^ expected enum `Option`, found struct
`JoinHandle`
   |
   = note: expected enum `Option<JoinHandle<()>>`
            found struct `JoinHandle<_>`
help: try wrapping the expression in `Some`
   |
72 |         Worker { id, thread: Some(thread) }
   |                      +++++++++++++      +
```

두 번째 오류부터 해결해 봅시다. 이 오류는 `Worker::new`의 끝 부분에 있는 코드를 가리킵니다; 새로운 `Worker`를 생성할 때 `thread` 값을 `Some`으로 래핑해야 합니다. 이 오류를 수정하려면 다음 변경 사항을 적용하십시오:

파일 이름: `src/lib.rs`

```rust
impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        --snip--

        Worker {
            id,
            thread: Some(thread),
        }
    }
}
```

첫 번째 오류는 `Drop` 구현에 있습니다. 앞서 `Option` 값에서 `take`를 호출하여 `thread`를 `worker`에서 이동시키려고 했습니다. 다음 변경 사항을 통해 이를 수행할 수 있습니다:

파일 이름: `src/lib.rs`

```rust
impl Drop for ThreadPool {
    fn drop(&mut self) {
        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);

          1 if let Some(thread) = worker.thread.take() {
              2 thread.join().unwrap();
            }
        }
    }
}
```

17 장에서 논의했듯이, `Option`의 `take` 메서드는 `Some` 변형을 가져와서 `None`을 그 자리에 남깁니다. `if let`을 사용하여 `Some`을 분해하고 스레드를 가져옵니다 \[1]; 그런 다음 스레드에서 `join`을 호출합니다 \[2]. `Worker` 인스턴스의 스레드가 이미 `None`인 경우, 해당 `Worker`가 이미 스레드를 정리했으므로 이 경우에는 아무 일도 일어나지 않습니다.
