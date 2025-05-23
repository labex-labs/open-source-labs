# はじめに

この実験では、Rust の外部関数インターフェイス（FFI）について学びます。FFI を使うことで、`extern`ブロック内で外部関数を宣言し、それに対して外部ライブラリ名を含む`#[link]`属性を付与することで、C ライブラリとの相互作用が可能になります。コード例では、`libm`ライブラリからの外部関数を呼び出す FFI の使い方を示しており、たとえば単精度複素数の平方根を計算したり、複素数の余弦を計算したりします。これらの非セーフな外部関数呼び出しの周りには、セーフなラッパーが一般的に使われます。この実験ではまた、単精度複素数の最小限の実装も含まれており、非セーフな操作をラップしたセーフな API をどのように呼び出すかを示しています。

> **注：** 実験でファイル名が指定されていない場合、好きなファイル名を使うことができます。たとえば、`main.rs`を使って、`rustc main.rs &&./main`でコンパイルして実行することができます。
