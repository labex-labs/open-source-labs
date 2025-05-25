# 새 프로젝트 설정

새 프로젝트를 설정하려면 1 장에서 생성한 `project` 디렉토리로 이동하여 다음과 같이 Cargo 를 사용하여 새 프로젝트를 만듭니다.

```bash
cargo new guessing_game
cd guessing_game
```

첫 번째 명령인 `cargo new`는 프로젝트 이름 (`guessing_game`) 을 첫 번째 인수로 사용합니다. 두 번째 명령은 새 프로젝트의 디렉토리로 변경합니다.

생성된 `Cargo.toml` 파일을 살펴보십시오.

파일 이름: `Cargo.toml`

```toml
[package]
name = "guessing_game"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at
https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
```

1 장에서 보았듯이 `cargo new`는 "Hello, world!" 프로그램을 생성합니다. `src/main.rs` 파일을 확인하십시오.

파일 이름: `src/main.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

이제 이 "Hello, world!" 프로그램을 컴파일하고 `cargo run` 명령을 사용하여 동일한 단계에서 실행해 보겠습니다.

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50s
     Running `target/debug/guessing_game`
Hello, world!
```

`run` 명령은 이 게임에서 할 것처럼 프로젝트를 빠르게 반복해야 할 때, 다음 반복으로 넘어가기 전에 각 반복을 빠르게 테스트할 때 유용합니다.

`src/main.rs` 파일을 다시 엽니다. 이 파일에 모든 코드를 작성할 것입니다.
