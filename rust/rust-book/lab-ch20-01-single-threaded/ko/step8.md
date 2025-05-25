# 약간의 리팩토링

현재 `if` 및 `else` 블록에는 많은 중복이 있습니다. 둘 다 파일을 읽고 파일의 내용을 스트림에 쓰고 있습니다. 유일한 차이점은 상태 라인과 파일 이름입니다. 이러한 차이점을 별도의 `if` 및 `else` 라인으로 분리하여 코드를 더 간결하게 만들어 상태 라인과 파일 이름의 값을 변수에 할당할 수 있습니다. 그런 다음 해당 변수를 사용하여 파일을 읽고 응답을 쓰는 코드를 무조건 사용할 수 있습니다. Listing 20-9 는 큰 `if` 및 `else` 블록을 대체한 후의 결과 코드를 보여줍니다.

Filename: `src/main.rs`

```rust
--snip--

fn handle_connection(mut stream: TcpStream) {
    --snip--

    let (status_line, filename) =
        if request_line == "GET / HTTP/1.1" {
            ("HTTP/1.1 200 OK", "hello.html")
        } else {
            ("HTTP/1.1 404 NOT FOUND", "404.html")
        };

    let contents = fs::read_to_string(filename).unwrap();
    let length = contents.len();

    let response = format!(
        "{status_line}\r\n\
         Content-Length: {length}\r\n\r\n\
         {contents}"
    );

    stream.write_all(response.as_bytes()).unwrap();
}
```

Listing 20-9: 두 경우의 차이점만 포함하도록 `if` 및 `else` 블록 리팩토링

이제 `if` 및 `else` 블록은 튜플에서 상태 라인과 파일 이름에 대한 적절한 값만 반환합니다. 그런 다음 18 장에서 설명한 대로 `let` 문에서 패턴을 사용하여 이러한 두 값을 `status_line` 및 `filename`에 할당하기 위해 구조 분해를 사용합니다.

이전에 중복된 코드는 이제 `if` 및 `else` 블록 외부에 있으며 `status_line` 및 `filename` 변수를 사용합니다. 이렇게 하면 두 경우의 차이점을 쉽게 확인할 수 있으며, 파일 읽기 및 응답 쓰기 작동 방식을 변경하려는 경우 코드를 업데이트할 위치가 하나만 있다는 의미입니다. Listing 20-9 의 코드 동작은 Listing 20-8 의 코드 동작과 동일합니다.

훌륭합니다! 이제 약 40 줄의 Rust 코드로 된 간단한 웹 서버가 있어 하나의 요청에 콘텐츠 페이지로 응답하고 다른 모든 요청에 404 응답으로 응답합니다.

현재 서버는 단일 스레드에서 실행되므로 한 번에 하나의 요청만 처리할 수 있습니다. 몇 가지 느린 요청을 시뮬레이션하여 문제가 될 수 있는 방식을 살펴보겠습니다. 그런 다음 서버가 한 번에 여러 요청을 처리할 수 있도록 수정하겠습니다.
