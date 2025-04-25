# `assert!` マクロを使った結果のチェック

標準ライブラリによって提供される `assert!` マクロは、テスト内のある条件が `true` であることを確認したい場合に便利です。`assert!` マクロには、ブール値に評価される引数を渡します。値が `true` の場合、何も起こらず、テストは合格します。値が `false` の場合、`assert!` マクロは `panic!` を呼び出してテストを失敗させます。`assert!` マクロを使うことで、コードが意図通りに機能していることを確認できます。

リスト 5-15 では、`Rectangle` 構造体と `can_hold` メソッドを使用しました。これらは、リスト 11-5 に再掲してあります。このコードを `src/lib.rs` ファイルに入れて、`assert!` マクロを使ってそれに対するいくつかのテストを書きましょう。

ファイル名：`src/lib.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

リスト 11-5: 第 5 章の `Rectangle` 構造体とその `can_hold` メソッドの使用

`can_hold` メソッドはブール値を返すので、`assert!` マクロに最適なケースです。リスト 11-6 では、幅が 8 で高さが 7 の `Rectangle` インスタンスを作成し、幅が 5 で高さが 1 の別の `Rectangle` インスタンスを保持できることをアサートすることで、`can_hold` メソッドをテストします。

ファイル名：`src/lib.rs`

```rust
#[cfg(test)]
mod tests {
  1 use super::*;

    #[test]
  2 fn larger_can_hold_smaller() {
      3 let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

      4 assert!(larger.can_hold(&smaller));
    }
}
```

リスト 11-6: 大きな四角形が小さな四角形を実際に保持できるかどうかをチェックする `can_hold` のテスト

`tests` モジュールの中に新しい行 `use super::*;` を追加しています\[1\]。`tests` モジュールは、「モジュールツリー内のアイテムを参照するためのパス」で説明した通常の可視性ルールに従う通常のモジュールです。`tests` モジュールは内部モジュールなので、テスト対象のコードを外部モジュールから内部モジュールのスコープに持ち込む必要があります。ここではグロブを使っているので、外部モジュールで定義したものはすべてこの `tests` モジュールで利用できます。

テストの名前を `larger_can_hold_smaller` にしています\[2\]。そして、必要な 2 つの `Rectangle` インスタンスを作成しています\[3\]。その後、`assert!` マクロを呼び出し、`larger.can_hold(&smaller)` の呼び出し結果を渡しています\[4\]。この式は `true` を返すはずなので、テストは合格するはずです。確認してみましょう！

    running 1 test
    test tests::larger_can_hold_smaller... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

合格しました！もう 1 つのテストを追加しましょう。今度は、小さな四角形が大きな四角形を保持できないことをアサートします。

ファイル名：`src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn larger_can_hold_smaller() {
        --snip--
    }

    #[test]
    fn smaller_cannot_hold_larger() {
        let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

        assert!(!smaller.can_hold(&larger));
    }
}
```

この場合、`can_hold` 関数の正しい結果は `false` なので、`assert!` マクロに渡す前にその結果を否定する必要があります。その結果、`can_hold` が `false` を返す場合、テストは合格します。

    running 2 tests
    test tests::larger_can_hold_smaller... ok
    test tests::smaller_cannot_hold_larger... ok

    test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

2 つのテストが合格しました！では、コードにバグを入れた場合、テスト結果がどうなるか見てみましょう。`can_hold` メソッドの実装を変更して、幅を比較する際の大なり記号を小なり記号に置き換えます。

    --snip--

    impl Rectangle {
        fn can_hold(&self, other: &Rectangle) -> bool {
            self.width < other.width && self.height > other.height
        }
    }

今、テストを実行すると次のような結果になります。

    running 2 tests
    test tests::smaller_cannot_hold_larger... ok
    test tests::larger_can_hold_smaller... FAILED

    failures:

    ---- tests::larger_can_hold_smaller stdout ----
    thread'main' panicked at 'assertion failed:
    larger.can_hold(&smaller)', src/lib.rs:28:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace


    failures:
        tests::larger_can_hold_smaller

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

テストがバグを検出しました！`larger.width` が 8 で `smaller.width` が 5 なので、`can_hold` での幅の比較は今では `false` を返します。8 は 5 未満ではありません。
