# 存储匹配的行

为了完成这个函数，我们需要一种方法来存储我们想要返回的匹配行。为此，我们可以在 `for` 循环之前创建一个可变向量，并调用 `push` 方法将 `line` 存储在向量中。在 `for` 循环之后，我们返回该向量，如清单 12-19 所示。

文件名：`src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.contains(query) {
            results.push(line);
        }
    }

    results
}
```

清单 12-19：存储匹配的行以便我们可以返回它们

现在，`search` 函数应该只返回包含 `query` 的行，并且我们的测试应该会通过。让我们运行测试：

```bash
$ cargo test
--snip--
running 1 test
test tests::one_result... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
0
filtered out
finished in 0.00s
```

我们的测试通过了，所以我们知道它能正常工作！

在这一点上，我们可以考虑在保持测试通过以维持相同功能的同时，对搜索函数的实现进行重构的机会。搜索函数中的代码还不算太糟，但它没有利用迭代器的一些有用特性。我们将在第 13 章回到这个例子，在那里我们将详细探讨迭代器，并看看如何改进它。
