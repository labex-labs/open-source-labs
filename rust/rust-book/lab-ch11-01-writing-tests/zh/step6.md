# 使用 `should_panic` 检查是否发生恐慌

除了检查返回值之外，检查我们的代码是否按预期处理错误情况也很重要。例如，考虑我们在清单 9 - 13 中创建的 `Guess` 类型。其他使用 `Guess` 的代码依赖于 `Guess` 实例将只包含 1 到 100 之间的值这一保证。我们可以编写一个测试来确保尝试创建一个值超出该范围的 `Guess` 实例时会导致程序恐慌。

我们通过在测试函数上添加 `should_panic` 属性来做到这一点。如果函数内部的代码导致程序恐慌，则测试通过；如果函数内部的代码没有导致程序恐慌，则测试失败。

清单 11 - 8 展示了一个测试，用于检查 `Guess::new` 的错误情况是否在我们期望的时候发生。

    // src/lib.rs
    pub struct Guess {
        value: i32,
    }

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 || value > 100 {
                panic!(
                    "Guess value must be between 1 and 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        #[should_panic]
        fn greater_than_100() {
            Guess::new(200);
        }
    }

清单 11 - 8：测试一个条件是否会导致程序恐慌！

我们将 `#[should_panic]` 属性放在 `#[test]` 属性之后，以及它所应用的测试函数之前。让我们看看这个测试通过时的结果：

    running 1 test
    test tests::greater_than_100 - should panic... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

看起来不错！现在让我们通过移除 `new` 函数中当值大于 100 时会导致程序恐慌的条件来在代码中引入一个错误：

    // src/lib.rs
    --snip--

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 {
                panic!(
                    "Guess value must be between 1 and 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

当我们运行清单 11 - 8 中的测试时，它将会失败：

    running 1 test
    test tests::greater_than_100 - should panic... FAILED

    failures:

    ---- tests::greater_than_100 stdout ----
    note: test did not panic as expected

    failures:
        tests::greater_than_100

    test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

在这种情况下，我们没有得到一个非常有用的消息，但是当我们查看测试函数时，我们会看到它被标注了 `#[should_panic]`。我们得到的失败结果意味着测试函数中的代码没有导致程序恐慌。

使用 `should_panic` 的测试可能不够精确。即使测试因为与我们预期不同的原因而导致程序恐慌，`should_panic` 测试也会通过。为了使 `should_panic` 测试更精确，我们可以向 `should_panic` 属性添加一个可选的 `expected` 参数。测试框架将确保失败消息包含提供的文本。例如，考虑清单 11 - 9 中 `Guess` 的修改后的代码，其中 `new` 函数根据值是太小还是太大而以不同的消息导致程序恐慌。

    // src/lib.rs
    --snip--

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 {
                panic!(
                    "Guess value must be greater than or equal to 1, got {}.",
                    value
                );
            } else if value > 100 {
                panic!(
                    "Guess value must be less than or equal to 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        #[should_panic(expected = "less than or equal to 100")]
        fn greater_than_100() {
            Guess::new(200);
        }
    }

清单 11 - 9：测试一个包含指定子字符串的恐慌消息的 `panic!`

这个测试将会通过，因为我们放在 `should_panic` 属性的 `expected` 参数中的值是 `Guess::new` 函数导致程序恐慌时的消息的一个子字符串。我们本可以指定我们期望的整个恐慌消息，在这种情况下就是 `Guess value must be less than or equal to 100, got 200`。你选择指定什么取决于恐慌消息中有多少是唯一的或动态的，以及你希望你的测试有多精确。在这种情况下，恐慌消息的一个子字符串就足以确保测试函数中的代码执行了 `else if value > 100` 这个分支。

为了看看当一个带有 `expected` 消息的 `should_panic` 测试失败时会发生什么，让我们再次通过交换 `if value < 1` 和 `else if value > 100` 块的主体来在代码中引入一个错误：

    // src/lib.rs
    --snip--
    if value < 1 {
        panic!(
            "Guess value must be less than or equal to 100, got {}.",
            value
        );
    } else if value > 100 {
        panic!(
            "Guess value must be greater than or equal to 1, got {}.",
            value
        );
    }
    --snip--

这次当我们运行 `should_panic` 测试时，它将会失败：

    running 1 test
    test tests::greater_than_100 - should panic... FAILED

    failures:

    ---- tests::greater_than_100 stdout ----
    thread'main' panicked at 'Guess value must be greater than or equal to 1, got
    200.', src/lib.rs:13:13
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
    note: panic did not contain expected string
          panic message: `"Guess value must be greater than or equal to 1, got
    200."`,
     expected substring: `"less than or equal to 100"`

    failures:
        tests::greater_than_100

    test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out;
    finished in 0.00s

失败消息表明这个测试确实如我们所期望的那样导致了程序恐慌，但是恐慌消息没有包含预期的字符串 `'Guess value must be less than or equal to 100'`。在这种情况下我们得到的恐慌消息是 `Guess value must be greater than or equal to 1, got 200`。现在我们可以开始找出我们的错误在哪里了！
