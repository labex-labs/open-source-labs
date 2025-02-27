# 統合テストにおけるサブモジュール

統合テストを増やすにつれて、`tests` ディレクトリにさらにファイルを作成して整理することが望ましくなる場合があります。たとえば、テスト関数をテストする機能ごとにグループ化することができます。前述のとおり、`tests` ディレクトリ内の各ファイルは個別のクレートとしてコンパイルされます。これは、個別のスコープを作成して最終ユーザーがクレートを使用する方法により密接に似せるために役立ちます。ただし、これは、`tests` ディレクトリ内のファイルが、第7章でコードをモジュールとファイルに分離する方法に関して学んだ通り、`src` 内のファイルと同じ動作を共有しないことを意味します。

`tests` ディレクトリのファイルの異なる動作は、複数の統合テストファイルで使用する一連のヘルパー関数があり、「モジュールを別のファイルに分離する」の手順に従ってそれらを共通のモジュールに抽出しようとするときに最も顕著になります。たとえば、`tests/common.rs` を作成し、その中に `setup` という名前の関数を配置すると、複数のテストファイルの複数のテスト関数から呼び出したいコードを `setup` に追加できます。

ファイル名: `tests/common.rs`

```rust
pub fn setup() {
    // setup code specific to your library's tests would go here
}
```

テストを再度実行すると、`common.rs` ファイル用の新しいセクションがテスト出力に表示されます。このファイルにはテスト関数が含まれておらず、どこからも `setup` 関数を呼び出していません。

    running 1 test
    test tests::internal... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

         Running tests/common.rs (target/debug/deps/common-
    92948b65e88960b4)

    running 0 tests

    test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

         Running tests/integration_test.rs
    (target/debug/deps/integration_test-92948b65e88960b4)

    running 1 test
    test it_adds_two... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

       Doc-tests adder

    running 0 tests

    test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

`common` が `running 0 tests` が表示された状態でテスト結果に表示されるのは、私たちが望んだものではありません。他の統合テストファイルとコードを共有したかっただけです。`common` がテスト出力に表示されないようにするには、`tests/common.rs` を作成する代わりに、`tests/common/mod.rs` を作成します。現在のプロジェクトディレクトリは次のようになります。

    ├── Cargo.lock
    ├── Cargo.toml
    ├── src
    │   └── lib.rs
    └── tests
        ├── common
        │   └── mod.rs
        └── integration_test.rs

これは、「代替ファイルパス」で説明した、Rustが理解する古い命名規則です。このようにファイル名を付けることで、Rustに対して `common` モジュールを統合テストファイルとして扱わないように伝えます。`setup` 関数のコードを `tests/common/mod.rs` に移動し、`tests/common.rs` ファイルを削除すると、テスト出力のセクションはもはや表示されません。`tests` ディレクトリのサブディレクトリ内のファイルは、個別のクレートとしてコンパイルされたり、テスト出力にセクションが表示されたりしません。

`tests/common/mod.rs` を作成した後、統合テストファイルのいずれかからモジュールとして使用できます。以下は、`tests/integration_test.rs` の `it_adds_two` テストから `setup` 関数を呼び出す例です。

ファイル名: `tests/integration_test.rs`

```rust
use adder;

mod common;

#[test]
fn it_adds_two() {
    common::setup();
    assert_eq!(4, adder::add_two(2));
}
```

`mod common;` 宣言は、リスト7-21で示したモジュール宣言と同じであることに注意してください。そして、テスト関数内では、`common::setup()` 関数を呼び出すことができます。
