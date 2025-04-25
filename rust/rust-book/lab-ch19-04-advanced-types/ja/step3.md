# 型エイリアスを使った型のエイリアスの作成

Rust は、既存の型に別名を付けるための _型エイリアス_ を宣言する機能を備えています。これには `type` キーワードを使います。たとえば、`Kilometers` を `i32` にエイリアス付けするには、次のようにします。

```rust
type Kilometers = i32;
```

これで、エイリアス `Kilometers` は `i32` の _エイリアス_ になります。19-15 のリストで作成した `Millimeters` や `Meters` 型とは異なり、`Kilometers` は別の新しい型ではありません。`Kilometers` 型の値は、`i32` 型の値と同じように扱われます。

    type Kilometers = i32;

    let x: i32 = 5;
    let y: Kilometers = 5;

    println!("x + y = {}", x + y);

`Kilometers` と `i32` は同じ型なので、両方の型の値を加算でき、`Kilometers` 型の値を `i32` 型のパラメータを持つ関数に渡すことができます。ただし、この方法を使うと、先ほど議論した新しい型パターンから得られる型チェックの恩恵は得られません。つまり、`Kilometers` と `i32` の値をどこかで混同した場合、コンパイラはエラーを表示しません。

型エイリアスの主な使い道は、繰り返しを減らすことです。たとえば、次のような長い型がある場合があります。

```rust
Box<dyn Fn() + Send + 'static>
```

この長い型を関数のシグネチャやコード全体の型アノテーションに書くのは面倒で、エラーが発生しやすいです。19-24 のリストのようなコードがたくさんあるプロジェクトを想像してみてください。

```rust
let f: Box<dyn Fn() + Send + 'static> = Box::new(|| {
    println!("hi");
});

fn takes_long_type(f: Box<dyn Fn() + Send + 'static>) {
    --snip--
}

fn returns_long_type() -> Box<dyn Fn() + Send + 'static> {
    --snip--
}
```

リスト 19-24: 多くの場所で長い型を使用する

型エイリアスを使うことで、繰り返しを減らしてコードをより管理しやすくすることができます。19-25 のリストでは、冗長な型に対して `Thunk` というエイリアスを導入し、型のすべての使用箇所を短いエイリアス `Thunk` に置き換えています。

    type Thunk = Box<dyn Fn() + Send + 'static>;

    let f: Thunk = Box::new(|| println!("hi"));

    fn takes_long_type(f: Thunk) {
        --snip--
    }

    fn returns_long_type() -> Thunk {
        --snip--
    }

リスト 19-25: 繰り返しを減らすための型エイリアス `Thunk` の導入

このコードははるかに読みやすく書きやすくなっています！型エイリアスに意味のある名前を付けることで、意図を伝えるのに役立ちます（_thunk_ は後で評価するコードのことを指す言葉なので、保存されるクロージャに適切な名前です）。

型エイリアスはまた、繰り返しを減らすために `Result<T, E>` 型と共に頻繁に使用されます。標準ライブラリの `std::io` モジュールを考えてみてください。I/O 操作は、操作が失敗した場合の状況を処理するために、しばしば `Result<T, E>` を返します。このライブラリには、すべての可能な I/O エラーを表す `std::io::Error` 構造体があります。`std::io` の多くの関数は、`E` が `std::io::Error` である `Result<T, E>` を返します。たとえば、`Write` トレイトのこれらの関数です。

```rust
use std::fmt;
use std::io::Error;

pub trait Write {
    fn write(&mut self, buf: &[u8]) -> Result<usize, Error>;
    fn flush(&mut self) -> Result<(), Error>;

    fn write_all(&mut self, buf: &[u8]) -> Result<(), Error>;
    fn write_fmt(
        &mut self,
        fmt: fmt::Arguments,
    ) -> Result<(), Error>;
}
```

`Result<..., Error>` がたくさん繰り返されています。そのため、`std::io` には次のような型エイリアスの宣言があります。

```rust
type Result<T> = std::result::Result<T, std::io::Error>;
```

この宣言が `std::io` モジュールにあるため、完全修飾エイリアス `std::io::Result<T>` を使うことができます。つまり、`E` が `std::io::Error` として埋め込まれた `Result<T, E>` です。`Write` トレイトの関数のシグネチャは、次のようになります。

```rust
pub trait Write {
    fn write(&mut self, buf: &[u8]) -> Result<usize>;
    fn flush(&mut self) -> Result<()>;

    fn write_all(&mut self, buf: &[u8]) -> Result<()>;
    fn write_fmt(&mut self, fmt: fmt::Arguments) -> Result<()>;
}
```

型エイリアスは 2 つの点で役立ちます。コードを書きやすくし、`std::io` 全体で一貫したインターフェイスを提供します。エイリアスなので、`Result<T, E>` と同じ `Result<T, E>` であり、`Result<T, E>` で機能するすべてのメソッドや `?` 演算子のような特殊な構文を使用できます。
