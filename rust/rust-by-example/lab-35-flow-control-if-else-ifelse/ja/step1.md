# if/else

`if`-`else` による分岐は他の言語と似ています。その多くとは異なり、論理値の条件は丸括弧で囲む必要はなく、各条件の後にブロックが続きます。`if`-`else` の条件分岐は式であり、すべてのブランチは同じ型を返さなければなりません。

```rust
fn main() {
    let n = 5;

    if n < 0 {
        print!("{} is negative", n);
    } else if n > 0 {
        print!("{} is positive", n);
    } else {
        print!("{} is zero", n);
    }

    let big_n =
        if n < 10 && n > -10 {
            println!(", and is a small number, increase ten-fold");

            // この式は `i32` を返します。
            10 * n
        } else {
            println!(", and is a big number, halve the number");

            // この式も `i32` を返さなければなりません。
            n / 2
            // TODO ^ Try suppressing this expression with a semicolon.
        };
    //   ^ ここにセミコロンを忘れないでください！すべての `let` 束縛には必要です。

    println!("{} -> {}", n, big_n);
}
```
