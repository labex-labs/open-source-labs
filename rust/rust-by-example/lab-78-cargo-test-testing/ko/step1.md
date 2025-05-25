# 테스트

소프트웨어의 어떤 부분에도 테스트는 필수적입니다! Rust 는 단위 테스트와 통합 테스트에 대한 우수한 지원을 제공합니다 ([TRPL 의 이 장](https://doc.rust-lang.org/book/ch11-00-testing.html) 참조).

위 링크된 테스트 챕터에서 단위 테스트와 통합 테스트를 작성하는 방법을 볼 수 있습니다. 조직적으로, 단위 테스트는 테스트하는 모듈 내에, 통합 테스트는 자체 `tests/` 디렉토리에 배치할 수 있습니다.

```txt
foo
├── Cargo.toml
├── src
│   └── main.rs
│   └── lib.rs
└── tests
    ├── my_test.rs
    └── my_other_test.rs
```

`tests` 디렉토리의 각 파일은 별도의 [통합 테스트](https://doc.rust-lang.org/book/ch11-03-test-organization.html#integration-tests)입니다. 즉, 종속된 크레이트에서 호출되는 것처럼 라이브러리를 테스트하기 위한 테스트입니다.

테스트 챕터에서는 단위, 문서, 통합의 세 가지 테스트 스타일을 자세히 설명합니다.

`cargo`는 자연스럽게 모든 테스트를 실행하는 쉬운 방법을 제공합니다!

```shell
$ cargo test
```

다음과 같은 출력을 볼 수 있습니다.

```shell
[object Object]
```

패턴과 일치하는 테스트를 실행할 수도 있습니다.

```shell
$ cargo test test_foo
```

```shell
[object Object]
```

주의 사항: Cargo 는 여러 테스트를 동시에 실행할 수 있으므로 서로 경쟁하지 않도록 해야 합니다.

이러한 동시 실행으로 문제가 발생하는 한 가지 예는 두 개의 테스트가 아래와 같이 파일로 출력하는 경우입니다.

```rust
#[cfg(test)]
mod tests {
    // 필요한 모듈 가져오기
    use std::fs::OpenOptions;
    use std::io::Write;

    // 파일로 출력하는 테스트
    #[test]
    fn test_file() {
        // ferris.txt 파일을 열거나 존재하지 않으면 생성합니다.
        let mut file = OpenOptions::new()
            .append(true)
            .create(true)
            .open("ferris.txt")
            .expect("Failed to open ferris.txt");

        // "Ferris"를 5 번 출력합니다.
        for _ in 0..5 {
            file.write_all("Ferris\n".as_bytes())
                .expect("Could not write to ferris.txt");
        }
    }

    // 동일한 파일로 출력하는 테스트
    #[test]
    fn test_file_also() {
        // ferris.txt 파일을 열거나 존재하지 않으면 생성합니다.
        let mut file = OpenOptions::new()
            .append(true)
            .create(true)
            .open("ferris.txt")
            .expect("Failed to open ferris.txt");

        // "Corro"를 5 번 출력합니다.
        for _ in 0..5 {
            file.write_all("Corro\n".as_bytes())
                .expect("Could not write to ferris.txt");
        }
    }
}
```

의도는 다음과 같습니다.

```shell
$ cat ferris.txt
Ferris
Ferris
Ferris
Ferris
Ferris
Corro
Corro
Corro
Corro
Corro
```

그러나 실제로 `ferris.txt`에 저장되는 내용은 다음과 같습니다.

```shell
$ cargo test test_foo
Corro
Ferris
Corro
Ferris
Corro
Ferris
Corro
Ferris
Corro
Ferris
```
