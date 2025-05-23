# はじめに

この実験では、Rust の`std`ライブラリにある`Option`列挙型について学びます。これは、存在しない可能性がある場合を処理するために使用されます。これには 2 つのオプションがあります。型`T`の要素が見つかった場合には`Some(T)`で、要素が見つからなかった場合には`None`です。これらのケースは、`match`を使って明示的に処理することも、`unwrap`を使って暗黙的に処理することもできます。明示的な処理は、より大きな制御と意味のある出力を可能にしますが、`unwrap`は内部要素を返すか、パニックを引き起こす可能性があります。

> **注：** 実験でファイル名が指定されていない場合、好きなファイル名を使うことができます。たとえば、`main.rs`を使って、`rustc main.rs &&./main`でコンパイルして実行することができます。
