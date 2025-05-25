# 내부 가변성의 사용 사례: 모의 객체 (Mock Objects)

때때로 프로그래머는 특정 동작을 관찰하고 올바르게 구현되었는지 확인하기 위해 다른 타입 대신에 한 타입을 사용합니다. 이 자리 표시자 타입은 *테스트 더블 (test double)*이라고 합니다. 영화 제작에서 스턴트 배우와 같은 의미로 생각해보세요. 스턴트 배우는 배우를 대신하여 특히 까다로운 장면을 수행합니다. 테스트 더블은 테스트를 실행할 때 다른 타입을 대신합니다. *모의 객체 (mock objects)*는 테스트 중에 발생하는 내용을 기록하여 올바른 작업이 수행되었는지 확인할 수 있는 특정 유형의 테스트 더블입니다.

Rust 는 다른 언어에서 객체를 사용하는 것과 같은 방식으로 객체를 가지고 있지 않으며, 다른 언어에서처럼 표준 라이브러리에 모의 객체 기능이 내장되어 있지 않습니다. 그러나 모의 객체와 동일한 목적을 수행하는 구조체를 확실히 만들 수 있습니다.

다음은 테스트할 시나리오입니다. 최대 값에 대한 값을 추적하고 현재 값이 최대 값에 얼마나 가까운지에 따라 메시지를 보내는 라이브러리를 만들 것입니다. 이 라이브러리는 예를 들어 사용자가 허용된 API 호출 횟수에 대한 할당량을 추적하는 데 사용할 수 있습니다.

저희 라이브러리는 값의 최대 값에 대한 근접성을 추적하고 어떤 시점에 어떤 메시지를 보내야 하는지에 대한 기능만 제공합니다. 저희 라이브러리를 사용하는 애플리케이션은 메시지를 보내는 메커니즘을 제공해야 합니다. 애플리케이션은 애플리케이션에 메시지를 넣거나, 이메일을 보내거나, 문자 메시지를 보내거나, 다른 작업을 수행할 수 있습니다. 라이브러리는 그 세부 사항을 알 필요가 없습니다. 필요한 것은 `Messenger`라는 트레이트를 구현하는 것입니다. Listing 15-20 은 라이브러리 코드를 보여줍니다.

파일 이름: `src/lib.rs`

```rust
pub trait Messenger {
  1 fn send(&self, msg: &str);
}

pub struct LimitTracker<'a, T: Messenger> {
    messenger: &'a T,
    value: usize,
    max: usize,
}

impl<'a, T> LimitTracker<'a, T>
where
    T: Messenger,
{
    pub fn new(
        messenger: &'a T,
        max: usize
    ) -> LimitTracker<'a, T> {
        LimitTracker {
            messenger,
            value: 0,
            max,
        }
    }

  2 pub fn set_value(&mut self, value: usize) {
        self.value = value;

        let percentage_of_max =
            self.value as f64 / self.max as f64;

        if percentage_of_max >= 1.0 {
            self.messenger
                .send("Error: You are over your quota!");
        } else if percentage_of_max >= 0.9 {
            self.messenger
                .send("Urgent: You're at 90% of your quota!");
        } else if percentage_of_max >= 0.75 {
            self.messenger
                .send("Warning: You're at 75% of your quota!");
        }
    }
}
```

Listing 15-20: 값의 최대 값에 대한 근접성을 추적하고 값이 특정 수준에 도달하면 경고하는 라이브러리

이 코드의 중요한 부분 중 하나는 `Messenger` 트레이트가 `self`에 대한 불변 참조와 메시지 텍스트를 받는 `send`라는 메서드를 하나 가지고 있다는 것입니다 \[1]. 이 트레이트는 모의 객체가 실제 객체와 동일한 방식으로 사용될 수 있도록 모의 객체가 구현해야 하는 인터페이스입니다. 또 다른 중요한 부분은 `LimitTracker`의 `set_value` 메서드의 동작을 테스트하려는 것입니다 \[2]. `value` 매개변수에 전달하는 값을 변경할 수 있지만, `set_value`는 어떠한 것도 반환하지 않으므로 어떠한 단언도 할 수 없습니다. `Messenger` 트레이트를 구현하는 것과 `max`에 대한 특정 값을 사용하여 `LimitTracker`를 생성하면, `value`에 대해 다른 숫자를 전달할 때 메신저가 적절한 메시지를 보내도록 할 수 있기를 원합니다.

`send`를 호출할 때 이메일이나 문자 메시지를 보내는 대신, 보내도록 지시받은 메시지만 추적하는 모의 객체가 필요합니다. 모의 객체의 새 인스턴스를 생성하고, 모의 객체를 사용하는 `LimitTracker`를 생성하고, `LimitTracker`에서 `set_value` 메서드를 호출한 다음, 모의 객체에 예상되는 메시지가 있는지 확인할 수 있습니다. Listing 15-21 은 이를 수행하기 위해 모의 객체를 구현하려는 시도를 보여주지만, 차용 검사기는 이를 허용하지 않습니다.

파일 이름: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

  1 struct MockMessenger {
      2 sent_messages: Vec<String>,
    }

    impl MockMessenger {
      3 fn new() -> MockMessenger {
            MockMessenger {
                sent_messages: vec![],
            }
        }
    }

  4 impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
          5 self.sent_messages.push(String::from(message));
        }
    }

    #[test]
  6 fn it_sends_an_over_75_percent_warning_message() {
        let mock_messenger = MockMessenger::new();
        let mut limit_tracker = LimitTracker::new(
            &mock_messenger,
            100
        );

        limit_tracker.set_value(80);

        assert_eq!(mock_messenger.sent_messages.len(), 1);
    }
}
```

Listing 15-21: 차용 검사기가 허용하지 않는 `MockMessenger`를 구현하려는 시도

이 테스트 코드는 `sent_messages` 필드에 `String` 값의 `Vec`를 사용하여 보낼 메시지를 추적하는 `MockMessenger` 구조체를 정의합니다 \[1, 2]. 또한 빈 메시지 목록으로 시작하는 새 `MockMessenger` 값을 편리하게 생성하기 위해 연결된 함수 `new` \[3]을 정의합니다. 그런 다음 `MockMessenger`에 `LimitTracker`를 제공할 수 있도록 `MockMessenger`에 대한 `Messenger` 트레이트를 구현합니다 \[4]. `send` 메서드의 정의에서 \[5] 매개변수로 전달된 메시지를 가져와 `MockMessenger`의 `sent_messages` 목록에 저장합니다.

테스트에서 `LimitTracker`가 `value`를 `max` 값의 75% 이상으로 설정하도록 지시받을 때 발생하는 상황을 테스트하고 있습니다 \[6]. 먼저, 빈 메시지 목록으로 시작하는 새 `MockMessenger`를 생성합니다. 그런 다음 새 `LimitTracker`를 생성하고 새 `MockMessenger`에 대한 참조와 `max` 값 `100`을 제공합니다. `LimitTracker`에서 `set_value` 메서드를 값 `80`으로 호출합니다. 이는 100 의 75% 이상입니다. 그런 다음 `MockMessenger`가 추적하는 메시지 목록에 이제 하나의 메시지가 있어야 한다고 단언합니다.

그러나 이 테스트에는 다음과 같이 한 가지 문제가 있습니다.

```bash
error[E0596]: cannot borrow `self.sent_messages` as mutable, as it is behind a
`&` reference
  --> src/lib.rs:58:13
   |
2  |     fn send(&self, msg: &str);
   |             ----- help: consider changing that to be a mutable reference:
`&mut self`
...
58 |             self.sent_messages.push(String::from(message));
   |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ `self` is a
`&` reference, so the data it refers to cannot be borrowed as mutable
```

`send` 메서드가 `self`에 대한 불변 참조를 사용하므로 메시지를 추적하기 위해 `MockMessenger`를 수정할 수 없습니다. 또한 오류 텍스트에서 `&mut self`를 사용하라는 제안을 따를 수도 없습니다. 그렇게 하면 `send`의 시그니처가 `Messenger` 트레이트 정의의 시그니처와 일치하지 않기 때문입니다 (시도해보고 어떤 오류 메시지가 나오는지 확인해 보세요).

이것은 내부 가변성이 도움이 될 수 있는 상황입니다! `sent_messages`를 `RefCell<T>` 내에 저장하면 `send` 메서드가 `sent_messages`를 수정하여 본 메시지를 저장할 수 있습니다. Listing 15-22 는 그 모습입니다.

파일 이름: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;
    use std::cell::RefCell;

    struct MockMessenger {
      1 sent_messages: RefCell<Vec<String>>,
    }

    impl MockMessenger {
        fn new() -> MockMessenger {
            MockMessenger {
              2 sent_messages: RefCell::new(vec![]),
            }
        }
    }

    impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
            self.sent_messages
              3 .borrow_mut()
                .push(String::from(message));
        }
    }

    #[test]
    fn it_sends_an_over_75_percent_warning_message() {
        --snip--

        assert_eq!(
          4 mock_messenger.sent_messages.borrow().len(),
            1
        );
    }
}
```

Listing 15-22: 외부 값은 불변으로 간주되는 동안 내부 값을 변경하기 위해 `RefCell<T>` 사용

`sent_messages` 필드는 이제 `Vec<String>` 대신 `RefCell<Vec<String>>` 타입입니다 \[1]. `new` 함수에서 빈 벡터 \[2] 주위에 새 `RefCell<Vec<String>>` 인스턴스를 생성합니다.

`send` 메서드의 구현에서 첫 번째 매개변수는 여전히 `self`의 불변 차용이며, 이는 트레이트 정의와 일치합니다. `self.sent_messages` \[3]에서 `RefCell<Vec<String>>`에 대해 `borrow_mut`을 호출하여 `RefCell<Vec<String>>` 내부의 값, 즉 벡터에 대한 가변 참조를 가져옵니다. 그런 다음 벡터에 대한 가변 참조에서 `push`를 호출하여 테스트 중에 전송된 메시지를 추적할 수 있습니다.

마지막으로 변경해야 할 사항은 단언입니다. 내부 벡터에 몇 개의 항목이 있는지 확인하려면 `RefCell<Vec<String>>`에서 `borrow`를 호출하여 벡터에 대한 불변 참조를 가져옵니다 \[4].

이제 `RefCell<T>`를 사용하는 방법을 보았으므로, 작동 방식을 자세히 살펴보겠습니다!
