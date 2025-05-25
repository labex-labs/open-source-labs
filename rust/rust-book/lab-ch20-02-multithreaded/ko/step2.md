# 느린 요청 시뮬레이션

느린 처리 요청이 현재 서버 구현에 대한 다른 요청에 어떤 영향을 미칠 수 있는지 살펴보겠습니다. Listing 20-10 은 서버가 응답하기 전에 5 초 동안 대기하도록 하는 시뮬레이션된 느린 응답으로 */sleep*에 대한 요청을 처리하는 방법을 구현합니다.

파일 이름: `src/main.rs`

```rust
use std::{
    fs,
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
    thread,
    time::Duration,
};
--snip--

fn handle_connection(mut stream: TcpStream) {
    --snip--

    let (status_line, filename) = 1 match &request_line[..] {
      2 "GET / HTTP/1.1" => ("HTTP/1.1 200 OK", "hello.html"),
      3 "GET /sleep HTTP/1.1" => {
            thread::sleep(Duration::from_secs(5));
            ("HTTP/1.1 200 OK", "hello.html")
        }
      4 _ => ("HTTP/1.1 404 NOT FOUND", "404.html"),
    };

    --snip--
}
```

Listing 20-10: 5 초 동안 대기하여 느린 요청 시뮬레이션

이제 세 가지 경우 \[1]가 있으므로 `if`에서 `match`로 전환했습니다. 문자열 리터럴 값에 대해 패턴 일치를 수행하려면 `request_line`의 슬라이스를 명시적으로 일치시켜야 합니다. `match`는 동등성 메서드처럼 자동 참조 및 역참조를 수행하지 않습니다.

첫 번째 arm \[2]은 Listing 20-9 의 `if` 블록과 동일합니다. 두 번째 arm \[3]은 */sleep*에 대한 요청과 일치합니다. 해당 요청을 받으면 서버는 성공적인 HTML 페이지를 렌더링하기 전에 5 초 동안 대기합니다. 세 번째 arm \[4]은 Listing 20-9 의 `else` 블록과 동일합니다.

서버가 얼마나 원시적인지 알 수 있습니다. 실제 라이브러리는 여러 요청의 인식을 훨씬 덜 장황한 방식으로 처리할 것입니다!

`cargo run`을 사용하여 서버를 시작합니다. 그런 다음 두 개의 브라우저 창을 엽니다. 하나는 *http://127.0.0.1:7878*이고 다른 하나는 *http://127.0.0.1:7878/sleep*입니다. 이전과 마찬가지로 _/_ URI 를 몇 번 입력하면 빠르게 응답하는 것을 볼 수 있습니다. 그러나 */sleep*을 입력한 다음 */*를 로드하면 */*가 `sleep`이 전체 5 초 동안 대기한 후에 로드되는 것을 볼 수 있습니다.

느린 요청 뒤에서 요청이 백업되는 것을 방지하기 위해 사용할 수 있는 여러 기술이 있습니다. 우리가 구현할 기술은 스레드 풀 (thread pool) 입니다.
