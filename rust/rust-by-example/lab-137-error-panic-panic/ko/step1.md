# `panic`

가장 간단한 오류 처리 메커니즘은 `panic`입니다. `panic`은 오류 메시지를 출력하고 스택 언와인딩 (stack unwinding) 을 시작하며, 일반적으로 프로그램을 종료합니다. 여기서는 오류 조건에서 `panic`을 명시적으로 호출합니다.

```rust
fn drink(beverage: &str) {
    // You shouldn't drink too much sugary beverages.
    if beverage == "lemonade" { panic!("AAAaaaaa!!!!"); }

    println!("Some refreshing {} is all I need.", beverage);
}

fn main() {
    drink("water");
    drink("lemonade");
}
```
