# 열거형 (Enums)

`enum` 키워드는 몇 가지 다른 변형 중 하나일 수 있는 타입을 생성할 수 있게 해줍니다. `struct`로 유효한 모든 변형은 `enum`에서도 유효합니다.

```rust
// 웹 이벤트를 분류하기 위해 `enum` 을 생성합니다. 이름과 타입 정보가 함께 변형을 어떻게 지정하는지 확인하세요:
// `PageLoad != PageUnload` 및 `KeyPress(char) != Paste(String)`.
// 각각은 서로 다르고 독립적입니다.
enum WebEvent {
    // `enum` 변형은 `unit-like` 일 수 있으며,
    PageLoad,
    PageUnload,
    // 튜플 구조체와 유사하며,
    KeyPress(char),
    Paste(String),
    // 또는 C-like 구조체일 수 있습니다.
    Click { x: i64, y: i64 },
}

// `WebEvent` enum 을 인수로 받아들이고
// 아무것도 반환하지 않는 함수입니다.
fn inspect(event: WebEvent) {
    match event {
        WebEvent::PageLoad => println!("page loaded"),
        WebEvent::PageUnload => println!("page unloaded"),
        // `enum` 변형 내부에서 `c` 를 분해합니다.
        WebEvent::KeyPress(c) => println!("pressed '{}'.", c),
        WebEvent::Paste(s) => println!("pasted \"{}\".", s),
        // `Click` 을 `x` 와 `y` 로 분해합니다.
        WebEvent::Click { x, y } => {
            println!("clicked at x={}, y={}.", x, y);
        },
    }
}

fn main() {
    let pressed = WebEvent::KeyPress('x');
    // `to_owned()` 는 문자열 슬라이스에서 소유된 `String` 을 생성합니다.
    let pasted  = WebEvent::Paste("my text".to_owned());
    let click   = WebEvent::Click { x: 20, y: 80 };
    let load    = WebEvent::PageLoad;
    let unload  = WebEvent::PageUnload;

    inspect(pressed);
    inspect(pasted);
    inspect(click);
    inspect(load);
    inspect(unload);
}
```

## 타입 별칭 (Type aliases)

타입 별칭을 사용하면 각 열거형 변형을 해당 별칭을 통해 참조할 수 있습니다. 열거형의 이름이 너무 길거나 일반적이고 이름을 바꾸고 싶을 때 유용할 수 있습니다.

```rust
enum VeryVerboseEnumOfThingsToDoWithNumbers {
    Add,
    Subtract,
}

// 타입 별칭을 생성합니다.
type Operations = VeryVerboseEnumOfThingsToDoWithNumbers;

fn main() {
    // 긴 이름을 사용하지 않고 각 변형을 별칭을 통해 참조할 수 있습니다.
    let x = Operations::Add;
}
```

가장 흔하게 볼 수 있는 곳은 `Self` 별칭을 사용하는 `impl` 블록입니다.

```rust
enum VeryVerboseEnumOfThingsToDoWithNumbers {
    Add,
    Subtract,
}

impl VeryVerboseEnumOfThingsToDoWithNumbers {
    fn run(&self, x: i32, y: i32) -> i32 {
        match self {
            Self::Add => x + y,
            Self::Subtract => x - y,
        }
    }
}
```

열거형과 타입 별칭에 대해 더 자세히 알아보려면 이 기능이 Rust 에 안정화되었을 때의 안정화 보고서를 읽어볼 수 있습니다.
