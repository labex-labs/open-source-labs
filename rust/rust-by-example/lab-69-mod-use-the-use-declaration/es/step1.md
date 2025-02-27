# La declaración `use`

La declaración `use` se puede utilizar para enlazar una ruta completa a un nuevo nombre, para un acceso más fácil. A menudo se utiliza de la siguiente manera:

```rust
use crate::deeply::nested::{
    my_first_function,
    my_second_function,
    AndATraitType
};

fn main() {
    my_first_function();
}
```

Puede utilizar la palabra clave `as` para enlazar importaciones a un nombre diferente:

```rust
// Enlace la ruta `deeply::nested::function` a `other_function`.
use deeply::nested::function as other_function;

fn function() {
    println!("llamado `function()`");
}

mod deeply {
    pub mod nested {
        pub fn function() {
            println!("llamado `deeply::nested::function()`");
        }
    }
}

fn main() {
    // Acceso más fácil a `deeply::nested::function`
    other_function();

    println!("Entrando al bloque");
    {
        // Esto es equivalente a `use deeply::nested::function as function`.
        // Esta `function()` sombreará la externa.
        use crate::deeply::nested::function;

        // Los enlaces `use` tienen un ámbito local. En este caso, la
        // sombreado de `function()` solo es en este bloque.
        function();

        println!("Saliendo del bloque");
    }

    function();
}
```
