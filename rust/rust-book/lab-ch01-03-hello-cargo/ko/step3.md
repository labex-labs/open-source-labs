# Cargo 프로젝트 빌드 및 실행하기

이제 Cargo 로 "Hello, world!" 프로그램을 빌드하고 실행할 때 무엇이 다른지 살펴보겠습니다! `hello_cargo` 디렉토리에서 다음 명령을 입력하여 프로젝트를 빌드합니다.

```bash
$ cargo build
   Compiling hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 2.85 secs
```

이 명령은 현재 디렉토리가 아닌 `target/debug/hello_cargo`에 실행 파일을 생성합니다. 기본 빌드는 디버그 빌드이므로 Cargo 는 바이너리를 `debug`라는 디렉토리에 넣습니다. 다음 명령으로 실행 파일을 실행할 수 있습니다.

```bash
$ ./target/debug/hello_cargo
Hello, world!
```

모든 것이 잘 진행되면 `Hello, world!`가 터미널에 출력됩니다. 처음으로 `cargo build`를 실행하면 Cargo 는 최상위 레벨에 새로운 파일인 *Cargo.lock*을 생성합니다. 이 파일은 프로젝트의 의존성의 정확한 버전을 추적합니다. 이 프로젝트에는 의존성이 없으므로 파일이 약간 비어 있습니다. 이 파일을 수동으로 변경할 필요는 없습니다. Cargo 가 내용을 관리합니다.

방금 `cargo build`로 프로젝트를 빌드하고 `./target/debug/hello_cargo`로 실행했지만, `cargo run`을 사용하여 코드를 컴파일한 다음 결과 실행 파일을 한 번의 명령으로 실행할 수도 있습니다.

```bash
$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.0 secs
     Running `target/debug/hello_cargo`
Hello, world!
```

`cargo build`를 실행한 다음 바이너리의 전체 경로를 기억해야 하는 것보다 `cargo run`을 사용하는 것이 더 편리하므로 대부분의 개발자는 `cargo run`을 사용합니다.

이번에는 Cargo 가 `hello_cargo`를 컴파일하고 있다는 출력이 표시되지 않았습니다. Cargo 는 파일이 변경되지 않았다는 것을 파악했으므로 다시 빌드하지 않고 바이너리를 실행했습니다. 소스 코드를 수정했다면 Cargo 는 실행하기 전에 프로젝트를 다시 빌드했을 것이고, 다음과 같은 출력을 보았을 것입니다.

```bash
$ cargo run
   Compiling hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 0.33 secs
     Running `target/debug/hello_cargo`
Hello, world!
```

Cargo 는 또한 `cargo check`라는 명령을 제공합니다. 이 명령은 코드가 컴파일되는지 빠르게 확인하지만 실행 파일을 생성하지 않습니다.

```bash
$ cargo check
   Checking hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 0.32 secs
```

왜 실행 파일이 필요하지 않을까요? 종종 `cargo check`는 실행 파일을 생성하는 단계를 건너뛰기 때문에 `cargo build`보다 훨씬 빠릅니다. 코드를 작성하는 동안 지속적으로 작업을 확인하는 경우 `cargo check`를 사용하면 프로젝트가 여전히 컴파일되는지 알려주는 프로세스 속도가 빨라집니다! 따라서 많은 Rust 개발자는 프로그램 작성 시 정기적으로 `cargo check`를 실행하여 컴파일되는지 확인합니다. 그런 다음 실행 파일을 사용할 준비가 되면 `cargo build`를 실행합니다.

지금까지 Cargo 에 대해 배운 내용을 요약해 보겠습니다.

- `cargo new`를 사용하여 프로젝트를 생성할 수 있습니다.
- `cargo build`를 사용하여 프로젝트를 빌드할 수 있습니다.
- `cargo run`을 사용하여 한 단계로 프로젝트를 빌드하고 실행할 수 있습니다.
- `cargo check`를 사용하여 오류를 확인하기 위해 바이너리를 생성하지 않고 프로젝트를 빌드할 수 있습니다.
- Cargo 는 빌드 결과를 코드와 동일한 디렉토리에 저장하는 대신 `target/debug` 디렉토리에 저장합니다.

Cargo 를 사용하는 또 다른 장점은 어떤 운영 체제에서 작업하든 명령이 동일하다는 것입니다. 따라서 이 시점부터 Linux 및 macOS 와 Windows 에 대한 구체적인 지침을 더 이상 제공하지 않겠습니다.
