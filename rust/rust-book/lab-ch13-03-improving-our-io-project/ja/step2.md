# 反復子を使ったクローンの削除

リスト 12-6 では、`String`値のスライスを取り、スライスにインデックスを付けて値をクローンすることで`Config`構造体のインスタンスを作成し、`Config`構造体がそれらの値を所有するようにしました。リスト 13-17 では、リスト 12-23 にあった`Config::build`関数の実装を再現しています。

ファイル名：`src/lib.rs`

```rust
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

リスト 13-17: リスト 12-23 の`Config::build`関数の再現

当時、非効率的な`clone`呼び出しは心配しなくて良いと言いました。なぜなら、将来的にそれらを削除するからです。さて、その時が来ました！

ここで`clone`が必要だったのは、パラメータ`args`に`String`要素のスライスがあるためですが、`build`関数は`args`を所有していません。`Config`インスタンスの所有権を返すには、`Config`の`query`と`filename`フィールドから値をクローンする必要がありました。そうすることで、`Config`インスタンスがそれらの値を所有できるようになります。

反復子に関する新しい知識を使って、`build`関数を変更して、スライスを借りる代わりに反復子の所有権を引数として取るようにします。スライスの長さをチェックし、特定の場所にインデックスを付けるコードの代わりに、反復子機能を使います。これにより、`Config::build`関数が何をしているかが明確になります。なぜなら、反復子が値にアクセスするからです。

`Config::build`が反復子の所有権を取得し、借りるインデックス操作を使わなくなると、`String`値を反復子から`Config`に移動できるようになります。その代わりに`clone`を呼び出して新しい割り当てを行う必要はありません。
