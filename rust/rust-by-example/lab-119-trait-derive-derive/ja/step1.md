# 派生

コンパイラは、`#[derive]`属性を通じていくつかのトレイトに対する基本的な実装を提供することができます。より複雑な動作が必要な場合は、これらのトレイトを手動で実装することもできます。

以下は、派生可能なトレイトの一覧です。

- 比較トレイト: `Eq`、`PartialEq`、`Ord`、`PartialOrd`。
- `Clone`、コピーを介して`&T`から`T`を作成します。
- `Copy`、型に「ムーブセマンティクス」ではなく「コピーセマンティクス」を与えます。
- `Hash`、`&T`からハッシュを計算します。
- `Default`、データ型の空のインスタンスを作成します。
- `Debug`、`{:?}`フォーマッタを使用して値をフォーマットします。

```rust
// `Centimeters`、比較可能なタプル構造体
#[derive(PartialEq, PartialOrd)]
struct Centimeters(f64);

// `Inches`、表示可能なタプル構造体
#[derive(Debug)]
struct Inches(i32);

impl Inches {
    fn to_centimeters(&self) -> Centimeters {
        let &Inches(inches) = self;

        Centimeters(inches as f64 * 2.54)
    }
}

// `Seconds`、追加の属性のないタプル構造体
struct Seconds(i32);

fn main() {
    let _one_second = Seconds(1);

    // エラー: `Seconds`は表示できません。`Debug`トレイトを実装していません
    //println!("One second looks like: {:?}", _one_second);
    // TODO ^ この行のコメントを外してみてください

    // エラー: `Seconds`は比較できません。`PartialEq`トレイトを実装していません
    //let _this_is_true = (_one_second == _one_second);
    // TODO ^ この行のコメントを外してみてください

    let foot = Inches(12);

    println!("One foot equals {:?}", foot);

    let meter = Centimeters(100.0);

    let cmp =
        if foot.to_centimeters() < meter {
            "smaller"
        } else {
            "bigger"
        };

    println!("One foot is {} than one meter.", cmp);
}
```
