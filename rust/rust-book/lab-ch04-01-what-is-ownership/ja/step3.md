# 変数のスコープ

これで、Rust の基本的な構文を超えた段階になりましたので、例にはすべての `fn main() {` コードを含めません。従って、あなたがコードを追っている場合、以下の例を手動で `main` 関数の中に入れるようにしてください。その結果、私たちの例はもう少し簡潔になり、定型コードではなく、実際の詳細に焦点を当てることができます。

所有権の最初の例として、いくつかの変数の「スコープ」を見てみましょう。スコープとは、プログラム内で項目が有効な範囲のことです。次の変数を見てみましょう。

```rust
let s = "hello";
```

変数 `s` は文字列リテラルを参照しており、文字列の値はプログラムのテキストにハードコードされています。変数は宣言された時点から現在の「スコープ」の終わりまで有効です。リスト 4-1 には、変数 `s` が有効になる場所をコメントで注釈付けしたプログラムが示されています。

    {                      // sはまだ宣言されていないので、ここでは有効ではありません
        let s = "hello";   // sはこの時点以降有効です

        // sを使って何かをする
    }                      // このスコープはもう終了し、sはもはや有効ではありません

リスト 4-1: 変数とその有効なスコープ

言い換えると、ここでは 2 つの重要な時点があります。

- `s` がスコープに「入る」とき、それは有効です。
- それはスコープから「出る」まで有効です。

この時点で、スコープと変数が有効になる時期の関係は、他のプログラミング言語と同様です。次に、`String` 型を導入することで、この理解の上にさらに発展させます。
