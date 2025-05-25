# 요청 유효성 검사 및 선택적 응답

현재 웹 서버는 클라이언트가 요청한 내용에 관계없이 파일의 HTML 을 반환합니다. 브라우저가 HTML 파일을 반환하기 전에 */*를 요청하는지 확인하고, 브라우저가 다른 것을 요청하는 경우 오류를 반환하는 기능을 추가해 보겠습니다. 이를 위해 Listing 20-6 에 표시된 대로 `handle_connection`을 수정해야 합니다. 이 새로운 코드는 수신된 요청의 내용을 */*에 대한 요청이 어떻게 보이는지 알고 있는 내용과 비교하고, 요청을 다르게 처리하기 위해 `if` 및 `else` 블록을 추가합니다.

Filename: `src/main.rs`

```rust
--snip--

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
  1 let request_line = buf_reader
        .lines()
        .next()
        .unwrap()
        .unwrap();

  2 if request_line == "GET / HTTP/1.1" {
        let status_line = "HTTP/1.1 200 OK";
        let contents = fs::read_to_string("hello.html").unwrap();
        let length = contents.len();

        let response = format!(
            "{status_line}\r\n\
             Content-Length: {length}\r\n\r\n\
             {contents}"
        );

        stream.write_all(response.as_bytes()).unwrap();
  3 } else {
        // some other request
    }
}
```

Listing 20-6: 다른 요청과 다르게 */*에 대한 요청 처리

HTTP 요청의 첫 번째 줄만 볼 것이므로 전체 요청을 벡터로 읽는 대신 `next`를 호출하여 반복자에서 첫 번째 항목을 가져옵니다 \[1]. 첫 번째 `unwrap`은 `Option`을 처리하고 반복자에 항목이 없으면 프로그램을 중지합니다. 두 번째 `unwrap`은 `Result`를 처리하며 Listing 20-2 에 추가된 `map`의 `unwrap`과 동일한 효과를 갖습니다.

다음으로, `request_line`이 _/_ 경로에 대한 GET 요청의 요청 줄과 같은지 확인합니다 \[2]. 그렇다면 `if` 블록은 HTML 파일의 내용을 반환합니다.

`request_line`이 _/_ 경로에 대한 GET 요청과 같지 않으면 다른 요청을 받았다는 의미입니다. 잠시 후 `else` 블록 \[3]에 코드를 추가하여 다른 모든 요청에 응답합니다.

지금 이 코드를 실행하고 *127.0.0.1:7878*을 요청하면 *hello.html*의 HTML 을 얻을 수 있습니다. *127.0.0.1:7878/something-else*와 같은 다른 요청을 하면 Listing 20-1 및 Listing 20-2 에서 코드를 실행할 때 보았던 것과 같은 연결 오류가 발생합니다.

이제 Listing 20-7 의 코드를 `else` 블록에 추가하여 요청에 대한 콘텐츠를 찾을 수 없음을 나타내는 상태 코드 404 로 응답을 반환해 보겠습니다. 또한 최종 사용자에게 응답을 나타내는 브라우저에서 렌더링할 페이지에 대한 일부 HTML 을 반환합니다.

Filename: `src/main.rs`

```rust
--snip--
} else {
  1 let status_line = "HTTP/1.1 404 NOT FOUND";
  2 let contents = fs::read_to_string("404.html").unwrap();
    let length = contents.len();

    let response = format!(
        "{status_line}\r\n\
         Content-Length: {length}\r\n\r\n
         {contents}"
    );

    stream.write_all(response.as_bytes()).unwrap();
}
```

Listing 20-7: _/_ 이외의 요청이 있는 경우 상태 코드 404 및 오류 페이지로 응답

여기서 응답에는 상태 코드 404 와 이유 구문 `NOT FOUND`가 있는 상태 라인이 있습니다 \[1]. 응답 본문은 파일 *404.html*의 HTML 이 됩니다 \[1]. 오류 페이지에 대해 _hello.html_ 옆에 _404.html_ 파일을 만들어야 합니다. 다시 한 번 원하는 HTML 을 자유롭게 사용하거나 Listing 20-8 의 예제 HTML 을 사용하십시오.

Filename: `404.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Hello!</title>
  </head>
  <body>
    <h1>Oops!</h1>
    <p>Sorry, I don't know what you're asking for.</p>
  </body>
</html>
```

Listing 20-8: 404 응답과 함께 다시 보낼 페이지의 샘플 콘텐츠

이러한 변경 사항을 적용하여 서버를 다시 실행합니다. *127.0.0.1:7878*을 요청하면 *hello.html*의 내용이 반환되고, *127.0.0.1:7878/foo*와 같은 다른 요청은 *404.html*의 오류 HTML 을 반환해야 합니다.
