# トレイトの実装

次に、`Draw` トレイトを実装するいくつかの型を追加します。`Button` 型を用意します。もう一度申しますが、本書の範囲外でGUIライブラリを実際に実装することはできませんので、`draw` メソッドの本体には役に立つ実装はありません。実装がどのようになるかを想像すると、`Button` 構造体には `width`、`height`、`label` のフィールドがあるかもしれません。リスト17-7を参照してください。

ファイル名: `src/lib.rs`

```rust
pub struct Button {
    pub width: u32,
    pub height: u32,
    pub label: String,
}

impl Draw for Button {
    fn draw(&self) {
        // ボタンを実際に描画するコード
    }
}
```

リスト17-7: `Draw` トレイトを実装する `Button` 構造体

`Button` の `width`、`height`、`label` のフィールドは、他のコンポーネントのフィールドとは異なります。たとえば、`TextField` 型にはこれらと同じフィールドに加えて、`placeholder` フィールドがあるかもしれません。画面に描画したい各型はすべて、`Draw` トレイトを実装しますが、`draw` メソッドでは、その特定の型をどのように描画するかを定義するために異なるコードを使用します。ここでは `Button` がそうです（前述の通り、実際のGUIコードはありません）。たとえば、`Button` 型には、ユーザーがボタンをクリックしたときに何が起こるかに関連するメソッドを含む追加の `impl` ブロックがあるかもしれません。この種のメソッドは、`TextField` のような型には適用されません。

ライブラリを使用する人が、`width`、`height`、`options` のフィールドを持つ `SelectBox` 構造体を実装することを決定した場合、彼らは `SelectBox` 型にも `Draw` トレイトを実装します。リスト17-8を参照してください。

ファイル名: `src/main.rs`

```rust
use gui::Draw;

struct SelectBox {
    width: u32,
    height: u32,
    options: Vec<String>,
}

impl Draw for SelectBox {
    fn draw(&self) {
        // セレクトボックスを実際に描画するコード
    }
}
```

リスト17-8: もう1つのクレートが `gui` を使用し、`SelectBox` 構造体に `Draw` トレイトを実装する

ライブラリのユーザーは、これで `main` 関数を書いて `Screen` インスタンスを作成することができます。`Screen` インスタンスには、それぞれを `Box<T>` に入れてトレイトオブジェクトにすることで、`SelectBox` と `Button` を追加できます。そして、`Screen` インスタンスの `run` メソッドを呼び出すことができます。これにより、各コンポーネントの `draw` が呼び出されます。リスト17-9にこの実装を示します。

ファイル名: `src/main.rs`

```rust
use gui::{Button, Screen};

fn main() {
    let screen = Screen {
        components: vec![
            Box::new(SelectBox {
                width: 75,
                height: 10,
                options: vec![
                    String::from("Yes"),
                    String::from("Maybe"),
                    String::from("No"),
                ],
            }),
            Box::new(Button {
                width: 50,
                height: 10,
                label: String::from("OK"),
            }),
        ],
    };

    screen.run();
}
```

リスト17-9: 同じトレイトを実装する異なる型の値を格納するためのトレイトオブジェクトの使用

ライブラリを書いたとき、誰かが `SelectBox` 型を追加するかもしれないことはわかりませんでしたが、`Screen` の実装は、`SelectBox` が `Draw` トレイトを実装しているため、つまり `draw` メソッドを実装しているため、新しい型で動作し、描画することができました。

この概念は、値が応答するメッセージのみに関心を持ち、値の具体的な型には関心を持たないという点で、動的型付け言語の _ダックタイピング_ の概念に似ています。「ダックが歩き、ガガッと鳴くなら、それはダックであるに違いない！」 リスト17-5の `Screen` の `run` の実装では、`run` は各コンポーネントの具体的な型を知る必要がありません。コンポーネントが `Button` のインスタンスか `SelectBox` のインスタンスかをチェックする必要はありません。コンポーネントの `draw` メソッドを単に呼び出します。`components` ベクターの値の型として `Box<dyn Draw>` を指定することで、`Screen` が `draw` メソッドを呼び出せる値を必要とするように定義しました。

ダックタイピングを使用したコードに似たコードを書くために、トレイトオブジェクトとRustの型システムを使用する利点は、実行時に値が特定のメソッドを実装しているかどうかをチェックする必要がないこと、また、値がメソッドを実装していない場合でも呼び出してしまうときのエラーを心配する必要がないことです。値がトレイトオブジェクトが必要とするトレイトを実装していない場合、Rustはコードをコンパイルしません。

たとえば、リスト17-10は、`String` をコンポーネントとして持つ `Screen` を作成しようとしたときに何が起こるかを示しています。

ファイル名: `src/main.rs`

```rust
use gui::Screen;

fn main() {
    let screen = Screen {
        components: vec![Box::new(String::from("Hi"))],
    };

    screen.run();
}
```

リスト17-10: トレイトオブジェクトのトレイトを実装していない型を使用しようとする

`String` が `Draw` トレイトを実装していないため、次のエラーが表示されます。

```bash
error[E0277]: the trait bound `String: Draw` is not satisfied
 --> src/main.rs:5:26
  |
5 |         components: vec![Box::new(String::from("Hi"))],
  |                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ the trait `Draw` is
not implemented for `String`
  |
  = note: required for the cast to the object type `dyn Draw`
```

このエラーは、何かを意図しないものを `Screen` に渡しているため、別の型を渡す必要があるか、または `Screen` が `draw` を呼び出せるようにするために `String` に `Draw` を実装する必要があることを知らせてくれます。
