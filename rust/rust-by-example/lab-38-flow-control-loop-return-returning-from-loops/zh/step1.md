# 从循环中返回

`loop` 的用途之一是重试一个操作，直到它成功。不过，如果该操作返回一个值，你可能需要将其传递给代码的其余部分：将它放在 `break` 之后，它将由 `loop` 表达式返回。

```rust
fn main() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };

    assert_eq!(result, 20);
}
```
