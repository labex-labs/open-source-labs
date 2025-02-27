# ネストされた `_` を使った値の一部の無視

値の一部のみを無視するために、別のパターンの中でも `_` を使用することができます。たとえば、値の一部のみをテストしたいが、実行したい対応するコードで他の部分を使用する必要がない場合です。リスト18-18は、設定の値を管理するためのコードを示しています。ビジネス要件は、既存の設定のカスタマイズを上書きすることはできないが、設定を解除して、現在解除されている場合には値を与えることができるというものです。

ファイル名: `src/main.rs`

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

リスト18-18: `Some` バリアント内の値を使用する必要がない場合に、`Some` バリアントとマッチするパターン内でアンダースコアを使用する

このコードは、`Can't overwrite an existing customized value` とその後 `setting is Some(5)` を出力します。最初のマッチアームでは、どちらの `Some` バリアント内の値ともマッチさせる必要はなく、使用する必要もありません。ただし、`setting_value` と `new_setting_value` が `Some` バリアントである場合をテストする必要があります。その場合、`setting_value` を変更しない理由を表示し、変更されません。

2番目のアームの `_` パターンで表されるすべての他の場合（`setting_value` または `new_setting_value` のどちらかが `None` の場合）では、`new_setting_value` を `setting_value` にすることを許可します。

また、1つのパターン内の複数の場所でアンダースコアを使用して、特定の値を無視することもできます。リスト18-19は、5つの要素のタプルの2番目と4番目の値を無視する例を示しています。

ファイル名: `src/main.rs`

```rust
let numbers = (2, 4, 8, 16, 32);

match numbers {
    (first, _, third, _, fifth) => {
        println!("Some numbers: {first}, {third}, {fifth}");
    }
}
```

リスト18-19: タプルの複数の部分を無視する

このコードは、`Some numbers: 2, 8, 32` を出力し、値 `4` と `16` は無視されます。