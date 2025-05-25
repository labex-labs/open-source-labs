# 스레드에게 작업 수신 중단을 알리기

우리가 변경한 모든 사항으로 인해, 코드는 경고 없이 컴파일됩니다. 하지만, 좋지 않은 소식은 이 코드가 아직 원하는 방식으로 작동하지 않는다는 것입니다. 핵심은 `Worker` 인스턴스의 스레드에서 실행되는 클로저의 로직입니다: 현재, `join`을 호출하지만, 스레드는 영원히 작업을 찾기 위해 `loop`하므로 종료되지 않습니다. 현재 `drop` 구현으로 `ThreadPool`을 drop 하려고 하면, 메인 스레드는 첫 번째 스레드가 완료될 때까지 영원히 블록됩니다.

이 문제를 해결하려면, `ThreadPool` `drop` 구현을 변경한 다음 `Worker` 루프를 변경해야 합니다.

먼저, 스레드가 완료될 때까지 기다리기 전에 `sender`를 명시적으로 drop 하도록 `ThreadPool` `drop` 구현을 변경합니다. Listing 20-23 은 `sender`를 명시적으로 drop 하도록 `ThreadPool`에 대한 변경 사항을 보여줍니다. `sender`를 `ThreadPool`에서 이동할 수 있도록 스레드에서 사용했던 것과 동일한 `Option` 및 `take` 기술을 사용합니다.

파일 이름: `src/lib.rs`

```rust
pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: Option<mpsc::Sender<Job>>,
}
--snip--
impl ThreadPool {
    pub fn new(size: usize) -> ThreadPool {
        --snip--

        ThreadPool {
            workers,
            sender: Some(sender),
        }
    }

    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
        let job = Box::new(f);

        self.sender
            .as_ref()
            .unwrap()
            .send(job)
            .unwrap();
    }
}

impl Drop for ThreadPool {
    fn drop(&mut self) {
      1 drop(self.sender.take());

        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);

            if let Some(thread) = worker.thread.take() {
                thread.join().unwrap();
            }
        }
    }
}
```

Listing 20-23: `Worker` 스레드를 join 하기 전에 `sender`를 명시적으로 drop

`sender`를 drop \[1]하면 채널이 닫히고, 더 이상 메시지가 전송되지 않음을 나타냅니다. 그렇게 되면, `Worker` 인스턴스가 무한 루프에서 수행하는 모든 `recv` 호출은 오류를 반환합니다. Listing 20-24 에서, `Worker` 루프를 변경하여 해당 경우에 루프를 graceful 하게 종료합니다. 즉, `ThreadPool` `drop` 구현이 스레드에서 `join`을 호출할 때 스레드가 완료됩니다.

파일 이름: `src/lib.rs`

```rust
impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || loop {
            let message = receiver.lock().unwrap().recv();

            match message {
                Ok(job) => {
                    println!(
                        "Worker {id} got a job; executing."
                    );

                    job();
                }
                Err(_) => {
                    println!(
                        "Worker {id} shutting down."
                    );
                    break;
                }
            }
        });

        Worker {
            id,
            thread: Some(thread),
        }
    }
}
```

Listing 20-24: `recv`가 오류를 반환할 때 루프에서 명시적으로 break

이 코드가 작동하는 것을 보기 위해, Listing 20-25 에 표시된 대로 서버를 graceful 하게 종료하기 전에 두 개의 요청만 수락하도록 `main`을 수정해 보겠습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
    let pool = ThreadPool::new(4);

    for stream in listener.incoming().take(2) {
        let stream = stream.unwrap();

        pool.execute(|| {
            handle_connection(stream);
        });
    }

    println!("Shutting down.");
}
```

Listing 20-25: 루프를 종료하여 두 개의 요청을 처리한 후 서버 종료

실제 웹 서버가 두 개의 요청만 처리한 후 종료되도록 하지는 않을 것입니다. 이 코드는 graceful shutdown 및 정리가 제대로 작동하는 것을 보여줍니다.

`take` 메서드는 `Iterator` 트레이트에 정의되어 있으며, 반복을 처음 두 항목으로 제한합니다. `ThreadPool`은 `main`의 끝에서 범위를 벗어나고, `drop` 구현이 실행됩니다.

`cargo run`으로 서버를 시작하고 세 개의 요청을 보냅니다. 세 번째 요청은 오류가 발생해야 하며, 터미널에서 다음과 유사한 출력을 볼 수 있습니다:

```bash
$ cargo run
   Compiling hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 1.0s
     Running `target/debug/hello`
Worker 0 got a job; executing.
Shutting down.
Shutting down worker 0
Worker 3 got a job; executing.
Worker 1 disconnected; shutting down.
Worker 2 disconnected; shutting down.
Worker 3 disconnected; shutting down.
Worker 0 disconnected; shutting down.
Shutting down worker 1
Shutting down worker 2
Shutting down worker 3
```

`Worker` ID 와 메시지가 다른 순서로 출력될 수 있습니다. 메시지에서 이 코드가 어떻게 작동하는지 확인할 수 있습니다: `Worker` 인스턴스 0 과 3 이 처음 두 개의 요청을 받았습니다. 서버는 두 번째 연결 후 연결 수락을 중단하고, `ThreadPool`의 `Drop` 구현은 `Worker` 3 이 작업을 시작하기도 전에 실행을 시작합니다. `sender`를 drop 하면 모든 `Worker` 인스턴스가 연결 해제되고 종료하라는 지시를 받습니다. `Worker` 인스턴스는 연결 해제될 때 각각 메시지를 출력한 다음, 스레드 풀은 `join`을 호출하여 각 `Worker` 스레드가 완료될 때까지 기다립니다.

이 특정 실행의 한 가지 흥미로운 측면에 주목하십시오: `ThreadPool`은 `sender`를 drop 했고, 어떤 `Worker`도 오류를 받기 전에 `Worker` 0 을 join 하려고 했습니다. `Worker` 0 은 아직 `recv`에서 오류를 받지 못했으므로, 메인 스레드는 `Worker` 0 이 완료될 때까지 블록되었습니다. 그동안, `Worker` 3 은 작업을 받았고, 그 다음 모든 스레드가 오류를 받았습니다. `Worker` 0 이 완료되면, 메인 스레드는 나머지 `Worker` 인스턴스가 완료될 때까지 기다렸습니다. 그 시점에서, 그들은 모두 루프를 종료하고 중단했습니다.

축하합니다! 이제 프로젝트를 완료했습니다; 비동기적으로 응답하기 위해 스레드 풀을 사용하는 기본 웹 서버가 있습니다. 서버의 graceful shutdown 을 수행할 수 있으며, 이는 풀의 모든 스레드를 정리합니다. 이 장의 전체 코드를 참조하려면 *https://www.nostarch.com/Rust2021*을 참조하십시오.

여기서 더 많은 작업을 수행할 수 있습니다! 이 프로젝트를 계속 개선하려면, 다음과 같은 아이디어가 있습니다:

- `ThreadPool` 및 해당 public 메서드에 더 많은 문서를 추가합니다.
- 라이브러리의 기능에 대한 테스트를 추가합니다.
- `unwrap` 호출을 보다 강력한 오류 처리로 변경합니다.
- 웹 요청을 처리하는 것 외에 다른 작업을 수행하기 위해 `ThreadPool`을 사용합니다.
- *https://crates.io*에서 스레드 풀 크레이트를 찾아 해당 크레이트를 사용하여 유사한 웹 서버를 구현합니다. 그런 다음, 해당 API 와 견고성을 우리가 구현한 스레드 풀과 비교합니다.
