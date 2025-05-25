# Workspace 에서 두 번째 패키지 생성하기

다음으로, workspace 에 다른 멤버 패키지를 생성하고 `add_one`이라고 부르겠습니다. 최상위 `Cargo.toml`을 변경하여 `members` 목록에 _add_one_ 경로를 지정합니다.

파일 이름: `Cargo.toml`

```toml
[workspace]

members = [
    "adder",
    "add_one",
]
```

그런 다음 `add_one`이라는 새 라이브러리 크레이트를 생성합니다.

```bash
$ cargo new add_one --lib
Created library $(add_one) package
```

`add` 디렉토리에는 이제 다음과 같은 디렉토리와 파일이 있어야 합니다.

    ├── Cargo.lock
    ├── Cargo.toml
    ├── add_one
    │   ├── Cargo.toml
    │   └── src
    │       └── lib.rs
    ├── adder
    │   ├── Cargo.toml
    │   └── src
    │       └── main.rs
    └── target

`add_one/src/lib.rs` 파일에 `add_one` 함수를 추가해 보겠습니다.

파일 이름: `add_one/src/lib.rs`

```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}
```

이제 바이너리가 있는 `adder` 패키지가 라이브러리가 있는 `add_one` 패키지에 의존하도록 할 수 있습니다. 먼저 *adder/Cargo.toml*에 `add_one`에 대한 경로 종속성을 추가해야 합니다.

파일 이름: `adder/Cargo.toml`

```tomlrust
[dependencies]
add_one = { path = "../add_one" }
```

Cargo 는 workspace 의 크레이트가 서로 의존한다고 가정하지 않으므로 종속성 관계를 명시적으로 지정해야 합니다.

다음으로, `adder` 크레이트에서 (`add_one` 크레이트에서) `add_one` 함수를 사용해 보겠습니다. `adder/src/main.rs` 파일을 열고 맨 위에 `use` 줄을 추가하여 새 `add_one` 라이브러리 크레이트를 범위 내로 가져옵니다. 그런 다음 Listing 14-7 과 같이 `main` 함수를 변경하여 `add_one` 함수를 호출합니다.

파일 이름: `adder/src/main.rs`

```rust
use add_one;

fn main() {
    let num = 10;
    println!(
        "Hello, world! {num} plus one is {}!",
        add_one::add_one(num)
    );
}
```

Listing 14-7: `adder` 크레이트에서 `add_one` 라이브러리 크레이트 사용하기

최상위 _add_ 디렉토리에서 `cargo build`를 실행하여 workspace 를 빌드해 보겠습니다!

```bash
$ cargo build
   Compiling add_one v0.1.0 (file:///projects/add/add_one)
   Compiling adder v0.1.0 (file:///projects/add/adder)
    Finished dev [unoptimized + debuginfo] target(s) in 0.68s
```

`add` 디렉토리에서 바이너리 크레이트를 실행하려면 `-p` 인자와 패키지 이름을 사용하여 `cargo run`으로 workspace 에서 실행하려는 패키지를 지정할 수 있습니다.

```bash
$ cargo run -p adder
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/adder`
Hello, world! 10 plus one is 11!
```

이것은 `add_one` 크레이트에 의존하는 `adder/src/main.rs`의 코드를 실행합니다.
