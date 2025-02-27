# 関連型

「関連型」を使用することで、内部型を _出力_ 型としてトレイト内にローカルに移動させることで、コード全体の読みやすさが向上します。`trait` 定義の構文は以下の通りです。

```rust
// `A` と `B` は `type` キーワードを使ってトレイト内で定義されます。
// （注: このコンテキストでの `type` は、エイリアスとして使用するときの `type` とは異なります）。
trait Contains {
    type A;
    type B;

    // これらの新しい型を一般的に参照するための更新された構文。
    fn contains(&self, _: &Self::A, _: &Self::B) -> bool;
}
```

`Contains` トレイトを使用する関数は、もはや `A` や `B` を全く明示する必要がないことに注意してください。

```rust
// 関連型を使用しない場合
fn difference<A, B, C>(container: &C) -> i32 where
    C: Contains<A, B> {... }

// 関連型を使用する場合
fn difference<C: Contains>(container: &C) -> i32 {... }
```

前のセクションの例を関連型を使って書き直してみましょう。

```rust
struct Container(i32, i32);

// コンテナ内に2つの項目が格納されているかどうかをチェックするトレイト。
// また、最初または最後の値も取得します。
trait Contains {
    // ここでメソッドが利用できる汎用型を定義します。
    type A;
    type B;

    fn contains(&self, _: &Self::A, _: &Self::B) -> bool;
    fn first(&self) -> i32;
    fn last(&self) -> i32;
}

impl Contains for Container {
    // `A` と `B` がどの型であるかを指定します。`input` 型が `Container(i32, i32)` の場合、`output` 型は `i32` と `i32` として決定されます。
    type A = i32;
    type B = i32;

    // `&Self::A` と `&Self::B` もここでは有効です。
    fn contains(&self, number_1: &i32, number_2: &i32) -> bool {
        (&self.0 == number_1) && (&self.1 == number_2)
    }
    // 最初の数値を取得します。
    fn first(&self) -> i32 { self.0 }

    // 最後の数値を取得します。
    fn last(&self) -> i32 { self.1 }
}

fn difference<C: Contains>(container: &C) -> i32 {
    container.last() - container.first()
}

fn main() {
    let number_1 = 3;
    let number_2 = 10;

    let container = Container(number_1, number_2);

    println!("Does container contain {} and {}: {}",
        &number_1, &number_2,
        container.contains(&number_1, &number_2));
    println!("First number: {}", container.first());
    println!("Last number: {}", container.last());

    println!("The difference is: {}", difference(&container));
}
```
