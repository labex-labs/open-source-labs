# Dropトレイトを使ったクリーンアップ時のコード実行

スマートポインタパターンにとって重要な2番目のトレイトは`Drop`で、これは値がスコープ外になろうとしているときに何が起こるかをカスタマイズできるようにします。任意の型に対して`Drop`トレイトの実装を提供でき、そのコードを使ってファイルやネットワーク接続などのリソースを解放できます。

私たちは、`Drop`トレイトの機能がスマートポインタを実装する際にほとんど常に使用されるため、スマートポインタの文脈で`Drop`を紹介しています。たとえば、`Box<T>`が破棄されると、ボックスが指すヒープ上の領域が解放されます。

一部の言語では、一部の型について、プログラマはそれらの型のインスタンスを使用し終えるたびに、メモリやリソースを解放するコードを呼び出さなければなりません。これには、ファイルハンドル、ソケット、ロックなどが挙げられます。もし忘れてしまうと、システムが過負荷になりクラッシュする可能性があります。Rustでは、値がスコープ外になるたびに特定のコードを実行するように指定でき、コンパイラが自動的にこのコードを挿入します。その結果、特定の型のインスタンスが使用終了したプログラム内のあらゆる場所にクリーンアップコードを配置することに注意する必要がなくなります。それでもリソースが漏れることはありません！

値がスコープ外になるときに実行するコードを指定するには、`Drop`トレイトを実装します。`Drop`トレイトでは、`self`へのミュータブル参照を取る`drop`という名前の1つのメソッドを実装する必要があります。Rustが`drop`を呼び出すタイミングを見るために、今は`println!`文で`drop`を実装しましょう。

リスト15-14には、`CustomSmartPointer`構造体が示されています。この構造体の唯一のカスタム機能は、インスタンスがスコープ外になるときに`Dropping CustomSmartPointer!`と表示することで、Rustが`drop`メソッドを実行するタイミングを示します。

ファイル名: `src/main.rs`

```rust
struct CustomSmartPointer {
    data: String,
}

1 impl Drop for CustomSmartPointer {
    fn drop(&mut self) {
      2 println!(
            "Dropping CustomSmartPointer with data `{}`!",
            self.data
        );
    }
}

fn main() {
  3 let c = CustomSmartPointer {
        data: String::from("my stuff"),
    };
  4 let d = CustomSmartPointer {
        data: String::from("other stuff"),
    };
  5 println!("CustomSmartPointers created.");
6 }
```

リスト15-14: `Drop`トレイトを実装した`CustomSmartPointer`構造体で、クリーンアップコードを配置する場所を示す

`Drop`トレイトはプレリュードに含まれているため、スコープに持ち込む必要はありません。私たちは`CustomSmartPointer`に対して`Drop`トレイトを実装し\[1\]、`println!`を呼び出す`drop`メソッドの実装を提供します\[2\]。`drop`メソッドの本体は、型のインスタンスがスコープ外になるときに実行したい任意のロジックを配置する場所です。ここでは、Rustが`drop`を呼び出すタイミングを視覚的に示すために、いくつかのテキストを表示しています。

`main`関数では、\[3\]と\[4\]で`CustomSmartPointer`の2つのインスタンスを作成し、その後`CustomSmartPointers created`を表示します\[5\]。`main`の末尾\[6\]で、`CustomSmartPointer`のインスタンスはスコープ外になり、Rustは`drop`メソッド\[2\]に入れたコードを呼び出し、最終的なメッセージを表示します。明示的に`drop`メソッドを呼ぶ必要はありません。

このプログラムを実行すると、以下の出力が表示されます。

    CustomSmartPointers created.
    Dropping CustomSmartPointer with data `other stuff`!
    Dropping CustomSmartPointer with data `my stuff`!

インスタンスがスコープ外になるとき、Rustは自動的に私たちのために`drop`を呼び出し、指定したコードを呼び出しました。変数は作成順の逆順で破棄されるため、`d`は`c`の前に破棄されました。この例の目的は、`drop`メソッドがどのように機能するかを視覚的なガイドにすることです。通常は、型が実行するクリーンアップコードを指定することになります。印刷メッセージではなく、型が実行するクリーンアップコードを指定することになります。

残念ながら、自動的な`drop`機能を無効にするのは簡単ではありません。`drop`を無効にすることは通常必要ありません。`Drop`トレイトの主なポイントは、自動的に処理されることです。ただし、場合によっては、値を早期にクリーンアップしたい場合があります。その1つの例は、ロックを管理するスマートポインタを使用する場合です。同じスコープ内の他のコードがロックを取得できるように、ロックを解放する`drop`メソッドを強制したい場合があります。Rustは、`Drop`トレイトの`drop`メソッドを手動で呼ぶことはできません。代わりに、値がスコープの終了前に破棄されるように強制したい場合は、標準ライブラリに提供されている`std::mem::drop`関数を呼び出す必要があります。

リスト15-14の`main`関数を変更して、`Drop`トレイトの`drop`メソッドを手動で呼び出そうとすると、コンパイラエラーが発生します。

ファイル名: `src/main.rs`

```rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    c.drop();
    println!(
        "CustomSmartPointer dropped before the end of main."
    );
}
```

リスト15-15: 早期にクリーンアップするために、`Drop`トレイトの`drop`メソッドを手動で呼び出そうとする

このコードをコンパイルしようとすると、以下のエラーが表示されます。

```bash
error[E0040]: explicit use of destructor method
  --> src/main.rs:16:7
   |
16 |     c.drop();
   |     --^^^^--
   |     | |
   |     | explicit destructor calls not allowed
   |     help: consider using `drop` function: `drop(c)`
```

このエラーメッセージは、明示的に`drop`を呼ぶことはできないことを示しています。エラーメッセージでは、インスタンスをクリーンアップする関数を一般的なプログラミング用語である「デストラクタ」と呼んでいます。「デストラクタ」は、インスタンスを作成する「コンストラクタ」に似ています。Rustの`drop`関数は、特定のデストラクタです。

Rustは明示的に`drop`を呼び出さないようにしています。なぜなら、Rustは`main`の末尾でも自動的に値に対して`drop`を呼び出すからです。これは、同じ値を2回クリーンアップしようとするため、「二重解放」エラーを引き起こします。

値がスコープ外になるときに`drop`の自動挿入を無効にすることはできず、明示的に`drop`メソッドを呼ぶこともできません。したがって、値を早期にクリーンアップする必要がある場合は、`std::mem::drop`関数を使用します。

`std::mem::drop`関数は、`Drop`トレイトの`drop`メソッドとは異なります。強制的に破棄したい値を引数として渡して呼び出します。この関数はプレリュードにあるため、リスト15-15の`main`を変更して`drop`関数を呼び出すことができます。

ファイル名: `src/main.rs`

```rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    drop(c);
    println!(
        "CustomSmartPointer dropped before the end of main."
    );
}
```

リスト15-16: 値がスコープ外になる前に明示的に破棄するために`std::mem::drop`を呼び出す

このコードを実行すると、以下のように表示されます。

    CustomSmartPointer created.
    Dropping CustomSmartPointer with data `some data`!
    CustomSmartPointer dropped before the end of main.

`CustomSmartPointer created.`と`CustomSmartPointer dropped before the end of main.`の間に、`Dropping CustomSmartPointer with data `some data`!`というテキストが表示されます。これは、その時点で`c`を破棄するために`drop`メソッドコードが呼び出されたことを示しています。

`Drop`トレイトの実装で指定したコードを、クリーンアップを便利で安全にするために様々な方法で使用できます。たとえば、独自のメモリ割り当て器を作成するために使用できます！`Drop`トレイトとRustの所有権システムを使うことで、クリーンアップを忘れる必要がなくなります。なぜなら、Rustが自動的に行ってくれるからです。

また、まだ使用中の値を偶発的にクリーンアップすることで引き起こされる問題も心配する必要はありません。参照が常に有効であることを保証する所有権システムは、値がもはや使用されていないときに`drop`が1回だけ呼ばれることも保証します。

これまで`Box<T>`とスマートポインタのいくつかの特性を調べましたので、標準ライブラリで定義されている他のいくつかのスマートポインタを見てみましょう。
