# 統合テスト

単体テストは、1回に1つのモジュールを孤立してテストするものです。それらは小さく、プライベートコードをテストすることができます。統合テストは、クレートの外部にあり、他のコードと同じようにパブリックインターフェイスのみを使用します。その目的は、ライブラリの多くの部分が正しく一緒に機能することをテストすることです。

Cargoは、`src`の隣の`tests`ディレクトリで統合テストを探します。

ファイル`src/lib.rs`：

```rust
// これを`adder`というクレートで定義します。
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

テスト用のファイル：`tests/integration_test.rs`：

```rust
#[test]
fn test_add() {
    assert_eq!(adder::add(3, 2), 5);
}
```

`cargo test`コマンドでテストを実行する：

```shell
$ cargo test
running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out

Running target/debug/deps/integration_test-bcd60824f5fbfe19

running 1 test
test test_add... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
0 filtered out

Doc-tests adder

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

`tests`ディレクトリ内の各Rustソースファイルは、別個のクレートとしてコンパイルされます。統合テスト間でコードを共有するために、パブリック関数を持つモジュールを作成し、テスト内でインポートして使用することができます。

ファイル`tests/common/mod.rs`：

```rust
pub fn setup() {
    // 必要なファイル/ディレクトリを作成したり、サーバーを起動したりするなど、いくつかのセットアップコード。
}
```

テスト用のファイル：`tests/integration_test.rs`

```rust
// 共通モジュールをインポートします。
mod common;

#[test]
fn test_add() {
    // 共通コードを使用します。
    common::setup();
    assert_eq!(adder::add(3, 2), 5);
}
```

`tests/common.rs`としてモジュールを作成しても機能しますが、推奨されていません。なぜなら、テストランナーはこのファイルをテストクレートとして扱い、その中のテストを実行しようとするからです。
