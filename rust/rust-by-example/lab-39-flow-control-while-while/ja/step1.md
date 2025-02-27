# while

`while` キーワードは、条件が真の間、ループを実行するために使用できます。

悪名高い FizzBuzz を `while` ループを使って書いてみましょう。

```rust
fn main() {
    // カウンタ変数
    let mut n = 1;

    // `n` が 101 未満の間、ループする
    while n < 101 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }

        // カウンタをインクリメントする
        n += 1;
    }
}
```
