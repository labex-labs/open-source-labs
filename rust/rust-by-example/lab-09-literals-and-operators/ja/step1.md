# リテラルと演算子

整数 `1`、浮動小数点数 `1.2`、文字 `'a'`、文字列 `"abc"`、ブール値 `true`、およびユニット型 `()` は、リテラルを使って表現できます。

整数は、それぞれ `0x`、`0o`、または `0b` の接頭辞を使って、16 進数、8 進数、または 2 進数表記で表現することもできます。

数値リテラルにアンダースコアを挿入して、読みやすさを向上させることができます。たとえば、`1_000` は `1000` と同じで、`0.000_001` は `0.000001` と同じです。

Rust はまた、科学的な E 表記もサポートしています。たとえば、`1e6`、`7.6e-4` です。関連する型は `f64` です。

使うリテラルの型をコンパイラに知らせる必要があります。今のところ、リテラルが符号なし 32 ビット整数であることを示すには `u32` サフィックスを、符号付き 32 ビット整数であることを示すには `i32` サフィックスを使います。

Rust における利用可能な演算子とその優先順位は、他の C 系言語と似ています。

```rust
fn main() {
    // 整数の加算
    println!("1 + 2 = {}", 1u32 + 2);

    // 整数の減算
    println!("1 - 2 = {}", 1i32 - 2);
    // TODO ^ `1i32` を `1u32` に変更して、型が重要な理由を確認してみてください

    // 科学表記
    println!("1e4 is {}, -2.5e-3 is {}", 1e4, -2.5e-3);

    // 短絡型のブール論理
    println!("true AND false is {}", true && false);
    println!("true OR false is {}", true || false);
    println!("NOT true is {}",!true);

    // ビット演算
    println!("0011 AND 0101 is {:04b}", 0b0011u32 & 0b0101);
    println!("0011 OR 0101 is {:04b}", 0b0011u32 | 0b0101);
    println!("0011 XOR 0101 is {:04b}", 0b0011u32 ^ 0b0101);
    println!("1 << 5 is {}", 1u32 << 5);
    println!("0x80 >> 2 is 0x{:x}", 0x80u32 >> 2);

    // 読みやすさを向上させるためにアンダースコアを使いましょう！
    println!("One million is written as {}", 1_000_000u32);
}
```
