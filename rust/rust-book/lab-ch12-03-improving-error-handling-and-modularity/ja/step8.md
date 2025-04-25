# panic! を呼び出す代わりに Result を返す

代わりに、`Result`値を返します。成功した場合には`Config`インスタンスを含み、エラーの場合には問題を説明します。また、関数名を`new`から`build`に変更します。なぜなら、多くのプログラマーが`new`関数は決して失敗しないことを期待しているからです。`Config::build`が`main`に通信する際、`Result`型を使って問題があることを知らせることができます。そして、`main`を変更して、`Err`バリアントをユーザーにとってより実用的なエラーに変換します。`panic!`の呼び出しが引き起こす`thread'main'`や`RUST_BACKTRACE`に関する周辺のテキストなしです。

リスト 12-9 は、現在`Config::build`と呼び出している関数の返り値と、`Result`を返すために必要な関数の本体に対して行う変更を示しています。ただし、`main`も更新しない限りコンパイルされません。次のリストでそれを行います。

ファイル名：`src/main.rs`

```rust
impl Config {
    fn build(args: &[String]) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        Ok(Config { query, file_path })
    }
}
```

リスト 12-9: `Config::build`から`Result`を返す

`build`関数は、成功した場合には`Config`インスタンスを含む`Result`を返し、エラーの場合には`&'static str`を返します。エラー値は常に`'static`寿命を持つ文字列リテラルになります。

関数の本体で 2 つの変更を行いました。ユーザーが十分な引数を渡さない場合に`panic!`を呼び出す代わりに、今では`Err`値を返し、`Config`の返り値を`Ok`でラップしました。これらの変更により、関数が新しい型シグネチャに準拠するようになりました。

`Config::build`から`Err`値を返すことで、`main`関数は`build`関数から返される`Result`値を処理し、エラーの場合に処理をよりきれいに終了させることができます。
