# while let

`if let`と同様に、`while let`は厄介な`match`シーケンスをもっと許容可能にすることができます。`i`をインクリメントする次のシーケンスを考えてみましょう。

```rust
// 型`Option<i32>`の`optional`を作成する
let mut optional = Some(0);

// このテストを繰り返し行う
loop {
    match optional {
        // `optional`が分解された場合、ブロックを評価する
        Some(i) => {
            if i > 9 {
                println!("9を超えました、終了します！");
                optional = None;
            } else {
                println!("`i`は`{:?}`です。もう一度試してください。", i);
                optional = Some(i + 1);
            }
            // ^ インデントが3段必要です！
        },
        // 分解に失敗したときにループを終了する
        _ => { break; }
        // ^ なぜこれが必要なのでしょう？もっと良い方法があるはずです！
    }
}
```

`while let`を使うとこのシーケンスがはるかに良くなります。

```rust
fn main() {
    // 型`Option<i32>`の`optional`を作成する
    let mut optional = Some(0);

    // これは次のように読み取れます。「`let`が`optional`を`Some(i)`に分解する間、ブロック (`{}`) を評価する。そうでなければ`break`する。」
    while let Some(i) = optional {
        if i > 9 {
            println!("9を超えました、終了します！");
            optional = None;
        } else {
            println!("`i`は`{:?}`です。もう一度試してください。", i);
            optional = Some(i + 1);
        }
        // ^ 右方向のずれが少なく、失敗したケースを明示的に処理する必要がありません。
    }
    // ^ `if let`には追加のオプションの`else`/`else if`節がありました。`while let`にはこれらはありません。
}
```
