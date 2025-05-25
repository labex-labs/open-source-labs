# 동결 (Freezing)

동일한 이름으로 불변하게 바인딩된 데이터는 동결 (freezing) 됩니다. 동결된 데이터는 불변 바인딩의 범위가 종료될 때까지 수정할 수 없습니다.

```rust
fn main() {
    let mut _mutable_integer = 7i32;

    {
        // 불변 `_mutable_integer` 로 그림자화
        let _mutable_integer = _mutable_integer;

        // 오류! 이 범위에서 `_mutable_integer` 는 동결되었습니다.
        _mutable_integer = 50;
        // FIXME ^ 이 줄을 주석 처리하세요.

        // `_mutable_integer` 가 범위를 벗어납니다.
    }

    // 정상! 이 범위에서 `_mutable_integer` 는 동결되지 않았습니다.
    _mutable_integer = 3;
}
```
