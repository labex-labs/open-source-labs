# はじめに

この実験では、Rust の `Path` 構造体を調べます。これは、基礎となるファイルシステム内のファイルパスを表します。2 種類のバージョンがあります。UNIX 系のシステム向けの `posix::Path` と、Windows 向けの `windows::Path` です。`Path` は `OsStr` から作成でき、パスが指すファイルまたはディレクトリから情報を取得するための様々なメソッドを提供します。重要なことは、`Path` は不変であり、その所有バージョンは `PathBuf` と呼ばれ、それはインプレースで変更可能です。`Path` と `PathBuf` の関係は、`str` と `String` の関係に似ています。

> **注：** 実験でファイル名が指定されていない場合、好きなファイル名を使用できます。たとえば、`main.rs` を使用して、`rustc main.rs &&./main` でコンパイルして実行できます。
