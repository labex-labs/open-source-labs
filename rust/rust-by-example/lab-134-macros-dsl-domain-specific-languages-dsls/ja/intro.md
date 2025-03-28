# はじめに

この実験では、Rustにおけるドメイン固有言語 (DSL) の概念を探ります。これらのDSLは、Rustマクロに埋め込まれたミニ "言語" です。これらのマクロは通常のRust構文に展開されますが、特定の機能に対して簡潔で直感的な構文を提供します。実用的な例として、計算機APIを使って示します。ここでは、式をマクロに渡し、出力をコンソールに表示します。これにより、`lazy_static` や `clap` などのライブラリにあるような、より複雑なインターフェイスを作成できます。

> **注:** 実験でファイル名が指定されていない場合は、好きなファイル名を使うことができます。たとえば、`main.rs` を使って、`rustc main.rs &&./main` でコンパイルして実行することができます。
