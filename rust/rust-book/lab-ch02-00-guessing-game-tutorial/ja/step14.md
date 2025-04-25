# 予想値と秘密の数を比較する

これでユーザー入力と乱数があるので、それらを比較することができます。そのステップをリスト 2-4 に示します。ただし、説明するように、このコードはまだコンパイルされません。

ファイル名：`src/main.rs`

```rust
use rand::Rng;
1 use std::cmp::Ordering;
use std::io;

fn main() {
    --snip--

    println!("You guessed: {guess}");

  2 match guess.3 cmp(&secret_number) {
        Ordering::Less => println!("Too small!"),
        Ordering::Greater => println!("Too big!"),
        Ordering::Equal => println!("You win!"),
    }
}
```

リスト 2-4:2 つの数を比較したときの返り値を処理する

まず、もう一つの`use`文\[1\]を追加します。これにより、標準ライブラリから`std::cmp::Ordering`という型がスコープ内に持ち込まれます。`Ordering`型は別の列挙型であり、`Less`、`Greater`、`Equal`の各バリアントを持っています。これらは 2 つの値を比較したときに考えられる 3 つの結果です。

次に、底部に 5 行の新しいコードを追加します。これらは`Ordering`型を使用しています。`cmp`メソッド\[3\]は 2 つの値を比較し、比較可能な値に対して呼び出すことができます。比較対象の値への参照を引数に取ります。ここでは`guess`と`secret_number`を比較しています。そして、`use`文によってスコープ内に持ち込んだ`Ordering`列挙型のバリアントを返します。`cmp`関数に`guess`と`secret_number`の値を渡して返された`Ordering`のバリアントに基づいて、次に何をするかを決定するために`match`式\[2\]を使用します。

`match`式は「アーム」で構成されています。アームは、一致させる「パターン」と、`match`に渡された値がそのアームのパターンに合致した場合に実行するコードで構成されています。Rust は`match`に渡された値を取り、順番に各アームのパターンを調べます。パターンと`match`構文は強力な Rust の機能です。これらは、コードが遭遇する可能性のあるさまざまな状況を表現し、それらすべてを処理することを確実にします。これらの機能については、それぞれ第 6 章と第 18 章で詳細に説明されます。

ここで使用している`match`式の例を見てみましょう。ユーザーが 50 を予想し、今回ランダムに生成された秘密の数が 38 だったとします。

コードが 50 と 38 を比較すると、`cmp`メソッドは 50 が 38 より大きいため`Ordering::Greater`を返します。`match`式は`Ordering::Greater`の値を取得し、各アームのパターンを順に確認し始めます。最初のアームのパターンである`Ordering::Less`を見ると、`Ordering::Greater`の値が`Ordering::Less`と一致しないことがわかります。したがって、そのアームのコードを無視し、次のアームに移ります。次のアームのパターンは`Ordering::Greater`であり、これは`Ordering::Greater`と一致します！そのアームに関連付けられたコードが実行され、画面に`Too big!`が表示されます。`match`式は最初の成功した一致の後に終了するため、このシナリオでは最後のアームを見ません。

しかし、リスト 2-4 のコードはまだコンパイルされません。試してみましょう：

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
error[E0308]: mismatched types
  --> src/main.rs:22:21
   |
22 |     match guess.cmp(&secret_number) {
   |                     ^^^^^^^^^^^^^^ expected struct `String`, found integer
   |
   = note: expected reference `&String`
              found reference `&{integer}`
```

エラーの核心部分は、「型が一致しません」と表示されています。Rust は強力な静的型システムを持っています。ただし、型推論も備えています。`let mut guess = String::new()`と書いたとき、Rust は`guess`が`String`型であると推論し、型を明示的に書く必要はありませんでした。一方、`secret_number`は数値型です。Rust の数値型のいくつかは 1 から 100 の間の値を持つことができます。`i32`（32 ビット整数）、`u32`（符号なし 32 ビット整数）、`i64`（64 ビット整数）などです。明示的に指定しない限り、Rust はデフォルトで`i32`を使用します。これは`secret_number`の型です。ただし、他の場所で型情報を追加することで、Rust が異なる数値型を推論するようにすることもできます。エラーの原因は、Rust が文字列を数値型と比較できないからです。

最終的には、プログラムが入力として読み取った`String`を実際の数値型に変換して、秘密の数と数値的に比較できるようにする必要があります。そのために、`main`関数の本体にこの行を追加します。

ファイル名：`src/main.rs`

```rust
use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    println!("The secret number is: {secret_number}");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
      .read_line(&mut guess)
      .expect("Failed to read line");

    let guess: u32 = guess
      .trim()
      .parse()
      .expect("Please type a number!");

    println!("You guessed: {guess}");

    match guess.cmp(&secret_number) {
        Ordering::Less => println!("Too small!"),
        Ordering::Greater => println!("Too big!"),
        Ordering::Equal => println!("You win!"),
    }
}
```

`guess`という名前の変数を作成します。でも待ってください。プログラムには既に`guess`という名前の変数がありますよね？そうですが、便利なことに Rust は既存の`guess`の値を新しい値で上書きする（シャドーイング）ことを許可しています。シャドーイングにより、`guess_str`や`guess`のように 2 つの一意の変数を作成する代わりに、`guess`という変数名を再利用できます。これについては第 3 章で詳しく説明しますが、ここでは、値をある型から別の型に変換したい場合によく使用されることを知っておいてください。

この新しい変数を`guess.trim().parse()`という式にバインドします。式内の`guess`は、入力を文字列として含む元の`guess`変数を指します。`String`インスタンスの`trim`メソッドは、先頭と末尾の空白を削除します。これは、`u32`（数値データのみを含む）と文字列を比較するために必要です。ユーザーは`read_line`を満たすためにエンターキーを押して予想値を入力します。これにより、文字列に改行文字が追加されます。たとえば、ユーザーが`5`と入力してエンターキーを押すと、`guess`はこのようになります：`5\n`。`\n`は「改行」を表します。（Windows では、エンターキーを押すと復帰車と改行、`\r\n`が入ります。）`trim`メソッドは`\n`または`\r\n`を削除し、結果として`5`になります。

文字列の`parse`メソッドは、文字列を別の型に変換します。ここでは、文字列を数値に変換するために使用します。`let guess: u32`を使用して、Rust に変換したい正確な数値型を伝えます。`guess`の後のコロン（`:`）は、Rust に変数の型を注釈することを示しています。Rust にはいくつかの組み込み数値型があります。ここで見られる`u32`は、符号なし 32 ビット整数です。小さな正の数には適したデフォルトの選択肢です。第 3 章で他の数値型について学びます。

また、このサンプルプログラムにおける`u32`の注釈と`secret_number`との比較は、Rust が`secret_number`もまた`u32`であると推論することを意味します。したがって、今では同じ型の 2 つの値が比較されるようになりました！

`parse`メソッドは、論理的に数値に変換できる文字のみに対して機能し、したがってエラーを引き起こしやすくなります。たとえば、文字列に`A👍%`が含まれていた場合、それを数値に変換することはできません。失敗する可能性があるため、`parse`メソッドは`Result`型を返します。これは、`read_line`メソッドと同じように（「Result を使った潜在的な失敗の処理」の前半で説明した通り）。同じように`expect`メソッドを使ってこの`Result`を処理します。`parse`が文字列から数値を作成できなかったために`Err` `Result`バリアントを返した場合、`expect`呼び出しはゲームをクラッシュさせ、与えられたメッセージを表示します。`parse`が文字列から数値を正常に変換できた場合、`Result`の`Ok`バリアントを返し、`expect`は`Ok`値から必要な数値を返します。

では、今プログラムを実行してみましょう：

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 0.43s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 58
Please input your guess.
  76
You guessed: 76
Too big!
```

素晴らしい！予想値の前に空白を入れても、プログラムはユーザーが 76 を予想したことを正しく判断しました。正しく予想する、予想値が高すぎる、予想値が低すぎるなど、さまざまな入力に対する異なる動作を確認するために、プログラムを何回か実行してみてください。

これでゲームの大部分は機能していますが、ユーザーは 1 回の予想しかできません。ループを追加することでそれを変更しましょう！
