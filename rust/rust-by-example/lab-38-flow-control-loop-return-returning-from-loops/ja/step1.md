# ループからの戻り値

`loop` の用途の 1 つは、操作が成功するまで再試行することです。ただし、操作が値を返す場合、その値をコードの残りの部分に渡す必要がある場合があります。`break` の後にそれを置くと、`loop` 式によって返されます。

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
