# Casting

Rust no proporciona conversión de tipo implícita (coerción) entre tipos primitivos. Sin embargo, se puede realizar una conversión de tipo explícita (casting) utilizando la palabra clave `as`.

Las reglas para la conversión entre tipos enteros siguen generalmente las convenciones de C, excepto en los casos en los que C tiene un comportamiento indefinido. El comportamiento de todos los casts entre tipos enteros está bien definido en Rust.

```rust
// Suprime todas las advertencias de los casts que desbordan.
#![allow(overflowing_literals)]

fn main() {
    let decimal = 65.4321_f32;

    // Error! No hay conversión implícita
    let integer: u8 = decimal;
    // FIXME ^ Comenta esta línea

    // Conversión explícita
    let integer = decimal as u8;
    let character = integer as char;

    // Error! Hay limitaciones en las reglas de conversión.
    // Un flotante no se puede convertir directamente en un carácter.
    let character = decimal as char;
    // FIXME ^ Comenta esta línea

    println!("Casting: {} -> {} -> {}", decimal, integer, character);

    // cuando se convierte cualquier valor a un tipo sin signo, T,
    // se suma o resta T::MAX + 1 hasta que el valor
    // quepa en el nuevo tipo

    // 1000 ya cabe en un u16
    println!("1000 como u16 es: {}", 1000 as u16);

    // 1000 - 256 - 256 - 256 = 232
    // En el fondo, se conservan los primeros 8 bits menos significativos (LSB),
    // mientras que el resto hacia el bit más significativo (MSB) se trunca.
    println!("1000 como u8 es : {}", 1000 as u8);
    // -1 + 256 = 255
    println!("  -1 como u8 es : {}", (-1i8) as u8);

    // Para los números positivos, esto es lo mismo que el módulo
    println!("1000 mod 256 es : {}", 1000 % 256);

    // Cuando se convierte a un tipo con signo, el resultado (en bits) es el mismo que
    // primero convertir al tipo sin signo correspondiente. Si el bit más significativo
    // de ese valor es 1, entonces el valor es negativo.

    // A menos que ya quepa, por supuesto.
    println!(" 128 como i16 es: {}", 128 as i16);

    // En el caso límite, el valor 128 en representación de complemento a dos de 8 bits es -128
    println!(" 128 como i8 es : {}", 128 as i8);

    // repitiendo el ejemplo anterior
    // 1000 como u8 -> 232
    println!("1000 como u8 es : {}", 1000 as u8);
    // y el valor de 232 en representación de complemento a dos de 8 bits es -24
    println!(" 232 como i8 es : {}", 232 as i8);

    // Desde Rust 1.45, la palabra clave `as` realiza un *casting saturante*
    // cuando se convierte de flotante a entero. Si el valor de punto flotante excede
    // el límite superior o es menor que el límite inferior, el valor devuelto
    // será igual al límite cruzado.

    // 300.0 como u8 es 255
    println!(" 300.0 como u8 es : {}", 300.0_f32 as u8);
    // -100.0 como u8 es 0
    println!("-100.0 como u8 es : {}", -100.0_f32 as u8);
    // nan como u8 es 0
    println!("   nan como u8 es : {}", f32::NAN as u8);

    // Este comportamiento implica un pequeño costo de tiempo de ejecución y se puede evitar
    // con métodos no seguros, sin embargo los resultados pueden desbordarse y
    // devolver **valores no sólidos**. Utilice estos métodos con prudencia:
    unsafe {
        // 300.0 como u8 es 44
        println!(" 300.0 como u8 es : {}", 300.0_f32.to_int_unchecked::<u8>());
        // -100.0 como u8 es 156
        println!("-100.0 como u8 es : {}", (-100.0_f32).to_int_unchecked::<u8>());
        // nan como u8 es 0
        println!("   nan como u8 es : {}", f32::NAN.to_int_unchecked::<u8>());
    }
}
```
