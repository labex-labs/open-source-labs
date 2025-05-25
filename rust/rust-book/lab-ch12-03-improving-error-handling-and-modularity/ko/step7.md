# 오류 메시지 개선

목록 12-8 에서 `new` 함수에 슬라이스가 인덱스 1 과 인덱스 2 에 접근하기 전에 충분히 긴지 확인하는 검사를 추가합니다. 슬라이스가 충분히 길지 않으면 프로그램이 패닉 (panic) 상태가 되고 더 나은 오류 메시지를 표시합니다.

파일 이름: `src/main.rs`

```rust
--snip--
fn new(args: &[String]) -> Config {
    if args.len() < 3 {
        panic!("not enough arguments");
    }
    --snip--
```

목록 12-8: 인수의 수에 대한 검사 추가

이 코드는 목록 9-13 에서 작성한 `Guess::new` 함수와 유사합니다. 여기서 `value` 인수가 유효한 값의 범위를 벗어났을 때 `panic!`을 호출했습니다. 여기서는 값의 범위를 확인하는 대신 `args`의 길이가 최소 `3`인지 확인하고 나머지 함수는 이 조건이 충족되었다고 가정하고 작동할 수 있습니다. `args`에 세 개 미만의 항목이 있으면 이 조건이 `true`가 되고, `panic!` 매크로를 호출하여 프로그램을 즉시 종료합니다.

`new`에 이 몇 줄의 코드를 추가하여 인수가 없는 상태로 프로그램을 다시 실행하여 오류가 어떻게 보이는지 확인해 보겠습니다.

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep`
thread 'main' panicked at 'not enough arguments',
src/main.rs:26:13
note: run with `RUST_BACKTRACE=1` environment variable to display
a backtrace
```

이 출력은 더 좋습니다. 이제 합리적인 오류 메시지가 있습니다. 그러나 사용자에게 제공하고 싶지 않은 불필요한 정보도 있습니다. 아마도 목록 9-13 에서 사용한 기술이 여기에서 사용하기에 가장 좋은 방법은 아닐 것입니다. 9 장에서 논의했듯이 `panic!` 호출은 사용 문제보다는 프로그래밍 문제에 더 적합합니다. 대신, 9 장에서 배운 다른 기술, 즉 성공 또는 오류를 나타내는 `Result`를 반환하는 기술을 사용합니다.
