# 使用 `assert!` 宏检查结果

标准库提供的 `assert!` 宏，在你想要确保测试中的某个条件求值为 `true` 时非常有用。我们给 `assert!` 宏一个求值为布尔值的参数。如果该值为 `true`，则什么都不会发生，测试通过。如果该值为 `false`，`assert!` 宏会调用 `panic!` 使测试失败。使用 `assert!` 宏有助于我们检查代码是否按预期方式运行。

在清单 5 - 15 中，我们使用了一个 `Rectangle` 结构体和一个 `can_hold` 方法，清单 11 - 5 中再次给出了这些代码。让我们把这段代码放到 `src/lib.rs` 文件中，然后使用 `assert!` 宏为它编写一些测试。

文件名：`src/lib.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

清单 11 - 5：使用第五章中的 `Rectangle` 结构体及其 `can_hold` 方法

`can_hold` 方法返回一个布尔值，这意味着它是使用 `assert!` 宏的完美用例。在清单 11 - 6 中，我们编写了一个测试，通过创建一个宽度为 8、高度为 7 的 `Rectangle` 实例，并断言它可以容纳另一个宽度为 5、高度为 1 的 `Rectangle` 实例，来测试 `can_hold` 方法。

文件名：`src/lib.rs`

```rust
#[cfg(test)]
mod tests {
  1 use super::*;

    #[test]
  2 fn larger_can_hold_smaller() {
      3 let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

      4 assert!(larger.can_hold(&smaller));
    }
}
```

清单 11 - 6：对 `can_hold` 的测试，检查一个较大的矩形是否确实能容纳一个较小的矩形

注意，我们在 `tests` 模块中添加了新的一行：`use super::*;` \[1\]。`tests` 模块是一个常规模块，遵循我们在“模块树中引用项的路径”中介绍的常见可见性规则。因为 `tests` 模块是一个内部模块，我们需要将外部模块中要测试的代码引入到内部模块的作用域中。我们在这里使用了通配符，所以我们在外部模块中定义的任何内容对这个 `tests` 模块都是可用的。

我们将测试命名为 `larger_can_hold_smaller` \[2\]，并创建了所需的两个 `Rectangle` 实例 \[3\]。然后我们调用 `assert!` 宏，并将调用 `larger.can_hold(&smaller)` 的结果作为参数传递给它 \[4\]。这个表达式应该返回 `true`，所以我们的测试应该通过。让我们来验证一下！

    running 1 test
    test tests::larger_can_hold_smaller... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

它确实通过了！让我们再添加一个测试，这次断言一个较小的矩形不能容纳一个较大的矩形：

文件名：`src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn larger_can_hold_smaller() {
        --snip--
    }

    #[test]
    fn smaller_cannot_hold_larger() {
        let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

        assert!(!smaller.can_hold(&larger));
    }
}
```

因为在这种情况下 `can_hold` 函数的正确结果是 `false`，所以在将结果传递给 `assert!` 宏之前，我们需要对其取反。这样，如果 `can_hold` 返回 `false`，我们的测试就会通过：

    running 2 tests
    test tests::larger_can_hold_smaller... ok
    test tests::smaller_cannot_hold_larger... ok

    test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

两个测试都通过了！现在让我们看看当我们在代码中引入一个错误时，测试结果会发生什么。我们将通过在比较宽度时把大于号替换为小于号来更改 `can_hold` 方法的实现：

    --snip--

    impl Rectangle {
        fn can_hold(&self, other: &Rectangle) -> bool {
            self.width < other.width && self.height > other.height
        }
    }

现在运行测试会产生以下结果：

    running 2 tests
    test tests::smaller_cannot_hold_larger... ok
    test tests::larger_can_hold_smaller... FAILED

    failures:

    ---- tests::larger_can_hold_smaller stdout ----
    thread'main' panicked at 'assertion failed:
    larger.can_hold(&smaller)', src/lib.rs:28:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace


    failures:
        tests::larger_can_hold_smaller

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

我们的测试发现了这个错误！因为 `larger.width` 是 8，`smaller.width` 是 5，所以 `can_hold` 中宽度的比较现在返回 `false`：8 不小于 5。
