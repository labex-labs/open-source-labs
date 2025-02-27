# if let

一部のケースでは、列挙型をマッチングする際に `match` は厄介です。たとえば：

```rust
// 型 `Option<i32>` の `optional` を作成
let optional = Some(7);

match optional {
    Some(i) => {
        println!("This is a really long string and `{:?}`", i);
        // ^ オプションから `i` を分解するためにインデントを 2 つ必要とします。
    },
    _ => {},
    // ^ 必要です。`match` は網羅的です。無駄な空間に見えませんか？
};
```

このケースでは `if let` の方がクリーンで、さらに様々な失敗オプションを指定できます：

```rust
fn main() {
    // すべて型 `Option<i32>` です
    let number = Some(7);
    let letter: Option<i32> = None;
    let emoticon: Option<i32> = None;

    // `if let` 構文は次のように読みます：「`let` が `number` を `Some(i)` に分解した場合、ブロック (`{}`) を評価する」。
    if let Some(i) = number {
        println!("Matched {:?}!", i);
    }

    // 失敗を指定する必要がある場合は、`else` を使います：
    if let Some(i) = letter {
        println!("Matched {:?}!", i);
    } else {
        // 分解に失敗しました。失敗ケースに切り替えます。
        println!("Didn't match a number. Let's go with a letter!");
    }

    // 変更された失敗条件を提供します。
    let i_like_letters = false;

    if let Some(i) = emoticon {
        println!("Matched {:?}!", i);
    // 分解に失敗しました。代替の失敗ブランチを採用するかどうかを確認するために `else if` 条件を評価します：
    } else if i_like_letters {
        println!("Didn't match a number. Let's go with a letter!");
    } else {
        // 条件が偽で評価されました。このブランチはデフォルトです：
        println!("I don't like letters. Let's go with an emoticon :)!");
    }
}
```

同じように、`if let` を使って任意の列挙型値をマッチングできます：

```rust
// 私たちの例の列挙型
enum Foo {
    Bar,
    Baz,
    Qux(u32)
}

fn main() {
    // 例の変数を作成
    let a = Foo::Bar;
    let b = Foo::Baz;
    let c = Foo::Qux(100);

    // 変数 a は Foo::Bar とマッチします
    if let Foo::Bar = a {
        println!("a is foobar");
    }

    // 変数 b は Foo::Bar とマッチしません
    // だからこれは何も表示されません
    if let Foo::Bar = b {
        println!("b is foobar");
    }

    // 変数 c は値を持つ Foo::Qux とマッチします
    // 前の例の Some() に似ています
    if let Foo::Qux(value) = c {
        println!("c is {}", value);
    }

    // バインディングも `if let` で機能します
    if let Foo::Qux(value @ 100) = c {
        println!("c is one hundred");
    }
}
```

もう一つの利点は、`if let` がパラメータなしの列挙型バリアントをマッチングできることです。列挙型が `PartialEq` を実装または派生していない場合でも、これは当てはまります。そのような場合、`if Foo::Bar == a` はコンパイルエラーになります。なぜなら列挙型のインスタンスは等しくできないからですが、`if let` は引き続き機能します。

チャレンジしませんか？次の例を `if let` を使って修正してみましょう：

```rust
// この列挙型は意図的に `PartialEq` を実装または派生していません。
// そのため、次の Foo::Bar == a の比較が失敗するのです。
enum Foo {Bar}

fn main() {
    let a = Foo::Bar;

    // 変数 a は Foo::Bar とマッチします
    if Foo::Bar == a {
    // ^-- これはコンパイル時エラーを引き起こします。代わりに `if let` を使ってください。
        println!("a is foobar");
    }
}
```
