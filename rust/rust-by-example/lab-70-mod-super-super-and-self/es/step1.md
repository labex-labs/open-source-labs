# `super` y `self`

Las palabras clave `super` y `self` se pueden usar en la ruta para eliminar la ambigüedad al acceder a elementos y evitar la codificación manual innecesaria de rutas.

```rust
fn function() {
    println!("llamado `function()`");
}

mod cool {
    pub fn function() {
        println!("llamado `cool::function()`");
    }
}

mod my {
    fn function() {
        println!("llamado `my::function()`");
    }

    mod cool {
        pub fn function() {
            println!("llamado `my::cool::function()`");
        }
    }

    pub fn indirect_call() {
        // Vamos a acceder a todas las funciones llamadas `function` a partir de este ámbito!
        print!("llamado `my::indirect_call()`, que\n> ");

        // La palabra clave `self` se refiere al ámbito del módulo actual - en este caso `my`.
        // Llamar `self::function()` y llamar `function()` directamente ambos dan
        // el mismo resultado, porque se refieren a la misma función.
        self::function();
        function();

        // También podemos usar `self` para acceder a otro módulo dentro de `my`:
        self::cool::function();

        // La palabra clave `super` se refiere al ámbito padre (fuera del módulo `my`).
        super::function();

        // Esto se vinculará a la `cool::function` en el ámbito del *crate*.
        // En este caso el ámbito del crate es el ámbito más externo.
        {
            use crate::cool::function as root_function;
            root_function();
        }
    }
}

fn main() {
    my::indirect_call();
}
```
