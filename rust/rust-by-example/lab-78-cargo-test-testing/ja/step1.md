# テスト

私たちが知っているように、テストはソフトウェアのどの部分にも不可欠です！Rustは、ユニットテストと統合テストに対して一流のサポートを備えています（TRPLの[この章](https://doc.rust-lang.org/book/ch11-00-testing.html)を参照）。

上記のリンクされたテストの章から、ユニットテストと統合テストを書く方法がわかります。組織的には、ユニットテストをそれがテストするモジュールに配置し、統合テストを独自の`tests/`ディレクトリに配置することができます。

```txt
foo
├── Cargo.toml
├── src
│   └── main.rs
│   └── lib.rs
└── tests
    ├── my_test.rs
    └── my_other_test.rs
```

`tests`内の各ファイルは、独立した[統合テスト](https://doc.rust-lang.org/book/ch11-03-test-organization.html#integration-tests)です。つまり、依存クレートから呼び出されているかのように、ライブラリをテストするためのテストです。

テストの章では、3つの異なるテストスタイル：ユニット、ドキュメント、および統合について詳しく説明されています。

`cargo`は自然に、すべてのテストを実行する簡単な方法を提供します！

```shell
$ cargo test
```

以下のような出力が表示されるはずです。

```shell

```

また、名前がパターンに一致するテストを実行することもできます。

```shell
$ cargo test test_foo
```

```shell

```

注意点として1つだけ：Cargoは複数のテストを同時に実行する場合があるので、互いに競合しないようにしてください。

この並列実行が問題を引き起こす1つの例は、2つのテストがファイルに出力する場合です。例えば、以下のようになります。

```rust
#[cfg(test)]
mod tests {
    // 必要なモジュールをインポート
    use std::fs::OpenOptions;
    use std::io::Write;

    // このテストはファイルに書き込みます
    #[test]
    fn test_file() {
        // ferris.txtを開き、存在しない場合は作成します。
        let mut file = OpenOptions::new()
         .append(true)
         .create(true)
         .open("ferris.txt")
         .expect("Failed to open ferris.txt");

        // "Ferris"を5回表示します。
        for _ in 0..5 {
            file.write_all("Ferris\n".as_bytes())
             .expect("Could not write to ferris.txt");
        }
    }

    // このテストは同じファイルに書き込もうとします
    #[test]
    fn test_file_also() {
        // ferris.txtを開き、存在しない場合は作成します。
        let mut file = OpenOptions::new()
         .append(true)
         .create(true)
         .open("ferris.txt")
         .expect("Failed to open ferris.txt");

        // "Corro"を5回表示します。
        for _ in 0..5 {
            file.write_all("Corro\n".as_bytes())
             .expect("Could not write to ferris.txt");
        }
    }
}
```

意図したのは以下のようになるはずです。

```shell
$ cat ferris.txt
Ferris
Ferris
Ferris
Ferris
Ferris
Corro
Corro
Corro
Corro
Corro
```

実際に`ferris.txt`に入るのはこれです。

```shell
$ cargo test test_foo
Corro
Ferris
Corro
Ferris
Corro
Ferris
Corro
Ferris
Corro
Ferris
```
