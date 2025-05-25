# 실제 HTML 반환

빈 페이지 이상을 반환하는 기능을 구현해 보겠습니다. 프로젝트 디렉토리의 루트 ( `src` 디렉토리 아님) 에 새 파일 *hello.html*을 만듭니다. 원하는 HTML 을 입력할 수 있습니다. Listing 20-4 는 한 가지 가능성을 보여줍니다.

Filename: `hello.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Hello!</title>
  </head>
  <body>
    <h1>Hello!</h1>
    <p>Hi from Rust</p>
  </body>
</html>
```

Listing 20-4: 응답으로 반환할 샘플 HTML 파일

이것은 제목과 텍스트가 있는 최소한의 HTML5 문서입니다. 요청을 받으면 서버에서 이 문서를 반환하기 위해 Listing 20-5 에 표시된 대로 `handle_connection`을 수정하여 HTML 파일을 읽고, 본문으로 응답에 추가하고, 전송합니다.

Filename: `src/main.rs`

```rust
use std::{
  1 fs,
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
};
--snip--

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let http_request: Vec<_> = buf_reader
        .lines()
        .map(|result| result.unwrap())
        .take_while(|line| !line.is_empty())
        .collect();

    let status_line = "HTTP/1.1 200 OK";
    let contents = fs::read_to_string("hello.html").unwrap();
    let length = contents.len();

  2 let response = format!(
        "{status_line}\r\n\
         Content-Length: {length}\r\n\r\n\
         {contents}"
    );

    stream.write_all(response.as_bytes()).unwrap();
}
```

Listing 20-5: *hello.html*의 내용을 응답 본문으로 전송

표준 라이브러리의 파일 시스템 모듈을 범위 내로 가져오기 위해 `use` 문에 `fs`를 추가했습니다 \[1]. 파일의 내용을 문자열로 읽는 코드는 익숙해야 합니다. Listing 12-4 에서 I/O 프로젝트에 대한 파일의 내용을 읽을 때 사용했습니다.

다음으로, `format!`을 사용하여 파일의 내용을 성공 응답의 본문으로 추가합니다 \[2]. 유효한 HTTP 응답을 보장하기 위해 응답 본문의 크기, 즉 이 경우 `hello.html`의 크기로 설정된 `Content-Length` 헤더를 추가합니다.

`cargo run`으로 이 코드를 실행하고 브라우저에서 *127.0.0.1:7878*을 로드하면 HTML 이 렌더링되는 것을 볼 수 있습니다!

현재 `http_request`의 요청 데이터를 무시하고 HTML 파일의 내용을 무조건 다시 보내고 있습니다. 즉, 브라우저에서 *127.0.0.1:7878/something-else*를 요청하려고 하면 동일한 HTML 응답을 받게 됩니다. 현재 서버는 매우 제한적이며 대부분의 웹 서버가 수행하는 작업을 수행하지 않습니다. 요청에 따라 응답을 사용자 정의하고 */*에 대한 올바른 형식의 요청에 대해서만 HTML 파일을 다시 보내고 싶습니다.
