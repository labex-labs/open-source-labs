# if/else

`if`-`else`를 사용한 분기는 다른 언어와 유사합니다. 많은 언어와 달리 부울 조건은 괄호로 묶을 필요가 없으며, 각 조건 뒤에는 블록이 따라옵니다. `if`-`else` 조건문은 표현식이며, 모든 분기는 같은 형식을 반환해야 합니다.

```rust
fn main() {
    let n = 5;

    if n < 0 {
        print!("{} is negative", n);
    } else if n > 0 {
        print!("{} is positive", n);
    } else {
        print!("{} is zero", n);
    }

    let big_n =
        if n < 10 && n > -10 {
            println!(", and is a small number, increase ten-fold");

            // 이 표현식은 `i32` 를 반환합니다.
            10 * n
        } else {
            println!(", and is a big number, halve the number");

            // 이 표현식도 `i32` 를 반환해야 합니다.
            n / 2
            // TODO ^ 세미콜론으로 이 표현식을 억제해 보세요.
        };
    //   ^ 여기에 세미콜론을 넣는 것을 잊지 마세요! 모든 `let` 바인딩에는 필요합니다.

    println!("{} -> {}", n, big_n);
}
```
