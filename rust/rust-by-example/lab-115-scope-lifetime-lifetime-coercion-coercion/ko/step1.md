# 강제 변환 (Coercion)

더 긴 생명주기는 일반적으로 작동하지 않는 범위 내에서 작동하도록 더 짧은 생명주기로 강제 변환될 수 있습니다. 이는 Rust 컴파일러에 의한 추론된 강제 변환 형태로 나타나며, 생명주기 차이를 선언하는 형태로도 나타납니다.

```rust
// 여기서 Rust 는 가능한 가장 짧은 생명주기를 추론합니다.
// 그런 다음 두 참조는 해당 생명주기로 강제 변환됩니다.
fn multiply<'a>(first: &'a i32, second: &'a i32) -> i32 {
    first * second
}

// `<'a: 'b, 'b>`는 생명주기 `'a` 가 최소한 `'b` 만큼 길다는 의미로 읽습니다.
// 여기서 `&'a i32`를 입력받아 강제 변환의 결과로 `&'b i32`를 반환합니다.
fn choose_first<'a: 'b, 'b>(first: &'a i32, _: &'b i32) -> &'b i32 {
    first
}

fn main() {
    let first = 2; // 더 긴 생명주기

    {
        let second = 3; // 더 짧은 생명주기

        println!("The product is {}", multiply(&first, &second));
        println!("{} is the first", choose_first(&first, &second));
    };
}
```
