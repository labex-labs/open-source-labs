# 参照と借用

リスト 4-5 のタプルコードの問題は、`calculate_length`関数に渡す前に`String`を返さなければならないことです。なぜなら、`calculate_length`関数に渡した後でも`String`を使い続ける必要があるからです。なぜなら、`String`は`calculate_length`関数に移動してしまうからです。代わりに、`String`値への参照を提供することができます。「参照」は、そのアドレスに格納されているデータにアクセスするためにたどることができるアドレスのようなポインタと同じです。そのデータは他の変数によって所有されています。ポインタとは異なり、参照はその参照の生存期間中、特定の型の有効な値を指すことが保証されています。

以下は、値の所有権を取得する代わりにオブジェクトへの参照をパラメータとして持つ`calculate_length`関数を定義して使用する方法です。

ファイル名：`src/main.rs`

```rust
fn main() {
    let s1 = String::from("hello");

    let len = calculate_length(&s1);

    println!("The length of '{s1}' is {len}.");
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

まず、変数宣言と関数の返り値にあるすべてのタプルコードが消えていることに注意してください。次に、`&s1`を`calculate_length`に渡し、その定義では`String`ではなく`&String`を受け取ることに注意してください。これらのアンパサンドは「参照」を表し、所有権を取得することなく値を参照することができます。図 4-5 はこの概念を示しています。

図 4-5: `&String s`が`String s1`を指す図

> 注：`&`を使って参照することの逆は、参照解除です。これは、参照解除演算子`*`を使って行われます。第 8 章で参照解除演算子のいくつかの使い方を見て、第 15 章で参照解除の詳細について説明します。

ここで関数呼び出しをもう少し詳しく見てみましょう。

```rust
let s1 = String::from("hello");

let len = calculate_length(&s1);
```

`&s1`の構文は、`s1`の値を参照する参照を作成しますが、その所有権は取得しません。所有権を取得していないため、参照が使用されなくなったときに参照先の値は破棄されません。

同様に、関数のシグネチャは`&`を使って、パラメータ`s`の型が参照であることを示しています。説明用の注釈を追加しましょう。

```rust
fn calculate_length(s: &String) -> usize { // s は String への参照
    s.len()
} // ここで、s はスコープ外になります。ただし、s が所有しているものではないため、
  // String は破棄されません
```

変数`s`が有効なスコープは、他の関数パラメータのスコープと同じですが、参照が指す値は`s`が使用されなくなったときに破棄されません。なぜなら、`s`は所有権を持っていないからです。関数が実際の値ではなく参照をパラメータとして持つ場合、所有権を返すために値を返す必要はありません。なぜなら、所有権を持っていなかったからです。

参照を作成する操作を「借用」と呼びます。現実の生活のように、ある人が何かを所有している場合、あなたは彼らからそれを借用することができます。使い終わったら、必ず返さなければなりません。あなたはそれを所有していません。

では、借用しているものを変更しようとするとどうなりますか？リスト 4-6 のコードを試してみてください。ネタバレ注意：動作しません！

ファイル名：`src/main.rs`

```rust
fn main() {
    let s = String::from("hello");

    change(&s);
}

fn change(some_string: &String) {
    some_string.push_str(", world");
}
```

リスト 4-6: 借用した値を変更しようとする

エラーはこちらです。

```bash
error[E0596]: cannot borrow `*some_string` as mutable, as it is behind a `&`
reference
 --> src/main.rs:8:5
  |
7 | fn change(some_string: &String) {
  |                        ------- help: consider changing this to be a mutable
reference: `&mut String`
8 |     some_string.push_str(", world");
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ `some_string` is a `&` reference, so
the data it refers to cannot be borrowed as mutable
```

変数はデフォルトで不変であるように、参照も同様です。参照先のものを変更することはできません。
