# はじめに

この実験では、Rust の `HashMap` における代替/カスタム キー型の使用方法を検討します。これには、`bool`、`int`、`uint`、`String`、`&str` など、`Eq` と `Hash` トレイトを実装する型が含まれます。また、`#[derive(PartialEq, Eq, Hash)]` 属性を使用してカスタム型にこれらのトレイトを実装することができ、`HashMap` のキーとして使用できるようになります。

> **注：** 実験でファイル名が指定されていない場合は、好きなファイル名を使用できます。たとえば、`main.rs` を使用して、`rustc main.rs &&./main` でコンパイルして実行することができます。
