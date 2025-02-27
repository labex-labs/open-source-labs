# クロージャからキャプチャされた値をクロージャ外に移動させることとFnトレイト

クロージャが定義された環境から参照をキャプチャしたり、値の所有権を取得したりすると（これにより、クロージャに何かが移動するかどうかが影響されます）、クロージャの本体のコードは、後でクロージャが評価されたときに参照や値がどうなるかを定義します（これにより、クロージャから何かが移動するかどうかが影響されます）。

クロージャの本体は、次のいずれかを行うことができます。クロージャからキャプチャされた値をクロージャ外に移動させる、キャプチャされた値を変更する、値を移動も変更もしない、または最初から環境から何もキャプチャしない。

クロージャが環境から値をキャプチャして処理する方法は、クロージャが実装するトレイトに影響します。トレイトは、関数や構造体がどの種類のクロージャを使用できるかを指定する方法です。クロージャは、クロージャの本体が値をどのように処理するかに応じて、これらの`Fn`トレイトのうちの1つ、2つ、またはすべてを追加的に自動的に実装します。

- `FnOnce`は、一度だけ呼び出せるクロージャに適用されます。すべてのクロージャは少なくともこのトレイトを実装します。なぜなら、すべてのクロージャは呼び出せるからです。クロージャの本体からキャプチャされた値を移動させるクロージャは、一度だけ呼び出せるため、`FnOnce`のみを実装し、他の`Fn`トレイトは実装しません。
- `FnMut`は、クロージャの本体からキャプチャされた値を移動させないが、キャプチャされた値を変更する可能性のあるクロージャに適用されます。これらのクロージャは複数回呼び出すことができます。
- `Fn`は、クロージャの本体からキャプチャされた値を移動させず、キャプチャされた値を変更しないクロージャ、および環境から何もキャプチャしないクロージャに適用されます。これらのクロージャは、環境を変更することなく複数回呼び出すことができます。これは、同時に複数回クロージャを呼び出す場合などに重要です。

リスト13-1で使用した`Option<T>`の`unwrap_or_else`メソッドの定義を見てみましょう。

```rust
impl<T> Option<T> {
    pub fn unwrap_or_else<F>(self, f: F) -> T
    where
        F: FnOnce() -> T
    {
        match self {
            Some(x) => x,
            None => f(),
        }
    }
}
```

思い出してください。`T`は、`Option`の`Some`バリアントに含まれる値の型を表すジェネリック型です。その型`T`はまた、`unwrap_or_else`関数の戻り値の型でもあります。たとえば、`Option<String>`に対して`unwrap_or_else`を呼び出すコードは、`String`を取得します。

次に、`unwrap_or_else`関数には追加のジェネリック型パラメータ`F`があることに注意してください。`F`型は、`f`という名前のパラメータの型であり、これは`unwrap_or_else`を呼び出すときに提供するクロージャです。

ジェネリック型`F`に指定されたトレイト境界は`FnOnce() -> T`であり、これは`F`が一度だけ呼び出せ、引数を取らず、`T`を返すことができることを意味します。トレイト境界で`FnOnce`を使用することで、`unwrap_or_else`が`f`を最大で一度だけ呼び出すという制約が表現されています。`unwrap_or_else`の本体では、`Option`が`Some`の場合、`f`は呼び出されません。`Option`が`None`の場合、`f`は一度呼び出されます。すべてのクロージャは`FnOnce`を実装するため、`unwrap_or_else`は最も多様なクロージャを受け付け、可能な限り柔軟です。

> 注：関数も3つの`Fn`トレイトすべてを実装することができます。何を行うかが環境から値をキャプチャする必要がない場合、`Fn`トレイトの1つを実装するものが必要な場所で、クロージャの代わりに関数名を使用することができます。たとえば、`Option<Vec<T>>`値に対して、値が`None`の場合に新しい空のベクトルを取得するには、`unwrap_or_else(Vec::new)`を呼び出すことができます。

次に、スライスに定義された標準ライブラリのメソッド`sort_by_key`を見てみましょう。これが`unwrap_or_else`とどのように異なるか、およびなぜ`sort_by_key`がトレイト境界に`FnMut`を使用するのかを理解しましょう。クロージャは、考慮されているスライス内の現在の要素への参照の形式で1つの引数を取得し、比較可能な`K`型の値を返します。この関数は、各要素の特定の属性に基づいてスライスをソートしたい場合に便利です。リスト13-7では、`Rectangle`インスタンスのリストがあり、`sort_by_key`を使用してそれらを`width`属性で昇順に並べ替えています。

ファイル名: `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let mut list = [
        Rectangle { width: 10, height: 1 },
        Rectangle { width: 3, height: 5 },
        Rectangle { width: 7, height: 12 },
    ];

    list.sort_by_key(|r| r.width);
    println!("{:#?}", list);
}
```

リスト13-7: `width`で四角形を並べ替えるために`sort_by_key`を使用する

このコードは次のように表示されます。

    [
        Rectangle {
            width: 3,
            height: 5,
        },
        Rectangle {
            width: 7,
            height: 12,
        },
        Rectangle {
            width: 10,
            height: 1,
        },
    ]

`sort_by_key`が`FnMut`クロージャを取るように定義されている理由は、スライス内の各要素に対して一度ずつクロージャを呼び出すからです。クロージャ`|r| r.width`は、環境から何もキャプチャせず、変更せず、移動しません。したがって、トレイト境界の要件を満たしています。

対照的に、リスト13-8は、`FnOnce`トレイトのみを実装するクロージャの例を示しています。なぜなら、値を環境から移動させるからです。コンパイラは、このクロージャを`sort_by_key`と一緒に使用しようとしません。

ファイル名: `src/main.rs`

```rust
--snip--

fn main() {
    let mut list = [
        Rectangle { width: 10, height: 1 },
        Rectangle { width: 3, height: 5 },
        Rectangle { width: 7, height: 12 },
    ];

    let mut sort_operations = vec![];
    let value = String::from("by key called");

    list.sort_by_key(|r| {
        sort_operations.push(value);
        r.width
    });
    println!("{:#?}", list);
}
```

リスト13-8: `sort_by_key`に`FnOnce`クロージャを使用しようとする

これは、`list`をソートするときに`sort_by_key`が呼び出される回数を数えようとする、工夫された複雑な方法（機能しません）です。このコードは、クロージャの環境からの`String`である`value`を`sort_operations`ベクトルにプッシュすることにより、このカウントを行おうとしています。クロージャは`value`をキャプチャし、その後、`value`の所有権を`sort_operations`ベクトルに転送することにより、`value`をクロージャから移動させます。このクロージャは一度だけ呼び出すことができます。2回目に呼び出そうとすると機能しません。なぜなら、`value`はもう環境に存在せず、再度`sort_operations`にプッシュすることはできないからです！したがって、このクロージャは`FnOnce`のみを実装します。このコードをコンパイルしようとすると、`value`がクロージャから移動できないというエラーが表示されます。なぜなら、クロージャは`FnMut`を実装しなければならないからです。

```bash
error[E0507]: cannot move out of `value`, a captured variable in an `FnMut`
closure
  --> src/main.rs:18:30
   |
15 |       let value = String::from("by key called");
   |           ----- captured outer variable
16 |
17 |       list.sort_by_key(|r| {
   |  ______________________-
18 | |         sort_operations.push(value);
   | |                              ^^^^^ move occurs because `value` has
type `String`, which does not implement the `Copy` trait
19 | |         r.width
20 | |     });
   | |_____- captured by this `FnMut` closure
```

エラーは、クロージャの本体の`value`を環境から移動させる行を指しています。これを修正するには、クロージャの本体を変更して、環境から値を移動させないようにする必要があります。環境にカウンターを保持し、クロージャの本体でその値をインクリメントすることは、`sort_by_key`が呼び出される回数を数えるよりも単純な方法です。リスト13-9のクロージャは`sort_by_key`と一緒に機能します。なぜなら、`num_sort_operations`カウンターへの可変参照のみをキャプチャしているため、複数回呼び出すことができます。

ファイル名: `src/main.rs`

```rust
--snip--

fn main() {
    --snip--

    let mut num_sort_operations = 0;
    list.sort_by_key(|r| {
        num_sort_operations += 1;
        r.width
    });
    println!(
        "{:#?}, sorted in {num_sort_operations} operations",
        list
    );
}
```

リスト13-9: `sort_by_key`に`FnMut`クロージャを使用することが許される

`Fn`トレイトは、クロージャを使用する関数や型を定義または使用する際に重要です。次のセクションでは、反復子について説明します。多くの反復子メソッドはクロージャ引数を取るため、続ける際にはこれらのクロージャの詳細を覚えておいてください！
