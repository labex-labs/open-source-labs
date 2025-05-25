# Literais e operadores

Inteiros `1`, floats (ponto flutuante) `1.2`, caracteres `'a'`, strings `"abc"`, booleanos `true` e o tipo unitário `()` podem ser expressos usando literais.

Inteiros podem, alternativamente, ser expressos usando notação hexadecimal, octal ou binária, usando estes prefixos, respectivamente: `0x`, `0o` ou `0b`.

Underscores (sublinhados) podem ser inseridos em literais numéricos para melhorar a legibilidade, por exemplo, `1_000` é o mesmo que `1000`, e `0.000_001` é o mesmo que `0.000001`.

Rust também suporta notação científica E, por exemplo, `1e6`, `7.6e-4`. O tipo associado é `f64`.

Precisamos informar ao compilador o tipo dos literais que usamos. Por enquanto, usaremos o sufixo `u32` para indicar que o literal é um inteiro sem sinal de 32 bits, e o sufixo `i32` para indicar que é um inteiro com sinal de 32 bits.

Os operadores disponíveis e sua precedência em Rust são semelhantes a outras linguagens semelhantes a C.

```rust
fn main() {
    // Integer addition
    println!("1 + 2 = {}", 1u32 + 2);

    // Integer subtraction
    println!("1 - 2 = {}", 1i32 - 2);
    // TODO ^ Try changing `1i32` to `1u32` to see why the type is important

    // Scientific notation
    println!("1e4 is {}, -2.5e-3 is {}", 1e4, -2.5e-3);

    // Short-circuiting boolean logic
    println!("true AND false is {}", true && false);
    println!("true OR false is {}", true || false);
    println!("NOT true is {}", !true);

    // Bitwise operations
    println!("0011 AND 0101 is {:04b}", 0b0011u32 & 0b0101);
    println!("0011 OR 0101 is {:04b}", 0b0011u32 | 0b0101);
    println!("0011 XOR 0101 is {:04b}", 0b0011u32 ^ 0b0101);
    println!("1 << 5 is {}", 1u32 << 5);
    println!("0x80 >> 2 is 0x{:x}", 0x80u32 >> 2);

    // Use underscores to improve readability!
    println!("One million is written as {}", 1_000_000u32);
}
```
