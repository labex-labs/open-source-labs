# 스레드를 저장할 공간 만들기

이제 풀에 저장할 유효한 스레드 수를 아는 방법이 있으므로, 해당 스레드를 생성하고 구조체를 반환하기 전에 `ThreadPool` 구조체에 저장할 수 있습니다. 하지만 어떻게 스레드를 "저장"할까요? `thread::spawn` 시그니처를 다시 살펴보겠습니다.

```rust
pub fn spawn<F, T>(f: F) -> JoinHandle<T>
    where
        F: FnOnce() -> T,
        F: Send + 'static,
        T: Send + 'static,
```

`spawn` 함수는 `JoinHandle<T>`를 반환하며, 여기서 `T`는 클로저가 반환하는 타입입니다. `JoinHandle`도 사용해 보고 어떤 일이 발생하는지 살펴보겠습니다. 우리의 경우, 스레드 풀에 전달하는 클로저는 연결을 처리하고 아무것도 반환하지 않으므로, `T`는 유닛 타입 `()`이 됩니다.

Listing 20-14 의 코드는 컴파일되지만 아직 스레드를 생성하지 않습니다. `ThreadPool`의 정의를 `thread::JoinHandle<()>` 인스턴스의 벡터를 포함하도록 변경하고, `size`의 용량으로 벡터를 초기화하고, 스레드를 생성하기 위해 일부 코드를 실행하는 `for` 루프를 설정하고, 이를 포함하는 `ThreadPool` 인스턴스를 반환했습니다.

파일 이름: `src/lib.rs`

```rust
1 use std::thread;

pub struct ThreadPool {
  2 threads: Vec<thread::JoinHandle<()>>,
}

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

      3 let mut threads = Vec::with_capacity(size);

        for _ in 0..size {
            // create some threads and store them in the vector
        }

        ThreadPool { threads }
    }
    --snip--
}
```

Listing 20-14: 스레드를 저장하기 위해 `ThreadPool`이 사용할 벡터 생성하기

`thread::JoinHandle`을 `ThreadPool` \[2]의 벡터 항목의 타입으로 사용하고 있으므로, 라이브러리 크레이트에서 `std::thread`를 범위 내로 가져왔습니다 \[1].

유효한 크기가 수신되면, `ThreadPool`은 `size` 항목을 저장할 수 있는 새 벡터를 생성합니다 \[3]. `with_capacity` 함수는 `Vec::new`와 동일한 작업을 수행하지만 중요한 차이점이 있습니다. 즉, 벡터에 공간을 미리 할당합니다. `size` 요소를 벡터에 저장해야 한다는 것을 알고 있으므로, 이 할당을 미리 수행하는 것이 요소가 삽입될 때 자체적으로 크기를 조정하는 `Vec::new`을 사용하는 것보다 약간 더 효율적입니다.

`cargo check`를 다시 실행하면 성공해야 합니다.
