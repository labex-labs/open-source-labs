# タプル

タプルは、異なる型の値のコレクションです。タプルは丸括弧 `()` を使って構築され、各タプル自体は型シグネチャ `(T1, T2,...)` を持つ値であり、ここで `T1`、`T2` はその要素の型です。関数は、タプルを使って複数の値を返すことができます。なぜなら、タプルは任意の数の値を保持できるからです。

```rust
// タプルは関数の引数として、また返り値としても使うことができます。
fn reverse(pair: (i32, bool)) -> (bool, i32) {
    // `let` を使って、タプルの要素を変数にバインドすることができます。
    let (int_param, bool_param) = pair;

    (bool_param, int_param)
}

// 以下の構造体はアクティビティ用です。
#[derive(Debug)]
struct Matrix(f32, f32, f32, f32);

fn main() {
    // 様々な型の要素を持つタプルです。
    let long_tuple = (1u8, 2u16, 3u32, 4u64,
                      -1i8, -2i16, -3i32, -4i64,
                      0.1f32, 0.2f64,
                      'a', true);

    // タプルインデックスを使って、タプルから値を抽出することができます。
    println!("Long tuple first value: {}", long_tuple.0);
    println!("Long tuple second value: {}", long_tuple.1);

    // タプルは他のタプルの要素としても使うことができます。
    let tuple_of_tuples = ((1u8, 2u16, 2u32), (4u64, -1i8), -2i16);

    // タプルは表示可能です。
    println!("tuple of tuples: {:?}", tuple_of_tuples);

    // ただし、長いタプル（12 要素以上）は表示できません。
    //let too_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13);
    //println!("Too long tuple: {:?}", too_long_tuple);
    // TODO ^ 上の 2 行を解除して、コンパイラエラーを確認してください。

    let pair = (1, true);
    println!("Pair is {:?}", pair);

    println!("The reversed pair is {:?}", reverse(pair));

    // 1 要素のタプルを作成するには、丸括弧で囲まれたリテラルと区別するためにコンマが必要です。
    println!("One element tuple: {:?}", (5u32,));
    println!("Just an integer: {:?}", (5u32));

    // タプルを分解して、バインディングを作成することができます。
    let tuple = (1, "hello", 4.5, true);

    let (a, b, c, d) = tuple;
    println!("{:?}, {:?}, {:?}, {:?}", a, b, c, d);

    let matrix = Matrix(1.1, 1.2, 2.1, 2.2);
    println!("{:?}", matrix);
}
```

## アクティビティ

1.  _復習_: 上の例の `Matrix` 構造体に `fmt::Display` トレイトを追加しましょう。これにより、デバッグ形式 `{:?}` から表示形式 `{}` に切り替えると、次のような出力が得られます。

    ```plaintext
    ( 1.1 1.2 )
    ( 2.1 2.2 )
    ```

    表示形式の例を参照すると良いでしょう。

2.  `reverse` 関数をテンプレートにして `transpose` 関数を追加しましょう。この関数は、行列を引数として受け取り、2 つの要素が交換された行列を返します。たとえば：

    ```rust
    println!("Matrix:\n{}", matrix);
    println!("Transpose:\n{}", transpose(matrix));
    ```

    出力は次のようになります。

    ```plaintext
    Matrix:
    ( 1.1 1.2 )
    ( 2.1 2.2 )
    Transpose:
    ( 1.1 2.1 )
    ( 1.2 2.2 )
    ```
