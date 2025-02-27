# tests ディレクトリ

プロジェクトディレクトリのトップレベルに、`src` の隣に `tests` ディレクトリを作成します。Cargoはこのディレクトリ内の統合テストファイルを探すようになっています。その後、必要なだけ多くのテストファイルを作成でき、Cargoは各ファイルを個別のクレートとしてコンパイルします。

統合テストを作成しましょう。`src/lib.rs` ファイルにまだリスト11-12のコードがある状態で、`tests` ディレクトリを作成し、新しいファイル `tests/integration_test.rs` を作成します。ディレクトリ構造は以下のようになります。

    adder
    ├── Cargo.lock
    ├── Cargo.toml
    ├── src
    │   └── lib.rs
    └── tests
        └── integration_test.rs

リスト11-13のコードを `tests/integration_test.rs` ファイルに入力します。

ファイル名: `tests/integration_test.rs`

```rust
use adder;

#[test]
fn it_adds_two() {
    assert_eq!(4, adder::add_two(2));
}
```

リスト11-13: `adder` クレート内の関数の統合テスト

`tests` ディレクトリ内の各ファイルは別個のクレートであるため、ライブラリを各テストクレートのスコープに入れる必要があります。そのため、コードの上部に `use adder;` を追加します。これは単体テストでは必要ありませんでした。

`tests/integration_test.rs` 内のコードには `#[cfg(test)]` でアノテートする必要はありません。Cargoは `tests` ディレクトリを特別扱いし、`cargo test` を実行したときのみこのディレクトリ内のファイルをコンパイルします。今 `cargo test` を実行してみましょう。

```bash
$ cargo test
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 1.31s
     Running unittests src/lib.rs (target/debug/deps/adder-
1082c4b063a8fbe6)

1 running 1 test
test tests::internal... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.00s

   2 Running tests/integration_test.rs
(target/debug/deps/integration_test-1082c4b063a8fbe6)

running 1 test
3 test it_adds_two... ok

4 test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.00s

   Doc-tests adder

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.00s
```

出力の3つのセクションには、単体テスト、統合テスト、ドキュメントテストが含まれています。セクション内のテストが1つでも失敗すると、次のセクションは実行されません。たとえば、単体テストが失敗すると、統合テストとドキュメントテストの出力はありません。なぜなら、それらのテストはすべての単体テストが合格した場合にのみ実行されるからです。

単体テストの最初のセクション\[1\]は、これまで見てきたものと同じです。各単体テストに1行（リスト11-12で追加した `internal` という名前のもの）があり、その後に単体テストのサマリー行があります。

統合テストのセクションは、`Running tests/integration_test.rs` という行で始まります\[2\]。次に、その統合テスト内の各テスト関数に1行があり\[3\]、`Doc-tests adder` セクションが始まる直前に統合テストの結果のサマリー行があります\[4\]。

各統合テストファイルには独自のセクションがあるため、`tests` ディレクトリにさらにファイルを追加すると、統合テストのセクションが増えます。

特定の統合テスト関数を実行するには、`cargo test` に対してテスト関数の名前を引数として指定します。特定の統合テストファイル内のすべてのテストを実行するには、`cargo test` の `--test` 引数に続けてファイル名を指定します。

```bash
$ cargo test --test integration_test
    Finished test [unoptimized + debuginfo] target(s) in 0.64s
     Running tests/integration_test.rs
(target/debug/deps/integration_test-82e7799c1bc62298)

running 1 test
test it_adds_two... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.00s
```

このコマンドは、`tests/integration_test.rs` ファイル内のテストのみを実行します。
