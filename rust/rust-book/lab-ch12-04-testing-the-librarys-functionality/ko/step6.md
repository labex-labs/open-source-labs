# 일치하는 줄 저장하기

이 함수를 완성하려면 반환하려는 일치하는 줄을 저장하는 방법이 필요합니다. 이를 위해 `for` 루프 전에 가변 벡터 (mutable vector) 를 만들고 `push` 메서드를 호출하여 벡터에 `line`을 저장할 수 있습니다. `for` 루프 후, 목록 12-19 와 같이 벡터를 반환합니다.

파일 이름: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.contains(query) {
            results.push(line);
        }
    }

    results
}
```

목록 12-19: 일치하는 줄을 저장하여 반환할 수 있도록 함

이제 `search` 함수는 `query`를 포함하는 줄만 반환해야 하며, 테스트가 통과해야 합니다. 테스트를 실행해 보겠습니다.

```bash
$ cargo test
--snip--
running 1 test
test tests::one_result ... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
0
filtered out
finished in 0.00s
```

테스트가 통과했으므로 작동하는 것을 알 수 있습니다!

이 시점에서 동일한 기능을 유지하면서 테스트를 통과시키는 동안 search 함수의 구현을 리팩터링할 기회를 고려할 수 있습니다. search 함수의 코드는 그다지 나쁘지 않지만 이터레이터의 몇 가지 유용한 기능을 활용하지 않습니다. 13 장에서 이 예제로 돌아가 이터레이터를 자세히 살펴보고 개선 방법을 살펴보겠습니다.
