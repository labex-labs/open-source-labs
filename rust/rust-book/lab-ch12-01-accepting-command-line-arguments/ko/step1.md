# 명령줄 인자 수락하기 (Accepting Command Line Arguments)

언제나 그렇듯이, `cargo new`를 사용하여 새 프로젝트를 생성해 봅시다. 프로젝트 이름을 `minigrep`으로 지정하여 시스템에 이미 있을 수 있는 `grep` 도구와 구별합니다.

```bash
$ cargo new minigrep
     Created binary (application) `minigrep` project
$ cd minigrep
```

첫 번째 작업은 `minigrep`이 두 개의 명령줄 인자를 받도록 만드는 것입니다: 파일 경로와 검색할 문자열입니다. 즉, 다음과 같이 `cargo run`과 함께 프로그램을 실행할 수 있기를 원합니다. 두 개의 하이픈은 다음 인자가 `cargo`가 아닌 우리 프로그램에 대한 것임을 나타내고, 검색할 문자열과 검색할 파일의 경로를 지정합니다.

```bash
cargo run -- searchstring example-filename.txt
```

현재, `cargo new`로 생성된 프로그램은 우리가 제공하는 인자를 처리할 수 없습니다. *https://crates.io*에 있는 몇몇 기존 라이브러리가 명령줄 인자를 받는 프로그램을 작성하는 데 도움이 될 수 있지만, 이 개념을 배우는 중이므로 직접 이 기능을 구현해 보겠습니다.
