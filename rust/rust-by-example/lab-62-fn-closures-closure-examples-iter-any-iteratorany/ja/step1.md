# Iterator::any

`Iterator::any` は、イテレータを渡された場合、どれかの要素が述語を満たす場合に `true` を返す関数です。それ以外の場合は `false` を返します。そのシグネチャは以下の通りです。

```rust
pub trait Iterator {
    // 反復処理される型。
    type Item;

    // `any` は `&mut self` を取り、呼び出し元が借用されて変更される可能性があることを意味しますが、消費されません。
    fn any<F>(&mut self, f: F) -> bool where
        // `FnMut` は、キャプチャされた変数が最大で変更される可能性があることを意味しますが、消費されません。`Self::Item` は、クロージャに引数を値で渡すことを示します。
        F: FnMut(Self::Item) -> bool;
}
```

```rust
fn main() {
    let vec1 = vec![1, 2, 3];
    let vec2 = vec![4, 5, 6];

    // Vec の `iter()` は `&i32` を生成します。`i32` に分解します。
    println!("2 in vec1: {}", vec1.iter()    .any(|&x| x == 2));
    // Vec の `into_iter()` は `i32` を生成します。分解は不要です。
    println!("2 in vec2: {}", vec2.into_iter().any(|x| x == 2));

    // `iter()` は `vec1` とその要素を借用するだけなので、再利用できます。
    println!("vec1 len: {}", vec1.len());
    println!("First element of vec1 is: {}", vec1[0]);
    // `into_iter()` は `vec2` とその要素を移動させるので、再利用できません。
    // println!("First element of vec2 is: {}", vec2[0]);
    // println!("vec2 len: {}", vec2.len());
    // TODO: 上の 2 行をコメントアウト解除してコンパイラエラーを確認してください。

    let array1 = [1, 2, 3];
    let array2 = [4, 5, 6];

    // 配列の `iter()` は `&i32` を生成します。
    println!("2 in array1: {}", array1.iter()    .any(|&x| x == 2));
    // 配列の `into_iter()` は `i32` を生成します。
    println!("2 in array2: {}", array2.into_iter().any(|x| x == 2));
}
```
