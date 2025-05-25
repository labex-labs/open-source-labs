# 요청 읽기

브라우저에서 요청을 읽는 기능을 구현해 봅시다! 먼저 연결을 얻은 다음 연결에 대한 작업을 수행하는 문제를 분리하기 위해 연결을 처리하기 위한 새로운 함수를 시작합니다. 이 새로운 `handle_connection` 함수에서 TCP 스트림에서 데이터를 읽고 출력하여 브라우저에서 전송되는 데이터를 볼 수 있습니다. 코드를 Listing 20-2 와 같이 변경합니다.

Filename: `src/main.rs`

```rust
1 use std::{
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
};

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();

      2 handle_connection(stream);
    }
}

fn handle_connection(mut stream: TcpStream) {
  3 let buf_reader = BufReader::new(&mut stream);
  4 let http_request: Vec<_> = buf_reader
      5 .lines()
      6 .map(|result| result.unwrap())
      7 .take_while(|line| !line.is_empty())
        .collect();

  8 println!("Request: {:#?}", http_request);
}
```

Listing 20-2: `TcpStream`에서 읽고 데이터를 출력

스트림에서 읽고 쓰기 위한 트레이트 (traits) 와 타입을 얻기 위해 `std::io::prelude` 및 `std::io::BufReader`를 범위 내로 가져옵니다 \[1]. `main` 함수의 `for` 루프에서 연결을 만들었다는 메시지를 출력하는 대신, 이제 새로운 `handle_connection` 함수를 호출하고 `stream`을 전달합니다 \[2].

`handle_connection` 함수에서 `stream`에 대한 가변 참조를 래핑하는 새로운 `BufReader` 인스턴스를 생성합니다 \[3]. `BufReader`는 `std::io::Read` 트레이트 메서드에 대한 호출을 관리하여 버퍼링을 추가합니다.

브라우저가 서버로 보내는 요청의 줄을 수집하기 위해 `http_request`라는 변수를 생성합니다. `Vec<_>` 타입 주석 \[4]을 추가하여 이러한 줄을 벡터로 수집하려는 것을 나타냅니다.

`BufReader`는 `std::io::BufRead` 트레이트를 구현하며, 이는 `lines` 메서드 \[5]를 제공합니다. `lines` 메서드는 줄 바꿈 바이트를 볼 때마다 데이터 스트림을 분할하여 `Result<String, std::io::Error>`의 반복자를 반환합니다. 각 `String`을 얻기 위해 각 `Result`를 매핑하고 `unwrap`합니다 \[6]. 데이터가 유효한 UTF-8 이 아니거나 스트림에서 읽는 데 문제가 있는 경우 `Result`가 오류일 수 있습니다. 다시 말하지만, 프로덕션 프로그램은 이러한 오류를 더 적절하게 처리해야 하지만, 단순성을 위해 오류가 발생한 경우 프로그램을 중지하도록 선택했습니다.

브라우저는 HTTP 요청의 끝을 연속으로 두 개의 줄 바꿈 문자를 전송하여 신호를 보냅니다. 따라서 스트림에서 하나의 요청을 얻기 위해 빈 문자열인 줄을 얻을 때까지 줄을 가져옵니다 \[7]. 줄을 벡터로 수집했으면, 웹 브라우저가 서버로 보내는 지침을 살펴볼 수 있도록 예쁜 디버그 형식 \[8]을 사용하여 출력합니다.

이 코드를 사용해 봅시다! 프로그램을 시작하고 웹 브라우저에서 다시 요청을 보냅니다. 브라우저에서 여전히 오류 페이지가 표시되지만 터미널의 프로그램 출력은 다음과 유사하게 표시됩니다.

```bash
$ cargo run
   Compiling hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 0.42s
     Running `target/debug/hello`
Request: [
    "GET / HTTP/1.1",
    "Host: 127.0.0.1:7878",
    "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0)
Gecko/20100101 Firefox/99.0",
    "Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*
;q=0.8",
    "Accept-Language: en-US,en;q=0.5",
    "Accept-Encoding: gzip, deflate, br",
    "DNT: 1",
    "Connection: keep-alive",
    "Upgrade-Insecure-Requests: 1",
    "Sec-Fetch-Dest: document",
    "Sec-Fetch-Mode: navigate",
    "Sec-Fetch-Site: none",
    "Sec-Fetch-User: ?1",
    "Cache-Control: max-age=0",
]
```

브라우저에 따라 약간 다른 출력을 얻을 수 있습니다. 이제 요청 데이터를 출력하고 있으므로 요청의 첫 번째 줄에서 `GET` 뒤의 경로를 보면 하나의 브라우저 요청에서 여러 연결을 얻는 이유를 알 수 있습니다. 반복되는 연결이 모두 */*를 요청하는 경우, 브라우저가 프로그램에서 응답을 받지 못하므로 */*를 반복적으로 가져오려고 한다는 것을 알 수 있습니다.

브라우저가 프로그램에 요청하는 내용을 이해하기 위해 이 요청 데이터를 분석해 보겠습니다.
