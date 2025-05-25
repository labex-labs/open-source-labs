# 중첩된 트레이트의 모호성 해결

타입은 여러 개의 서로 다른 트레이트를 구현할 수 있습니다. 두 개의 트레이트가 모두 동일한 이름을 요구하는 경우 어떻게 될까요? 예를 들어, 많은 트레이트가 `get()`이라는 메서드를 가질 수 있습니다. 심지어 서로 다른 반환 타입을 가질 수도 있습니다!

다행히, 각 트레이트 구현은 자체적인 `impl` 블록을 가지기 때문에, 어떤 트레이트의 `get` 메서드를 구현하는지 명확합니다.

그 메서드를 *호출*할 때가 되면 어떻게 될까요? 그들 사이의 모호성을 해결하기 위해, 완전한 정규화된 구문 (Fully Qualified Syntax) 을 사용해야 합니다.

```rust
trait UsernameWidget {
    // Get the selected username out of this widget
    fn get(&self) -> String;
}

trait AgeWidget {
    // Get the selected age out of this widget
    fn get(&self) -> u8;
}

// A form with both a UsernameWidget and an AgeWidget
struct Form {
    username: String,
    age: u8,
}

impl UsernameWidget for Form {
    fn get(&self) -> String {
        self.username.clone()
    }
}

impl AgeWidget for Form {
    fn get(&self) -> u8 {
        self.age
    }
}

fn main() {
    let form = Form {
        username: "rustacean".to_owned(),
        age: 28,
    };

    // If you uncomment this line, you'll get an error saying
    // "multiple `get` found". Because, after all, there are multiple methods
    // named `get`.
    // println!("{}", form.get());

    let username = <Form as UsernameWidget>::get(&form);
    assert_eq!("rustacean".to_owned(), username);
    let age = <Form as AgeWidget>::get(&form);
    assert_eq!(28, age);
}
```
