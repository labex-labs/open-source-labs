# 테스트로서의 문서 주석

문서 주석에 예제 코드 블록을 추가하면 라이브러리 사용 방법을 시연하는 데 도움이 되며, 이렇게 하면 추가적인 보너스가 있습니다. `cargo test`를 실행하면 문서의 코드 예제가 테스트로 실행됩니다! 예제가 있는 문서보다 더 좋은 것은 없습니다. 그러나 코드가 문서 작성 이후 변경되어 작동하지 않는 예제보다 더 나쁜 것은 없습니다. 목록 14-1 의 `add_one` 함수에 대한 문서를 사용하여 `cargo test`를 실행하면 테스트 결과에 다음과 같은 섹션이 표시됩니다.

```rust
   Doc-tests my_crate

running 1 test
test src/lib.rs - add_one (line 5) ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.27s
```

이제 함수 또는 예제를 변경하여 예제의 `assert_eq!`가 패닉되도록 하고 `cargo test`를 다시 실행하면 문서 테스트가 예제와 코드가 서로 동기화되지 않음을 감지하는 것을 볼 수 있습니다!
