# Rust 프로그램 작성 및 실행

다음으로, 새로운 소스 파일을 만들고 이름을 `main.rs`로 지정합니다. Rust 파일은 항상 `.rs` 확장자로 끝납니다. 파일 이름에 두 단어 이상을 사용하는 경우, 관례적으로 밑줄을 사용하여 구분합니다. 예를 들어, `helloworld.rs` 대신 `hello_world.rs`를 사용합니다.

이제 방금 만든 `main.rs` 파일을 열고 Listing 1-1 의 코드를 입력합니다.

파일 이름: `main.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

Listing 1-1: `Hello, world!`를 출력하는 프로그램

파일을 저장하고 `~/project/hello_world` 디렉토리의 터미널 창으로 돌아갑니다. Linux 또는 macOS 에서 다음 명령을 입력하여 파일을 컴파일하고 실행합니다.

```bash
$ rustc main.rs
$ ./main
Hello, world!
```

운영 체제에 관계없이 문자열 `Hello, world!`가 터미널에 출력되어야 합니다. 이 출력이 보이지 않으면, 도움을 얻는 방법에 대한 "문제 해결"을 참조하십시오.

`Hello, world!`가 출력되었다면 축하합니다! 공식적으로 Rust 프로그램을 작성했습니다. 이제 당신은 Rust 프로그래머입니다---환영합니다!
