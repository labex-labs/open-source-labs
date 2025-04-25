# フィールド初期化省略記法の使用

リスト 5-4 では、パラメータ名と構造体のフィールド名がまったく同じであるため、*フィールド初期化省略記法*の構文を使用して`build_user`を書き換えることができます。これにより、同じように動作するが、`username`と`email`の繰り返しがなくなります。これはリスト 5-5 に示されています。

```rust
fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username,
        email,
        sign_in_count: 1,
    }
}
```

リスト 5-5: `username`と`email`のパラメータが構造体のフィールドと同じ名前であるため、フィールド初期化省略記法を使用する`build_user`関数

ここでは、`email`という名前のフィールドを持つ`User`構造体の新しいインスタンスを作成しています。`build_user`関数の`email`パラメータの値に、`email`フィールドの値を設定したいと考えています。`email`フィールドと`email`パラメータが同じ名前であるため、`email: email`ではなく、単に`email`と書くだけです。
