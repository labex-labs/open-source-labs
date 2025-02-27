# `panic`

私たちが見る最も単純なエラーハンドリングメカニズムは `panic` です。これは、エラーメッセージを表示し、スタックを unwind し始め、通常はプログラムを終了します。ここでは、エラー条件で明示的に `panic` を呼び出します。

```rust
fn drink(beverage: &str) {
    // 糖分の多い飲料は多く飲んではいけません。
    if beverage == "lemonade" { panic!("AAAaaaaa!!!!"); }

    println!("Some refreshing {} is all I need.", beverage);
}

fn main() {
    drink("water");
    drink("lemonade");
}
```
