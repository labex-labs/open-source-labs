# はじめに

この実験では、コンパイラは未使用の関数について警告する `dead_code` リントを提供しますが、`#[allow(dead_code)]` などの属性を使用して、リントを無効にし、警告を防ぐことができます。

> **注意：** 実験でファイル名が指定されていない場合は、任意のファイル名を使用できます。たとえば、`main.rs` を使用し、`rustc main.rs &&./main` でコンパイルして実行することができます。
