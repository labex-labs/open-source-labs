# 配列型

複数の値のコレクションを持つ別の方法は、「配列」を使うことです。タプルとは異なり、配列の各要素は必ず同じ型でなければなりません。他の一部の言語の配列とは異なり、Rust の配列は固定長です。

配列の値は、角括弧の中にカンマ区切りのリストとして書きます。

ファイル名：`src/main.rs`

```rust
fn main() {
    let a = [1, 2, 3, 4, 5];
}
```

データをスタックに割り当てたい場合や、常に固定数の要素を持つことを保証したい場合、配列は便利です。ただし、配列はベクター型ほど柔軟ではありません。ベクターは、標準ライブラリによって提供される似たようなコレクション型で、サイズの増減が可能です。配列とベクターのどちらを使うか迷った場合は、おそらくベクターを使うべきです。第 8 章ではベクターについて詳しく説明します。

ただし、要素数が変更される必要がないことがわかっている場合、配列の方が便利です。たとえば、プログラムで月の名前を使う場合、12 個の要素が常に含まれることがわかっているため、おそらく配列を使う方が適切でしょう。

```rust
let months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"];
```

配列の型は、各要素の型、セミコロン、そして配列の要素数を角括弧で囲んで書きます。例えば：

```rust
let a: [i32; 5] = [1, 2, 3, 4, 5];
```

ここで、`i32`は各要素の型です。セミコロンの後の数字`5`は、配列が 5 つの要素を含むことを示しています。

また、各要素に同じ値を含む配列を初期化することもできます。方法は、初期値を指定してからセミコロン、そして角括弧で囲んだ配列の長さを指定することです。例えば：

```rust
let a = [3; 5];
```

`a`と名付けられた配列は、最初にすべての要素が値`3`に設定された`5`つの要素を含みます。これは`let a = [3, 3, 3, 3, 3];`と書くのと同じですが、もっと簡潔な書き方です。
