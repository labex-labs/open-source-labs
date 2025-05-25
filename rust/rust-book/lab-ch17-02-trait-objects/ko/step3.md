# 트레이트 구현하기

이제 `Draw` 트레이트를 구현하는 몇 가지 타입을 추가해 보겠습니다. `Button` 타입을 제공할 것입니다. 다시 말하지만, 실제로 GUI 라이브러리를 구현하는 것은 이 책의 범위를 벗어나므로, `draw` 메서드는 본문에 유용한 구현을 갖지 않습니다. 구현이 어떻게 보일지 상상하기 위해, `Button` 구조체는 Listing 17-7 에 표시된 것처럼 `width`, `height`, `label` 필드를 가질 수 있습니다.

파일 이름: `src/lib.rs`

```rust
pub struct Button {
    pub width: u32,
    pub height: u32,
    pub label: String,
}

impl Draw for Button {
    fn draw(&self) {
        // code to actually draw a button
    }
}
```

Listing 17-7: `Draw` 트레이트를 구현하는 `Button` 구조체

`Button`의 `width`, `height`, `label` 필드는 다른 구성 요소의 필드와 다를 것입니다. 예를 들어, `TextField` 타입은 동일한 필드와 `placeholder` 필드를 가질 수 있습니다. 화면에 그리려는 각 타입은 `Draw` 트레이트를 구현하지만, `Button`이 여기에서 (언급했듯이 실제 GUI 코드가 없는) 와 같이 해당 특정 타입을 그리는 방법을 정의하기 위해 `draw` 메서드에서 다른 코드를 사용할 것입니다. 예를 들어, `Button` 타입은 사용자가 버튼을 클릭했을 때 발생하는 것과 관련된 메서드를 포함하는 추가적인 `impl` 블록을 가질 수 있습니다. 이러한 종류의 메서드는 `TextField`와 같은 타입에는 적용되지 않습니다.

우리 라이브러리를 사용하는 사람이 `width`, `height`, `options` 필드를 가진 `SelectBox` 구조체를 구현하기로 결정하면, Listing 17-8 에 표시된 것처럼 `SelectBox` 타입에 `Draw` 트레이트를 구현할 것입니다.

파일 이름: `src/main.rs`

```rust
use gui::Draw;

struct SelectBox {
    width: u32,
    height: u32,
    options: Vec<String>,
}

impl Draw for SelectBox {
    fn draw(&self) {
        // code to actually draw a select box
    }
}
```

Listing 17-8: `gui`를 사용하고 `SelectBox` 구조체에 `Draw` 트레이트를 구현하는 다른 크레이트

이제 우리 라이브러리의 사용자는 `Screen` 인스턴스를 생성하기 위해 `main` 함수를 작성할 수 있습니다. `Screen` 인스턴스에, 각 항목을 `Box<T>`에 넣어 트레이트 객체가 되도록 하여 `SelectBox`와 `Button`을 추가할 수 있습니다. 그런 다음 `Screen` 인스턴스에서 `run` 메서드를 호출할 수 있으며, 이 메서드는 각 구성 요소에서 `draw`를 호출합니다. Listing 17-9 는 이 구현을 보여줍니다.

파일 이름: `src/main.rs`

```rust
use gui::{Button, Screen};

fn main() {
    let screen = Screen {
        components: vec![
            Box::new(SelectBox {
                width: 75,
                height: 10,
                options: vec![
                    String::from("Yes"),
                    String::from("Maybe"),
                    String::from("No"),
                ],
            }),
            Box::new(Button {
                width: 50,
                height: 10,
                label: String::from("OK"),
            }),
        ],
    };

    screen.run();
}
```

Listing 17-9: 동일한 트레이트를 구현하는 서로 다른 타입의 값을 저장하기 위해 트레이트 객체 사용하기

우리가 라이브러리를 작성했을 때, 누군가가 `SelectBox` 타입을 추가할 수 있다는 것을 몰랐지만, `Screen` 구현은 `SelectBox`가 `Draw` 트레이트를 구현했기 때문에 새 타입에서 작동하고 그릴 수 있었습니다. 즉, `draw` 메서드를 구현합니다.

이 개념은 - 값의 구체적인 타입보다는 값이 응답하는 메시지에만 관심을 갖는 것 - 동적으로 타입이 지정된 언어의 _덕 타이핑_ 개념과 유사합니다. 오리가 걷고 오리처럼 꽥꽥거린다면, 그것은 오리임에 틀림없습니다! Listing 17-5 의 `Screen`에서 `run`의 구현에서, `run`은 각 구성 요소의 구체적인 타입이 무엇인지 알 필요가 없습니다. 구성 요소가 `Button`의 인스턴스인지 `SelectBox`의 인스턴스인지 확인하지 않고, 단순히 구성 요소에서 `draw` 메서드를 호출합니다. `components` 벡터의 값의 타입으로 `Box<dyn Draw>`를 지정함으로써, 우리는 `Screen`이 `draw` 메서드를 호출할 수 있는 값을 필요로 하도록 정의했습니다.

트레이트 객체와 Rust 의 타입 시스템을 사용하여 덕 타이핑을 사용하는 코드와 유사한 코드를 작성하는 것의 장점은 런타임에 값이 특정 메서드를 구현하는지 확인할 필요가 없고, 값이 메서드를 구현하지 않지만 어쨌든 호출하는 경우 오류가 발생할까 걱정할 필요가 없다는 것입니다. Rust 는 트레이트 객체가 필요로 하는 트레이트를 값이 구현하지 않으면 코드를 컴파일하지 않습니다.

예를 들어, Listing 17-10 은 `String`을 구성 요소로 사용하여 `Screen`을 생성하려고 하면 어떻게 되는지 보여줍니다.

파일 이름: `src/main.rs`

```rust
use gui::Screen;

fn main() {
    let screen = Screen {
        components: vec![Box::new(String::from("Hi"))],
    };

    screen.run();
}
```

Listing 17-10: 트레이트 객체의 트레이트를 구현하지 않는 타입을 사용하려는 시도

`String`이 `Draw` 트레이트를 구현하지 않기 때문에 이 오류가 발생합니다.

```bash
error[E0277]: the trait bound `String: Draw` is not satisfied
 --> src/main.rs:5:26
  |
5 |         components: vec![Box::new(String::from("Hi"))],
  |                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ the trait `Draw` is
not implemented for `String`
  |
  = note: required for the cast to the object type `dyn Draw`
```

이 오류는 우리가 `Screen`에 전달하려는 것을 의도하지 않았고 다른 타입을 전달해야 하거나, `Screen`이 `draw`를 호출할 수 있도록 `String`에 `Draw`를 구현해야 함을 알려줍니다.
