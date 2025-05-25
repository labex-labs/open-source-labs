# 특별히 요청하지 않는 한 일부 테스트 무시하기

때로는 특정 테스트 몇 개를 실행하는 데 시간이 오래 걸릴 수 있으므로, `cargo test`의 대부분의 실행에서 해당 테스트를 제외하고 싶을 수 있습니다. 실행하려는 모든 테스트를 인수로 나열하는 대신, 다음 예제와 같이 `ignore` 속성을 사용하여 시간이 오래 걸리는 테스트에 주석을 달아 제외할 수 있습니다.

파일 이름: `src/lib.rs`

```rust
#[test]
fn it_works() {
    let result = 2 + 2;
    assert_eq!(result, 4);
}

#[test]
#[ignore]
fn expensive_test() {
    // code that takes an hour to run
}
```

`#[test]` 뒤에, 제외하려는 테스트에 `#[ignore]` 줄을 추가합니다. 이제 테스트를 실행하면 `it_works`가 실행되지만 `expensive_test`는 실행되지 않습니다.

```bash
[object Object]
```

`expensive_test` 함수는 `ignored`로 나열됩니다. 무시된 테스트만 실행하려면 `cargo test -- --ignored`를 사용할 수 있습니다.

```bash
[object Object]
```

어떤 테스트를 실행할지 제어하여 `cargo test` 결과가 빠르게 반환되도록 할 수 있습니다. `ignored` 테스트의 결과를 확인하고 결과를 기다릴 시간이 있을 때, `cargo test -- --ignored`를 실행할 수 있습니다. 무시되었는지 여부에 관계없이 모든 테스트를 실행하려면 `cargo test -- --include-ignored`를 실행할 수 있습니다.
