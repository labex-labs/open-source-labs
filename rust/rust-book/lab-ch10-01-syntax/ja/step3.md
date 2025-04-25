# 関数定義におけるジェネリクス

ジェネリクスを使用して関数を定義する場合、通常はパラメータや戻り値のデータ型を指定する場所である関数のシグネチャにジェネリクスを配置します。これにより、コードがより柔軟になり、関数の呼び出し元に対してより多くの機能を提供する一方で、コードの重複を防止します。

`largest` 関数を続けて話しますと、リスト 10-4 は、スライス内の最大値を見つける 2 つの関数を示しています。その後、これらを 1 つのジェネリクスを使用する関数に結合します。

ファイル名：`src/main.rs`

```rust
fn largest_i32(list: &[i32]) -> &i32 {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn largest_char(list: &[char]) -> &char {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest_i32(&number_list);
    println!("The largest number is {result}");

    let char_list = vec!['y','m', 'a', 'q'];

    let result = largest_char(&char_list);
    println!("The largest char is {result}");
}
```

リスト 10-4: 名前とシグネチャ内の型のみが異なる 2 つの関数

`largest_i32` 関数は、リスト 10-3 で抽出したもので、スライス内の最大の `i32` を見つけます。`largest_char` 関数は、スライス内の最大の `char` を見つけます。関数の本体は同じコードなので、単一の関数にジェネリック型パラメータを導入することで重複を排除しましょう。

新しい単一の関数内の型をパラメータ化するには、関数の値パラメータと同じように、型パラメータに名前を付ける必要があります。型パラメータ名としては任意の識別子を使用できます。ただし、Rust では型パラメータ名は短く、多くの場合 1 文字だけで、Rust の型名付け規則はキャメルケースになっています。_type_ の略である `T` は、ほとんどの Rust プログラマーの既定の選択肢です。

関数の本体でパラメータを使用する場合、コンパイラがその名前の意味を知るように、シグネチャでパラメータ名を宣言する必要があります。同様に、関数シグネチャで型パラメータ名を使用する場合、使用する前に型パラメータ名を宣言する必要があります。ジェネリックな `largest` 関数を定義するには、関数名とパラメータリストの間に角括弧 `<>` の中に型名の宣言を置きます。

```rust
fn largest<T>(list: &[T]) -> &T {
```

この定義を読むと、関数 `largest` は型 `T` のジェネリックであることがわかります。この関数には `list` という 1 つのパラメータがあり、これは型 `T` の値のスライスです。`largest` 関数は、同じ型 `T` の値への参照を返します。

リスト 10-5 は、シグネチャにジェネリックデータ型を使用した結合された `largest` 関数の定義を示しています。また、`i32` 値のスライスまたは `char` 値を使って関数を呼び出す方法も示しています。このコードはまだコンパイルされませんが、この章の後半で修正します。

ファイル名：`src/main.rs`

```rust
fn largest<T>(list: &[T]) -> &T {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest(&number_list);
    println!("The largest number is {result}");

    let char_list = vec!['y','m', 'a', 'q'];

    let result = largest(&char_list);
    println!("The largest char is {result}");
}
```

リスト 10-5: ジェネリック型パラメータを使用した `largest` 関数; これはまだコンパイルされません

このコードを今すぐコンパイルすると、次のエラーが表示されます。

```bash
error[E0369]: binary operation `>` cannot be applied to type `&T`
 --> src/main.rs:5:17
  |
5 |         if item > largest {
  |            ---- ^ ------- &T
  |            |
  |            &T
  |
help: consider restricting type parameter `T`
  |
1 | fn largest<T: std::cmp::PartialOrd>(list: &[T]) -> &T {
  |             ++++++++++++++++++++++
```

ヘルプメッセージには `std::cmp::PartialOrd` が記載されており、これは _トレイト_ で、次のセクションでトレイトについて説明します。今のところ、このエラーは `largest` の本体が `T` があり得るすべての可能な型に対して機能しないことを示しています。本体で型 `T` の値を比較したいので、順序付け可能な値の型のみを使用できます。比較を可能にするために、標準ライブラリには型に対して実装できる `std::cmp::PartialOrd` トレイトがあります（このトレイトに関する詳細は付録 C を参照）。ヘルプメッセージの提案に従って、`T` に有効な型を `PartialOrd` を実装するものに制限すると、この例はコンパイルされます。なぜなら、標準ライブラリは `i32` と `char` の両方に対して `PartialOrd` を実装しているからです。
