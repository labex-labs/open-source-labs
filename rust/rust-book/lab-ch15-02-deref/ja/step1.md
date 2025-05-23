# Deref を使って通常の参照と同じようにスマートポインタを扱う

`Deref`トレイトを実装することで、_参照演算子_`*`の動作をカスタマイズできます（乗算演算子やグロブ演算子と混同しないでください）。スマートポインタを通常の参照と同じように扱えるように`Deref`を実装することで、参照で動作するコードを書き、それをスマートポインタでも使うことができます。

まず、通常の参照で参照演算子がどのように機能するか見てみましょう。次に、`Box<T>`と同じように動作するカスタム型を定義し、新しく定義した型で参照と同じように参照演算子が機能しない理由を見てみましょう。`Deref`トレイトを実装することでスマートポインタが参照と同じように動作するようになる方法を探ります。そして、Rust の*deref 強制*機能と、それが参照またはスマートポインタのどちらでも動作させる方法を見てみましょう。

> 注：これから作成する`MyBox<T>`型と本物の`Box<T>`には大きな違いがあります。私たちのバージョンはデータをヒープに格納しません。この例では`Deref`に焦点を当てているため、データが実際に格納されている場所は、ポインタのような動作よりも重要ではありません。
