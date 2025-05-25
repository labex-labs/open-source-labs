# if let

일부 경우, 열거형 (enum) 과 일치할 때 `match`는 다소 번거롭습니다. 예를 들어:

```rust
// `optional` 은 `Option<i32>` 타입입니다.
let optional = Some(7);

match optional {
    Some(i) => {
        println!("This is a really long string and `{:?}`", i);
        // ^ `i` 를 option 에서 분리하기 위해 2 개의 들여쓰기가 필요합니다.
    },
    _ => {},
    // ^ `match` 는 모든 경우를 다루어야 하므로 필요합니다.
    // 공간 낭비처럼 보이지 않나요?
};
```

`if let`은 이러한 경우에 더욱 간결하며, 다양한 실패 옵션을 지정할 수 있습니다.

```rust
fn main() {
    // 모두 `Option<i32>` 타입입니다.
    let number = Some(7);
    let letter: Option<i32> = None;
    let emoticon: Option<i32> = None;

    // `if let` 구문은 "만약 `number` 가 `Some(i)` 로 분해되면, 블록 (`{}`) 을 평가한다"는 의미입니다.
    if let Some(i) = number {
        println!("Matched {:?}!", i);
    }

    // 실패 시 지정하려면 else 를 사용합니다.
    if let Some(i) = letter {
        println!("Matched {:?}!", i);
    } else {
        // 분해 실패. 실패 처리로 변경합니다.
        println!("숫자와 일치하지 않았습니다. 문자로 진행하겠습니다!");
    }

    // 다른 실패 조건을 제공합니다.
    let i_like_letters = false;

    if let Some(i) = emoticon {
        println!("Matched {:?}!", i);
    // 분해 실패. 대체 실패 분기를 취해야 하는지 확인하기 위해 `else if` 조건을 평가합니다.
    } else if i_like_letters {
        println!("숫자와 일치하지 않았습니다. 문자로 진행하겠습니다!");
    } else {
        // 조건이 거짓으로 평가되었습니다. 이 분기는 기본 분기입니다.
        println!("문자를 좋아하지 않습니다. 이모티콘으로 진행하겠습니다 :)!");
    }
}
```

마찬가지로, `if let`을 사용하여 모든 열거형 값과 일치시킬 수 있습니다.

```rust
// 예제 열거형
enum Foo {
    Bar,
    Baz,
    Qux(u32)
}

fn main() {
    // 예제 변수 생성
    let a = Foo::Bar;
    let b = Foo::Baz;
    let c = Foo::Qux(100);

    // 변수 a 는 Foo::Bar 와 일치합니다.
    if let Foo::Bar = a {
        println!("a 는 foobar 입니다");
    }

    // 변수 b 는 Foo::Bar 와 일치하지 않습니다.
    // 따라서 아무것도 출력되지 않습니다.
    if let Foo::Bar = b {
        println!("b 는 foobar 입니다");
    }

    // 변수 c 는 값을 갖는 Foo::Qux 와 일치합니다.
    // 이전 예제의 Some() 과 유사합니다.
    if let Foo::Qux(value) = c {
        println!("c 는 {}입니다", value);
    }

    // 바인딩은 `if let`에서도 작동합니다.
    if let Foo::Qux(value @ 100) = c {
        println!("c 는 백입니다");
    }
}
```

또 다른 장점은 `if let`이 매개변수가 없는 열거형 변형과 일치시킬 수 있다는 것입니다. 이는 열거형이 `PartialEq`를 구현하거나 파생하지 않은 경우에도 마찬가지입니다. 이러한 경우 `if Foo::Bar == a`는 열거형 인스턴스를 비교할 수 없기 때문에 컴파일되지 않지만, `if let`은 계속 작동합니다.

도전과제가 있으시나요? 다음 예제를 `if let`을 사용하여 수정해 보세요.

```rust
// 이 열거형은 의도적으로 PartialEq 를 구현하거나 파생하지 않습니다.
// 따라서 아래에서 Foo::Bar == a 를 비교하면 실패합니다.
enum Foo {Bar}

fn main() {
    let a = Foo::Bar;

    // 변수 a 는 Foo::Bar 와 일치합니다.
    if Foo::Bar == a {
    // ^-- 이것은 컴파일 타임 오류를 발생시킵니다. `if let`을 대신 사용하세요.
        println!("a 는 foobar 입니다");
    }
}
```
