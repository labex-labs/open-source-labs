# Newtype 패턴을 사용하여 외부 트레이트 구현하기

"타입에 트레이트 구현하기"에서, 트레이트 또는 타입, 또는 둘 다가 우리 크레이트에 로컬인 경우에만 타입에 트레이트를 구현할 수 있다는 고아 규칙 (orphan rule) 을 언급했습니다. *newtype 패턴*을 사용하여 이 제한을 우회할 수 있습니다. 이 패턴은 튜플 구조체에서 새로운 타입을 생성하는 것을 포함합니다. (튜플 구조체는 "이름 없는 필드를 사용하여 다른 타입 생성하기"에서 다루었습니다.) 튜플 구조체는 하나의 필드를 가지며, 트레이트를 구현하려는 타입 주위에 얇은 래퍼 (wrapper) 가 됩니다. 그러면 래퍼 타입은 우리 크레이트에 로컬이 되며, 래퍼에 트레이트를 구현할 수 있습니다. *Newtype*은 Haskell 프로그래밍 언어에서 유래된 용어입니다. 이 패턴을 사용하는 데는 런타임 성능 저하가 없으며, 래퍼 타입은 컴파일 시간에 제거됩니다.

예를 들어, 고아 규칙으로 인해 직접 수행할 수 없는 `Vec<T>`에 `Display`를 구현하고 싶다고 가정해 보겠습니다. `Display` 트레이트와 `Vec<T>` 타입은 우리 크레이트 외부에서 정의되기 때문입니다. `Vec<T>`의 인스턴스를 보유하는 `Wrapper` 구조체를 만들 수 있습니다. 그런 다음 Listing 19-23 과 같이 `Wrapper`에 `Display`를 구현하고 `Vec<T>` 값을 사용할 수 있습니다.

Filename: `src/main.rs`

```rust
use std::fmt;

struct Wrapper(Vec<String>);

impl fmt::Display for Wrapper {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "[{}]", self.0.join(", "))
    }
}

fn main() {
    let w = Wrapper(vec![
        String::from("hello"),
        String::from("world"),
    ]);
    println!("w = {w}");
}
```

Listing 19-23: `Display`를 구현하기 위해 `Vec<String>` 주위에 `Wrapper` 타입을 생성

`Display`의 구현은 내부 `Vec<T>`에 접근하기 위해 `self.0`을 사용합니다. `Wrapper`가 튜플 구조체이고 `Vec<T>`가 튜플의 인덱스 0 에 있는 항목이기 때문입니다. 그런 다음 `Wrapper`에서 `Display` 타입의 기능을 사용할 수 있습니다.

이 기술을 사용하는 단점은 `Wrapper`가 새로운 타입이므로, 보유하고 있는 값의 메서드가 없다는 것입니다. `Vec<T>`의 모든 메서드를 `Wrapper`에 직접 구현하여 메서드가 `self.0`에 위임하도록 해야 합니다. 이렇게 하면 `Wrapper`를 정확히 `Vec<T>`처럼 취급할 수 있습니다. 새로운 타입이 내부 타입이 가진 모든 메서드를 갖기를 원한다면, 내부 타입을 반환하도록 `Wrapper`에 `Deref` 트레이트를 구현하는 것이 해결책이 될 것입니다 ( "Deref 를 사용하여 스마트 포인터를 일반 참조처럼 취급하기"에서 `Deref` 트레이트 구현에 대해 논의했습니다). `Wrapper` 타입이 내부 타입의 모든 메서드를 갖기를 원하지 않는 경우 (예: `Wrapper` 타입의 동작을 제한하려는 경우), 원하는 메서드만 수동으로 구현해야 합니다.

이 newtype 패턴은 트레이트가 관련되지 않은 경우에도 유용합니다. 초점을 전환하여 Rust 의 타입 시스템과 상호 작용하는 몇 가지 고급 방법을 살펴보겠습니다.
