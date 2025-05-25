# `run` 함수에서 `search` 함수 사용하기

이제 `search` 함수가 작동하고 테스트되었으므로 `run` 함수에서 `search`를 호출해야 합니다. `config.query` 값과 `run`이 파일에서 읽은 `contents`를 `search` 함수에 전달해야 합니다. 그런 다음 `run`은 `search`에서 반환된 각 줄을 출력합니다.

파일 이름: `src/lib.rs`

```rust
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)?;

    for line in search(&config.query, &contents) {
        println!("{line}");
    }

    Ok(())
}
```

여전히 `search`에서 각 줄을 반환하고 출력하기 위해 `for` 루프를 사용하고 있습니다.

이제 전체 프로그램이 작동해야 합니다! 먼저 Emily Dickinson 의 시에서 정확히 한 줄을 반환해야 하는 단어인 *frog*로 시도해 보겠습니다.

```bash
$ cargo run -- frog poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.38s
     Running `target/debug/minigrep frog poem.txt`
How public, like a frog
```

멋지네요! 이제 *body*와 같이 여러 줄과 일치하는 단어를 시도해 보겠습니다.

```bash
$ cargo run -- body poem.txt
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep body poem.txt`
I'm nobody! Who are you?
Are you nobody, too?
How dreary to be somebody!
```

마지막으로, *monomorphization*과 같이 시에 없는 단어를 검색할 때 어떤 줄도 얻지 못하는지 확인해 보겠습니다.

```bash
$ cargo run -- monomorphization poem.txt
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep monomorphization poem.txt`
```

훌륭합니다! 우리는 고전적인 도구의 자체 미니 버전을 구축했으며 애플리케이션을 구조화하는 방법에 대해 많은 것을 배웠습니다. 또한 파일 입출력, 라이프타임 (lifetimes), 테스트 및 명령줄 구문 분석에 대해서도 조금 배웠습니다.

이 프로젝트를 마무리하기 위해 환경 변수를 사용하는 방법과 명령줄 프로그램을 작성할 때 유용한 표준 오류로 출력하는 방법을 간략하게 시연하겠습니다.
