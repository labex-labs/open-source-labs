# はじめに

この実験では、Rust で `enum` を使ってリンクリストを実装します。`List` 列挙型は 2 つのバリアントを持ちます。`Cons` は要素と次のノードへのポインタを持つノードを表し、`Nil` はリンクリストの終端を示します。この列挙型には、空のリストを作成する `new`、リストの先頭に要素を追加する `prepend`、リストの長さを返す `len`、およびリストの文字列表現を返す `stringify` などのメソッドがあります。提供されたメイン関数は、これらのメソッドを使ってリンクリストを作成および操作する方法を示しています。

> **注：** 実験でファイル名が指定されていない場合、好きなファイル名を使うことができます。たとえば、`main.rs` を使って、`rustc main.rs &&./main` でコンパイルして実行することができます。
