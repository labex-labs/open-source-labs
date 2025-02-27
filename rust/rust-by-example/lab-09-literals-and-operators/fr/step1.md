# Littéraux et opérateurs

Les entiers `1`, les flottants `1.2`, les caractères `'a'`, les chaînes de caractères `"abc"`, les booléens `true` et le type unité `()` peuvent être exprimés à l'aide de littéraux.

Les entiers peuvent également être exprimés en notation hexadécimale, octale ou binaire en utilisant respectivement ces préfixes : `0x`, `0o` ou `0b`.

Des tirets de soulignement peuvent être insérés dans les littéraux numériques pour améliorer la lisibilité, par exemple `1_000` est équivalent à `1000`, et `0.000_001` est équivalent à `0.000001`.

Rust prend également en charge la notation scientifique E, par exemple `1e6`, `7.6e-4`. Le type associé est `f64`.

Nous devons indiquer au compilateur le type des littéraux que nous utilisons. Pour l'instant, nous utiliserons le suffixe `u32` pour indiquer que le littéral est un entier non signé de 32 bits, et le suffixe `i32` pour indiquer qu'il s'agit d'un entier signé de 32 bits.

Les opérateurs disponibles et leur priorité en Rust sont similaires à celles des autres langages du type C.

```rust
fn main() {
    // Addition d'entiers
    println!("1 + 2 = {}", 1u32 + 2);

    // Soustraction d'entiers
    println!("1 - 2 = {}", 1i32 - 2);
    // TODO ^ Essayez de changer `1i32` en `1u32` pour voir pourquoi le type est important

    // Notation scientifique
    println!("1e4 est {}, -2.5e-3 est {}", 1e4, -2.5e-3);

    // Logique booléenne à court-circuit
    println!("true ET false est {}", true && false);
    println!("true OU false est {}", true || false);
    println!("NON true est {}",!true);

    // Opérations bit-à-bit
    println!("0011 ET 0101 est {:04b}", 0b0011u32 & 0b0101);
    println!("0011 OU 0101 est {:04b}", 0b0011u32 | 0b0101);
    println!("0011 XOR 0101 est {:04b}", 0b0011u32 ^ 0b0101);
    println!("1 << 5 est {}", 1u32 << 5);
    println!("0x80 >> 2 est 0x{:x}", 0x80u32 >> 2);

    // Utilisez des tirets de soulignement pour améliorer la lisibilité!
    println!("Un million est écrit {}", 1_000_000u32);
}
```
