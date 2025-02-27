# Devolviendo un Result en lugar de llamar a panic!

En lugar de eso, podemos devolver un valor `Result` que contendrá una instancia de `Config` en el caso de éxito y describirá el problema en el caso de error. También vamos a cambiar el nombre de la función de `new` a `build` porque muchos programadores esperan que las funciones `new` nunca fallen. Cuando `Config::build` se comunica con `main`, podemos usar el tipo `Result` para señalar que hubo un problema. Luego podemos cambiar `main` para convertir una variante `Err` en un error más práctico para nuestros usuarios sin el texto circundante sobre `thread'main'` y `RUST_BACKTRACE` que causa una llamada a `panic!`.

La Lista 12-9 muestra los cambios que necesitamos hacer al valor de retorno de la función que ahora estamos llamando `Config::build` y al cuerpo de la función necesario para devolver un `Result`. Tenga en cuenta que esto no se compilará hasta que actualicemos `main` también, lo que haremos en la siguiente lista.

Nombre de archivo: `src/main.rs`

```rust
impl Config {
    fn build(args: &[String]) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("no hay suficientes argumentos");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        Ok(Config { query, file_path })
    }
}
```

Lista 12-9: Devolviendo un `Result` desde `Config::build`

Nuestra función `build` devuelve un `Result` con una instancia de `Config` en el caso de éxito y un `&'static str` en el caso de error. Nuestros valores de error siempre serán literales de cadena que tienen la vida útil `'static`.

Hemos hecho dos cambios en el cuerpo de la función: en lugar de llamar a `panic!` cuando el usuario no pasa suficientes argumentos, ahora devolvemos un valor `Err`, y hemos envolto el valor de retorno de `Config` en un `Ok`. Estos cambios hacen que la función se ajuste a su nueva firma de tipo.

Devolver un valor `Err` desde `Config::build` permite que la función `main` maneje el valor `Result` devuelto por la función `build` y salga del proceso de manera más limpia en el caso de error.
