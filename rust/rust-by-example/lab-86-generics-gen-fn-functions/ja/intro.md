# はじめに

この実験では、Rust でジェネリック関数を定義する方法を学びます。関数をジェネリックにするには、型 `T` の前に `<T>` を付けます。場合によっては、ジェネリック関数を呼び出す際に型パラメータを明示的に指定する必要があります。これは `fun::<A, B,...>()` という構文を使って行うことができます。提供されたコードは、Rust でのジェネリック関数の使用方法を示しており、ジェネリックでない関数の例も含まれています。

> **注：** 実験でファイル名が指定されていない場合、好きなファイル名を使うことができます。たとえば、`main.rs` を使って、`rustc main.rs &&./main` でコンパイルして実行することができます。
