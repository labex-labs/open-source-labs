# 채널을 통해 스레드로 요청 보내기

다음으로 해결할 문제는 `thread::spawn`에 제공된 클로저가 아무것도 하지 않는다는 것입니다. 현재, `execute` 메서드에서 실행하려는 클로저를 가져옵니다. 하지만 `ThreadPool`을 생성하는 동안 각 `Worker`를 생성할 때 `thread::spawn`에 실행할 클로저를 제공해야 합니다.

방금 생성한 `Worker` 구조체가 `ThreadPool`에 보관된 큐에서 실행할 코드를 가져와 해당 코드를 실행하기 위해 스레드로 보내도록 하려고 합니다.

16 장에서 배운 채널 (두 스레드 간의 간단한 통신 방법) 은 이 사용 사례에 완벽합니다. 채널을 작업 큐로 사용하고, `execute`는 작업을 `ThreadPool`에서 `Worker` 인스턴스로 보내고, `Worker` 인스턴스는 작업을 해당 스레드로 보낼 것입니다. 계획은 다음과 같습니다.

1.  `ThreadPool`은 채널을 생성하고 발신자를 유지합니다.
2.  각 `Worker`는 수신자를 유지합니다.
3.  채널을 통해 보내려는 클로저를 보유할 새 `Job` 구조체를 생성합니다.
4.  `execute` 메서드는 실행하려는 작업을 발신자를 통해 보냅니다.
5.  `Worker`는 해당 스레드에서 수신자를 반복하고 수신하는 모든 작업의 클로저를 실행합니다.

Listing 20-16 과 같이 `ThreadPool::new`에서 채널을 생성하고 `ThreadPool` 인스턴스에서 발신자를 유지하는 것부터 시작해 보겠습니다. `Job` 구조체는 현재 아무것도 보유하지 않지만 채널을 통해 보내는 항목의 타입이 됩니다.

파일 이름: `src/lib.rs`

```rust
use std::{sync::mpsc, thread};

pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: mpsc::Sender<Job>,
}

struct Job;

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

      1 let (sender, receiver) = mpsc::channel();

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(Worker::new(id));
        }

        ThreadPool { workers, 2 sender }
    }
    --snip--
}
```

Listing 20-16: `Job` 인스턴스를 전송하는 채널의 발신자를 저장하도록 `ThreadPool` 수정하기

`ThreadPool::new`에서 새 채널 \[1]을 생성하고 풀이 발신자 \[2]를 유지하도록 합니다. 이렇게 하면 성공적으로 컴파일됩니다.

스레드 풀이 채널을 생성할 때 채널의 수신자를 각 `Worker`로 전달해 보겠습니다. `Worker` 인스턴스가 스폰하는 스레드에서 수신자를 사용하므로, 클로저에서 `receiver` 매개변수를 참조할 것입니다. Listing 20-17 의 코드는 아직 완전히 컴파일되지 않습니다.

파일 이름: `src/lib.rs`

```rust
impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
          1 workers.push(Worker::new(id, receiver));
        }

        ThreadPool { workers, sender }
    }
    --snip--
}

--snip--

impl Worker {
    fn new(id: usize, receiver: mpsc::Receiver<Job>) -> Worker {
        let thread = thread::spawn(|| {
          2 receiver;
        });

        Worker { id, thread }
    }
}
```

Listing 20-17: 각 `Worker`에 수신자 전달하기

몇 가지 작고 간단한 변경을 했습니다. 수신자를 `Worker::new` \[1]으로 전달한 다음 클로저 \[2] 내에서 사용합니다.

이 코드를 확인하려고 하면 다음과 같은 오류가 발생합니다.

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0382]: use of moved value: `receiver`
  --> src/lib.rs:26:42
   |
21 |         let (sender, receiver) = mpsc::channel();
   |                      -------- move occurs because `receiver` has type
`std::sync::mpsc::Receiver<Job>`, which does not implement the `Copy` trait
...
26 |             workers.push(Worker::new(id, receiver));
   |                                          ^^^^^^^^ value moved here, in
previous iteration of loop
```

이 코드는 `receiver`를 여러 `Worker` 인스턴스에 전달하려고 합니다. 16 장에서 기억하듯이, 이 방법은 작동하지 않습니다. Rust 가 제공하는 채널 구현은 다중 _생산자_, 단일 *소비자*입니다. 즉, 이 코드를 수정하기 위해 채널의 소비 측면을 복제할 수 없습니다. 또한 여러 소비자에게 여러 번 메시지를 보내고 싶지 않습니다. 각 메시지가 한 번 처리되도록 여러 `Worker` 인스턴스가 있는 메시지 목록을 원합니다.

또한 채널 큐에서 작업을 가져오는 것은 `receiver`를 변경하는 것을 포함하므로, 스레드는 `receiver`를 안전하게 공유하고 수정할 방법이 필요합니다. 그렇지 않으면 경쟁 조건이 발생할 수 있습니다 (16 장에서 다룸).

16 장에서 논의한 스레드 안전 스마트 포인터를 기억하세요. 여러 스레드에서 소유권을 공유하고 스레드가 값을 변경하도록 하려면 `Arc<Mutex<T>>`를 사용해야 합니다. `Arc` 타입은 여러 `Worker` 인스턴스가 수신자를 소유하도록 하고, `Mutex`는 한 번에 하나의 `Worker`만 수신자로부터 작업을 가져오도록 합니다. Listing 20-18 은 필요한 변경 사항을 보여줍니다.

파일 이름: `src/lib.rs`

```rust
use std::{
    sync::{mpsc, Arc, Mutex},
    thread,
};
--snip--

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

      1 let receiver = Arc::new(Mutex::new(receiver));

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(
                Worker::new(id, Arc::clone(& 2 receiver))
            );
        }

        ThreadPool { workers, sender }
    }

    --snip--
}

--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        --snip--
    }
}
```

Listing 20-18: `Arc` 및 `Mutex`를 사용하여 `Worker` 인스턴스 간에 수신자 공유하기

`ThreadPool::new`에서 수신자를 `Arc` 및 `Mutex` \[1]에 넣었습니다. 각 새 `Worker`에 대해 `Arc`를 복제하여 참조 횟수를 늘리므로 `Worker` 인스턴스가 수신자의 소유권을 공유할 수 있습니다 \[2].

이러한 변경 사항을 통해 코드가 컴파일됩니다! 거의 다 왔습니다!
