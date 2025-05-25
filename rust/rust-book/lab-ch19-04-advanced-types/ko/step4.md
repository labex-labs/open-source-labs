# 결코 반환하지 않는 Never 타입

Rust 에는 `!`라는 특수한 타입이 있습니다. 이 타입은 타입 이론 (type theory) 용어로는 *empty type*으로 알려져 있는데, 값을 갖지 않기 때문입니다. 우리는 이 타입을 *never type*이라고 부르는 것을 선호합니다. 함수가 결코 반환하지 않을 때 반환 타입의 자리에 있기 때문입니다. 다음은 예시입니다.

```rust
fn bar() -> ! {
    --snip--
}
```

이 코드는 "함수 `bar`는 never 를 반환한다"로 읽습니다. never 를 반환하는 함수를 *diverging functions*라고 부릅니다. `!` 타입의 값을 생성할 수 없으므로, `bar`는 절대로 반환할 수 없습니다.

하지만 값을 생성할 수 없는 타입은 어떤 용도로 사용될까요? 숫자 맞추기 게임의 일부인 Listing 2-5 의 코드를 기억하십시오. Listing 19-26 에서 그 일부를 재현했습니다.

```rust
let guess: u32 = match guess.trim().parse() {
    Ok(num) => num,
    Err(_) => continue,
};
```

Listing 19-26: `continue`로 끝나는 arm 이 있는 `match`

당시 이 코드의 몇 가지 세부 사항을 건너뛰었습니다. "The match Control Flow Construct"에서 `match` arm 은 모두 동일한 타입을 반환해야 한다고 논의했습니다. 따라서 예를 들어, 다음 코드는 작동하지 않습니다.

```rust
let guess = match guess.trim().parse() {
    Ok(_) => 5,
    Err(_) => "hello",
};
```

이 코드에서 `guess`의 타입은 정수 _및_ 문자열이어야 하며, Rust 는 `guess`가 하나의 타입만 갖도록 요구합니다. 그렇다면 `continue`는 무엇을 반환할까요? Listing 19-26 에서 한 arm 에서 `u32`를 반환하고 다른 arm 이 `continue`로 끝나는 것을 어떻게 허용했습니까?

짐작하셨겠지만, `continue`는 `!` 값을 갖습니다. 즉, Rust 가 `guess`의 타입을 계산할 때, 두 match arm 을 모두 살펴봅니다. 전자는 `u32` 값을 갖고, 후자는 `!` 값을 갖습니다. `!`는 값을 가질 수 없으므로, Rust 는 `guess`의 타입이 `u32`라고 결정합니다.

이 동작을 설명하는 공식적인 방법은 `!` 타입의 표현식이 다른 모든 타입으로 강제될 수 있다는 것입니다. `continue`가 값을 반환하지 않기 때문에 이 `match` arm 을 `continue`로 끝낼 수 있습니다. 대신, 제어를 루프의 맨 위로 다시 이동시키므로, `Err`의 경우 `guess`에 값을 할당하지 않습니다.

never 타입은 `panic!` 매크로와도 유용합니다. `Option<T>` 값에서 값을 생성하거나 다음과 같이 패닉 (panic) 을 발생시키기 위해 호출하는 `unwrap` 함수를 기억하십시오.

```rust
impl<T> Option<T> {
    pub fn unwrap(self) -> T {
        match self {
            Some(val) => val,
            None => panic!(
                "called `Option::unwrap()` on a `None` value"
            ),
        }
    }
}
```

이 코드에서는 Listing 19-26 의 `match`와 동일한 일이 발생합니다. Rust 는 `val`이 `T` 타입을 갖고 `panic!`이 `!` 타입을 갖는 것을 보므로, 전체 `match` 표현식의 결과는 `T`입니다. 이 코드는 `panic!`이 값을 생성하지 않고 프로그램을 종료하기 때문에 작동합니다. `None`의 경우, `unwrap`에서 값을 반환하지 않으므로 이 코드는 유효합니다.

`!` 타입을 갖는 마지막 표현식은 `loop`입니다.

    print!("forever ");

    loop {
        print!("and ever ");
    }

여기서 루프는 결코 끝나지 않으므로 `!`가 표현식의 값입니다. 그러나 `break`를 포함하면 루프가 `break`에 도달할 때 종료되므로 그렇지 않습니다.
