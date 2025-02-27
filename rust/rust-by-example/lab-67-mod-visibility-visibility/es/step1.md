# Visibilidad

Por defecto, los elementos de un módulo tienen visibilidad privada, pero esto se puede anular con el modificador `pub`. Solo los elementos públicos de un módulo pueden ser accedidos desde fuera del ámbito del módulo.

```rust
// Un módulo llamado `my_mod`
mod my_mod {
    // Los elementos en los módulos por defecto tienen visibilidad privada.
    fn private_function() {
        println!("llamado `my_mod::private_function()`");
    }

    // Utilice el modificador `pub` para anular la visibilidad predeterminada.
    pub fn function() {
        println!("llamado `my_mod::function()`");
    }

    // Los elementos pueden acceder a otros elementos en el mismo módulo,
    // incluso cuando son privados.
    pub fn indirect_access() {
        print!("llamado `my_mod::indirect_access()`, que\n> ");
        private_function();
    }

    // Los módulos también pueden estar anidados
    pub mod nested {
        pub fn function() {
            println!("llamado `my_mod::nested::function()`");
        }

        #[allow(dead_code)]
        fn private_function() {
            println!("llamado `my_mod::nested::private_function()`");
        }

        // Las funciones declaradas usando la sintaxis `pub(in path)` solo son visibles
        // dentro del camino dado. `path` debe ser un módulo padre o ancestro
        pub(in crate::my_mod) fn public_function_in_my_mod() {
            print!("llamado `my_mod::nested::public_function_in_my_mod()`, que\n> ");
            public_function_in_nested();
        }

        // Las funciones declaradas usando la sintaxis `pub(self)` solo son visibles dentro
        // del módulo actual, lo que es lo mismo que dejarlas privadas
        pub(self) fn public_function_in_nested() {
            println!("llamado `my_mod::nested::public_function_in_nested()`");
        }

        // Las funciones declaradas usando la sintaxis `pub(super)` solo son visibles dentro
        // del módulo padre
        pub(super) fn public_function_in_super_mod() {
            println!("llamado `my_mod::nested::public_function_in_super_mod()`");
        }
    }

    pub fn call_public_function_in_my_mod() {
        print!("llamado `my_mod::call_public_function_in_my_mod()`, que\n> ");
        nested::public_function_in_my_mod();
        print!("> ");
        nested::public_function_in_super_mod();
    }

    // pub(crate) hace que las funciones solo sean visibles dentro del crat actual
    pub(crate) fn public_function_in_crate() {
        println!("llamado `my_mod::public_function_in_crate()`");
    }

    // Los módulos anidados siguen las mismas reglas de visibilidad
    mod private_nested {
        #[allow(dead_code)]
        pub fn function() {
            println!("llamado `my_mod::private_nested::function()`");
        }

        // Los elementos privados del padre todavía restringirán la visibilidad de un elemento hijo,
        // incluso si se declara visible dentro de un ámbito más grande.
        #[allow(dead_code)]
        pub(crate) fn restricted_function() {
            println!("llamado `my_mod::private_nested::restricted_function()`");
        }
    }
}

fn function() {
    println!("llamado `function()`");
}

fn main() {
    // Los módulos permiten la disambiguación entre elementos que tienen el mismo nombre.
    function();
    my_mod::function();

    // Los elementos públicos, incluyendo aquellos dentro de los módulos anidados, pueden ser
    // accedidos desde fuera del módulo padre.
    my_mod::indirect_access();
    my_mod::nested::function();
    my_mod::call_public_function_in_my_mod();

    // Los elementos pub(crate) se pueden llamar desde cualquier parte del mismo crat
    my_mod::public_function_in_crate();

    // Los elementos pub(in path) solo se pueden llamar desde dentro del módulo especificado
    // Error! La función `public_function_in_my_mod` es privada
    //my_mod::nested::public_function_in_my_mod();
    // TODO ^ Intente descomentar esta línea

    // Los elementos privados de un módulo no pueden ser accedidos directamente, incluso si
    // están anidados en un módulo público:

    // Error! `private_function` es privada
    //my_mod::private_function();
    // TODO ^ Intente descomentar esta línea

    // Error! `private_function` es privada
    //my_mod::nested::private_function();
    // TODO ^ Intente descomentar esta línea

    // Error! `private_nested` es un módulo privado
    //my_mod::private_nested::function();
    // TODO ^ Intente descomentar esta línea

    // Error! `private_nested` es un módulo privado
    //my_mod::private_nested::restricted_function();
    // TODO ^ Intente descomentar esta línea
}
```
