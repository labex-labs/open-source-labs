# `Option`

Às vezes, é desejável capturar a falha de algumas partes de um programa em vez de chamar `panic!`; isso pode ser realizado usando o enum `Option`.

O enum `Option<T>` possui duas variantes:

- `None`, para indicar falha ou ausência de valor, e
- `Some(value)`, uma struct de tupla que encapsula um `value` com o tipo `T`.

```rust
// Uma divisão inteira que não causa `panic!`
fn checked_division(dividend: i32, divisor: i32) -> Option<i32> {
    if divisor == 0 {
        // A falha é representada como a variante `None`
        None
    } else {
        // O resultado é encapsulado em uma variante `Some`
        Some(dividend / divisor)
    }
}

// Esta função lida com uma divisão que pode não ter sucesso
fn try_division(dividend: i32, divisor: i32) {
    // Valores `Option` podem ser combinados por padrão, assim como outros enums
    match checked_division(dividend, divisor) {
        None => println!("{} / {} falhou!", dividend, divisor),
        Some(quotient) => {
            println!("{} / {} = {}", dividend, divisor, quotient)
        },
    }
}

fn main() {
    try_division(4, 2);
    try_division(1, 0);

    // Vincular `None` a uma variável precisa ser anotado com o tipo
    let none: Option<i32> = None;
    let _equivalent_none = None::<i32>;

    let optional_float = Some(0f32);

    // Desembrulhar uma variante `Some` extrairá o valor encapsulado.
    println!("{:?} desembrulha para {:?}", optional_float, optional_float.unwrap());

    // Desembrulhar uma variante `None` causará `panic!`
    println!("{:?} desembrulha para {:?}", none, none.unwrap());
}
```
