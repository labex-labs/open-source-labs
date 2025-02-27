# Drop

El trato `Drop` solo tiene un método: `drop`, que se llama automáticamente cuando un objeto sale del ámbito. La principal utilización del trato `Drop` es liberar los recursos que posee la instancia del implementador.

`Box`, `Vec`, `String`, `File` y `Process` son algunos ejemplos de tipos que implementan el trato `Drop` para liberar recursos. El trato `Drop` también se puede implementar manualmente para cualquier tipo de datos personalizado.

El siguiente ejemplo agrega una impresión en la consola a la función `drop` para anunciar cuando se llama.

```rust
struct Droppable {
    name: &'static str,
}

// Esta implementación trivial de `drop` agrega una impresión en la consola.
impl Drop for Droppable {
    fn drop(&mut self) {
        println!("> Dropping {}", self.name);
    }
}

fn main() {
    let _a = Droppable { name: "a" };

    // bloque A
    {
        let _b = Droppable { name: "b" };

        // bloque B
        {
            let _c = Droppable { name: "c" };
            let _d = Droppable { name: "d" };

            println!("Saliendo del bloque B");
        }
        println!("Acaba de salir del bloque B");

        println!("Saliendo del bloque A");
    }
    println!("Acaba de salir del bloque A");

    // La variable se puede eliminar manualmente usando la función `drop`
    drop(_a);
    // TODO ^ Intenta comentar esta línea

    println!("fin de la función principal");

    // `_a` *no* se `drop`ará nuevamente aquí, porque ya se ha
    // (manualmente) `drop`ado
}
```
