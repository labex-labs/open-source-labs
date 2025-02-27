# `Rc`

Cuando se necesita propiedad múltiple, se puede usar `Rc` (Referencia Contada). `Rc` lleva un registro del número de referencias, lo que significa el número de propietarios del valor envuelto dentro de un `Rc`.

El recuento de referencias de un `Rc` aumenta en 1 cada vez que se clona un `Rc`, y disminuye en 1 cada vez que un `Rc` clonado sale del ámbito. Cuando el recuento de referencias de un `Rc` llega a cero (lo que significa que no quedan propietarios), tanto el `Rc` como el valor se eliminan.

Clonar un `Rc` nunca realiza una copia profunda. La clonación crea solo otro puntero al valor envuelto, y aumenta el recuento.

```rust
use std::rc::Rc;

fn main() {
    let rc_examples = "Rc examples".to_string();
    {
        println!("--- rc_a se crea ---");

        let rc_a: Rc<String> = Rc::new(rc_examples);
        println!("Recuento de referencias de rc_a: {}", Rc::strong_count(&rc_a));

        {
            println!("--- rc_a se clona a rc_b ---");

            let rc_b: Rc<String> = Rc::clone(&rc_a);
            println!("Recuento de referencias de rc_b: {}", Rc::strong_count(&rc_b));
            println!("Recuento de referencias de rc_a: {}", Rc::strong_count(&rc_a));

            // Dos `Rc`s son iguales si sus valores internos son iguales
            println!("rc_a y rc_b son iguales: {}", rc_a.eq(&rc_b));

            // Podemos usar los métodos de un valor directamente
            println!("Longitud del valor dentro de rc_a: {}", rc_a.len());
            println!("Valor de rc_b: {}", rc_b);

            println!("--- rc_b sale del ámbito ---");
        }

        println!("Recuento de referencias de rc_a: {}", Rc::strong_count(&rc_a));

        println!("--- rc_a sale del ámbito ---");
    }

    // Error! `rc_examples` ya se ha movido a `rc_a`
    // Y cuando `rc_a` se elimina, `rc_examples` se elimina junto
    // println!("rc_examples: {}", rc_examples);
    // TODO ^ Intenta descomentar esta línea
}
```
