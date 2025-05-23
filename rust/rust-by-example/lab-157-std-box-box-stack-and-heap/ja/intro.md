# はじめに

この実験では、Rust におけるボクシング、スタック割り当て、およびヒープ割り当ての概念を調べます。Rust のすべての値はデフォルトでスタック割り当てされますが、`Box<T>` 型を使用してボクシング（ヒープ上に割り当てる）することができます。ボックスは、ヒープ上に割り当てられた値へのスマートポインタであり、スコープ外になると、そのデストラクタが呼び出され、ヒープ上のメモリが解放されます。ボクシングにより、二重の間接参照の作成が可能になり、`*` 演算子を使用して参照解除することができます。この実験では、ボクシングがどのように機能するか、およびスタック上のメモリ割り当てにどのように影響するかについて、コード例と説明を提供しています。

> **注：** 実験でファイル名が指定されていない場合、好きなファイル名を使用できます。たとえば、`main.rs` を使用して、`rustc main.rs &&./main` でコンパイルして実行することができます。
