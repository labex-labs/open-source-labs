# 가변 인터페이스 (Variadic Interfaces)

_가변적 (variadic)_ 인터페이스는 임의의 수의 인수를 받습니다. 예를 들어, `println!`은 형식 문자열에 의해 결정되는 임의의 수의 인수를 받을 수 있습니다.

이전 섹션에서 `calculate!` 매크로를 가변적으로 확장할 수 있습니다.

```rust
macro_rules! calculate {
    // The pattern for a single `eval`
    (eval $e:expr) => {
        {
            let val: usize = $e; // Force types to be integers
            println!("{} = {}", stringify!{$e}, val);
        }
    };

    // Decompose multiple `eval`s recursively
    (eval $e:expr, $(eval $es:expr),+) => {{
        calculate! { eval $e }
        calculate! { $(eval $es),+ }
    }};
}

fn main() {
    calculate! { // Look ma! Variadic `calculate!`!
        eval 1 + 2,
        eval 3 + 4,
        eval (2 * 3) + 1
    }
}
```

출력:

```txt
1 + 2 = 3
3 + 4 = 7
(2 * 3) + 1 = 7
```
