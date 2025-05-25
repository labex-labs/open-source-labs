# 오류 처리 수정

이제 오류 처리를 수정하는 작업을 수행하겠습니다. `args` 벡터의 인덱스 1 또는 인덱스 2 의 값에 접근하려고 할 때 벡터에 세 개 미만의 항목이 포함되어 있으면 프로그램이 패닉 (panic) 상태가 된다는 것을 기억하십시오. 인수가 없는 상태로 프로그램을 실행해 보십시오. 다음과 같이 표시됩니다.

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep`
thread 'main' panicked at 'index out of bounds: the len is 1 but
the index is 1', src/main.rs:27:21
note: run with `RUST_BACKTRACE=1` environment variable to display
a backtrace
```

`index out of bounds: the len is 1 but the index is 1` 줄은 프로그래머를 위한 오류 메시지입니다. 최종 사용자가 대신 무엇을 해야 하는지 이해하는 데 도움이 되지 않습니다. 이제 수정해 보겠습니다.
