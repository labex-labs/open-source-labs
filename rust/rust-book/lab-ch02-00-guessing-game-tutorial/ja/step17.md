# 無効な入力を処理する

ゲームの動作をさらに改善するために、ユーザーが数字以外を入力したときにプログラムがクラッシュする代わりに、ゲームが数字以外を無視してユーザーが続けて予想できるようにしましょう。これは、`guess`を`String`から`u32`に変換する行を変更することで行うことができます。リスト 2-5 に示すようになります。

ファイル名：`src/main.rs`

```rust
--snip--

io::stdin()
 .read_line(&mut guess)
 .expect("Failed to read line");

let guess: u32 = match guess.trim().parse() {
    Ok(num) => num,
    Err(_) => continue,
};

println!("You guessed: {guess}");

--snip--
```

リスト 2-5：数字以外の予想を無視し、プログラムをクラッシュさせる代わりに別の予想を求める

エラー発生時にクラッシュする代わりにエラーを処理するために、`expect`呼び出しから`match`式に切り替えます。覚えておいてください。`parse`は`Result`型を返し、`Result`は`Ok`と`Err`のバリアントを持つ列挙型です。ここでは、`cmp`メソッドの`Ordering`結果と同じように`match`式を使用しています。

`parse`が文字列を正常に数値に変換できた場合、それは結果の数値を含む`Ok`値を返します。その`Ok`値は最初のアームのパターンに一致し、`match`式は`parse`が生成して`Ok`値の中に入れた`num`値をそのまま返します。その数値は、作成している新しい`guess`変数の正しい場所に最終的に入ります。

`parse`が文字列を数値に変換できなかった場合、それはエラーに関する詳細な情報を含む`Err`値を返します。`Err`値は最初の`match`アームの`Ok(num)`パターンと一致しませんが、2 番目のアームの`Err(_)`パターンと一致します。アンダースコア`_`は全てをキャッチする値です。この例では、どんな情報が入っていようとすべての`Err`値と一致させたいと言っています。したがって、プログラムは 2 番目のアームのコードである`continue`を実行します。これは、プログラムに`loop`の次の反復に移り、別の予想を求めるように指示します。したがって、実際には、プログラムは`parse`が遭遇するすべてのエラーを無視します！

これで、プログラムのすべての部分が期待通りに動作するはずです。試してみましょう：

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 4.45s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 61
Please input your guess.
10
You guessed: 10
Too small!
Please input your guess.
99
You guessed: 99
Too big!
Please input your guess.
foo
Please input your guess.
61
You guessed: 61
You win!
```

素晴らしい！最後の小さな調整を加えることで、予想ゲームを完成させます。プログラムはまだ秘密の数を表示していることを思い出してください。これはテストには便利でしたが、ゲームを台無しにしてしまいます。秘密の数を出力する`println!`を削除しましょう。リスト 2-6 に最終コードを示します。

ファイル名：`src/main.rs`

```rust
use rand::Rng;
use std::cmp::Ordering;
use std::io;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();

        io::stdin()
         .read_line(&mut guess)
         .expect("Failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
```

リスト 2-6：完成した予想ゲームのコード

この時点で、あなたは成功裏に予想ゲームを作成しました。おめでとうございます！
