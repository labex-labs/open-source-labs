# はじめに

この実験では、クロージャを入力パラメータとして受け取る Rust の関数を書く際、クロージャの完全な型を、クロージャがキャプチャされた値を参照、可変参照、または値でどのように使用するかを決定する `Fn`、`FnMut`、または `FnOnce` のいずれかの `トレイト` を使用して注釈付けする必要があることを学びます。コンパイラは、クロージャに選択されたトレイトに基づいて、可能な限り制限の少ない方法で変数をキャプチャします。

> **注：** 実験でファイル名が指定されていない場合、好きなファイル名を使用できます。たとえば、`main.rs` を使用して、`rustc main.rs &&./main` でコンパイルして実行できます。
