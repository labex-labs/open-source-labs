# 출력 매개변수로서의 클로저

클로저를 입력 매개변수로 사용할 수 있다면, 출력 매개변수로서 클로저를 반환하는 것도 가능해야 합니다. 하지만 익명 클로저 유형은 정의상 알 수 없으므로, `impl Trait`를 사용하여 반환해야 합니다.

클로저를 반환하기 위한 유효한 트레이트는 다음과 같습니다.

- `Fn`
- `FnMut`
- `FnOnce`

이 외에도 모든 캡처가 값으로 발생한다는 것을 나타내는 `move` 키워드를 사용해야 합니다. 이는 참조에 의한 캡처는 함수가 종료되는 즉시 삭제되어 클로저에 유효하지 않은 참조를 남기기 때문입니다.

```rust
fn create_fn() -> impl Fn() {
    let text = "Fn".to_owned();

    move || println!("This is a: {}", text)
}

fn create_fnmut() -> impl FnMut() {
    let text = "FnMut".to_owned();

    move || println!("This is a: {}", text)
}

fn create_fnonce() -> impl FnOnce() {
    let text = "FnOnce".to_owned();

    move || println!("This is a: {}", text)
}

fn main() {
    let fn_plain = create_fn();
    let mut fn_mut = create_fnmut();
    let fn_once = create_fnonce();

    fn_plain();
    fn_mut();
    fn_once();
}
```
