# Iteradores

El trato `Iterator` se utiliza para implementar iteradores sobre colecciones como arrays.

El trato solo requiere que se defina un método para el elemento `next`, el cual puede definirse manualmente en un bloque `impl` o definirse automáticamente (como en arrays y rangos).

Como una conveniencia para situaciones comunes, la construcción `for` convierte algunas colecciones en iteradores utilizando el método `.into_iter()`.

```rust
struct Fibonacci {
    curr: u32,
    next: u32,
}

// Implemente `Iterator` para `Fibonacci`.
// El trato `Iterator` solo requiere que se defina un método para el elemento `next`.
impl Iterator for Fibonacci {
    // Podemos referirnos a este tipo utilizando Self::Item
    type Item = u32;

    // Aquí, definimos la secuencia utilizando `.curr` y `.next`.
    // El tipo de retorno es `Option<T>`:
    //     * Cuando el `Iterator` termina, se devuelve `None`.
    //     * De lo contrario, el siguiente valor se envuelve en `Some` y se devuelve.
    // Utilizamos Self::Item en el tipo de retorno, para que podamos cambiar
    // el tipo sin tener que actualizar las firmas de función.
    fn next(&mut self) -> Option<Self::Item> {
        let current = self.curr;

        self.curr = self.next;
        self.next = current + self.next;

        // Dado que no hay un punto final en una secuencia de Fibonacci, el `Iterator`
        // nunca devolverá `None`, y siempre se devuelve `Some`.
        Some(current)
    }
}

// Devuelve un generador de secuencia de Fibonacci
fn fibonacci() -> Fibonacci {
    Fibonacci { curr: 0, next: 1 }
}

fn main() {
    // `0..3` es un `Iterator` que genera: 0, 1 y 2.
    let mut sequence = 0..3;

    println!("Cuatro llamadas consecutivas a `next` en 0..3");
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());

    // `for` recorre un `Iterator` hasta que devuelve `None`.
    // Cada valor `Some` se desenvuelve y se asigna a una variable (aquí, `i`).
    println!("Iterar a través de 0..3 utilizando `for`");
    for i in 0..3 {
        println!("> {}", i);
    }

    // El método `take(n)` reduce un `Iterator` a sus primeros `n` términos.
    println!("Los primeros cuatro términos de la secuencia de Fibonacci son: ");
    for i in fibonacci().take(4) {
        println!("> {}", i);
    }

    // El método `skip(n)` acorta un `Iterator` eliminando sus primeros `n` términos.
    println!("Los siguientes cuatro términos de la secuencia de Fibonacci son: ");
    for i in fibonacci().skip(4).take(4) {
        println!("> {}", i);
    }

    let array = [1u32, 3, 3, 7];

    // El método `iter` produce un `Iterator` sobre un array/slice.
    println!("Iterar el siguiente array {:?}", &array);
    for i in array.iter() {
        println!("> {}", i);
    }
}
```
