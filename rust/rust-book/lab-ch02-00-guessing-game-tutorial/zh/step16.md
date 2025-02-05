# 猜对后退出

让我们通过添加一个 `break` 语句来编写程序，使其在用户猜对时退出：

文件名：`src/main.rs`

```rust
--snip--

match guess.cmp(&secret_number) {
    Ordering::Less => println!("Too small!"),
    Ordering::Greater => println!("Too big!"),
    Ordering::Equal => {
        println!("You win!");
        break;
    }
}
```

在 `You win!` 之后添加 `break` 行，会使程序在用户正确猜出秘密数字时退出循环。退出循环也意味着退出程序，因为循环是 `main` 函数的最后一部分。
