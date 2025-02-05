# 内部可变性的一个用例：模拟对象

有时在测试期间，程序员会使用一种类型来替代另一种类型，以便观察特定行为并断言其实现是否正确。这种占位类型称为**测试替身**。可以把它想象成电影制作中的替身演员，在拍摄特别棘手的场景时，由替身演员代替演员出演。在运行测试时，测试替身会替代其他类型。**模拟对象**是特定类型的测试替身，它会记录测试期间发生的事情，这样你就可以断言是否发生了正确的操作。

Rust 中的对象与其他语言中的对象概念不同，并且 Rust 的标准库中没有像其他一些语言那样内置模拟对象功能。不过，你肯定可以创建一个结构体来实现与模拟对象相同的目的。

下面是我们要测试的场景：我们将创建一个库，该库会根据最大值跟踪一个值，并根据当前值与最大值的接近程度发送消息。例如，这个库可用于跟踪用户允许进行的 API 调用次数配额。

我们的库仅提供跟踪值与最大值的接近程度以及在不同时刻应发送什么消息的功能。使用我们库的应用程序需要提供发送消息的机制：应用程序可以在应用内放置消息、发送电子邮件、发送短信或执行其他操作。库不需要了解这些细节。它所需要的只是实现我们提供的名为 `Messenger` 的 trait 的某个东西。清单 15 - 20 展示了库代码。

文件名：`src/lib.rs`

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

清单 15 - 20：一个用于跟踪值与最大值的接近程度并在值达到特定水平时发出警告的库

这段代码的一个重要部分是，`Messenger` trait 有一个名为 `send` 的方法，该方法接受对 `self` 的不可变引用和消息文本 \[1\]。这个 trait 是我们的模拟对象需要实现的接口，这样模拟对象就可以像真实对象一样被使用。另一个重要部分是，我们想要测试 `LimitTracker` 上的 `set_value` 方法的行为 \[2\]。我们可以更改传递给 `value` 参数的值，但 `set_value` 没有返回任何东西供我们进行断言。我们希望能够说，如果我们使用实现了 `Messenger` trait 的某个东西和特定的 `max` 值创建一个 `LimitTracker`，当我们为 `value` 传递不同的数字时，会告知信使发送适当的消息。

我们需要一个模拟对象，当我们调用 `send` 时，它不会发送电子邮件或短信，而是只跟踪被告知发送的消息。我们可以创建模拟对象的新实例，创建一个使用该模拟对象的 `LimitTracker`，调用 `LimitTracker` 上的 `set_value` 方法，然后检查模拟对象是否有我们期望的消息。清单 15 - 21 展示了尝试实现这样一个模拟对象的代码，但借用检查器不允许这样做。

文件名：`src/lib.rs`

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

清单 15 - 21：尝试实现一个借用检查器不允许的 `MockMessenger`

这段测试代码定义了一个 `MockMessenger` 结构体 \[1\]，它有一个 `sent_messages` 字段，该字段是一个 `String` 值的 `Vec` \[2\]，用于跟踪被告知发送的消息。我们还定义了一个关联函数 `new` \[3\]，以便于创建新的 `MockMessenger` 值，这些值以空消息列表开始。然后我们为 `MockMessenger` 实现 `Messenger` trait \[4\]，这样我们就可以将 `MockMessenger` 传递给 `LimitTracker`。在 `send` 方法的定义中 \[5\]，我们将传入的消息作为参数，并将其存储在 `MockMessenger` 的 `sent_messages` 列表中。

在测试中，我们测试当 `LimitTracker` 被告知将 `value` 设置为超过 `max` 值的 75% 时会发生什么 \[6\]。首先，我们创建一个新的 `MockMessenger`，它将以空消息列表开始。然后我们创建一个新的 `LimitTracker`，并将新的 `MockMessenger` 的引用和 `max` 值 `100` 传递给它。我们使用值 `80` 调用 `LimitTracker` 上的 `set_value` 方法，该值超过了 100 的 75%。然后我们断言 `MockMessenger` 正在跟踪的消息列表现在应该有一条消息。

然而，这段测试有一个问题，如下所示：

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

我们不能修改 `MockMessenger` 来跟踪消息，因为 `send` 方法接受对 `self` 的不可变引用。我们也不能按照错误提示使用 `&mut self`，因为那样 `send` 方法的签名就与 `Messenger` trait 定义中的签名不匹配了（你可以尝试一下，看看会得到什么错误消息）。

在这种情况下，内部可变性就能帮上忙了！我们将把 `sent_messages` 存储在一个 `RefCell<T>` 中，然后 `send` 方法就能够修改 `sent_messages` 来存储我们看到的消息。清单 15 - 22 展示了具体实现。

文件名：`src/lib.rs`

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
              3.borrow_mut()
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

清单 15 - 22：在外部值被视为不可变时使用 `RefCell<T>` 来变异内部值

`sent_messages` 字段现在是 `RefCell<Vec<String>>` 类型 \[1\]，而不是 `Vec<String>`。在 `new` 函数中，我们围绕空向量创建一个新的 `RefCell<Vec<String>>` 实例 \[2\]。

对于 `send` 方法的实现，第一个参数仍然是对 `self` 的不可变借用，这与 trait 定义匹配。我们对 `self.sent_messages` 中的 `RefCell<Vec<String>>` 调用 `borrow_mut` \[3\]，以获取对 `RefCell<Vec<String>>` 内部值（即向量）的可变引用。然后我们可以对向量的可变引用调用 `push` 来跟踪测试期间发送的消息。

我们必须做出的最后一个更改是在断言中：为了查看内部向量中有多少项，我们对 `RefCell<Vec<String>>` 调用 `borrow` 以获取对向量的不可变引用 \[4\]。

现在你已经了解了如何使用 `RefCell<T>`，让我们深入研究一下它是如何工作的！
