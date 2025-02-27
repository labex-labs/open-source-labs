# Configのコンストラクタの作成

これまで、コマンドライン引数を解析する責任のあるロジックを`main`から抽出し、`parse_config`関数に配置しました。これにより、`query`と`file_path`の値が関連していることがわかり、その関係をコードで表現する必要があることがわかりました。そこで、`query`と`file_path`の関連する目的を名前付けするために`Config`構造体を追加し、`parse_config`関数から値の名前を構造体フィールド名として返せるようにしました。

ですから、今では`parse_config`関数の目的が`Config`インスタンスを作成することになっているので、`parse_config`を単なる関数から`Config`構造体に関連付けられた`new`という名前の関数に変更することができます。この変更により、コードがより慣例に沿ったものになります。標準ライブラリの型（たとえば`String`）のインスタンスを作成するには、`String::new`を呼び出します。同様に、`parse_config`を`Config`に関連付けられた`new`関数に変更することで、`Config::new`を呼び出すことで`Config`のインスタンスを作成できるようになります。リスト12-7は必要な変更を示しています。

ファイル名: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

  1 let config = Config::new(&args);

    --snip--
}

--snip--

2 impl Config {
  3 fn new(args: &[String]) -> Config {
        let query = args[1].clone();
        let file_path = args[2].clone();

        Config { query, file_path }
    }
}
```

リスト12-7: `parse_config`を`Config::new`に変更する

`main`を更新して、`parse_config`を呼び出していた部分を`Config::new`を呼び出すように変更しました\[1\]。`parse_config`の名前を`new`に変更し\[3\]、`impl`ブロック内に移動しました\[2\]。これにより、`new`関数が`Config`と関連付けられます。このコードを再コンパイルして、正常に動作することを確認してみてください。
