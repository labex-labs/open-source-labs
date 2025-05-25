# 유한한 수의 스레드 생성하기

스레드 풀이 스레드에서 스레드 풀로 전환할 때 API 를 사용하는 코드에 큰 변경 사항이 필요하지 않도록, 스레드 풀이 유사하고 익숙한 방식으로 작동하기를 원합니다. Listing 20-12 는 `thread::spawn` 대신 사용하려는 `ThreadPool` 구조체의 가상 인터페이스를 보여줍니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
  1 let pool = ThreadPool::new(4);

    for stream in listener.incoming() {
        let stream = stream.unwrap();

      2 pool.execute(|| {
            handle_connection(stream);
        });
    }
}
```

Listing 20-12: 이상적인 `ThreadPool` 인터페이스

`ThreadPool::new`를 사용하여 구성 가능한 수의 스레드를 가진 새로운 스레드 풀을 생성합니다. 이 경우 4 개입니다 \[1]. 그런 다음 `for` 루프에서 `pool.execute`는 각 스트림에 대해 풀이 실행해야 하는 클로저를 사용한다는 점에서 `thread::spawn`과 유사한 인터페이스를 갖습니다 \[2]. `pool.execute`를 구현하여 클로저를 가져와 풀의 스레드에 제공하여 실행해야 합니다. 이 코드는 아직 컴파일되지 않지만, 컴파일러가 이를 수정하는 방법을 안내할 수 있도록 시도해 보겠습니다.
