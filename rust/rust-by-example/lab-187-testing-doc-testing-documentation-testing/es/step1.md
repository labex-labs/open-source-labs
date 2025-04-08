# Pruebas de documentación

La principal forma de documentar un proyecto de Rust es a través de la adición de comentarios al código fuente. Los comentarios de documentación se escriben en la especificación CommonMark Markdown y admiten bloques de código dentro de ellos. Rust se encarga de la corrección, por lo que estos bloques de código se compilan y se usan como pruebas de documentación.

````rust
/// La primera línea es un resumen corto que describe la función.
///
/// Las siguientes líneas presentan la documentación detallada. Los bloques de código empiezan con
/// triples comillas invertidas y tienen implícito `fn main()` dentro
/// y `extern crate <cratename>`. Asumamos que estamos probando el crate `doccomments`:
///
/// ```
/// let result = doccomments::add(2, 3);
/// assert_eq!(result, 5);
/// ```
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

/// Por lo general, los comentarios de documentación pueden incluir secciones "Ejemplos", "Panics" y "Fallos".
///
/// La siguiente función divide dos números.
///
/// # Ejemplos
///
/// ```
/// let result = doccomments::div(10, 2);
/// assert_eq!(result, 5);
/// ```
///
/// # Panics
///
/// La función produce un error si el segundo argumento es cero.
///
/// ```rust
/// // produce un error al dividir por cero
/// doccomments::div(10, 0);
/// ```
pub fn div(a: i32, b: i32) -> i32 {
    if b == 0 {
        panic!("Error al dividir por cero");
    }

    a / b
}
````

Los bloques de código en la documentación se prueban automáticamente al ejecutar el comando regular `cargo test`:

```shell

```

## Motivación detrás de las pruebas de documentación

El principal propósito de las pruebas de documentación es servir como ejemplos que demuestren la funcionalidad, lo cual es una de las pautas más importantes. Permite usar los ejemplos de la documentación como fragmentos de código completos. Pero usar `?` hace que la compilación falle ya que `main` devuelve `unit`. La capacidad de ocultar algunas líneas de código de la documentación viene en ayuda: se puede escribir `fn try_main() -> Result<(), ErrorType>`, ocultarla y `unwrap`arla en `main` oculto. ¿Suena complicado? Aquí hay un ejemplo:

````rust
/// Usando `try_main` oculto en las pruebas de documentación.
///
/// ```
/// # // las líneas ocultas empiezan con el símbolo `#`, pero todavía son compilables!
/// # fn try_main() -> Result<(), String> { // línea que envuelve el cuerpo mostrado en la documentación
/// let res = doccomments::try_div(10, 2)?;
/// # Ok(()) // devolviendo desde try_main
/// # }
/// # fn main() { // comenzando main que llamará a unwrap()
/// #    try_main().unwrap(); // llamando a try_main y desenvuelta
/// #                         // para que la prueba produzca un error en caso de error
/// # }
/// ```
pub fn try_div(a: i32, b: i32) -> Result<i32, String> {
    if b == 0 {
        Err(String::from("División por cero"))
    } else {
        Ok(a / b)
    }
}
````
