# Literale und Operatoren

Ganzzahlen `1`, Gleitkommazahlen `1.2`, Zeichen `'a'`, Strings `"abc"`, Boole'sche Werte `true` und der Einheitstyp `()` können mit Literalen ausgedrückt werden.

Ganzzahlen können alternativ in hexadezimaler, oktaler oder binärer Notation mit diesen Präfixen ausgedrückt werden: `0x`, `0o` oder `0b` jeweils.

Unterstriche können in numerischen Literalen eingefügt werden, um die Lesbarkeit zu verbessern, z.B. `1_000` ist gleich `1000`, und `0.000_001` ist gleich `0.000001`.

Rust unterstützt auch die wissenschaftliche E-Notation, z.B. `1e6`, `7.6e-4`. Der zugehörige Typ ist `f64`.

Wir müssen dem Compiler den Typ der Literale mitteilen, die wir verwenden. Für jetzt werden wir das Suffix `u32` verwenden, um anzuzeigen, dass das Literal ein vorzeichenloses 32-Bit-Ganzzahl ist, und das Suffix `i32`, um anzuzeigen, dass es eine vorzeichenbehaftete 32-Bit-Ganzzahl ist.

Die verfügbaren Operatoren und ihre Präzedenz in Rust sind ähnlich wie in anderen C-ähnlichen Sprachen.

```rust
fn main() {
    // Ganzzahladdition
    println!("1 + 2 = {}", 1u32 + 2);

    // Ganzzahlsubtraktion
    println!("1 - 2 = {}", 1i32 - 2);
    // TODO ^ Versuchen Sie, `1i32` in `1u32` umzuwandeln, um zu sehen, warum der Typ wichtig ist

    // Wissenschaftliche Notation
    println!("1e4 ist {}, -2.5e-3 ist {}", 1e4, -2.5e-3);

    // Kurzschluss-Logik für Boole'sche Werte
    println!("true AND false ist {}", true && false);
    println!("true OR false ist {}", true || false);
    println!("NOT true ist {}",!true);

    // Bitweise Operationen
    println!("0011 AND 0101 ist {:04b}", 0b0011u32 & 0b0101);
    println!("0011 OR 0101 ist {:04b}", 0b0011u32 | 0b0101);
    println!("0011 XOR 0101 ist {:04b}", 0b0011u32 ^ 0b0101);
    println!("1 << 5 ist {}", 1u32 << 5);
    println!("0x80 >> 2 ist 0x{:x}", 0x80u32 >> 2);

    // Verwenden Sie Unterstriche, um die Lesbarkeit zu verbessern!
    println!("Einen Millionen wird geschrieben als {}", 1_000_000u32);
}
```
