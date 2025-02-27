# 乱数の生成

では、予想するための数を生成するために`rand`を使ってみましょう。次のステップは、リスト2-3に示すように`src/main.rs`を更新することです。

ファイル名：`src/main.rs`

```rust
use std::io;
1 use rand::Rng;

fn main() {
    println!("Guess the number!");

  2 let secret_number = rand::thread_rng().gen_range(1..=100);

  3 println!("The secret number is: {secret_number}");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
     .read_line(&mut guess)
     .expect("Failed to read line");

    println!("You guessed: {guess}");
}
```

リスト2-3：乱数を生成するコードの追加

まず、`use rand::Rng;`という行を追加します\[1\]。`Rng`トレイトは、乱数生成器が実装するメソッドを定義しており、これらのメソッドを使用するためにはこのトレイトがスコープ内にある必要があります。第10章ではトレイトについて詳細に説明します。

次に、途中に2行を追加します。最初の行で\[2\]、`rand::thread_rng`関数を呼び出します。この関数は、使用する特定の乱数生成器を返します。これは、現在の実行スレッド固有のもので、オペレーティングシステムによってシードが設定されます。その後、乱数生成器の`gen_range`メソッドを呼び出します。このメソッドは、`use rand::Rng;`文によってスコープ内に持ち込んだ`Rng`トレイトによって定義されています。`gen_range`メソッドは、範囲式を引数として取り、その範囲内の乱数を生成します。ここで使用している範囲式の形式は`start..=end`で、下限と上限の両方が含まれます。したがって、1から100の間の数を要求するには`1..=100`を指定する必要があります。

> 注：どのトレイトを使用するか、またクレートからどのメソッドや関数を呼ぶかをすぐに知ることはできません。したがって、各クレートには使用方法の説明が含まれたドキュメントがあります。Cargoのもう一つの便利な機能は、`cargo doc --open`コマンドを実行すると、すべての依存関係によって提供されるドキュメントがローカルにビルドされ、ブラウザで開かれることです。たとえば、`rand`クレートの他の機能に興味がある場合は、`cargo doc --open`を実行して、左側のサイドバーの`rand`をクリックしてください。

2番目の新しい行で\[3\]、秘密の数を表示します。これは、プログラムを開発中にテストするために便利ですが、最終バージョンからは削除します。プログラムが始まるとすぐに答えを表示すると、あまりゲームになりません！

このプログラムを何回か実行してみてください：

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 7
Please input your guess.
4
You guessed: 4

$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.02s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 83
Please input your guess.
5
You guessed: 5
```

異なる乱数が得られるはずで、それらはすべて1から100の間の数であるはずです。素晴らしい仕事です！
