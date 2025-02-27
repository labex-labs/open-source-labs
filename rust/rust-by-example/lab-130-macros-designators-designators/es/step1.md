# Designadores

Los argumentos de un macro están prefijados por un signo de dólar `$` y se les anota el tipo con un _designador_:

```rust
macro_rules! create_function {
    // Este macro toma un argumento de designador `ident` y
    // crea una función llamada `$func_name`.
    // El designador `ident` se utiliza para nombres de variables/funciones.
    ($func_name:ident) => {
        fn $func_name() {
            // El macro `stringify!` convierte un `ident` en una cadena.
            println!("You called {:?}()",
                     stringify!($func_name));
        }
    };
}

// Crea funciones llamadas `foo` y `bar` con el macro anterior.
create_function!(foo);
create_function!(bar);

macro_rules! print_result {
    // Este macro toma una expresión de tipo `expr` y la imprime
    // como una cadena junto con su resultado.
    // El designador `expr` se utiliza para expresiones.
    ($expression:expr) => {
        // `stringify!` convertirá la expresión *tal cual* en una cadena.
        println!("{:?} = {:?}",
                 stringify!($expression),
                 $expression);
    };
}

fn main() {
    foo();
    bar();

    print_result!(1u32 + 1);

    // Recuerde que los bloques también son expresiones!
    print_result!({
        let x = 1u32;

        x * x + 2 * x - 1
    });
}
```

Estos son algunos de los designadores disponibles:

- `block`
- `expr` se utiliza para expresiones
- `ident` se utiliza para nombres de variables/funciones
- `item`
- `literal` se utiliza para constantes literales
- `pat` (_patrón_)
- `path`
- `stmt` (_sentencia_)
- `tt` (_árbol de tokens_)
- `ty` (_tipo_)
- `vis` (_calificador de visibilidad_)

Para una lista completa, consulte la \[Rust Reference\].
