# 省略

一部のライフタイムパターンは非常に一般的であるため、バローチェッカーは入力を省略して読みやすさを向上させるためにそれらを省略することを許可します。これは省略（elision）と呼ばれます。省略は、これらのパターンが一般的であるためにのみRustに存在します。

次のコードは、省略のいくつかの例を示しています。省略のより包括的な説明については、本のライフタイム省略を参照してください。

```rust
// `elided_input` と `annotated_input` は本質的に同じ署名を持っています
// なぜなら、`elided_input` のライフタイムはコンパイラによって推論されるからです:
fn elided_input(x: &i32) {
    println!("`elided_input`: {}", x);
}

fn annotated_input<'a>(x: &'a i32) {
    println!("`annotated_input`: {}", x);
}

// 同様に、`elided_pass` と `annotated_pass` は同じ署名を持っています
// なぜなら、ライフタイムが暗黙的に `elided_pass` に追加されるからです:
fn elided_pass(x: &i32) -> &i32 { x }

fn annotated_pass<'a>(x: &'a i32) -> &'a i32 { x }

fn main() {
    let x = 3;

    elided_input(&x);
    annotated_input(&x);

    println!("`elided_pass`: {}", elided_pass(&x));
    println!("`annotated_pass`: {}", annotated_pass(&x));
}
```
