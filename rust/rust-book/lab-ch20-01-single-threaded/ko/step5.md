# 응답 작성

클라이언트 요청에 대한 응답으로 데이터를 전송하는 것을 구현할 것입니다. 응답은 다음과 같은 형식을 갖습니다.

    HTTP-Version Status-Code Reason-Phrase CRLF
    headers CRLF
    message-body

첫 번째 줄은 응답에 사용된 HTTP 버전, 요청 결과를 요약하는 숫자 상태 코드, 상태 코드에 대한 텍스트 설명을 제공하는 이유 구문을 포함하는 *상태 라인*입니다. CRLF 시퀀스 다음에는 헤더, 다른 CRLF 시퀀스 및 응답 본문이 있습니다.

다음은 HTTP 버전 1.1 을 사용하고, 상태 코드 200, OK 이유 구문, 헤더 없음, 본문 없음이 있는 응답 예시입니다.

```rust
HTTP/1.1 200 OK\r\n\r\n
```

상태 코드 200 은 표준 성공 응답입니다. 텍스트는 작은 성공적인 HTTP 응답입니다. 성공적인 요청에 대한 응답으로 스트림에 이것을 작성해 봅시다! `handle_connection` 함수에서 요청 데이터를 출력하던 `println!`을 제거하고 Listing 20-3 의 코드로 바꿉니다.

Filename: `src/main.rs`

```rust
fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let http_request: Vec<_> = buf_reader
        .lines()
        .map(|result| result.unwrap())
        .take_while(|line| !line.is_empty())
        .collect();

  1 let response = "HTTP/1.1 200 OK\r\n\r\n";

  2 stream.write_all(response.3 as_bytes()).unwrap();
}
```

Listing 20-3: 스트림에 작은 성공적인 HTTP 응답을 작성

첫 번째 새 줄은 성공 메시지의 데이터를 담고 있는 `response` 변수를 정의합니다 \[1]. 그런 다음 문자열 데이터를 바이트로 변환하기 위해 `response`에서 `as_bytes`를 호출합니다 \[3]. `stream`의 `write_all` 메서드는 `&[u8]`을 가져와 해당 바이트를 연결로 직접 보냅니다 \[2]. `write_all` 작업이 실패할 수 있으므로 이전과 마찬가지로 모든 오류 결과에 대해 `unwrap`을 사용합니다. 다시 말하지만, 실제 애플리케이션에서는 여기에 오류 처리를 추가합니다.

이러한 변경 사항을 적용하여 코드를 실행하고 요청을 해 봅시다. 더 이상 터미널에 데이터를 출력하지 않으므로 Cargo 의 출력 외에는 어떤 출력도 볼 수 없습니다. 웹 브라우저에서 *127.0.0.1:7878*을 로드하면 오류 대신 빈 페이지가 표시됩니다. 방금 HTTP 요청을 수신하고 응답을 보내는 것을 직접 코딩했습니다!
