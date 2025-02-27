# Funciones divergentes

Las funciones divergentes nunca devuelven. Se marcan con `!`, que es un tipo vacío.

```rust
fn foo() ->! {
    panic!("Esta llamada nunca devuelve.");
}
```

En contraste con todos los demás tipos, este no se puede instanciar, porque el conjunto de todos los valores posibles que puede tener este tipo está vacío. Tenga en cuenta que es diferente del tipo `()`, que tiene exactamente un valor posible.

Por ejemplo, esta función devuelve como de costumbre, aunque no hay información en el valor de retorno.

```rust
fn some_fn() {
    ()
}

fn main() {
    let _a: () = some_fn();
    println!("Esta función devuelve y puede ver esta línea.");
}
```

En contraste con esta función, que nunca devolverá el control al llamador.

```rust
#![feature(never_type)]

fn main() {
    let x:! = panic!("Esta llamada nunca devuelve.");
    println!("Nunca verá esta línea!");
}
```

Aunque esto puede parecer un concepto abstracto, de hecho es muy útil y práctico. La principal ventaja de este tipo es que se puede convertir a cualquier otro y, por lo tanto, se puede usar en lugares donde se requiere un tipo exacto, por ejemplo, en las ramas `match`. Esto nos permite escribir código como este:

```rust
fn main() {
    fn sum_odd_numbers(up_to: u32) -> u32 {
        let mut acc = 0;
        for i in 0..up_to {
            // Tenga en cuenta que el tipo de retorno de esta expresión match debe ser u32
            // debido al tipo de la variable "addition".
            let addition: u32 = match i%2 == 1 {
                // La variable "i" es de tipo u32, lo cual está perfectamente bien.
                true => i,
                // Por otro lado, la expresión "continue" no devuelve
                // u32, pero sigue siendo correcta, porque nunca devuelve y, por lo tanto,
                // no viola los requisitos de tipo de la expresión match.
                false => continue,
            };
            acc += addition;
        }
        acc
    }
    println!("Suma de números impares hasta 9 (excluyendo): {}", sum_odd_numbers(9));
}
```

También es el tipo de retorno de funciones que bucle indefinidamente (por ejemplo, `loop {}`) como los servidores de red o funciones que terminan el proceso (por ejemplo, `exit()`).
