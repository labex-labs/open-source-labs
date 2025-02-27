# Devolviendo Errores desde la Función run

Con el resto de la lógica del programa separada en la función `run`, podemos mejorar el manejo de errores, como lo hicimos con `Config::build` en la Lista 12-9. En lugar de permitir que el programa se detenga con un error llamando a `expect`, la función `run` devolverá un `Result<T, E>` cuando algo salga mal. Esto nos permitirá consolidar aún más la lógica alrededor del manejo de errores en `main` de una manera amigable para el usuario. La Lista 12-12 muestra los cambios que necesitamos hacer a la firma y el cuerpo de `run`.

Nombre de archivo: `src/main.rs`

```rust
1 use std::error::Error;

--snip--

2 fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)3?;

    println!("Con el texto:\n{contents}");

  4 Ok(())
}
```

Lista 12-12: Cambiando la función `run` para devolver `Result`

Hemos hecho tres cambios significativos aquí. Primero, cambiamos el tipo de retorno de la función `run` a `Result<(), Box<dyn Error>>` \[2\]. Esta función anteriormente devolvía el tipo unitario, `()`, y lo mantenemos como el valor devuelto en el caso `Ok`.

Para el tipo de error, usamos el _objeto de tramo_ `Box<dyn Error>` (y hemos traído `std::error::Error` al alcance con una declaración `use` en la parte superior \[1\]). Cubriremos los objetos de tramo en el Capítulo 17. Por ahora, solo debes saber que `Box<dyn Error>` significa que la función devolverá un tipo que implemente el tramo `Error`, pero no tenemos que especificar qué tipo particular será el valor de retorno. Esto nos da flexibilidad para devolver valores de error que pueden ser de diferentes tipos en diferentes casos de error. La palabra clave `dyn` es abreviatura de _dinámico_.

Segundo, hemos eliminado la llamada a `expect` a favor del operador `?` \[3\], como hablamos en el Capítulo 9. En lugar de detenerse con un error con `panic!`, `?` devolverá el valor de error de la función actual para que el llamador lo maneje.

Tercero, la función `run` ahora devuelve un valor `Ok` en el caso de éxito \[4\]. Hemos declarado el tipo de éxito de la función `run` como `()` en la firma, lo que significa que necesitamos envolver el valor del tipo unitario en el valor `Ok`. Esta sintaxis `Ok(())` puede parecer un poco extraña al principio, pero usar `()` de esta manera es la forma idiómática de indicar que estamos llamando a `run` solo por sus efectos secundarios; no devuelve un valor que necesitemos.

Cuando ejecutes este código, se compilará pero mostrará una advertencia:

    advertencia: `Result` no utilizado que debe ser utilizado
      --> src/main.rs:19:5
       |
    19 |     run(config);
       |     ^^^^^^^^^^^^
       |
       = nota: `#[warn(unused_must_use)]` activado por defecto
       = nota: este `Result` puede ser una variante `Err`, que debe
    ser manejada

Rust nos dice que nuestro código ignoró el valor `Result` y el valor `Result` puede indicar que se produjo un error. Pero no estamos comprobando si hubo o no un error, y el compilador nos recuerda que probablemente queríamos tener algún código de manejo de errores aquí. Vamos a corregir ese problema ahora.
