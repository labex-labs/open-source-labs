# 루프에서 반환하기

`loop`의 용도 중 하나는 작업이 성공할 때까지 반복하는 것입니다. 그러나 작업이 값을 반환하는 경우 해당 값을 코드의 나머지 부분으로 전달해야 할 수 있습니다. `break` 뒤에 값을 놓으면 `loop` 표현식에서 반환됩니다.

```rust
fn main() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };

    assert_eq!(result, 20);
}
```
