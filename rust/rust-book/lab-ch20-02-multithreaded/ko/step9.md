# ThreadPool 에서 스레드로 코드 전송하기

Listing 20-14 의 `for` 루프에서 스레드 생성과 관련하여 주석을 남겼습니다. 여기서는 실제로 스레드를 생성하는 방법을 살펴보겠습니다. 표준 라이브러리는 스레드를 생성하는 방법으로 `thread::spawn`을 제공하며, `thread::spawn`은 스레드가 생성되는 즉시 스레드가 실행해야 하는 코드를 받기를 기대합니다. 그러나 우리의 경우, 스레드를 생성하고 나중에 보낼 코드를 *대기*하도록 하려고 합니다. 표준 라이브러리의 스레드 구현에는 이를 수행할 방법이 포함되어 있지 않으므로, 수동으로 구현해야 합니다.

이 동작을 구현하기 위해 `ThreadPool`과 이 새로운 동작을 관리할 스레드 사이에 새로운 데이터 구조를 도입할 것입니다. 이 데이터 구조를 *Worker*라고 부르겠습니다. 이는 풀링 구현에서 흔히 사용되는 용어입니다. `Worker`는 실행해야 하는 코드를 가져와 해당 스레드에서 코드를 실행합니다.

레스토랑 주방에서 일하는 사람들을 생각해 보세요. 작업자는 고객으로부터 주문이 들어올 때까지 기다린 다음, 해당 주문을 받아 채우는 역할을 합니다.

스레드 풀에 `JoinHandle<()>` 인스턴스의 벡터를 저장하는 대신, `Worker` 구조체의 인스턴스를 저장할 것입니다. 각 `Worker`는 단일 `JoinHandle<()>` 인스턴스를 저장합니다. 그런 다음 실행할 코드의 클로저를 가져와 이미 실행 중인 스레드로 실행을 위해 보내는 `Worker`에 대한 메서드를 구현할 것입니다. 또한 로깅 또는 디버깅 시 풀에서 서로 다른 `Worker` 인스턴스를 구별할 수 있도록 각 `Worker`에 `id`를 부여할 것입니다.

다음은 `ThreadPool`을 생성할 때 발생할 새로운 프로세스입니다. 이 방식으로 `Worker`를 설정한 후 클로저를 스레드로 보내는 코드를 구현할 것입니다.

1.  `id`와 `JoinHandle<()>`을 보유하는 `Worker` 구조체를 정의합니다.
2.  `ThreadPool`이 `Worker` 인스턴스의 벡터를 보유하도록 변경합니다.
3.  `id` 번호를 가져와 `id`와 빈 클로저로 스폰된 스레드를 보유하는 `Worker` 인스턴스를 반환하는 `Worker::new` 함수를 정의합니다.
4.  `ThreadPool::new`에서 `for` 루프 카운터를 사용하여 `id`를 생성하고, 해당 `id`로 새 `Worker`를 생성하고, `Worker`를 벡터에 저장합니다.

도전해 보고 싶다면, Listing 20-15 의 코드를 보기 전에 직접 이러한 변경 사항을 구현해 보세요.

준비되었나요? 다음은 앞의 수정을 수행하는 한 가지 방법인 Listing 20-15 입니다.

파일 이름: `src/lib.rs`

```rust
use std::thread;

pub struct ThreadPool {
  1 workers: Vec<Worker>,
}

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let mut workers = Vec::with_capacity(size);

      2 for id in 0..size {
          3 workers.push(Worker::new(id));
        }

        ThreadPool { workers }
    }
    --snip--
}

4 struct Worker {
    id: usize,
    thread: thread::JoinHandle<()>,
}

impl Worker {
  5 fn new(id: usize) -> Worker {
      6 let thread = thread::spawn(|| {});

        Worker { 7 id, 8 thread }
    }
}
```

Listing 20-15: 스레드를 직접 보유하는 대신 `Worker` 인스턴스를 보유하도록 `ThreadPool` 수정하기

`ThreadPool`의 필드 이름을 `threads`에서 `workers`로 변경했습니다. 이제 `JoinHandle<()>` 인스턴스 대신 `Worker` 인스턴스를 보유하고 있기 때문입니다 \[1]. `for` 루프 \[2]의 카운터를 `Worker::new`에 대한 인수로 사용하고, 각 새 `Worker`를 `workers`라는 벡터에 저장합니다 \[3].

외부 코드 (예: `src/main.rs`의 서버) 는 `ThreadPool` 내에서 `Worker` 구조체를 사용하는 것과 관련된 구현 세부 정보를 알 필요가 없으므로, `Worker` 구조체 \[4]와 해당 `new` 함수 \[5]를 비공개로 만듭니다. `Worker::new` 함수는 제공한 `id` \[7]를 사용하고, 빈 클로저 \[6]를 사용하여 새 스레드를 스폰하여 생성된 `JoinHandle<()>` 인스턴스 \[8]를 저장합니다.

> 참고: 운영 체제가 시스템 리소스가 부족하여 스레드를 생성할 수 없는 경우, `thread::spawn`은 패닉합니다. 그러면 일부 스레드 생성이 성공하더라도 전체 서버가 패닉하게 됩니다. 단순성을 위해 이 동작은 괜찮지만, 프로덕션 스레드 풀 구현에서는 `std::thread::Builder`와 `Result`를 반환하는 해당 `spawn` 메서드를 사용하는 것이 좋습니다.

이 코드는 컴파일되고 `ThreadPool::new`에 대한 인수로 지정한 `Worker` 인스턴스 수를 저장합니다. 하지만 `execute`에서 얻는 클로저는 _아직_ 처리하지 않고 있습니다. 다음으로 이를 수행하는 방법을 살펴보겠습니다.
