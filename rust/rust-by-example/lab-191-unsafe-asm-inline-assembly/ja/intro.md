# はじめに

この実験では、`asm!` マクロを使って Rust でインラインアセンブリの使い方を調べます。インラインアセンブリの基本的な使い方、入出力、遅延出力オペランド、明示的なレジスタオペランド、クロバーされるレジスタ、シンボルオペランドと ABI クロバー、レジスタテンプレート修飾子、メモリアドレスオペランド、ラベル、およびアセンブリコードを最適化するためのオプションについて説明します。

> **注：** 実験でファイル名が指定されていない場合、好きなファイル名を使うことができます。たとえば、`main.rs` を使って、`rustc main.rs &&./main` でコンパイルして実行することができます。
