# macro_rules!

Rust ofrece un sistema de macros poderoso que permite la metaprogramación. Como has visto en los capítulos anteriores, las macros se parecen a funciones, excepto que su nombre termina con un signo de exclamación `!`, pero en lugar de generar una llamada a función, las macros se expanden en código fuente que se compila con el resto del programa. Sin embargo, a diferencia de las macros en C y otros lenguajes, las macros de Rust se expanden en árboles de sintaxis abstracta, en lugar de un preprocesamiento de cadenas, por lo que no tendrás errores de precedencia inesperados.

Las macros se crean utilizando la macro `macro_rules!`.

```rust
// Esta es una macro simple llamada `say_hello`.
macro_rules! say_hello {
    // `()` indica que la macro no toma argumentos.
    () => {
        // La macro se expandirá en el contenido de este bloque.
        println!("Hello!")
    };
}

fn main() {
    // Esta llamada se expandirá en `println!("Hello")`
    say_hello!()
}
```

Entonces, ¿por qué son útiles las macros?

1.  No te repitas. Hay muchos casos en los que puede que necesites una funcionalidad similar en varios lugares pero con diferentes tipos. Con frecuencia, escribir una macro es una forma útil de evitar la repetición de código. (Más sobre esto más adelante)

2.  Lenguajes de dominio específicos. Las macros te permiten definir una sintaxis especial con un propósito específico. (Más sobre esto más adelante)

3.  Interfaces variádicas. A veces quieres definir una interfaz que tome un número variable de argumentos. Un ejemplo es `println!` que podría tomar cualquier número de argumentos, dependiendo de la cadena de formato. (Más sobre esto más adelante)
