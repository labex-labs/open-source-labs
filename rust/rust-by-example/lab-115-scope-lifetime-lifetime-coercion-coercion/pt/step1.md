# Coerção (Coercion)

Um tempo de vida (lifetime) mais longo pode ser coerido para um mais curto para que funcione dentro de um escopo em que normalmente não funcionaria. Isso ocorre na forma de coerção inferida pelo compilador Rust, e também na forma de declarar uma diferença de tempo de vida:

```rust
// Aqui, Rust infere um tempo de vida que é o mais curto possível.
// As duas referências são então coeridas para esse tempo de vida.
fn multiply<'a>(first: &'a i32, second: &'a i32) -> i32 {
    first * second
}

// `<'a: 'b, 'b>` lê-se como o tempo de vida `'a` é pelo menos tão longo quanto `'b`.
// Aqui, recebemos um `&'a i32` e retornamos um `&'b i32` como resultado da coerção.
fn choose_first<'a: 'b, 'b>(first: &'a i32, _: &'b i32) -> &'b i32 {
    first
}

fn main() {
    let first = 2; // Tempo de vida mais longo

    {
        let second = 3; // Tempo de vida mais curto

        println!("The product is {}", multiply(&first, &second));
        println!("{} is the first", choose_first(&first, &second));
    };
}
```
