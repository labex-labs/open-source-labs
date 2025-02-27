# 正解を予想した後にゲームを終了する

`break`文を追加することで、ユーザーが勝利したときにゲームを終了するようにプログラムを作成しましょう。

ファイル名：`src/main.rs`

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

`You win!`の後に`break`行を追加することで、ユーザーが秘密の数を正しく予想したときにプログラムがループを抜けます。ループを抜けることは、プログラムを終了することも意味します。なぜなら、ループは`main`の最後の部分だからです。
