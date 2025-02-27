# 問題

そのコンテナ型についてジェネリックな `trait` には型指定の要件があります。つまり、`trait` のユーザーは、そのジェネリック型をすべて指定する _必要があります_。

以下の例では、`Contains` `trait` はジェネリック型 `A` と `B` の使用を許可しています。そして、`Container` 型に対して `trait` を実装し、`A` と `B` に対して `i32` を指定しています。これにより、`fn difference()` で使用できるようになります。

`Contains` はジェネリックなので、`fn difference()` のすべてのジェネリック型を明示的に指定する必要があります。実際のところ、`A` と `B` が入力の `C` によって決まることを表現したい方法が必要です。次のセクションで見るように、関連型がまさにその機能を提供します。

```rust
struct Container(i32, i32);

// コンテナ内に2つの項目が格納されているかどうかをチェックするtrait。
// また、最初または最後の値を取得します。
trait Contains<A, B> {
    fn contains(&self, _: &A, _: &B) -> bool; // 明示的に `A` と `B` が必要です。
    fn first(&self) -> i32; // 明示的に `A` または `B` が必要ではありません。
    fn last(&self) -> i32;  // 明示的に `A` または `B` が必要ではありません。
}

impl Contains<i32, i32> for Container {
    // 格納されている数値が等しい場合はtrue。
    fn contains(&self, number_1: &i32, number_2: &i32) -> bool {
        (&self.0 == number_1) && (&self.1 == number_2)
    }

    // 最初の数値を取得する。
    fn first(&self) -> i32 { self.0 }

    // 最後の数値を取得する。
    fn last(&self) -> i32 { self.1 }
}

// `C` は `A` と `B` を含んでいます。そのため、再度 `A` と `B` を表現する必要があるのは面倒です。
fn difference<A, B, C>(container: &C) -> i32 where
    C: Contains<A, B> {
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
