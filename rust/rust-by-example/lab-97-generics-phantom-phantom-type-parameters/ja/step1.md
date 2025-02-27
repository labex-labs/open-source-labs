# ファントム型パラメータ

ファントム型パラメータは、ランタイムでは表示されず、コンパイル時にのみ（そして必ず）静的にチェックされるパラメータです。

データ型は、マーカーとして機能するか、コンパイル時に型チェックを行うために、追加のジェネリック型パラメータを使用できます。これらの追加のパラメータは、格納値を持たず、ランタイムの動作も持ちません。

次の例では、\[std::marker::PhantomData\] とファントム型パラメータの概念を組み合わせて、異なるデータ型を含むタプルを作成します。

```rust
use std::marker::PhantomData;

// 隠しパラメータ `B` を持つ `A` でジェネリックなファントムタプル構造体。
#[derive(PartialEq)] // この型に対して等価性テストを許可する。
struct PhantomTuple<A, B>(A, PhantomData<B>);

// 隠しパラメータ `B` を持つ `A` でジェネリックなファントム型構造体。
#[derive(PartialEq)] // この型に対して等価性テストを許可する。
struct PhantomStruct<A, B> { first: A, phantom: PhantomData<B> }

// 注: ジェネリック型 `A` には格納領域が割り当てられますが、`B` には割り当てられません。
//       したがって、`B` は計算で使用できません。

fn main() {
    // ここで、`f32` と `f64` が隠しパラメータです。
    // ファントムタプル型は `<char, f32>` と指定されています。
    let _tuple1: PhantomTuple<char, f32> = PhantomTuple('Q', PhantomData);
    // ファントムタプル型は `<char, f64>` と指定されています。
    let _tuple2: PhantomTuple<char, f64> = PhantomTuple('Q', PhantomData);

    // 型は `<char, f32>` と指定されています。
    let _struct1: PhantomStruct<char, f32> = PhantomStruct {
        first: 'Q',
        phantom: PhantomData,
    };
    // 型は `<char, f64>` と指定されています。
    let _struct2: PhantomStruct<char, f64> = PhantomStruct {
        first: 'Q',
        phantom: PhantomData,
    };

    // コンパイル時エラー！型が一致しないため、これらは比較できません:
    // println!("_tuple1 == _tuple2 yields: {}",
    //           _tuple1 == _tuple2);

    // コンパイル時エラー！型が一致しないため、これらは比較できません:
    // println!("_struct1 == _struct2 yields: {}",
    //           _struct1 == _struct2);
}
```
