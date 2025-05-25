# Conversão de Tipos

Rust não fornece conversão de tipo implícita (coerção) entre tipos primitivos. No entanto, a conversão de tipo explícita (conversão) pode ser realizada usando a palavra-chave `as`.

As regras para conversão entre tipos inteiros seguem as convenções C, geralmente, exceto em casos onde C tem comportamento indefinido. O comportamento de todas as conversões entre tipos inteiros está bem definido em Rust.

```rust
// Suprime todos os avisos de conversões que extrapolam.
#![allow(overflowing_literals)]

fn main() {
    let decimal = 65.4321_f32;

    // Erro! Não há conversão implícita
    let integer: u8 = decimal;
    // FIXME ^ Comente esta linha

    // Conversão explícita
    let integer = decimal as u8;
    let character = integer as char;

    // Erro! Há limitações nas regras de conversão.
    // Um float não pode ser convertido diretamente para um char.
    let character = decimal as char;
    // FIXME ^ Comente esta linha

    println!("Casting: {} -> {} -> {}", decimal, integer, character);

    // Ao converter qualquer valor para um tipo sem sinal, T,
    // T::MAX + 1 é adicionado ou subtraído até que o valor
    // caiba no novo tipo

    // 1000 já cabe em um u16
    println!("1000 como um u16 é: {}", 1000 as u16);

    // 1000 - 256 - 256 - 256 = 232
    // Internamente, os 8 bits menos significativos (LSB) são mantidos,
    // enquanto o restante em direção ao bit mais significativo (MSB) é truncado.
    println!("1000 como um u8 é: {}", 1000 as u8);
    // -1 + 256 = 255
    println!("  -1 como um u8 é: {}", (-1i8) as u8);

    // Para números positivos, isso é o mesmo que o módulo
    println!("1000 mod 256 é: {}", 1000 % 256);

    // Ao converter para um tipo assinado, o resultado (bit a bit) é o mesmo que
    // primeiro converter para o tipo sem sinal correspondente. Se o bit mais significativo
    // desse valor for 1, então o valor é negativo.

    // A menos que já caiba, é claro.
    println!(" 128 como um i16 é: {}", 128 as i16);

    // No caso limite, o valor 128 na representação em complemento de dois de 8 bits é -128
    println!(" 128 como um i8 é: {}", 128 as i8);

    // Repetindo o exemplo acima
    // 1000 como u8 -> 232
    println!("1000 como um u8 é: {}", 1000 as u8);
    // e o valor de 232 na representação em complemento de dois de 8 bits é -24
    println!(" 232 como um i8 é: {}", 232 as i8);

    // Desde o Rust 1.45, a palavra-chave `as` executa uma conversão *saturante*
    // ao converter de float para int. Se o valor de ponto flutuante exceder
    // o limite superior ou for menor que o limite inferior, o valor retornado
    // será igual ao limite cruzado.

    // 300.0 como u8 é 255
    println!(" 300.0 como u8 é: {}", 300.0_f32 as u8);
    // -100.0 como u8 é 0
    println!("-100.0 como u8 é: {}", -100.0_f32 as u8);
    // nan como u8 é 0
    println!("   nan como u8 é: {}", f32::NAN as u8);

    // Este comportamento incorre em um pequeno custo de tempo de execução e pode ser evitado
    // com métodos inseguros, no entanto, os resultados podem extrapolar e
    // retornar valores **inconsistentes**. Use esses métodos com sabedoria:
    unsafe {
        // 300.0 como u8 é 44
        println!(" 300.0 como u8 é: {}", 300.0_f32.to_int_unchecked::<u8>());
        // -100.0 como u8 é 156
        println!("-100.0 como u8 é: {}", (-100.0_f32).to_int_unchecked::<u8>());
        // nan como u8 é 0
        println!("   nan como u8 é: {}", f32::NAN.to_int_unchecked::<u8>());
    }
}
```
