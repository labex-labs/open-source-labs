# Literales y operadores

Los enteros `1`, los flotantes `1.2`, los caracteres `'a'`, las cadenas `"abc"`, los booleanos `true` y el tipo unitario `()` se pueden expresar utilizando literales.

Alternativamente, los enteros se pueden expresar utilizando notación hexadecimal, octal o binaria con estos prefijos respectivamente: `0x`, `0o` o `0b`.

Se pueden insertar guiones bajos en literales numéricos para mejorar la legibilidad, por ejemplo, `1_000` es igual a `1000`, y `0.000_001` es igual a `0.000001`.

Rust también admite la notación científica E, por ejemplo, `1e6`, `7.6e-4`. El tipo asociado es `f64`.

Debemos decirle al compilador el tipo de los literales que usamos. Por ahora, usaremos el sufijo `u32` para indicar que el literal es un entero sin signo de 32 bits, y el sufijo `i32` para indicar que es un entero con signo de 32 bits.

Los operadores disponibles y su precedencia en Rust son similares a otros lenguajes similares a C.

```rust
fn main() {
    // Suma de enteros
    println!("1 + 2 = {}", 1u32 + 2);

    // Resta de enteros
    println!("1 - 2 = {}", 1i32 - 2);
    // TODO ^ Intenta cambiar `1i32` a `1u32` para ver por qué el tipo es importante

    // Notación científica
    println!("1e4 es {}, -2.5e-3 es {}", 1e4, -2.5e-3);

    // Lógica booleana de circuito corto
    println!("true AND false es {}", true && false);
    println!("true OR false is {}", true || false);
    println!("NOT true is {}",!true);

    // Operaciones bit a bit
    println!("0011 AND 0101 is {:04b}", 0b0011u32 & 0b0101);
    println!("0011 OR 0101 is {:04b}", 0b0011u32 | 0b0101);
    println!("0011 XOR 0101 is {:04b}", 0b0011u32 ^ 0b0101);
    println!("1 << 5 is {}", 1u32 << 5);
    println!("0x80 >> 2 is 0x{:x}", 0x80u32 >> 2);

    // ¡Usa guiones bajos para mejorar la legibilidad!
    println!("Un millón se escribe como {}", 1_000_000u32);
}
```
