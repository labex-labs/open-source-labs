# はじめに

この実験では、Rust の配列とスライスを調べます。配列は、連続したメモリに格納された同じ型のオブジェクトのコレクションであり、その長さはコンパイル時に既知です。一方、スライスは配列に似ていますが、その長さはコンパイル時には既知ではありません。スライスは、配列の一部を借用するために使用できます。また、配列の作成方法、要素のアクセス方法、長さの計算方法、メモリの割り当て方法、配列をスライスとして借用する方法、空のスライスの操作方法についても説明します。さらに、`.get()` メソッドを使用して配列要素を安全にアクセスし、境界外エラーを処理する方法についても説明します。

> **注：** 実験でファイル名が指定されていない場合は、好きなファイル名を使用できます。たとえば、`main.rs` を使用して、`rustc main.rs &&./main` でコンパイルして実行できます。
