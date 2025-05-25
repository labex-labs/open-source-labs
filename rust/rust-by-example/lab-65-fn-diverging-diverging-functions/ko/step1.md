# 발산 함수 (Diverging functions)

발산 함수는 절대로 반환하지 않습니다. `!`로 표시되며, 이는 빈 타입입니다.

```rust
fn foo() -> ! {
    panic!("This call never returns.");
}
```

다른 모든 타입과 달리, 이 타입은 가능한 값의 집합이 비어 있기 때문에 인스턴스화될 수 없습니다. `()` 타입과는 다르다는 점에 유의하세요. `()` 타입은 정확히 하나의 가능한 값을 갖습니다.

예를 들어, 이 함수는 일반적으로 반환하지만 반환 값에는 정보가 없습니다.

```rust
fn some_fn() {
    ()
}

fn main() {
    let _a: () = some_fn();
    println!("This function returns and you can see this line.");
}
```

반면에 이 함수는 호출자에게 제어를 절대로 반환하지 않습니다.

```rust
#![feature(never_type)]

fn main() {
    let x: ! = panic!("This call never returns.");
    println!("You will never see this line!");
}
```

이 개념이 추상적으로 보일 수 있지만 실제로 매우 유용하고 자주 편리합니다. 이 타입의 주요 장점은 다른 모든 타입으로 캐스팅될 수 있기 때문에 `match` 분기와 같이 정확한 타입이 필요한 곳에서 사용할 수 있다는 것입니다. 이를 통해 다음과 같은 코드를 작성할 수 있습니다.

```rust
fn main() {
    fn sum_odd_numbers(up_to: u32) -> u32 {
        let mut acc = 0;
        for i in 0..up_to {
            // 이 match 표현식의 반환 타입은 "addition" 변수의 타입 때문에 u32 여야 합니다.
            let addition: u32 = match i%2 == 1 {
                // "i" 변수는 u32 타입이므로 문제 없습니다.
                true => i,
                // 반면에 "continue" 표현식은 u32 를 반환하지 않지만, 절대로 반환하지 않기 때문에 match 표현식의 타입 요구 사항을 위반하지 않습니다.
                false => continue,
            };
            acc += addition;
        }
        acc
    }
    println!("Sum of odd numbers up to 9 (excluding): {}", sum_odd_numbers(9));
}
```

또한 네트워크 서버와 같이 영원히 루프하는 함수 (예: `loop {}`) 또는 프로세스를 종료하는 함수 (예: `exit()`) 의 반환 타입이기도 합니다.
