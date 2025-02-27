# スーパートレイトの使用

時には、あるトレイトの定義が別のトレイトに依存する場合があります。ある型が最初のトレイトを実装するためには、その型が2番目のトレイトも実装することが必要です。これを行うことで、トレイトの定義で2番目のトレイトの関連項目を利用できるようになります。トレイトの定義が依存しているトレイトは、そのトレイトの*スーパートレイト*と呼ばれます。

たとえば、`outline_print`メソッドを持つ`OutlinePrint`トレイトを作成したいとしましょう。このメソッドは、与えられた値をアスタリスクで囲んだ形式で表示します。つまり、標準ライブラリの`Display`トレイトを実装して`(x, y)`となる`Point`構造体がある場合、`x`が`1`で`y`が`3`の`Point`インスタンスで`outline_print`を呼び出すと、以下のように表示されるはずです。

    **********
    *        *
    * (1, 3) *
    *        *
    **********

`outline_print`メソッドの実装では、`Display`トレイトの機能を使用したいと思います。したがって、`OutlinePrint`トレイトは`Display`を実装している型のみに対して機能し、`OutlinePrint`が必要とする機能を提供するように指定する必要があります。これは、トレイト定義で`OutlinePrint: Display`と指定することで行うことができます。この技術は、トレイトにトレイト境界を追加するのと似ています。リスト19-22に`OutlinePrint`トレイトの実装を示します。

ファイル名：`src/main.rs`

```rust
use std::fmt;

trait OutlinePrint: fmt::Display {
    fn outline_print(&self) {
        let output = self.to_string();
        let len = output.len();
        println!("{}", "*".repeat(len + 4));
        println!("*{}*", " ".repeat(len + 2));
        println!("* {} *", output);
        println!("*{}*", " ".repeat(len + 2));
        println!("{}", "*".repeat(len + 4));
    }
}
```

リスト19-22：`Display`からの機能を必要とする`OutlinePrint`トレイトの実装

`OutlinePrint`が`Display`トレイトを必要とするように指定したので、`Display`を実装している任意の型に対して自動的に実装される`to_string`関数を使用することができます。トレイト名の後にコロンを付けて`Display`トレイトを指定せずに`to_string`を使用しようとすると、現在のスコープ内の型`&Self`に対して`to_string`という名前のメソッドが見つからないというエラーが表示されます。

`Display`を実装していない型（たとえば`Point`構造体）に対して`OutlinePrint`を実装しようとするとどうなるか見てみましょう。

ファイル名：`src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
}

impl OutlinePrint for Point {}
```

`Display`が必要であるが実装されていないというエラーが表示されます。

```bash
error[E0277]: `Point` doesn't implement `std::fmt::Display`
  --> src/main.rs:20:6
   |
20 | impl OutlinePrint for Point {}
   |      ^^^^^^^^^^^^ `Point` cannot be formatted with the default formatter
   |
   = help: the trait `std::fmt::Display` is not implemented for `Point`
   = note: in format strings you may be able to use `{:?}` (or {:#?} for
pretty-print) instead
note: required by a bound in `OutlinePrint`
  --> src/main.rs:3:21
   |
3  | trait OutlinePrint: fmt::Display {
   |                     ^^^^^^^^^^^^ required by this bound in `OutlinePrint`
```

これを修正するには、`Point`に`Display`を実装して、`OutlinePrint`が必要とする制約を満たします。次のようになります。

ファイル名：`src/main.rs`

```rust
use std::fmt;

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}
```

その後、`Point`に対して`OutlinePrint`トレイトを実装するとコンパイルが成功し、`Point`インスタンスで`outline_print`を呼び出して、アスタリスクの枠内に表示することができます。
