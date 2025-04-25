# テストケース：単位の明確化

ファントム型パラメータを持つ`Add`を実装することで、単位変換の便利な方法を調べることができます。以下では`Add`トレイトを調べます。

```rust
// この構築により：`Self + RHS = Output`
// ただし、実装で指定されていない場合、RHS はデフォルトで Self になります。
pub trait Add<RHS = Self> {
    type Output;

    fn add(self, rhs: RHS) -> Self::Output;
}

// `Output` は `T<U>` でなければならないため、`T<U> + T<U> = T<U>` となります。
impl<U> Add for T<U> {
    type Output = T<U>;
  ...
}
```

全体の実装：

```rust
use std::ops::Add;
use std::marker::PhantomData;

/// 単位型を定義するための空の列挙型を作成します。
#[derive(Debug, Clone, Copy)]
enum Inch {}
#[derive(Debug, Clone, Copy)]
enum Mm {}

/// `Length` は、ファントム型パラメータ `Unit` を持つ型であり、
/// 長さの型 (つまり `f64`) はジェネリックではありません。
///
/// `f64` は既に `Clone` と `Copy` トレイトを実装しています。
#[derive(Debug, Clone, Copy)]
struct Length<Unit>(f64, PhantomData<Unit>);

/// `Add` トレイトは `+` 演算子の動作を定義します。
impl<Unit> Add for Length<Unit> {
    type Output = Length<Unit>;

    // add() は合計を含む新しい `Length` 構造体を返します。
    fn add(self, rhs: Length<Unit>) -> Length<Unit> {
        // `+` は `f64` の `Add` 実装を呼び出します。
        Length(self.0 + rhs.0, PhantomData)
    }
}

fn main() {
    // `one_foot` はファントム型パラメータ `Inch` を持つことを指定します。
    let one_foot:  Length<Inch> = Length(12.0, PhantomData);
    // `one_meter` はファントム型パラメータ `Mm` を持ちます。
    let one_meter: Length<Mm>   = Length(1000.0, PhantomData);

    // `+` は `Length<Unit>` 用に実装した `add()` メソッドを呼び出します。
    //
    // `Length` は `Copy` を実装しているため、`add()` は `one_foot` と `one_meter` を消費せず、
    // それらを `self` と `rhs` にコピーします。
    let two_feet = one_foot + one_foot;
    let two_meters = one_meter + one_meter;

    // 加算が機能します。
    println!("one foot + one_foot = {:?} in", two_feet.0);
    println!("one meter + one_meter = {:?} mm", two_meters.0);

    // 無意味な演算は失敗するはずです：
    // コンパイル時エラー: 型の不一致。
    //let one_feter = one_foot + one_meter;
}
```
