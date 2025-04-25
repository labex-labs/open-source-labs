# ネストされた `_` で値の一部を無視する

他のパターン内で `_` を使用して、値の一部のみを無視することもできます。たとえば、値の一部のみをテストしたいが、対応する実行コードで他の部分を使用する必要がない場合です。リスト 18-18 は、設定値を管理するコードを示しています。ビジネス要件は、ユーザーが既存の設定のカスタマイズを上書きできないようにする一方で、設定が現在未設定の場合には設定を解除して値を設定できるようにすることです。

ファイル名：`src/main.rs`

```rust
let mut setting_value = Some(5);
let new_setting_value = Some(10);

match (setting_value, new_setting_value) {
    (Some(_), Some(_)) => {
        println!("Can't overwrite an existing customized value");
    }
    _ => {
        setting_value = new_setting_value;
    }
}

println!("setting is {:?}", setting_value);
```

リスト 18-18: `Some` 内の値を使用する必要がない場合に、`Some` バリアントにマッチするパターン内でアンダースコアを使用する

このコードは、`Can't overwrite an existing customized value` を出力し、その後 `setting is Some(5)` を出力します。最初のマッチアームでは、どちらの `Some` バリアント内の値にもマッチする必要はなく、それらを使用する必要もありませんが、`setting_value` と `new_setting_value` が `Some` バリアントであるケースをテストする必要があります。その場合、`setting_value` を変更しない理由を出力し、`setting_value` は変更されません。

2 番目のアームの `_` パターンで表される他のすべてのケース（`setting_value` または `new_setting_value` が `None` の場合）では、`new_setting_value` を `setting_value` に設定できるようにします。

また、1 つのパターン内の複数の場所でアンダースコアを使用して、特定の値を無視することもできます。リスト 18-19 は、5 要素のタプル内の 2 番目と 4 番目の値を無視する例を示しています。

ファイル名：`src/main.rs`

```rust
let numbers = (2, 4, 8, 16, 32);

match numbers {
    (first, _, third, _, fifth) => {
        println!("Some numbers: {first}, {third}, {fifth}");
    }
}
```

リスト 18-19: タプルの複数の部分を無視する

このコードは `Some numbers: 2, 8, 32` を出力し、値 `4` と `16` は無視されます。
