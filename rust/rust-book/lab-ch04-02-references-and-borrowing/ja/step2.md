# 可変参照

リスト 4-6 のコードを修正して、借用した値を変更できるようにするには、少しの小さな修正が必要です。それは、代わりに「可変参照」を使用します。

ファイル名：`src/main.rs`

```rust
fn main() {
    let mut s = String::from("hello");

    change(&mut s);
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}
```

まず、`s`を`mut`に変更します。次に、`change`関数を呼び出すときに`&mut s`で可変参照を作成し、関数のシグネチャを更新して`some_string: &mut String`で可変参照を受け取るようにします。これにより、`change`関数が借用した値を変更することが非常に明確になります。

可変参照には大きな制限があります。値に対して可変参照を持っている場合、その値に対する他の参照はあり得ません。このコードは`s`に対して 2 つの可変参照を作成しようとしていますが、失敗します。

ファイル名：`src/main.rs`

```rust
let mut s = String::from("hello");

let r1 = &mut s;
let r2 = &mut s;

println!("{r1}, {r2}");
```

エラーはこちらです。

```bash
error[E0499]: cannot borrow `s` as mutable more than once at a time
 --> src/main.rs:5:14
  |
4 |     let r1 = &mut s;
  |              ------ first mutable borrow occurs here
5 |     let r2 = &mut s;
  |              ^^^^^^ second mutable borrow occurs here
6 |
7 |     println!("{r1}, {r2}");
  |                -- first borrow later used here
```

このエラーは、一度に`s`を可変参照として複数回借用できないため、このコードは無効であることを示しています。最初の可変参照は`r1`にあり、`println!`で使用されるまで続かなければなりません。しかし、その可変参照の作成と使用の間に、`r2`で`s`と同じデータを借用する別の可変参照を作成しようとしました。

同じデータに対する複数の可変参照を同時に防ぐ制限は、変更を可能にしますが、非常に制御された方法で行います。これは、新しい Rust プログラマが苦労することです。なぜなら、ほとんどの言語では、好きなときに変更できるからです。この制限の利点は、Rust がコンパイル時にデータ競合を防ぐことができることです。「データ競合」は、競合条件に似ており、次の 3 つの動作が発生するときに発生します。

- 2 つ以上のポインタが同時に同じデータにアクセスする。
- 少なくとも 1 つのポインタがデータに書き込むために使用されている。
- データへのアクセスを同期するメカニズムがない。

データ競合は未定義の動作を引き起こし、実行時にそれを追跡しようとすると診断と修正が困難になる場合があります。Rust は、データ競合のあるコードをコンパイルしないことでこの問題を防ぎます！

いつものように、波括弧を使って新しいスコープを作成することができます。これにより、複数の可変参照が可能になりますが、同時にはできません。

```rust
let mut s = String::from("hello");

{
    let r1 = &mut s;
} // ここで r1 はスコープ外になります。だから、問題なく新しい参照を作成できます

let r2 = &mut s;
```

Rust は、可変参照と不変参照を組み合わせるときに同様のルールを強制します。このコードはエラーになります。

```rust
let mut s = String::from("hello");

let r1 = &s; // 問題なし
let r2 = &s; // 問題なし
let r3 = &mut s; // 大きな問題

println!("{r1}, {r2}, and {r3}");
```

エラーはこちらです。

```bash
error[E0502]: cannot borrow `s` as mutable because it is also borrowed as
immutable
 --> src/main.rs:6:14
  |
4 |     let r1 = &s; // no problem
  |              -- immutable borrow occurs here
5 |     let r2 = &s; // no problem
6 |     let r3 = &mut s; // BIG PROBLEM
  |              ^^^^^^ mutable borrow occurs here
7 |
8 |     println!("{r1}, {r2}, and {r3}");
  |                -- immutable borrow later used here
```

ふーん！同じ値に対して不変参照がある間に可変参照を持つこともできません。

不変参照のユーザーは、値が突然変更されることを期待していません！ただし、複数の不変参照は許可されています。なぜなら、データを読み取るだけの誰もが、他の人のデータの読み取りに影響を与える能力を持っていないからです。

参照のスコープは、それが導入された場所から始まり、その参照が最後に使用される時点まで続きます。たとえば、このコードはコンパイルされます。なぜなら、不変参照の最後の使用である`println!`は、可変参照が導入される前に発生するからです。

```rust
let mut s = String::from("hello");

let r1 = &s; // no problem
let r2 = &s; // no problem
println!("{r1} and {r2}");
// この時点以降、変数 r1 と r2 は使用されません

let r3 = &mut s; // no problem
println!("{r3}");
```

不変参照`r1`と`r2`のスコープは、最後に使用される`println!`の後で終了します。これは、可変参照`r3`が作成される前です。これらのスコープは重複していません。したがって、このコードは許可されます。コンパイラは、スコープの終了前の時点で参照がもはや使用されていないことを判断できます。

借用エラーは時々悔しいことがありますが、Rust コンパイラが潜在的なバグを早期に（実行時ではなくコンパイル時）指摘し、問題の正確な場所を示してくれることを忘れないでください。そうすれば、データが思ったものと異なる原因を追跡する必要がありません。
