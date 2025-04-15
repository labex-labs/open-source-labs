# 特定の要求がない限り一部のテストを無視する

時には、特定のいくつかのテストを実行するのに非常に時間がかかる場合があります。そのため、`cargo test`のほとんどの実行時にそれらを除外したい場合があります。実行したいすべてのテストを引数として列挙する代わりに、時間がかかるテストに`ignore`属性を付けて除外することができます。以下に示します。

ファイル名: `src/lib.rs`

```rust
#[test]
fn it_works() {
    let result = 2 + 2;
    assert_eq!(result, 4);
}

#[test]
#[ignore]
fn expensive_test() {
    // 1時間かかる実行コード
}
```

`#[test]`の後に、除外したいテストに`#[ignore]`行を追加します。今、テストを実行すると、`it_works`は実行されますが、`expensive_test`は実行されません。

```bash
[object Object]
```

`expensive_test`関数は`ignored`として表示されます。無視されたテストのみを実行したい場合は、`cargo test -- --ignored`を使用できます。

```bash
[object Object]
```

どのテストを実行するかを制御することで、`cargo test`の結果が迅速に返されることを確認できます。無視されたテストの結果を確認するのが適切で、結果を待つ時間がある場合、代わりに`cargo test -- --ignored`を実行できます。無視されているかどうかに関係なくすべてのテストを実行したい場合は、`cargo test -- --include-ignored`を実行できます。
