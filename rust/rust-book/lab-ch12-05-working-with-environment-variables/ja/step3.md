# `search_case_insensitive`関数の実装

リスト 12-21 に示す`search_case_insensitive`関数は、`search`関数とほぼ同じになります。唯一の違いは、`query`と各`line`を小文字に変換することで、入力引数のケースに関係なく、行がクエリを含むかどうかをチェックする際に、ケースが同じになるようにすることです。

ファイル名：`src/lib.rs`

```rust
pub fn search_case_insensitive<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
  1 let query = query.to_lowercase();
    let mut results = Vec::new();

    for line in contents.lines() {
        if 2 line.to_lowercase().contains(3 &query) {
            results.push(line);
        }
    }

    results
}
```

リスト 12-21: クエリと行を比較する前に、クエリと行を小文字にする`search_case_insensitive`関数を定義する

まず、`query`文字列を小文字に変換し、同じ名前のシャドウ変数に格納します\[1\]。クエリに`to_lowercase`を呼び出すことは必要です。ユーザーのクエリが`"rust"`、`"RUST"`、`"Rust"`、または`"rUsT"`のいずれであっても、クエリを`"rust"`として扱い、ケースに関係なくなるようにするためです。`to_lowercase`は基本的な Unicode を処理しますが、100% 正確ではありません。本当のアプリケーションを書く場合、ここでもう少し作業が必要になりますが、このセクションは環境変数に関するものであり、Unicode ではないので、ここではそれにとどめます。

`query`は現在、文字列スライスではなく`String`になっています。なぜなら、`to_lowercase`を呼び出すと新しいデータが作成されるため、既存のデータを参照するわけではないからです。例えば、クエリが`"rUsT"`の場合、その文字列スライスには小文字の`u`や`t`が含まれておらず、使用できません。そのため、`"rust"`を含む新しい`String`を割り当てる必要があります。現在、`query`を`contains`メソッドの引数として渡す際には、アンパサンドを付ける必要があります\[3\]。なぜなら、`contains`のシグネチャは文字列スライスを取るように定義されているからです。

次に、各`line`に`to_lowercase`を呼び出して、すべての文字を小文字に変換します\[2\]。これで`line`と`query`が小文字になったので、クエリのケースに関係なく一致するものを見つけることができます。

この実装がテストに合格するかどうか見てみましょう：

    running 2 tests
    test tests::case_insensitive... ok
    test tests::case_sensitive... ok

    test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

素晴らしい！合格しました。次に、`run`関数から新しい`search_case_insensitive`関数を呼び出しましょう。まず、`Config`構造体にコンフィグオプションを追加して、大文字小文字を区別する検索と大文字小文字を区別しない検索の間で切り替えられるようにします。このフィールドを追加すると、コンパイラエラーが発生します。なぜなら、まだどこでもこのフィールドを初期化していないからです：

ファイル名：`src/lib.rs`

```rust
pub struct Config {
    pub query: String,
    pub file_path: String,
    pub ignore_case: bool,
}
```

`ignore_case`フィールドを追加しました。これはブール値を保持します。次に、`run`関数が`ignore_case`フィールドの値をチェックし、それを使って`search`関数か`search_case_insensitive`関数を呼び出すかを決定する必要があります。リスト 12-22 に示すようになります。これでもまだコンパイルされません。

ファイル名：`src/lib.rs`

```rust
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)?;

    let results = if config.ignore_case {
        search_case_insensitive(&config.query, &contents)
    } else {
        search(&config.query, &contents)
    };

    for line in results {
        println!("{line}");
    }

    Ok(())
}
```

リスト 12-22: `config.ignore_case`の値に基づいて`search`または`search_case_insensitive`を呼び出す

最後に、環境変数をチェックする必要があります。環境変数を操作する関数は、標準ライブラリの`env`モジュールにあります。そのため、`src/lib.rs`の先頭でそのモジュールをスコープに持ち込みます。そして、`env`モジュールの`var`関数を使って、`IGNORE_CASE`という名前の環境変数に値が設定されているかどうかをチェックします。リスト 12-23 に示すようになります。

ファイル名：`src/lib.rs`

```rust
use std::env;
--snip--

impl Config {
    pub fn build(
        args: &[String]
    ) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
```

リスト 12-23: `IGNORE_CASE`という名前の環境変数に値が設定されているかどうかをチェックする

ここで、新しい変数`ignore_case`を作成します。その値を設定するには、`env::var`関数を呼び出し、`IGNORE_CASE`環境変数の名前を渡します。`env::var`関数は`Result`を返します。環境変数が何らかの値に設定されている場合、それは環境変数の値を含む成功した`Ok`バリアントになります。環境変数が設定されていない場合、`Err`バリアントが返されます。

`Result`の`is_ok`メソッドを使って、環境変数が設定されているかどうかをチェックしています。これは、プログラムが大文字小文字を区別しない検索を行う必要があることを意味します。`IGNORE_CASE`環境変数が何も設定されていない場合、`is_ok`は`false`を返し、プログラムは大文字小文字を区別した検索を行います。環境変数の値には関係なく、設定されているかどうかだけを見ているので、`unwrap`、`expect`、または`Result`で見た他のメソッドを使わずに、`is_ok`をチェックしています。

`ignore_case`変数の値を`Config`インスタンスに渡します。そうすることで、`run`関数はその値を読み取り、リスト 12-22 で実装したように、`search_case_insensitive`または`search`を呼び出すかを決定できます。

試してみましょう！まず、環境変数を設定せずに、クエリ`to`でプログラムを実行します。これは、小文字の*to*を含む任意の行と一致するはずです：

```bash
$ cargo run -- to poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep to poem.txt`
Are you nobody, too?
How dreary to be somebody!
```

まだ機能しているようです！次に、`IGNORE_CASE`を`1`に設定して、同じクエリ`to`でプログラムを実行します：

```bash
IGNORE_CASE=1 cargo run -- to poem.txt
```

PowerShell を使っている場合は、環境変数を設定してプログラムを個別のコマンドで実行する必要があります：

```rust
PS> $Env:IGNORE_CASE=1; cargo run -- to poem.txt
```

これにより、`IGNORE_CASE`がシェルセッションの残りの間持続します。`Remove-Item`コマンドレットで解除できます：

```rust
PS> Remove-Item Env:IGNORE_CASE
```

大文字の*to*を含む行が得られるはずです：

    Are you nobody, too?
    How dreary to be somebody!
    To tell your name the livelong day
    To an admiring bog!

素晴らしい！*To*を含む行も得られました！`minigrep`プログラムは、環境変数によって制御される大文字小文字を区別しない検索ができるようになりました。これで、コマンドライン引数または環境変数を使って設定されるオプションを管理する方法がわかりました。

一部のプログラムでは、同じコンフィグに対して引数と環境変数の両方を許可しています。その場合、プログラムはどちらか一方が優先するように決定します。独自の演習として、コマンドライン引数または環境変数を通じて大文字小文字の区別を制御してみてください。プログラムを大文字小文字を区別するように設定し、大文字小文字を区別しないように設定した場合、コマンドライン引数と環境変数のどちらが優先するかを決定してみてください。

`std::env`モジュールには、環境変数を扱うためのさらに多くの便利な機能があります。利用可能な機能を確認するには、そのドキュメントを参照してください。
