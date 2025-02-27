# 名前でテストのサブセットを実行する

時には、完全なテストスイートを実行するのに長い時間がかかることがあります。特定のコード領域の作業中は、そのコードに関連するテストのみを実行したい場合があります。`cargo test`に実行したいテストの名前を引数として渡すことで、実行するテストを選ぶことができます。

テストのサブセットを実行する方法を示すために、まず`add_two`関数に対して3つのテストを作成します（リスト11-11を参照）。そして、実行するテストを選びます。

ファイル名: `src/lib.rs`

```rust
pub fn add_two(a: i32) -> i32 {
    a + 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn add_two_and_two() {
        assert_eq!(4, add_two(2));
    }

    #[test]
    fn add_three_and_two() {
        assert_eq!(5, add_two(3));
    }

    #[test]
    fn one_hundred() {
        assert_eq!(102, add_two(100));
    }
}
```

リスト11-11: 3つの異なる名前の3つのテスト

前述のように、引数を渡さずにテストを実行すると、すべてのテストが並列で実行されます。

    running 3 tests
    test tests::add_three_and_two... ok
    test tests::add_two_and_two... ok
    test tests::one_hundred... ok

    test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s
