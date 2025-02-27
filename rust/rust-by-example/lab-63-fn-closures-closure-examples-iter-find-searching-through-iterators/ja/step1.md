# イテレータを通した検索

`Iterator::find` は、イテレータを反復処理して、特定の条件を満たす最初の値を検索する関数です。値がすべて条件を満たさない場合は、`None` を返します。そのシグネチャは次の通りです。

```rust
pub trait Iterator {
    // 反復処理される型。
    type Item;

    // `find` は `&mut self` を取ります。これは呼び出し元が借用されて変更される可能性があるが、消費されないことを意味します。
    fn find<P>(&mut self, predicate: P) -> Option<Self::Item> where
        // `FnMut` は、キャプチャされた変数が最大で変更される可能性があるが、消費されないことを意味します。`&Self::Item` は、クロージャに引数を参照で渡すことを示します。
        P: FnMut(&Self::Item) -> bool;
}
```

```rust
fn main() {
    let vec1 = vec![1, 2, 3];
    let vec2 = vec![4, 5, 6];

    // Vec の `iter()` は `&i32` を返します。
    let mut iter = vec1.iter();
    // Vec の `into_iter()` は `i32` を返します。
    let mut into_iter = vec2.into_iter();

    // Vec の `iter()` は `&i32` を返します。そして、その要素の1つを参照したいので、`&&i32` を `i32` に分解する必要があります。
    println!("vec1 で 2 を見つける: {:?}", iter.find(|&&x| x == 2));
    // Vec の `into_iter()` は `i32` を返します。そして、その要素の1つを参照したいので、`&i32` を `i32` に分解する必要があります。
    println!("vec2 で 2 を見つける: {:?}", into_iter.find(| &x| x == 2));

    let array1 = [1, 2, 3];
    let array2 = [4, 5, 6];

    // 配列の `iter()` は `&&i32` を返します。
    println!("array1 で 2 を見つける: {:?}", array1.iter().find(|&&x| x == 2));
    // 配列の `into_iter()` は `&i32` を返します。
    println!("array2 で 2 を見つける: {:?}", array2.into_iter().find(|&x| x == 2));
}
```

`Iterator::find` は要素への参照を返します。ただし、要素の _インデックス_ を取得したい場合は、`Iterator::position` を使用します。

```rust
fn main() {
    let vec = vec![1, 9, 3, 3, 13, 2];

    // Vec の `iter()` は `&i32` を返します。そして、`position()` は参照を取らないので、`&i32` を `i32` に分解する必要があります。
    let index_of_first_even_number = vec.iter().position(|&x| x % 2 == 0);
    assert_eq!(index_of_first_even_number, Some(5));

    // Vec の `into_iter()` は `i32` を返します。そして、`position()` は参照を取らないので、分解する必要はありません。
    let index_of_first_negative_number = vec.into_iter().position(|x| x < 0);
    assert_eq!(index_of_first_negative_number, None);
}
```
