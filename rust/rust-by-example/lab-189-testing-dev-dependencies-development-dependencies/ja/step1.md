# 開発依存関係

時々、テスト（またはサンプル、またはベンチマーク）にのみ依存関係が必要な場合があります。このような依存関係は、`[dev-dependencies]` セクションの `Cargo.toml` に追加されます。これらの依存関係は、このパッケージに依存する他のパッケージには伝播されません。

そのような例の1つは、[`pretty_assertions`](https://docs.rs/pretty_assertions/1.0.0/pretty_assertions/index.html) です。これは、標準の `assert_eq!` と `assert_ne!` マクロを拡張して、カラー付きの差分を提供します。
ファイル `Cargo.toml`:

```toml
# 標準のクレートデータは省略
[dev-dependencies]
pretty_assertions = "1"
```

ファイル `src/lib.rs`:

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;
    use pretty_assertions::assert_eq; // テストのみで使用するクレート。非テストコードでは使用できません。

    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
    }
}
```
