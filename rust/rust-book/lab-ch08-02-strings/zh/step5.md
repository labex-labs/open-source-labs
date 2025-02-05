# 使用 push_str 和 push 向字符串追加内容

我们可以使用 `push_str` 方法来追加一个字符串切片，从而使 `String` 增长，如清单 8-15 所示。

```rust
let mut s = String::from("foo");
s.push_str("bar");
```

清单 8-15：使用 `push_str` 方法向 `String` 追加字符串切片

经过这两行代码后，`s` 将包含 “foobar”。`push_str` 方法接受一个字符串切片，因为我们不一定想要获取该参数的所有权。例如，在清单 8-16 的代码中，我们希望在将 `s2` 的内容追加到 `s1` 之后还能使用 `s2`。

```rust
let mut s1 = String::from("foo");
let s2 = "bar";
s1.push_str(s2);
println!("s2 is {s2}");
```

清单 8-16：将字符串切片的内容追加到 `String` 后使用该字符串切片

如果 `push_str` 方法获取了 `s2` 的所有权，那么我们就无法在最后一行打印它的值了。然而，这段代码能按我们期望的那样工作！

`push` 方法接受一个字符作为参数，并将其添加到 `String` 中。清单 8-17 使用 `push` 方法向一个 `String` 添加字母 “l”。

```rust
let mut s = String::from("lo");
s.push('l');
```

清单 8-17：使用 `push` 向 `String` 值添加一个字符

结果，`s` 将包含 “lol”。
