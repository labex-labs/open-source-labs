# 도메인 특화 언어 (DSL, Domain Specific Languages)

DSL 은 Rust 매크로에 내장된 미니 "언어"입니다. 매크로 시스템이 일반적인 Rust 구조로 확장되기 때문에 완전히 유효한 Rust 코드이며, 작은 언어처럼 보입니다. 이를 통해 (제한 내에서) 특정 기능에 대한 간결하거나 직관적인 구문을 정의할 수 있습니다.

작은 계산기 API 를 정의하고 싶다고 가정해 보겠습니다. 표현식을 제공하고 출력을 콘솔에 출력하고 싶습니다.

```rust
macro_rules! calculate {
    (eval $e:expr) => {
        {
            let val: usize = $e; // Force types to be integers
            println!("{} = {}", stringify!{$e}, val);
        }
    };
}

fn main() {
    calculate! {
        eval 1 + 2 // hehehe `eval` is _not_ a Rust keyword!
    }

    calculate! {
        eval (1 + 2) * (3 / 4)
    }
}
```

출력:

```txt
1 + 2 = 3
(1 + 2) * (3 / 4) = 0
```

이것은 매우 간단한 예시였습니다.

또한 매크로에서 두 쌍의 중괄호를 확인하십시오. 외부 중괄호는 `macro_rules!` 구문의 일부이며, `()` 또는 `[]` 외에도 사용됩니다.
