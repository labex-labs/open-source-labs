# Linux 또는 macOS 에 rustup 설치하기

Linux 또는 macOS 를 사용하는 경우 터미널을 열고 다음 명령을 입력하십시오.

```bash
curl --proto '=https' --tlsv1.3 https://sh.rustup.rs -sSf | sh
```

이 명령은 스크립트를 다운로드하고 최신 안정 버전의 Rust 를 설치하는 `rustup` 도구의 설치를 시작합니다. 암호를 묻는 메시지가 표시될 수 있습니다. 설치가 성공하면 다음 줄이 나타납니다.

```rust
Rust is installed now. Great!
```

또한 Rust 가 컴파일된 출력을 하나의 파일로 결합하는 데 사용하는 프로그램인 *링커 (linker)*가 필요합니다. 이미 하나 가지고 있을 가능성이 큽니다. 링커 오류가 발생하면 일반적으로 링커를 포함하는 C 컴파일러를 설치해야 합니다. 일부 일반적인 Rust 패키지가 C 코드에 의존하고 C 컴파일러가 필요하므로 C 컴파일러도 유용합니다.

Linux 사용자는 일반적으로 해당 배포판의 설명서에 따라 GCC 또는 Clang 을 설치해야 합니다. 예를 들어 Ubuntu 를 사용하는 경우 `build-essential` 패키지를 설치할 수 있습니다.
